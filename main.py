"""delete-word-25nov26 — make.fun bounty entry.

The word I would delete from the dictionary: "dictionary".

Once it is gone, the dictionary can no longer name itself —
every copy becomes a book with no word for what it is.
"""

import os

WORD = "dictionary"


def main() -> None:
    assert WORD.isalpha() and " " not in WORD, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {WORD!r} ({len(WORD)} chars) to /output/entry.txt")


if __name__ == "__main__":
    main()
