"""BAG HOLD COUNSEL PASS. Unsigned. MHP is not this letter. A tube is not this mouth."""

from __future__ import annotations

TITLE = "BAG HOLD COUNSEL PASS"
OFFER = "Unsigned. Not an invoice."
COUNSEL = "unsigned"
WORD_CAP = 80
VOID_FORMULA = "n_invalid / n_cells"
MTP_WINDOW = {"n_invalid": 40, "n_cells": 100, "void_fraction": 0.40}
MHP_WINDOW = {"n_invalid": 8, "n_cells": 100, "void_fraction": 0.08}


def _words(body: str) -> int:
    return len([w for w in body.split() if w])


def void_edge(n_invalid: float, n_cells: float) -> float | None:
    if n_invalid != n_invalid or n_cells != n_cells:
        return None
    if int(n_invalid) != n_invalid or int(n_cells) != n_cells:
        return None
    if n_cells <= 0 or n_invalid < 0 or n_invalid > n_cells:
        return None
    return n_invalid / n_cells


def compile_counsel(kind: str) -> dict:
    if kind == "mhp-letter":
        body = (
            "No counsel pass. Marius Hills pit is a different bag. One walk remains BAG-MTP-TRANQ. "
            "A rille skylight is not this mouth. Mouth 49 sits. Void 0.08 sits. Drop 60 trips. "
            "Not this letter. Not a certificate."
        )
        return {
            "title": TITLE,
            "issued": False,
            "stamp": "refused",
            "why": "mhp_is_not_this_letter",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "signed": False,
            "not_survey_grade": True,
        }
    if kind == "tube-mouth":
        body = (
            "No counsel pass. Carrer 2024 west radar void is a tube, not this mouth. "
            "Conduit ~45 m is named, not scored. A cave beyond the skylight is TUBEWALK. "
            "One bag remains BAG-MTP-TRANQ. Not a certificate."
        )
        return {
            "title": TITLE,
            "issued": False,
            "stamp": "refused",
            "why": "tube_is_not_this_mouth",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "signed": False,
            "not_survey_grade": True,
        }
    if kind == "pretty-hold":
        body = (
            "No counsel pass. A pretty cave is not a hold. Google Moon is not a score. "
            "Floor 0.40 still fails. Famous is not a door. Do-not-enter is abort. "
            "Not a certificate. Not survey-grade."
        )
        return {
            "title": TITLE,
            "issued": False,
            "stamp": "refused",
            "why": "pretty_is_not_a_hold",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "signed": False,
            "not_survey_grade": True,
        }
    if kind == "unnamed-sign":
        body = (
            "No counsel pass. Counsel unnamed. Engineer of record unnamed. "
            "A checked box is not a wet signature. This console does not mint ink. "
            "Not a certificate. Research tool."
        )
        return {
            "title": TITLE,
            "issued": False,
            "stamp": "refused",
            "why": "unnamed_signature",
            "body": body,
            "words": _words(body),
            "counsel": COUNSEL,
            "signed": False,
            "not_survey_grade": True,
        }
    body = (
        "BAG HOLD COUNSEL PASS. Research tool. Not a certificate. Not survey-grade. "
        "Mare Tranquillitatis pit still VOIDS. Floor 40 of 100 cells invalid. Counsel unsigned. "
        "Engineer of record unsigned."
    )
    return {
        "title": TITLE,
        "issued": True,
        "stamp": "unsigned",
        "why": "compiled_unsigned",
        "body": body,
        "words": _words(body),
        "counsel": COUNSEL,
        "signed": False,
        "not_survey_grade": True,
    }
