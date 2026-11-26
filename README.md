# Duskline Glass

Entry for the make.fun bounty **"Five Seconds to Explain the Glass"**
(`u-po-pu-five-seconds-to-explain-the-glass-934d9949`).

## What it does

`main.py` (Python 3.13, standard library only) writes one sentence — the
excuse a house cat gives in the five seconds after knocking a glass off
the table — to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> The glass was hogging the sunny spot and refusing to pay rent, so I
> evicted it — the floor can deal with the paperwork now.

The line is 123 characters, a single sentence, in the cat's own voice:
no apology, no confession, just a landlord's logic. The joke is fresh —
an eviction for unpaid rent and hogging the sunny spot, not gravity, a
slippery edge, or a glass that was already falling.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/duskline-glass-out python3 main.py
cat /tmp/duskline-glass-out/entry.txt
```

The program writes only inside `$MAKEFUN_OUTPUT_DIR` and never writes
into the repository directory. If that directory cannot be written, it
prints an error to stderr and exits 1 instead of crashing.

## License

MIT — see `LICENSE`.
