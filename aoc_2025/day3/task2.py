from pathlib import Path


def get_largest_joltage(large_num_string: str, num_batteries: int = 12) -> int:
    max_joltage = '1' * num_batteries

    for i in range(len(large_num_string)):
        for battery_idx in range(num_batteries):
            if i + num_batteries - battery_idx > len(large_num_string):
                continue
            if int(max_joltage[battery_idx]) < int(large_num_string[i]):
                max_joltage = max_joltage[:battery_idx] + large_num_string[i] + '1' * (num_batteries - battery_idx - 1)
                break

    return int(max_joltage) 

def main(input_path: Path):
    banks = []
    with input_path.open("r", encoding="utf-8") as f:
        banks = [line.rstrip() for line in f]

    joltage = 0
    for bank in banks:
        joltage += get_largest_joltage(bank)

    print(joltage)

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    main(input_path)