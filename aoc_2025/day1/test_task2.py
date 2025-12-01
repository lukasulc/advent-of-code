import unittest
from task1 import dial_zero_counter
from task2 import main, custom_condition

class TestTask1(unittest.TestCase):
    def test_single_right_rotation(self):
        self.assertEqual(main(), 6294)

    def test_single_right_rotation(self):
        self.assertEqual(dial_zero_counter(["R10"], condition=custom_condition), (0, 60))

    def test_single_left_rotation(self):
        self.assertEqual(dial_zero_counter(["L20"], condition=custom_condition), (0, 30))

    def test_multiple_rotations(self):
        rotations = ["R10", "L5", "R3"]
        # start at 50 -> R10=60 -> L5=55 -> R3=58
        self.assertEqual(dial_zero_counter(rotations, condition=custom_condition), (0, 58))

    def test_wrap_around(self):
        # start at 50 -> R60 = (50+60)%100 = 10
        self.assertEqual(dial_zero_counter(["R60"], condition=custom_condition), (1, 10))

    def test_handles_newline_strings(self):
        # simulates readlines() output containing newlines
        rotations = ["R4\n", "L2\n"]
        # start 50 -> R4=54 -> L2=52
        self.assertEqual(dial_zero_counter(rotations, condition=custom_condition), (0, 52))

    def test_special_case(self):
        rotations = [
            ("L49", 1, 0),
            ("L101", 0, 2),
        ]
        total_zeros = 0
        result_dial = 50
        for rotation, expected_position, expected_zeros in rotations:
            with self.subTest(rotation=rotation):
                num_zeros, result_dial = dial_zero_counter([rotation], condition=custom_condition, current=result_dial)
                total_zeros += num_zeros
                self.assertEqual((total_zeros, result_dial), (expected_zeros, expected_position))

    def test_official_example(self):
        rotations = [
            ("L68", 82, 1),
            ("L30", 52, 1),
            ("R48", 0, 2),
            ("L5", 95, 2),
            ("R60", 55, 3),
            ("L55", 0, 4),
            ("L1", 99, 4),
            ("L99", 0, 5),
            ("R14", 14, 5),
            ("L82", 32, 6),
        ]
        total_zeros = 0
        result_dial = 50
        for rotation, expected_position, expected_zeros in rotations:
            with self.subTest(rotation=rotation):
                num_zeros, result_dial = dial_zero_counter([rotation], condition=custom_condition, current=result_dial)
                total_zeros += num_zeros
                self.assertEqual((total_zeros, result_dial), (expected_zeros, expected_position))

    def test_expanded_example(self):
        rotations = [
            ("L68", 82, 1),
            ("L30", 52, 1),
            ("R48", 0, 2),
            ("L5", 95, 2),
            ("R60", 55, 3),
            ("L55", 0, 4),
            ("L1", 99, 4),
            ("L99", 0, 5),
            ("R14", 14, 5),
            ("L82", 32, 6),
            ("L32", 0, 7),
            ("R1", 1, 7),
            ("L1", 0, 8),
            ("L1", 99, 8),
            ("R1", 0, 9),
            ("L100", 0, 10),
            ("L99", 1, 10),
            ("R1000", 1, 20),
            ("L1000", 1, 30),
            ("L2", 99, 31),
            ("R1", 0, 32),
            ("R1", 1, 32),
            ("L1", 0, 33),
            ("R99", 99, 33),
            ("L99", 0, 34),
            ("L1", 99, 34),
            ("R2", 1, 35),
            ("L1", 0, 36),
            ("L101", 99, 37),
            ("R1", 0, 38),
            ("R101", 1, 39)
        ]
        total_zeros = 0
        result_dial = 50
        for rotation, expected_position, expected_zeros in rotations:
            with self.subTest(rotation=rotation):
                num_zeros, result_dial = dial_zero_counter([rotation], condition=custom_condition, current=result_dial)
                total_zeros += num_zeros
                self.assertEqual((total_zeros, result_dial), (expected_zeros, expected_position))


if __name__ == "__main__":
    unittest.main()
