import unittest
from task2 import main
from pathlib import Path

class TestTask1(unittest.TestCase):

    def test_offical_example(self):
        script_dir = Path(__file__).parent
        input_path = script_dir / "input_test.txt"
        self.assertEqual(main(input_path), 43)


if __name__ == "__main__":
    unittest.main()
