#!/usr/bin/env python3
"""Make the AI Judge Laugh - make.fun bounty entry.

Writes one funny line about office life to /output/entry.txt.

Fully deterministic: the same bytes on every run, no input, no network,
no randomness, no clock.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

JOKE = ("Our boss said the meeting could have been an email, then "
        "scheduled a meeting to discuss why it could have been an email.")

DEFAULT_OUTPUT = "/output/entry.txt"


def build_joke():
    return JOKE


def emit_entry(target, text):
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def run():
    target = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    emit_entry(target, build_joke())


if __name__ == "__main__":
    run()
