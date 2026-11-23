"""Make the Judge Fall in Love in One Line.

Writes a single love line (<=240 chars) to /output/entry.txt.
Deterministic, no network, no randomness.
"""
import os
from pathlib import Path

ENTRY = (
    "She still saves the last bite for me, even now that she forgets my name "
    "\u2014 love, it turns out, lives in the hands long after it leaves the head."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
