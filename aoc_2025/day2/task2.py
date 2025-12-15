from pathlib import Path

def parse_csv(input_str: str) -> list[str]:
    return input_str.split(',')

def parse_ranges(ranges_str: list[str]) -> list[tuple[(str,str)]]:
    return [tuple(range_string.split('-')) for range_string in ranges_str]

def is_invalid_id(current: str):
    
    for curr_subrange_len in range(1, len(current)):
        # Optimization, if the length of substring isn't a divisor of 
        # the full length, the processing can be skipped
        if len(current) % curr_subrange_len != 0:
            continue

        reference_subrange = current[:curr_subrange_len]

        # Previous condition makes sure we don't exit out of range in the next checks
        for i in range(0, len(current) - curr_subrange_len, curr_subrange_len):
            check_subrange = current[curr_subrange_len+i:curr_subrange_len*2+i]

            # If finds the one substring that is not equal to first, immediately fail
            if reference_subrange != check_subrange:
                break

            # If True, we've found a repeating pattern
            if curr_subrange_len*2 + i == len(current):
                return True
    
    return False

def get_invalid_in_range(start: str, end: str) -> list[int]:
    result: list[int] = []

    current = start
    
    while int(current) <= int(end):
        
        if is_invalid_id(current):
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