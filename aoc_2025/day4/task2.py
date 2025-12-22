from pathlib import Path
from collections import deque
from collections.abc import Callable

def check_occupancy(rows: deque, levels: int, condition: Callable):
    result = 0

    len_of_row = len(rows[0])
    row_for_next_step = rows[levels]

    for i in range(levels, len_of_row-levels):
        num_rolls = 0

        if rows[levels][i] == "X":
            row_for_next_step = row_for_next_step[:i] + "." + row_for_next_step[i+1:]

        if rows[levels][i] != "@":
            continue

        for level_i in range(-levels, levels + 1):
            for level_j in range(-levels, levels + 1):
                if level_i == 0 and level_j == 0:
                    continue

                if rows[levels+level_j][i+level_i] == "@":
                    num_rolls += 1

        if condition(num_rolls):
            result += 1
            row_for_next_step = row_for_next_step[:i] + "X" + row_for_next_step[i+1:]
        
    return result, row_for_next_step

def prefix_postfix_line(line: str, repeat: int, condition: bool, symbol = '.'):
    if condition:
        line = symbol * repeat + line + symbol * repeat
    return line


def iteration(input_path: Path, step_path: Path, levels: int, init = False):
    result = 0
    with input_path.open("r", encoding="utf-8") as f:
        queue = deque(maxlen=1+2*levels)
        queue.append(prefix_postfix_line(f.readline().strip(), levels, init))
        condition = (lambda x: x < 4)

        filler_string = '.'*(len(queue[0]))

        for _ in range(levels):
            queue.appendleft(filler_string)

        # Normal case, start_idx is at the middle of the matrix
        for line in f:
            queue.append(prefix_postfix_line(line.strip(), levels, init))
            if not init and not line.find("X"):
                continue
            occupied, new_row = check_occupancy(queue, levels, condition)
            result += occupied

            with step_path.open("a", encoding="utf-8") as g:
                g.write(new_row + '\n')

        # End of the algo, no more lines to read but have to check until the end of the array
        for _ in range(levels):
            queue.append(filler_string)
            if not init and not queue[0].find("X"):
                continue
            occupied, new_row = check_occupancy(queue, levels, condition)
            result += occupied

            with step_path.open("a", encoding="utf-8") as g:
                g.write(new_row + '\n')

    return result

def main(input_path: Path, levels = 1):
    result = 0
    current_iter = 1
    
    script_dir = Path(__file__).parent
    
    step_path_dir = script_dir / "step"
    Path(step_path_dir).mkdir(exist_ok=True)
    step_path = step_path_dir / f"step_{current_iter}.txt"
    

    # Clear file of contents
    with step_path.open("w", encoding="utf-8") as f:
        pass

    result += iteration(input_path, step_path, levels, init=True)
    occurances = None

    while occurances is None or occurances > 0:
        current_iter += 1

        input_path = step_path
        step_path = step_path_dir / f"step_{current_iter}.txt"
        # Clear file of contents
        with step_path.open("w", encoding="utf-8") as f:
            pass

        occurances = iteration(input_path, step_path, levels)
        result += occurances
        
    print(result)
    return result

if __name__ == "__main__":
    # Open input relative to this script's directory so the script works
    # no matter what the current working directory is when invoked.
    script_dir = Path(__file__).parent
    input_path = script_dir / "input.txt"

    main(input_path)