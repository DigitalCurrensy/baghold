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

"""BAGHOLD kernel tests. Counsel pass. MHP is not this letter."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from baghold.bag import hold  # noqa: E402
from baghold.bags import INGENII, LACUS_MORTIS, MHP, MTP  # noqa: E402
from baghold.counsel import compile_counsel, void_edge  # noqa: E402
from baghold.letter import MTP_WINDOW, VOID_FORMULA, compile_letter, void_fraction_of  # noqa: E402


class HoldTests(unittest.TestCase):
    def test_pinch_first(self) -> None:
        self.assertEqual(hold(20, 0.02, 10, 5), "pinch")
        self.assertEqual(hold(88, 0.4, 133, 15), "voids")
        self.assertEqual(hold(49, 0.08, 60, 5), "drop")
        self.assertEqual(hold(49, 0.08, 10, 25), "slope")
        self.assertEqual(hold(49, 0.08, 10, 5), "ok")
        self.assertEqual(hold(30, 0.15, 30, 20), "ok")
        self.assertEqual(hold(88, 0.02, None, 5), "ok")

    def test_missing_required_input_is_not_a_pass(self) -> None:
        self.assertEqual(hold(None, 0.02, 10, 5), "missing")
        self.assertEqual(hold(49, None, 10, 5), "missing")
        self.assertEqual(hold(49, 0.02, 10, None), "missing")
        self.assertNotEqual(hold(None, None, None, None), "ok")

    def test_clear_pass(self) -> None:
        self.assertEqual(hold(100, 0.0, 0, 0), "ok")

    def test_clear_fail(self) -> None:
        self.assertEqual(hold(50, 0.5, 10, 5), "voids")

    def test_named_catalog_is_not_a_fetched_survey(self) -> None:
        self.assertEqual(MTP["id"], "BAG-MTP-TRANQ")
        self.assertEqual(MTP["lat"], 8.336)
        self.assertEqual(MTP["lon"], 33.222)
        self.assertEqual(MTP["mouth_m"], 88)
        self.assertEqual(MTP["drop_m"], 133)
        self.assertEqual(MTP["floor_void_fraction"], 0.40)
        self.assertFalse(MTP["fetched"])
        self.assertEqual(MHP["id"], "BAG-MHP-MARIUS")
        self.assertEqual(MHP["lat"], 14.091)
        self.assertEqual(MHP["lon"], 303.230)
        self.assertEqual(MHP["mouth_m"], 49)
        self.assertEqual(MHP["drop_m"], 60)
        self.assertEqual(MHP["floor_void_fraction"], 0.08)
        self.assertFalse(MHP["fetched"])
        self.assertEqual(hold(MTP["mouth_m"], MTP["floor_void_fraction"], MTP["drop_m"], MTP["floor_slope_deg"]), "voids")
        self.assertEqual(hold(MHP["mouth_m"], MHP["floor_void_fraction"], MHP["drop_m"], MHP["floor_slope_deg"]), "drop")

    def test_landmarks_not_this_catalog(self) -> None:
        self.assertFalse(INGENII["this_catalog"])
        self.assertFalse(LACUS_MORTIS["this_catalog"])
        self.assertEqual(INGENII["lat"], -35.948)
        self.assertEqual(LACUS_MORTIS["lat"], 44.962)


class WalkTests(unittest.TestCase):
    def test_mtp_walk_is_voids_and_frames_are_named(self) -> None:
        from baghold.walk import MTP_WALK, lunar_offset_m, score_mhp, score_published

        self.assertEqual(score_published(), "voids")
        self.assertEqual(score_mhp(), "drop")
        self.assertEqual(MTP_WALK["id"], "BAG-MTP-TRANQ")
        published = (MTP_WALK["lat"], MTP_WALK["lon"])
        self.assertEqual(round(lunar_offset_m(published, MTP_WALK["haruyama"])), MTP_WALK["haruyama_m"])
        self.assertEqual(round(lunar_offset_m(published, MTP_WALK["carrer"])), MTP_WALK["carrer_m"])
        self.assertEqual(MTP_WALK["lola_gap_m"], 500)
        self.assertFalse(MHP.get("this_walk", False))


class LetterTests(unittest.TestCase):
    def test_hold_letter_issues_voids_and_refuses_mhp(self) -> None:
        walk = compile_letter("walk")
        self.assertTrue(walk["issued"])
        self.assertEqual(walk["stamp"], "voids")
        self.assertEqual(walk["title"], "HOLD LETTER")
        self.assertTrue(walk["not_a_certificate"])
        self.assertTrue(walk["do_not_enter"])
        self.assertLessEqual(walk["words"], 80)
        mhp = compile_letter("mhp")
        self.assertFalse(mhp["issued"])
        self.assertEqual(mhp["why"], "not_this_letter")
        self.assertEqual(mhp["bag_id"], MHP["id"])
        self.assertEqual(void_fraction_of(40, 100), 0.40)
        self.assertEqual(void_fraction_of(15, 100), 0.15)
        self.assertIsNone(void_fraction_of(0, 0))
        self.assertEqual(VOID_FORMULA, "n_invalid / n_cells")
        self.assertEqual(MTP_WINDOW["n_invalid"], 40)


class CounselTests(unittest.TestCase):
    def test_compiled_unsigned(self) -> None:
        paper = compile_counsel("compiled")
        self.assertTrue(paper["issued"])
        self.assertEqual(paper["stamp"], "unsigned")
        self.assertFalse(paper["signed"])
        self.assertEqual(paper["title"], "BAG HOLD COUNSEL PASS")
        self.assertLessEqual(paper["words"], 80)

    def test_refused_remaps(self) -> None:
        mhp = compile_counsel("mhp-letter")
        self.assertFalse(mhp["issued"])
        self.assertEqual(mhp["why"], "mhp_is_not_this_letter")
        tube = compile_counsel("tube-mouth")
        self.assertEqual(tube["why"], "tube_is_not_this_mouth")
        pretty = compile_counsel("pretty-hold")
        self.assertEqual(pretty["why"], "pretty_is_not_a_hold")
        unnamed = compile_counsel("unnamed-sign")
        self.assertEqual(unnamed["why"], "unnamed_signature")
        self.assertIsNone(void_edge(0, 0))
        self.assertEqual(void_edge(15, 100), 0.15)
        self.assertEqual(void_edge(16, 100), 0.16)
        self.assertIsNone(void_edge(2.5, 100))


if __name__ == "__main__":
    unittest.main()
