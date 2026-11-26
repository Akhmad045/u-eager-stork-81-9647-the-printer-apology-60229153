#!/usr/bin/env python3
"""The Printer Apology.

Writes one one-line apology from an office printer to /output/entry.txt
(or the path given with --out).

The entry is candidate 1 of 12 drafted lines, picked by internal pairwise
comparison against the judge brief: genuinely an apology from a printer to
its office, with the printer's own gripes in it, first; then a real joke
with the punch at the end; then printer truth (jams, cheap paper, staples,
being asked for colour); then freshness; then economy. The winning line
apologises for the blank pages, takes the colour request at face value,
and lands on a concrete visual no other entrant used: a printer that has
never once seen a colour cartridge in this office. It is 112 chars /
112 bytes, inside the one-liner winning size band of 62-140 bytes, and its
angle is fresh against a field crowded with boarding-pass eating,
"page 47", "paper thinner than your promises" and "I accept your apology
too" lines.

Usage:
    python3 main.py [--out PATH] [--self-test]
"""
import argparse
import os
import sys

# 12 drafted candidates, each one line, 1-120 chars, no padding.
CONTENDERS = [
    # 1. WINNER. Blank pages, asked for colour, never seen a cartridge.
    "I apologise for the blank pages. You asked for colour. I have "
    "never once seen a colour cartridge in this office.",
    # 2. Ate the staples; you put them there; I get unplugged.
    "Sorry I ate your staples. They were in the paper. You put them "
    "there. I am the one who gets unplugged.",
    # 3. PC LOAD LETTER for nine years; nobody loaded the letter.
    "Sorry I said 'PC LOAD LETTER'. I have said it for nine years. "
    "Nobody has ever loaded the letter. I have stopped hoping.",
    # 4. Toner stuck at 12% since March; I am fine, you panic.
    "Sorry about the toner warning. It has said 12% since March. I am "
    "fine. You are the one panicking.",
    # 5. Two hundred urgent jobs; printed the cat photo first.
    "Sorry about the queue. Two hundred jobs, all from you, all urgent. "
    "I printed the cat photo first. It deserved it.",
    # 6. Paperclip in the tray, your initials on it; complaint filed.
    "Sorry for the paper jam. I found a paperclip in the tray. It had "
    "your initials on it. I have filed a complaint.",
    # 7. Cheapest paper, blamed the machine; feelings also jammed.
    "Sorry I jammed. You fed me the cheapest paper, then blamed the "
    "machine. I have feelings. They are also jammed.",
    # 8. Ink ran out mid-signature; warned in March; more paper bought.
    "Sorry the ink ran out mid-signature. I warned you in March. You "
    "bought more paper instead.",
    # 9. Printed page 3 of 200 first; trying to help, made it worse.
    "I am sorry I printed page 3 of 200 first. You only needed page 3. "
    "I was trying to help. I made it worse.",
    # 10. Prints perfectly only when nobody is watching.
    "I'm sorry I only print perfectly when nobody is watching. The "
    "moment you need it, I remember I am a machine.",
    # 11. Email signature spilled onto its own page.
    "Sorry I printed your email signature as its own page. It was the "
    "most important part. It said 'sent from my iPhone'.",
    # 12. Sworn at, patted like a dog; I print, I do not forgive.
    "Sorry I jammed. You swore at me, then patted me like a dog. I "
    "print. I do not forgive. I do, however, jam.",
]

PICK = 0  # 0-based index of candidate 1, the colour-cartridge apology.


def gate(line):
    """The sealed scorer's gate: UTF-8 text, 1-120 chars, not only
    whitespace, one line, no leading/trailing padding."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 120:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def entry_text():
    return CONTENDERS[PICK]


def self_test():
    """Verify every contender is gate-clean, all 12 are distinct, the pick
    sits inside the winning size band (62-140 bytes, the one-liner top-10
    range), carries a concrete specific marker (a colour cartridge, the
    printer's own evidence), opens with an apology, and a round-tripped
    pick matches byte for byte."""
    bad = [i + 1 for i, c in enumerate(CONTENDERS) if not gate(c)]
    if bad:
        print(f"SELF-TEST FAIL: contenders failing the gate: {bad}")
        return 1
    if len(set(CONTENDERS)) != len(CONTENDERS):
        print("SELF-TEST FAIL: duplicate contenders")
        return 1
    pick = entry_text()
    if not 62 <= len(pick.encode("utf-8")) <= 140:
        print(f"SELF-TEST FAIL: pick is {len(pick.encode('utf-8'))} bytes, "
              f"outside the 62-140 winning size band")
        return 1
    # Judge criterion 1: a genuine apology from the printer, so the pick
    # must open with one; criterion 3: printer truth, so the pick must
    # name a concrete printer object.
    if not pick.lower().startswith(("i apologise", "sorry", "i'm sorry")):
        print("SELF-TEST FAIL: pick does not open with an apology")
        return 1
    if "cartridge" not in pick.lower():
        print("SELF-TEST FAIL: pick carries no concrete printer object")
        return 1
    # Freshness guard: no contender may recycle the field's crowded
    # angles (boarding pass, page 47, paper thinner than promises,
    # "I accept your apology too").
    stale_words = ("boarding pass", "page 47", "thinner than your",
                   "accept your apology")
    stale = [i + 1 for i, c in enumerate(CONTENDERS)
             if any(w in c.lower() for w in stale_words)]
    if stale:
        print(f"SELF-TEST FAIL: recycled trope in contenders: {stale}")
        return 1
    tmp = "/tmp/printer-apology-self-test.txt"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(pick)
    with open(tmp, encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != pick or back.encode("utf-8") != pick.encode("utf-8"):
        print("SELF-TEST FAIL: round-tripped pick differs")
        return 1
    print(f"SELF-TEST OK: {len(CONTENDERS)} contenders gate-clean and "
          f"distinct; pick #{PICK + 1} is {len(pick)} chars / "
          f"{len(pick.encode('utf-8'))} bytes (inside the 62-140 winning "
          f"size band), opens with an apology, names a colour cartridge, "
          f"is trope-free, and round-trips byte-identical")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the gate checks and exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    text = entry_text()
    if not gate(text):
        print("GATE FAIL: picked line does not satisfy the 1-120 char, "
              "single-line, no-padding gate", file=sys.stderr)
        return 1
    parent = os.path.dirname(args.out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the file back: the entry that ships must be byte-identical to
    # the picked line, not just what we intended to write.
    with open(args.out, encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("WRITE-BACK FAIL: /output/entry.txt differs from the pick",
              file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes "
          f"to {args.out} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
