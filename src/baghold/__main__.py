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
import sys
from pathlib import Path

from .bag import hold

HEADER = ("mouth_m", "floor_void_fraction", "drop_m", "floor_slope_deg")


def _parse_float(value: str | None) -> float | None:
    if value is None:
        raise ValueError("missing column")
    text = value.strip()
    if text == "":
        return None
    return float(text)


def score_csv(path: Path) -> list[str]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != HEADER:
            raise ValueError(
                "header must be mouth_m,floor_void_fraction,drop_m,floor_slope_deg"
            )
        verdicts: list[str] = []
        for row in reader:
            verdicts.append(
                hold(
                    _parse_float(row["mouth_m"]),
                    _parse_float(row["floor_void_fraction"]),
                    _parse_float(row["drop_m"]),
                    _parse_float(row["floor_slope_deg"]),
                )
            )
    return verdicts


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("usage: python -m baghold examples/pit.csv", file=sys.stderr)
        return 2
    try:
        for verdict in score_csv(Path(args[0])):
            print(verdict)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
