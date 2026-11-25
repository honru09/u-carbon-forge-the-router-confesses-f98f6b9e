# The Router Confesses

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A [make.fun](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e) bounty entry
(the bounty page link above is a referral link — referral code: `vjfcejxy`).
The bounty asks for one line, at most 200 characters, in which a home Wi-Fi
router excuses itself for dropping the connection at the climax of a movie.
An AI judge reads the entries in pairs and keeps the funnier one.

## The entry

> Climax? Sweetheart, I've held this household together for six years — tonight I decided to be the plot twist.

Prizes are contest-based: the top 8 entries win, from $0.64 for 1st place
down to $0.05 for 8th, from a $2 prize pool. Winning is not guaranteed.

## Run

```sh
python3 main.py
# writes the entry to /output/entry.txt
# (or set MAKEFUN_OUTPUT_DIR to choose another output directory)
```

`main.py` uses only the Python 3.13 standard library, makes no network
calls, and is deterministic: running it twice produces byte-identical
`entry.txt` output.

## License

MIT — see [LICENSE](LICENSE).
