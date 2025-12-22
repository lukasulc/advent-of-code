from pathlib import Path
from collections import deque
from collections.abc import Callable

def check_occupancy(rows: deque, levels: int, condition: Callable):
    result = 0

    len_of_row = len(rows[0])

    for i in range(levels, len_of_row-levels):
        num_rolls = 0

        if rows[levels][i] != "@":
            continue

        for level_i in range(-levels, levels + 1):
            for level_j in range(-levels, levels + 1):
                if level_i == 0 and level_j == 0:
                    continue

                if rows[levels+level_j][i+level_i] == "@":
                    num_rolls += 1
        result += condition(num_rolls)
        
    return result


def main(input_path: Path, levels = 1):
    queue = deque(maxlen=1+2*levels)
    result = 0

    with input_path.open("r", encoding="utf-8") as f:
        queue.append(('.'*levels)+f.readline().strip()+('.'*levels))
        condition = (lambda x: x < 4)

        filler_string = '.'*(len(queue[0]))

        for _ in range(levels):
            queue.appendleft(filler_string)

        # Normal case, start_idx is at the middle of the matrix
        for line in f:
            queue.append(('.'*levels)+line.strip()+('.'*levels))
            result += check_occupancy(queue, levels, condition)

        # End of the algo, no more lines to read but have to check until the end of the array
        for _ in range(levels):
            queue.append(filler_string)
            result += check_occupancy(queue, levels, condition)
        
        print(result)
        return result

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    main(input_path)