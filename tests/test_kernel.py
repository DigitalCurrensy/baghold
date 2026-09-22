"""BAGHOLD kernel tests. Catalog freeze. Scorer idle."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from baghold.bag import hold  # noqa: E402
from baghold.bags import INGENII, LACUS_MORTIS, MHP, MTP  # noqa: E402


class HoldTests(unittest.TestCase):
    def test_pinch_first(self) -> None:
        self.assertEqual(hold(20, 0.02, 10, 5), "pinch")
        self.assertEqual(hold(88, 0.4, 133, 15), "voids")
        self.assertEqual(hold(49, 0.08, 60, 5), "drop")
        self.assertEqual(hold(49, 0.08, 10, 25), "slope")
        self.assertEqual(hold(49, 0.08, 10, 5), "ok")
        self.assertEqual(hold(30, 0.15, 30, 20), "ok")
        self.assertEqual(hold(88, 0.02, None, 5), "ok")

    def test_catalog_named_not_scored_as_wave0_verdict(self) -> None:
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


if __name__ == "__main__":
    unittest.main()
