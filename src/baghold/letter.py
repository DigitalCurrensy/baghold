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

"""HOLD LETTER. Paper on the bag. Fail still issues. Not a certificate. Not survey-grade."""

from __future__ import annotations

from .bag import hold
from .bags import MHP, MTP
from .walk import MTP_WALK

TITLE = "HOLD LETTER"
OFFER = "Unsigned. Not an invoice."
COUNSEL = "unsigned"
WORD_CAP = 80
VOID_FORMULA = "n_invalid / n_cells"
MTP_WINDOW = {"n_invalid": 40, "n_cells": 100, "void_fraction": 0.40}
MHP_WINDOW = {"n_invalid": 8, "n_cells": 100, "void_fraction": 0.08}


def _words(body: str) -> int:
    return len([w for w in body.split() if w])


def void_fraction_of(n_invalid: float, n_cells: float) -> float | None:
    if n_cells <= 0 or n_invalid < 0 or n_invalid > n_cells:
        return None
    return n_invalid / n_cells


def compile_letter(kind: str) -> dict:
    if kind == "mhp":
        body = (
            "No letter issued. Marius Hills pit is a different bag. "
            "One walk remains BAG-MTP-TRANQ. A rille skylight is not this mouth. "
            "Not this letter. Not survey-grade."
        )
        return {
            "title": TITLE,
            "issued": False,
            "stamp": "refused",
            "bag_id": MHP["id"],
            "why": "not_this_letter",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "do_not_enter": False,
            "mhp_is_this_letter": False,
            "not_a_certificate": True,
            "not_survey_grade": True,
        }
    if kind == "okform":
        body = (
            "HOLD LETTER. Synthetic walk-in vs SYN-HOLD-FLAT. OK. Not BAG-MTP-TRANQ. "
            "Different bag. ok is not survey-grade. Not a certificate. Counsel unsigned."
        )
        return {
            "title": TITLE,
            "issued": True,
            "stamp": "ok",
            "bag_id": "SYN-BAG-FLAT",
            "why": "ok_form_other_bag",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "do_not_enter": False,
            "mhp_is_this_letter": False,
            "not_a_certificate": True,
            "not_survey_grade": True,
        }
    if kind == "undeclared":
        body = (
            "No letter issued. BAG-MTP-TRANQ identity is off. Undeclared is not a bag. "
            "Not a certificate. Not survey-grade."
        )
        return {
            "title": TITLE,
            "issued": False,
            "stamp": "refused",
            "bag_id": MTP_WALK["id"],
            "why": "undeclared_identity",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "do_not_enter": False,
            "mhp_is_this_letter": False,
            "not_a_certificate": True,
            "not_survey_grade": True,
        }
    stamp = hold(MTP["mouth_m"], MTP["floor_void_fraction"], MTP["drop_m"], MTP["floor_slope_deg"])
    body = (
        "HOLD LETTER. BAG-MTP-TRANQ vs SYN-HOLD-MTP. VOIDS. Floor 40 of 100 cells invalid. "
        "LOLA gap swallows the mouth. Famous is not a hold. Not survey-grade. Counsel unsigned."
    )
    return {
        "title": TITLE,
        "issued": True,
        "stamp": stamp,
        "bag_id": MTP["id"],
        "why": stamp,
        "body": body,
        "words": _words(body),
        "counsel": COUNSEL,
        "do_not_enter": True,
        "mhp_is_this_letter": False,
        "not_a_certificate": True,
        "not_survey_grade": True,
        "void_fraction": MTP_WINDOW["void_fraction"],
        "n_invalid": MTP_WINDOW["n_invalid"],
        "n_cells": MTP_WINDOW["n_cells"],
    }
