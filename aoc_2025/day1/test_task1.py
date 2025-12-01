import unittest
from task1 import dial_zero_counter

class TestTask1(unittest.TestCase):
    def test_single_right_rotation(self):
        self.assertEqual(dial_zero_counter(["R10"]), (0, 60))

    def test_single_left_rotation(self):
        self.assertEqual(dial_zero_counter(["L20"]), (0, 30))

    def test_multiple_rotations(self):
        rotations = ["R10", "L5", "R3"]
        # start at 50 -> R10=60 -> L5=55 -> R3=58
        self.assertEqual(dial_zero_counter(rotations), (0, 58))

    def test_wrap_around(self):
        # start at 50 -> R60 = (50+60)%100 = 10
        self.assertEqual(dial_zero_counter(["R60"]), (0, 10))

    def test_handles_newline_strings(self):
        # simulates readlines() output containing newlines
        rotations = ["R4\n", "L2\n"]
        # start 50 -> R4=54 -> L2=52
        self.assertEqual(dial_zero_counter(rotations), (0, 52))

    def test_official_example(self):
        rotations = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        self.assertEqual(dial_zero_counter(rotations), (3, 32))


if __name__ == "__main__":
    unittest.main()
