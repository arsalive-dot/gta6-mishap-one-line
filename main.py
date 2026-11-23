#!/usr/bin/env python3
"""Write the one-line GTA 6 launch-week mishap entry to /output/entry.txt."""
import os

TEXT = "While I was on my third hour of GTA 6, my coding agent finished the feature, fixed the bug I'd fought all week, and opened a pull request against my own repo: 'please review, you have been AFK since Tuesday'."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
