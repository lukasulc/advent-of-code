# 0x434C49434B is "CLICK"

from pathlib import Path
from task1 import dial_zero_counter, calculate_dial_position

def custom_condition(current: int, rotation: int, max_range: int) -> int:
    dial_position = calculate_dial_position(current, rotation, max_range)
    if current == 0 and rotation < 0:
        current = max_range - 1
    q, r = divmod(current + rotation, max_range)
    print(f"Custom condition: current={current}, rotation={rotation}, dial_position={dial_position}, q={q}, r={r}")
    if q < 0:
        return (abs(q), dial_position)
    if q > 0:
        return (q, dial_position)
    if r == 0:
        return (1, dial_position)
    return (0, dial_position)

def main():
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    with input_path.open("r", encoding="utf-8") as f:
        # possible to read lines one by one in the case of a really large file
        result, _ = dial_zero_counter(
            f.readlines(), 
            condition=custom_condition)
        return result

if __name__ == "__main__":
    print(main())