# 0x434C49434B is "CLICK"

from pathlib import Path
from task1 import dial_zero_counter, calculate_dial_position

def custom_condition(current: int, rotation: int, max_range: int) -> int:
    dial_position = calculate_dial_position(current, rotation, max_range)

    if current == 0:
        return divmod(abs(rotation), max_range)[0], dial_position

    # Assume rotation can't be zero
    tmp_dial = current + rotation
    if tmp_dial == 0:
        return 1, dial_position
    
    if tmp_dial < 0:
        return divmod(-tmp_dial, max_range)[0] + 1, dial_position
        
    return divmod(tmp_dial, max_range)[0], dial_position

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