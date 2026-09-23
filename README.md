# BAGHOLD

This does not survey a cave. A collapsed skylight is not a shelter. The caller supplies the mouth measurements.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited.

## What it decides

A pit-mouth score from the numbers the caller supplies. Passing the mouth does not make the pit a habitat.

## The rule

`hold` returns the first gate that trips, in this order:

1. mouth, floor void fraction, or floor slope is missing → `missing`
2. mouth is under 30 m → `pinch`
3. floor void fraction is over 0.15 → `voids`
4. a supplied drop is over 30 m → `drop`
5. floor slope is over 20 degrees → `slope`
6. otherwise → `ok`

A missing drop is not a required input and is not a fail by itself. Equal to a limit does not trip that gate: mouth 30 m, void fraction 0.15, drop 30 m, and slope 20 degrees continue, so `hold(30, 0.15, 30, 20)` is `ok`. `hold(88, 0.02, None, 5)` is `ok`.

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
