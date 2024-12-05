# solving: https://adventofcode.com/2024/day/1


from pathlib import Path


def get_data(path_to_file):
    reports = []
    with open(path_to_file) as f:
        for line in f:
            items = line.split(" ")
            int_items = list(map(lambda x: int(x), items))
            reports.append(int_items)
    return reports


def level_safe(level: list[int]) -> bool:
    # edge case: single item
    if len(level) <= 1:
        return True

    # first items equal
    if level[0] == level[1]:
        return False

    # determine trend (increasing or decreasing)
    is_increasing = level[0] - level[1] > 0

    i = 1  # start at second element
    while i < len(level):
        item = level[i]
        prev_item = level[i - 1]

        diff = abs(item - prev_item)
        if diff < 1 or diff > 3:
            return i
        if is_increasing and (prev_item <= item):
            return i
        if not is_increasing and (prev_item >= item):
            return i

        i += 1
    return None


def safe_level_count(levels, allow_damper=False):
    safe_levels = 0
    for level in levels:
        problem_item = level_safe(level)

        if problem_item == None:
            safe_levels += 1

        elif (
            problem_item != None
            and allow_damper
            # and level_safe(levels.copy().pop(problem_item)) == None
        ):
            removal_item_index = 0
            while removal_item_index < len (level):
                trimmed_level = level.copy()
                trimmed_level.pop(removal_item_index)
                
                if level_safe(trimmed_level) == None:
                    safe_levels += 1
                    break
                removal_item_index += 1

    return safe_levels


if __name__ == "__main__":
    
    input = get_data(f"{Path(__file__).resolve().parents[1]}/input/day02.txt")
    print(f"Safe levels (un-dampened): {safe_level_count(input, False)}")
    print(f"Safe levels (dampened): {safe_level_count(input, True)}")
