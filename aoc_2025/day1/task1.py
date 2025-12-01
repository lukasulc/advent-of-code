from pathlib import Path
from typing import Callable

def calculate_dial_position(current: int, rotation: int, max_range: int) -> int:
    """Calculate the new dial position after applying the rotation."""
    return (current + rotation) % max_range

def custom_condition(current: int, rotation: int, max_range: int) -> tuple[int, int]:
    dial_position = calculate_dial_position(current, rotation, max_range)
    return (1, dial_position) if current % max_range == 0 else (0, dial_position)

def dial_zero_counter(
        rotations: list[str] = [],
        current = 50,
        max_range = 100,
        condition: Callable[[int, int, int],tuple[int,int]] = custom_condition):
    """Apply a list of rotations and return the final dial value.

    rotations - iterable of strings like 'R10' or 'L5'
    """
    num_zeros = 0

    for rotation in rotations:
        # Read the digits and convert to an integer
        rotation_number = int(rotation[1:])

        # Check on which side we should rotate
        if rotation[0] == "L":
            rotation_number = -rotation_number

        increment, current = condition(current, rotation_number, max_range)
        print(f"Rotation {rotation} results in dial at {current}")
        if increment > 0:
            print(f"Dial hit zero {increment} times!")
            num_zeros += increment

    return num_zeros, current

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    with input_path.open("r", encoding="utf-8") as f:
        # possible to read lines one by one in the case of a really large file
        result, _ = dial_zero_counter(f.readlines())
        print(result)