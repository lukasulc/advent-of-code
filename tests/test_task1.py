import unittest
from pathlib import Path
import importlib.util


# load task1.py directly (workspace isn't packaged)
task1_path = Path(__file__).resolve().parents[1] / "2025" / "day1" / "task1.py"
spec = importlib.util.spec_from_file_location("task1", task1_path)
task1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task1)


class TestDialZeroCounter(unittest.TestCase):
    def test_single_right_rotation(self):
        self.assertEqual(task1.dialZeroCounter(["R10"], current=50, max_range=100), (0, 60))

    def test_single_left_rotation(self):
        self.assertEqual(task1.dialZeroCounter(["L20"], current=50, max_range=100), (0, 30))

    def test_multiple_rotations(self):
        rotations = ["R10", "L5", "R3"]
        # start at 50 -> R10=60 -> L5=55 -> R3=58
        self.assertEqual(task1.dialZeroCounter(rotations, current=50, max_range=100), (0, 58))

    def test_wrap_around(self):
        # start at 50 -> R60 = (50+60)%100 = 10
        self.assertEqual(task1.dialZeroCounter(["R60"], current=50, max_range=100), (0, 10))

    def test_handles_newline_strings(self):
        # simulates readlines() output containing newlines
        rotations = ["R4\n", "L2\n"]
        # start 50 -> R4=54 -> L2=52
        self.assertEqual(task1.dialZeroCounter(rotations, current=50, max_range=100), (0, 52))

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
        self.assertEqual(task1.dialZeroCounter(rotations, current=50, max_range=100), (3, 32))


if __name__ == "__main__":
    unittest.main()
