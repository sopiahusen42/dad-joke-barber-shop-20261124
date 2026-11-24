"""Write the make.fun "Dad Joke Showdown" entry line to entry.txt.

The program is deterministic: the same reserialised bytes on every run.
It validates JOKE against the bounty gate, writes JOKE plus a newline as
UTF-8 (newline="\\n") into MAKEFUN_OUTPUT_DIR (default /output), reads the
bytes back to confirm them, and stays silent on success. On any invalid
entry it prints one line to stderr and exits 1.
"""

import os
import sys

JOKE = "I asked the barber for just a little off the top. He took my hat and charged me for a haircut."


def validate_entry(text: str) -> str | None:
    """Return an error message for an invalid entry, or None when it is valid."""
    if not isinstance(text, str):
        return "not a str"
    if not text.strip():
        return "blank"
    length = len(text)
    if length < 1 or length > 200:
        return f"{length} code points (limit 200)"
    if "\n" in text or "\r" in text:
        return "multi-line"
    if text != text.strip():
        return "untrimmed whitespace"
    if '"' in text:
        return "contains a double quote"
    return None


def write_entry(out_dir: str, text: str) -> bool:
    """Write text + newline as UTF-8 and confirm the bytes on disk match."""
    payload = (text + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    with open(path, "rb") as handle:
        return handle.read() == payload


def main() -> int:
    error = validate_entry(JOKE)
    if error is not None:
        print(f"invalid entry: {error}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not write_entry(out_dir, JOKE):
        print("write verification failed: bytes on disk differ from payload", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
