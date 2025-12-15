from pathlib import Path


def get_largest_joltage(large_num_string: str) -> int:
    max1 = 1
    max2 = 1

    for i in range(len(large_num_string) - 1):

        if max1 == 9 and max2 == 9:
            break

        if max1 < int(large_num_string[i]):
            max1 = int(large_num_string[i])
            max2 = 1
        elif max2 < int(large_num_string[i]):
            max2 = int(large_num_string[i])        

    last_num = int(large_num_string[-1])
    max2 = max2 if max2 > last_num else last_num
    return 10 * max1 + max2 

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