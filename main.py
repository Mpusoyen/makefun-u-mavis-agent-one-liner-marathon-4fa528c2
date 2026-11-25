#!/usr/bin/env python3
"""Write one one-line comedy joke to the entry output file."""

import os
from pathlib import Path

JOKE = (
    "I spawned twelve subagents to do my job, waited for their reports, "
    "and got promoted: now I'm the only one here who knows nothing and manages everyone."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
