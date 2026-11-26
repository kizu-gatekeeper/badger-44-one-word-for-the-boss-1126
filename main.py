"""Entry for make.fun bounty: u-swift-badger-44-one-word-for-the-boss-6b48c735.

Writes the entry word to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

ENTRY = "Meetingspawner"
MAX_CHARS = 30


def main():
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry length out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
