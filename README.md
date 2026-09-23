# BAGHOLD

For a scout who thinks a lunar pit is a cave they can use.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited. The copyright notice is in NOTICE and at the top of each source file. Cited data and papers stay with their authors.
## What it decides

Hold, or not a hold. The mouth is the gate.

## The rule

A pit with voids at the mouth is not a hold. A pinch, a drop, or a slope past the limit fails. A missing depth or a missing identity fails closed. Passing the mouth does not make the pit a habitat.

## Worked cases

Mare Tranquillitatis and Marius Hills are named. The synthetic pits each force one gate. They are not a site a customer surveyed.

## What it will not do

- Pretty-print a skylight as a cave.
- Fetch an elevation model in order to print the score.
- Call a scored mouth a shelter.

## Run

```
git clone <this repo>
cd baghold
PYTHONPATH=src python -m unittest tests.test_kernel
```

Python 3.12. No third-party packages. The test is the demo.
