import unittest
from task1 import get_largest_joltage

class TestTask1(unittest.TestCase):

    def test_offical_example(self):
        banks = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        solutions = [
            98,
            89,
            78,
            92,
        ]
        for bank, solution in zip(banks, solutions):
            self.assertEqual(get_largest_joltage(bank), solution)


if __name__ == "__main__":
    unittest.main()
