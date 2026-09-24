import unittest

from rota import Slot, owner_at


class RotaTests(unittest.TestCase):
    def test_adjacent_handoff(self):
        slots = [Slot(0, 10, "Ada"), Slot(10, 20, "Bo")]
        self.assertEqual(owner_at(slots, 9), "Ada")
        self.assertEqual(owner_at(slots, 10), "Bo")
        self.assertIsNone(owner_at(slots, 20))

    def test_overlapping_slots_rejected(self):
        with self.assertRaises(ValueError):
            owner_at([Slot(0, 10, "Ada"), Slot(9, 20, "Bo")], 9)

    def test_invalid_interval_rejected(self):
        with self.assertRaises(ValueError):
            owner_at([Slot(10, 10, "Ada")], 10)
