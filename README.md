# dad-joke-barber-shop-20261124

[![make.fun · Dad Joke Showdown](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/sopiahusen42/dad-joke-barber-shop-20261124/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/sopiahusen42/dad-joke-barber-shop-20261124/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

The hat is the joke. "Just a little off the top" sounds like hair, but "the top" is a place you can also be wearing something — so when the barber takes the hat, he has answered the request literally and charged for the haircut nobody got. The pun never announces itself: the setup is plain small talk, and the turn arrives inside a straight-faced complaint, which is exactly how a dad delivers one. It also reads aloud well, because the rhythm is a normal sentence followed by a normal sentence, with the flat drop on "haircut" doing the work instead of an exclamation.

## The joke

> I asked the barber for just a little off the top. He took my hat and charged me for a haircut.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the line in the module constant `JOKE` and validates it with `validate_entry(text)` before writing anything: the entry must be a `str`, non-blank after strip, 1 to 200 Unicode code points, a single line with no `\n` or `\r`, equal to its stripped form, and free of double quotes. Any failure prints one line to stderr and exits 1. On success it writes `JOKE` plus a newline as UTF-8 into `MAKEFUN_OUTPUT_DIR` (default `/output`), reads the bytes back to confirm they match, prints nothing, and exits 0.
