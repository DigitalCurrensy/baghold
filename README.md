# BAGHOLD

The bag is the goal. A lunar pit looks like a cave you can enter. Score the hold.

**Owner:** Digital Currensy Inc.
**Status:** Private. Independent tool. Not a NASA Space Apps 2026 submission.
**License of our code:** Apache-2.0

## One sentence

A lunar pit looks like a cave you can enter. Score the hold against mouth pinch, floor void, drop, and floor slope — or say the bag is not a hold.

## Wave freeze

- W0 catalog: Mare Tranquillitatis pit (Wagner 2022) and Marius Hills pit (Haruyama 2009 / Wagner 2022). bag.py named, not run.
- W1 hold scorer: bag.py ported. Pinch first. MTP fails voids. MHP fails drop.

W2 bad-bag walk waits. TUBEWALK locked.

## bag.py

```
if mouth_m < 30: pinch
elif floor_void_fraction > 0.15: voids
elif drop_m is not None and drop_m > 30: drop
elif floor_slope_deg > 20: slope
else: ok
```

Pinch first. Equality sits. DEM unfetched.

## What it is not

- Not FEASFRONT lighting. A dark pit is not a hold.
- Not DOSEPATH occupancy. The shelter bag is a graph box, not this mouth.
- Not PINFAULT pin score. West crater is not this hold.
- Not RIMKEEP. A bag is a goal you enter. A rim keep is a box you do not.
- Not Mare Ingenii or Lacus Mortis as this catalog.
- Not TUBEWALK.

## Run

```
PYTHONPATH=src python -m unittest tests.test_kernel
```
