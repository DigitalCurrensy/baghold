# Copyright 2026 Digital Currensy Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Score each row of a pit CSV. Empty fields are missing."""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

from .bag import from_ends, hold
from .record import finish
from .letter import void_fraction_of

HEADER = ("mouth_m", "floor_void_fraction", "drop_m", "floor_slope_deg")
ENDS_HEADER = ("x1", "y1", "z1", "x2", "y2", "z2", "n_invalid", "n_cells")


def _parse_float(value: str | None) -> float | None:
    if value is None:
        raise ValueError("missing column")
    text = value.strip()
    if text == "":
        return None
    return float(text)



def _show(value: float | None) -> str:
    if value is None:
        return "missing"
    if not math.isfinite(value):
        return "bad"
    return f"{value:.10g}"


def score_csv(path: Path) -> list[str]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        names = tuple(reader.fieldnames or ())
        if names == ENDS_HEADER:
            verdicts = []
            for row in reader:
                ends = [_parse_float(row[name]) for name in ("x1", "y1", "z1", "x2", "y2", "z2")]
                n_invalid = _parse_float(row["n_invalid"])
                n_cells = _parse_float(row["n_cells"])
                if None in ends or n_invalid is None or n_cells is None:
                    mouth = drop = slope = voids = None
                else:
                    mouth, drop, slope = from_ends(*ends)
                    voids = void_fraction_of(n_invalid, n_cells)
                word = hold(mouth, voids, drop, slope)
                verdicts.append(
                    f"{word} mouth={_show(mouth)} void={_show(voids)} drop={_show(drop)} slope={_show(slope)}"
                )
            return verdicts
        if names != HEADER:
            raise ValueError(
                "header must be mouth_m,floor_void_fraction,drop_m,floor_slope_deg"
            )
        verdicts: list[str] = []
        for row in reader:
            mouth = _parse_float(row["mouth_m"])
            voids = _parse_float(row["floor_void_fraction"])
            drop = _parse_float(row["drop_m"])
            slope = _parse_float(row["floor_slope_deg"])
            word = hold(mouth, voids, drop, slope)
            verdicts.append(
                f"{word} mouth={_show(mouth)} void={_show(voids)} drop={_show(drop)} slope={_show(slope)}"
            )
    return verdicts


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in args
    args = [item for item in args if item != "--json"]
    if len(args) != 1:
        print("usage: python -m baghold examples/pit.csv [--json]", file=sys.stderr)
        return 2
    try:
        lines = score_csv(Path(args[0]))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    words = [line.split()[0] for line in lines]
    return finish("baghold", "A skylight is not a shelter.", lines, as_json, words)


if __name__ == "__main__":
    raise SystemExit(main())
