"""Write the make.fun dad joke entry to entry.txt.

The joke is a single string constant; the program writes it as UTF-8 with no
trailing newline, creating the output folder, then prints the character count
to stderr.
"""

import os
import sys

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)

assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"


def output_dir() -> str:
    """Folder to write entry.txt into: MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
