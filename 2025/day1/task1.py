from pathlib import Path

def dialZeroCounter(rotations: list[str] = [], current = 50, max_range = 100):
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

        current = (current + rotation_number + max_range) % max_range
        print(f"Rotation {rotation} results in dial at {current}")

        if current == 0:
            print("Dial hit zero!")
            num_zeros += 1

    return num_zeros, current

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    with input_path.open("r", encoding="utf-8") as f:
        # possible to read lines one by one in the case of a really large file
        result, _ = dialZeroCounter(f.readlines())
        print(result)