"""One Letter for Your Day: the letter C.

Behind C sits the word "chaotic" — the day in one letter. Everything
happening at once, nothing going to plan, and you lived to tell it.
"""

import os

LETTER = "C"


def output_path():
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for key in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        if os.environ.get(key):
            return os.path.join(os.environ[key], "entry.txt")
    return "/output/entry.txt"


def main():
    # Gate: exactly one ASCII letter A-Z, nothing else — no newline,
    # no whitespace, no gloss. Re-read the file after writing and
    # refuse to finish unless the bytes are exactly the letter.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "letter must be one A-Z"
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    assert written == LETTER.encode("ascii"), "output must be exactly one byte"


if __name__ == "__main__":
    main()
