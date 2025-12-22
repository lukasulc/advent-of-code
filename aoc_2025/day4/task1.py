from pathlib import Path
from collections import deque
from collections.abc import Callable

def check_occupancy(rows: deque, levels: int, condition: Callable, start_row: int = None):
    result = 0
    if start_row == None:
        start_row = levels

    len_of_row = len(rows[start_row])

    for i in range(len_of_row):
        num_rolls = 0
        for level_i in range(-levels, levels):
            if i + level_i < 0 or i + level_i > len_of_row:
                continue
            for level_j in range(-start_row, levels):
                if start_row+level_j > len(rows):
                    break
                if rows[start_row+level_j][i+level_i] == "@":
                    num_rolls += 1
        result += condition(num_rolls)
        
    return result


def main(input_path: Path, levels = 1):
    queue = deque(maxlen=1+2*levels)
    result = 0

    with input_path.open("r", encoding="utf-8") as f:
        queue.append(f.readline())
        condition = (lambda x: x < 4)

        # The initial setup until the start_idx is at the middle of the matrix
        for i in range(levels):
            queue.append(f.readline())
            result += check_occupancy(queue, levels, condition, i)

        # Normal case, start_idx is at the middle of the matrix
        for line in f:
            queue.append(line)
            result += check_occupancy(queue, levels, condition)

        # End of the algo, no more lines to read but have to check until the end of the array
        queue.popleft()
        while len(queue) > levels:
            result += check_occupancy(queue, levels, condition, start_row=levels)
            queue.popleft()
        
        print(result)
        return result

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    main(input_path)