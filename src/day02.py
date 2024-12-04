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

    prev_item = None
    for item in level:
        if prev_item == None:
            prev_item = item
            continue
        diff = abs(item - prev_item)
        if diff < 1 or diff > 3:
            return False
        if is_increasing and (prev_item <= item):
            return False
        if not is_increasing and (prev_item >= item):
            return False
        prev_item = item
    return True


def safe_level_count(levels):
    safe_levels = 0
    for level in levels:
        if level_safe(level):
            safe_levels += 1

    return safe_levels


input = get_data(f"{Path(__file__).resolve().parents[1]}/input/day02.txt")
print (f"Safe levels: {safe_level_count(input)}")
