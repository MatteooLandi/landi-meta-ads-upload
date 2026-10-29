#!/usr/bin/env python3
"""Inventario compatto delle creatività per la skill meta-ads-upload.

Scansione, hash e dimensioni sono operazioni meccaniche: niente AI. Prodotto,
versione, URL e naming li compila l'agente nella matrice.

Uso:
  inventory.py CARTELLA [CARTELLA ...] [--video-subdir Export] [--no-probe]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp"}

SEP = r"[x_:\-]"
FORMAT_TOKEN = re.compile(
    r"(?<![0-9])(?:1" + SEP + r"1|4" + SEP + r"5|9" + SEP + r"16|16" + SEP + r"9"
    r"|\d{3,4}x\d{3,4})(?![0-9])",
    re.I,
)
WORD_TOKEN = re.compile(
    r"(?<![a-z0-9])(?:feed|story|stories|reel|reels|square|vertical|quadrato|verticale)(?![a-z0-9])",
    re.I,
)
RATIOS = (("1:1", 1.0), ("4:5", 0.8), ("9:16", 0.5625), ("16:9", 1.7778), ("1.91:1", 1.91))
RATIO_TOLERANCE = 0.02


def group_key(path: Path) -> str:
    """Chiave di raggruppamento: cartella e nome senza i token di formato.

    Euristica: file con la stessa chiave sono versioni di formato della stessa
    creatività. L'agente conferma il raggruppamento.
    """
    stem = FORMAT_TOKEN.sub(" ", path.stem.lower())
    stem = WORD_TOKEN.sub(" ", stem)
    stem = re.sub(r"[_\-\s.]+", "-", stem).strip("-")
    return f"{path.parent.name}/{stem}"


def ratio_label(width: int, height: int) -> str:
    if not width or not height:
        return "?"
    value = width / height
    for label, target in RATIOS:
        if abs(value - target) <= RATIO_TOLERANCE:
            return label
    return "altro"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def probe(path: Path):
    """Ritorna (larghezza, altezza, durata) oppure zeri se ffprobe manca o fallisce."""
    if not shutil.which("ffprobe"):
        return 0, 0, 0.0
    cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height:format=duration",
        "-of", "json", str(path),
    ]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        data = json.loads(out.stdout or "{}")
        stream = (data.get("streams") or [{}])[0]
        duration = float((data.get("format") or {}).get("duration") or 0)
        return int(stream.get("width") or 0), int(stream.get("height") or 0), duration
    except (subprocess.SubprocessError, ValueError, OSError):
        return 0, 0, 0.0


def in_video_subdir(path: Path, root: Path, video_subdir: str) -> bool:
    if not video_subdir:
        return True
    wanted = video_subdir.lower()
    rel_parts = path.relative_to(root.parent).parent.parts
    return any(part.lower() == wanted for part in rel_parts)


def scan(roots, video_subdir: str = "Export", use_probe: bool = True):
    rows, discarded, ignored = [], [], 0
    seen = {}
    for root in roots:
        root = Path(root).resolve()
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            if path.name.startswith("."):
                continue
            ext = path.suffix.lower()
            if ext not in VIDEO_EXT and ext not in IMAGE_EXT:
                ignored += 1
                continue
            kind = "video" if ext in VIDEO_EXT else "immagine"
            if kind == "video" and not in_video_subdir(path, root, video_subdir):
                discarded.append(str(path))
                continue
            width, height, duration = probe(path) if use_probe else (0, 0, 0.0)
            digest = sha256_of(path)
            dup_of = seen.setdefault(digest, str(path))
            rows.append({
                "path": str(path.parent),
                "file": path.name,
                "tipo": kind,
                "dim": f"{width}x{height}" if width and height else "?",
                "ratio": ratio_label(width, height),
                "durata": f"{duration:.1f}s" if duration else "-",
                "sha": digest[:12],
                "gruppo": group_key(path),
                "dup_di": "-" if dup_of == str(path) else dup_of,
            })
    return rows, discarded, ignored


def render(rows, discarded, ignored) -> str:
    header = "Path|File|Tipo|WxH|Rapporto|Durata|SHA256(12)|Gruppo|DupDi"
    lines = [header]
    for r in rows:
        lines.append("|".join([
            r["path"], r["file"], r["tipo"], r["dim"], r["ratio"],
            r["durata"], r["sha"], r["gruppo"], r["dup_di"],
        ]))
    unique = [r for r in rows if r["dup_di"] == "-"]
    groups = {r["gruppo"] for r in unique}
    lines.append("")
    lines.append(
        f"File: {len(rows)} | Duplicati esatti: {len(rows) - len(unique)} | "
        f"Gruppi (creatività): {len(groups)} | Video scartati: {len(discarded)} | "
        f"Altri file ignorati: {ignored}"
    )
    for path in discarded:
        lines.append(f"SCARTATO (video fuori dalla sottocartella indicata): {path}")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("roots", nargs="+", help="cartelle con le creatività")
    parser.add_argument(
        "--video-subdir", default="Export",
        help="i video contano solo se stanno in una sottocartella con questo nome; vuoto = tutti",
    )
    parser.add_argument("--no-probe", action="store_true", help="non chiamare ffprobe")
    args = parser.parse_args(argv)
    missing = [r for r in args.roots if not Path(r).is_dir()]
    if missing:
        print(f"Cartella non trovata: {', '.join(missing)}", file=sys.stderr)
        return 2
    rows, discarded, ignored = scan(args.roots, args.video_subdir, not args.no_probe)
    print(render(rows, discarded, ignored))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
