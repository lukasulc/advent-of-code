import unittest
from task2 import get_largest_joltage

class TestTask1(unittest.TestCase):
    def test_dummy_example(self):
        banks = [
            "821111111119",
        ]
        solutions = [
            821111111119,
        ]
        for bank, solution in zip(banks, solutions):
            self.assertEqual(get_largest_joltage(bank), solution)

    def test_last_numbers_example(self):
        banks = [
            "8121111111119",
            "3222222212222211211322212225122222252212233221262132222211112313222322122232122222232222222223162122"
        ]
        solutions = [
            821111111119,
            633333362122,
        ]
        for bank, solution in zip(banks, solutions):
            self.assertEqual(get_largest_joltage(bank), solution)

    def test_offical_example(self):
        banks = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        solutions = [
            987654321111,
            811111111119,
            434234234278,
            888911112111,
        ]
        for bank, solution in zip(banks, solutions):
            self.assertEqual(get_largest_joltage(bank), solution)


if __name__ == "__main__":
    unittest.main()
