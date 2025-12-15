import unittest
from task2 import get_invalid_in_range

class TestTask1(unittest.TestCase):
    
    def test_dummy_example(self):
        ranges = [
            ("12341234", "12341234"),
            ("123123123", "123123123"),
            ("1212121212", "1212121212"),
            ("1111111", "1111111"),
        ]
        solutions = [
            [12341234],
            [123123123],
            [1212121212],
            [1111111],
        ]
        for (start, end), solutions in zip(ranges, solutions):
            self.assertEqual(get_invalid_in_range(start, end), solutions)

    def test_offical_example(self):
        ranges = [
            ("11", "22"),
            ("95", "115"),
            ("998", "1012"),
            ("1188511880", "1188511890"),
            ("222220", "222224"),
            ("1698522", "1698528"),
            ("446443", "446449"),
            ("38593856", "38593862"),
            ("565653", "565659"),
            ("824824821", "824824827"),
            ("2121212118", "2121212124"),
        ]
        solutions = [
            [11, 22],
            [99, 111],
            [999, 1010],
            [1188511885],
            [222222],
            [],
            [446446],
            [38593859],
            [565656],
            [824824824],
            [2121212121],
        ]
        for (start, end), solutions in zip(ranges, solutions):
            self.assertEqual(get_invalid_in_range(start, end), solutions)


if __name__ == "__main__":
    unittest.main()
