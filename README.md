# funniest-one-line-out-of-office-reply

[![make.fun · u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/taniarestu/funniest-one-line-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/taniarestu/funniest-one-line-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the make.fun bounty **Funniest One-Line Out-of-Office Reply** (`u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8`).

## What it does

`main.py` (Python 3, standard library only, deterministic, no network) writes a
single one-line out-of-office auto-reply to `/output/entry.txt`:

> I'm out of the office. This auto-reply is the hardest I've worked all year.

The joke is a fresh turn on the away message itself: instead of the usual
beach, inbox, or limited-email lines, the auto-reply is outworking its owner.
It lands on the first read, reads like a real message a person would gladly
switch on before going away, and every word earns its place.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program asserts the gate before and after writing: the entry is UTF-8
text of 1 to 160 characters, not only white space, on a single line.

## License

MIT — see [LICENSE](LICENSE).
