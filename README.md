# BAGHOLD

BAGHOLD scores a pit as a hold. A collapsed skylight is not a cave you can use.

**Owner:** Digital Currensy Inc.
**License:** Apache-2.0. Our code only. Cited maps stay with their authors.

## What it decides

Hold, or not a hold. The mouth is the gate.

## The rule

A pit with voids at the mouth is not a hold. A pinch, a drop, or a slope past the limit fails. A missing depth, equal sites, an undeclared identity, or missing inputs fail closed. Passing the mouth does not make the pit a habitat.

## Worked cases

Mare Tranquillitatis, Marius Hills, and synthetic pits in this repository. The synthetic cases each force one gate: walk-in, pinch, void, drop, slope, pinch first, a null drop, equal sites, an undeclared identity, or missing inputs. They are the desk’s cases, not a site a customer surveyed.

## What it will not do

- Pretty-print a skylight as a cave.
- Fetch an elevation model in order to print the score.
- Call a scored mouth a shelter.

## Run

```
PYTHONPATH=src python -m unittest tests.test_kernel
```

Notes under `docs/` are the build record. This page is the description.
