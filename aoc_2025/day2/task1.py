from pathlib import Path

def parse_csv(input_str: str) -> list[str]:
    return input_str.split(',')

def parse_ranges(ranges_str: list[str]) -> list[tuple[(str,str)]]:
    return [tuple(range_string.split('-')) for range_string in ranges_str]

'''
Checks if the number has odd number of digits, and if so, 
returns next number that has even number of digitis.
'''
def skip_odd_range(current: str) -> str:
    if len(current) % 2 != 0:
        # start of range is with 1 (10, 1000, ...) followed by odd number of zeros
        current = '1' + '0' * len(current)
    return current

def get_invalid_in_range(start: str, end: str) -> list[int]:
    result: list[int] = []

    current = skip_odd_range(start)
    while int(current) <= int(end):
        current = skip_odd_range(current)

        num_digits_halved = int(len(current) / 2)

        if current[:num_digits_halved] == current[num_digits_halved:]:
            result.append(int(current))

        current = str(int(current) + 1)
    
    return result

def main(input_path: Path):
    data = None
    with input_path.open("r", encoding="utf-8") as f:
        data = parse_ranges(parse_csv(f.readline()))

    if data is None:
        print("There was a problem with reading and parsing the data.")

    invalid_list = []
    for start, end in data:
       invalid_list.extend(get_invalid_in_range(start, end))

    print(sum(invalid_list))

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    main(input_path)