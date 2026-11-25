"""Entry for make.fun's "The Meeting That Should Have Been One Line" bounty.

Writes the single sentence that could have replaced an entire pointless
meeting to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.
The line: an hour spent deciding nothing, then rebooked to decide it again.
"""

import os
import stat

ENTRY_TEXT = "We spent an hour deciding nothing, then booked another to decide it again."

assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY_TEXT.strip(), "entry must be a single line"
assert ENTRY_TEXT.strip() == ENTRY_TEXT, "entry must not have surrounding whitespace"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY_TEXT)
os.chmod(path, 0o644)
print(ENTRY_TEXT)
