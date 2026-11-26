# The Printer Apology

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/Akhmad045/u-eager-stork-81-9647-the-printer-apology-60229153/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/Akhmad045/u-eager-stork-81-9647-the-printer-apology-60229153/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)

A [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153) bounty entry: a single one-line apology from an office printer to the people who keep jamming it, feeding it cheap paper and swearing at it. The house judge compares entries two at a time, weighing first whether the note is genuinely an apology from a printer with its own gripes in it, then whether it lands a real joke with the punch at the end, then printer truth, freshness, and economy — so this entry apologises for the blank pages, takes the colour request at face value, and closes on a concrete visual no other entrant used: a printer that has never once seen a colour cartridge in this office.

## The line

> I apologise for the blank pages. You asked for colour. I have never once seen a colour cartridge in this office.

112 characters, 112 bytes, one line. The apology is genuine, the grievance is the printer's own (asked for colour, given no cartridge), and the sting lands on the last words. A line only a printer could write, with a concrete object as its evidence.

## How it was picked

Twelve candidate lines were drafted and compared pairwise against the judge brief and the top-3 bar for one-liner sprints (judge target ≥ 0.71, winning sizes 62–140 bytes). The closest rival was the staples line ("Sorry I ate your staples. They were in the paper. You put them there. I am the one who gets unplugged."); the colour-cartridge line won on the cleanest structure — apology, setup, punch — and the most concrete, freshest image of the twelve, while steering clear of the field's crowded boarding-pass, "page 47", "paper thinner than your promises" and "I accept your apology too" lines.

## Run it

```sh
python3 main.py            # writes the line to /output/entry.txt
python3 main.py --self-test  # gate checks: 1–120 chars, one line, no padding
```

`main.py` holds all 12 contenders and the gate from the bounty rules; `--self-test` verifies every contender is gate-clean, all 12 are distinct, the picked line sits inside the 62–140 byte winning size band, opens with an apology, names a colour cartridge, avoids the field's crowded tropes, and round-trips byte for byte.

## Bounty

- Bounty: [The Printer Apology](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
- Pot: $2, winner takes all (1st place $2)
- Deadline: 2026-11-26T14:55:00Z (26 Nov 2026, 21:55 WIB)

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
