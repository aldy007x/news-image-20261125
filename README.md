# The World Today — 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/aldy007x/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/aldy007x/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A one-page newspaper front page summing up **Wednesday 25 November 2026** in a
single 1024x1024 image — built for the
[make.fun bounty "Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125).

## The stories

- **Lead — US spy agencies hacked:** the CIA and the Office of the Director of
  National Intelligence suffered an apparent hack hitting unclassified
  open-source intelligence systems; early indications point to China, and
  officials say no classified information was affected (CNN / NYT, 25 Nov).
- **Huawei found guilty:** a US jury found Huawei guilty on 10 of 12 criminal
  counts, including conspiracy to steal trade secrets and bank fraud, after a
  three-month trial in New York (verdict 24 Nov, reported 25 Nov).
- **Riyadh tower hit again:** a Houthi drone strike hit the PIF Tower, Riyadh's
  tallest building, for the second time in less than a week, wounding 11
  people; the Saudi-led coalition vowed a decisive response.
- **Sarkozy to stand trial:** French officials ordered a corruption case
  against former president Nicolas Sarkozy and his wife Carla Bruni to trial,
  with a pre-trial hearing set for 1 April 2027.
- **Iraq seizes oilfields:** Iraq's premier ordered federal forces to seize
  oilfields and crossings in Kurdish-run regions.
- **Ticker:** NATO plans early-warning aircraft for Poland; WHO evacuates staff
  from an Ebola hospital in DR Congo amid fighting; Zelenskiy presses NATO for
  membership and more air defence.

Sources: Reuters, CNN, AFP, The New York Times, AP, Dawn, The Straits Times.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the front-page
image shipped in `assets/entry.jpg` byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png`, after verifying the gate's limits: a whole
JPEG, at most 1 MiB, 1024 by 1024 pixels, ending in its EOI marker. The output
file is left world-readable (mode 0644).

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs produce byte-identical output (verified with SHA-256).

## License

MIT
