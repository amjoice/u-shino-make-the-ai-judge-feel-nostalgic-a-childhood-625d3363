"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (a childhood memory) to /output/entry.txt.
Standard library only; deterministic; no network, no input files.
"""

import os

ENTRY = "The last summer before they sold the house, I fell asleep on a bamboo mat under the mango tree while Grandma sang off-key, and the night air smelled of smoke, rain, and ripe fruit."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
