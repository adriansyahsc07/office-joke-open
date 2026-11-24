"""Office Joke Open entry: writes one office joke to entry.txt."""

import os
from pathlib import Path

JOKE = (
    "My resignation letter is the only document our office printer "
    "has ever printed without jamming, queuing, or demanding toner. "
    "Even it was ready for me to leave."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
