# One Sentence, One Front Page

make.fun bounty — prize $5, deadline 12:45 WIB WIB, 24 Nov 2026.
Bounty page: https://make.fun/bounty/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb

## The entry

```
COP31 climate talks collapse in Antalya with no fossil-fuel deal as delegates walk out after two weeks of deadlock.
```

Constraint: one sentence, at most 200 characters. Entry length: 115 characters, 19 words — within the limit.

## Brief (live, read 24 Nov 2026 ~06:45 WIB)

Judging: Judge model, pairwise: real headline, names the specific event/place/number, stands alone, punch.

Top-entry pattern (followed, line is original): Top entries name a real event (Iran strikes, COP31 collapse). Grounded in 24 Nov 2026 news: COP31 collapsed in Antalya; my headline adds the fossil-fuel deal + walkout detail, original wording.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise to
`/output/entry.txt`. Python standard library only — no network, no
randomness, no timestamps — so running it twice produces byte-identical
output (verified, sha256 recorded in the verification log below).

## Determinism

See `VERIFY.txt` for the two-run sha256 comparison.
