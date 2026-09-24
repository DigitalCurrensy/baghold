# BAGHOLD

[![check](https://github.com/DigitalCurrensy/baghold/actions/workflows/check.yml/badge.svg)](https://github.com/DigitalCurrensy/baghold/actions/workflows/check.yml)

For a pit or skylight check when you have the two ends.

Mouth, drop, grade, and void fraction are computed from those ends. A skylight is not a shelter.

Ok is not a decision to enter.

## Install

```bash
pip install -e .
PYTHONPATH=src python -m unittest tests.test_kernel
```

## First command

```bash
PYTHONPATH=src python -m baghold examples/ends.csv
```

The rest of this file is the rule that command prints.

## Record

`--json` prints one object. The process exit code is that object's `exit`. 0 is a pass word (`ok`, `pass`, `scored`, `path`). 1 is a refusal. 2 means the file could not be read. `keep` is false. `absent` is what this output does not contain: a stamp, measured basin months, and the points inside a `.laz` file.

This object is not WaterML and it is not a USGS response.

```json
{
  "absent": [
    "stamp",
    "measured_months",
    "laz_points"
  ],
  "desk": "baghold",
  "exit": 0,
  "formula": "A skylight is not a shelter.",
  "keep": false,
  "rows": [
    {
      "line": "ok mouth=40 void=0.02 drop=10 slope=14.03624347",
      "word": "ok"
    }
  ],
  "word": "ok"
}
```


This does not survey a cave. A collapsed skylight is not a shelter. `examples/ends.csv` computes the mouth, the drop, and the floor grade from two points, and the void fraction from a count. Ok is not a shelter.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited.

## What it decides

A pit-mouth score from the numbers the caller supplies. Passing the mouth does not make the pit a habitat.

## The rule

`hold` returns the first gate that trips, in this order:

1. mouth, floor void fraction, or floor slope is missing → `missing`
2. mouth is negative, floor slope is negative, a supplied drop is negative, or the floor void fraction is under 0 or over 1 → `missing`
3. mouth is under 30 m → `pinch`
4. floor void fraction is over 0.15 → `voids`
5. a supplied drop is over 30 m → `drop`
6. floor slope is over 20 degrees → `slope`
7. otherwise → `ok`

A missing drop is not a required input and is not a fail by itself. The line prints mouth, void fraction, drop, and floor slope next to the word. A non-finite number is missing. A negative drop is missing. A negative measure, or a void fraction outside 0 to 1, is missing. Equal to a limit does not trip that gate: mouth 30 m, void fraction 0.15, drop 30 m, and slope 20 degrees continue, so `hold(30, 0.15, 30, 20)` is `ok`. `hold(88, 0.02, None, 5)` is `ok`.

## Worked rows

`examples/pit.csv` columns are exactly `mouth_m,floor_void_fraction,drop_m,floor_slope_deg`. Empty fields are missing. Worked rows are not a customer survey.

## What it will not do

- Survey a cave.
- Treat a collapsed skylight as a shelter.
- Fetch an elevation model. The caller supplies the mouth measurements.

## Run

```
git clone <this repo>
cd baghold
PYTHONPATH=src python -m unittest tests.test_kernel
PYTHONPATH=src python -m baghold examples/pit.csv
```

Python 3.11 or newer. No third-party packages.

Copyright 2026 Digital Currensy Inc. Apache-2.0.
