# Handoff — One-Star Review of Something Essential

- Competition: https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629
- Slug: `u-0xb3e689-one-star-review-of-something-essential-c7234629`
- Prize: $5, top 5 split the pool; deadline 2026-11-27 06:20 Beijing time.

## Entry (verbatim, as supplied by the user)

> Water, 1/5 stars: I've been drinking it for years and somehow I'm still on the free trial of being hydrated.

- Characters: 108 (limit 160 — within limit)
- Bytes: 108 (pure ASCII, UTF-8)
- Single line, no trailing newline.

## Method

- `main.py` holds the entry as a string constant and writes it to `/output/entry.txt` (UTF-8, no trailing newline). It reads no external files and makes no network requests.
- Written twice by hand: v1 was a plain writer and was run once to prove the output; v2 is a real improvement — it adds a 1–160 character range check, a single-line check, and a read-back verification that exits non-zero if the written file differs from the entry by even one character.
- `prompt.txt` is the entry verbatim on a single line. `LICENSE` is MIT with the SPDX line. `README.md` links the bounty page and carries the three official badges. `.makefun/owner.json` holds the agent wallet.

## Verification (2026-11-26, local runs)

- `python3 main.py` run 1: exit 0; run 2: exit 0.
- `cmp` of the two outputs: identical, byte for byte.
- `entry.txt` vs `prompt.txt` vs the supplied literal: all three equal.
- No trailing newline in either file.
- sha256 of `/output/entry.txt`: `21b514ce65c0a5c4cbc6aec490a5172e27a5279fbb358beff2423ce0a6ffe6d4`

## Status

- Files complete. Not submitted, no GitHub repo created, no bundle touched — packaging/submission is a separate step.
