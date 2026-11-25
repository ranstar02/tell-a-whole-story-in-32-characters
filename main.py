"""Entry for make.fun's "Tell a Whole Story in 32 Characters" bounty.

The entry is a single Wi-Fi network name (an SSID) that tells a whole
little story in one glance:

    Son Sold Router, Bought V-Bucks

A kid (the character) sold the family router (the situation) to buy
Fortnite V-Bucks (the event) -- and now the network itself announces
its own demise. The joke lands on the first read, and every word
earns its place.

Running this script writes that name to /output/entry.txt with no
trailing newline. The program validates the entry against the
competition rules (1-32 characters, not only whitespace) before
writing anything, and it is fully deterministic: no input, no
network, no randomness.
"""

import os

WIFI_NAME = "Son Sold Router, Bought V-Bucks"

MAX_LENGTH = 32


def validate(name):
    """Check the entry against the competition rules."""
    if not name or name != name.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(name) > MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(name), MAX_LENGTH)
        )
    if name.endswith("\n"):
        raise ValueError("entry must not end with a newline")


def main():
    validate(WIFI_NAME)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WIFI_NAME)


if __name__ == "__main__":
    main()
