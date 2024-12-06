# Failed :(
import re
import advent_utils


def get_mull_match_total(s):
    total = 0
    mull_matches = re.finditer(r"mul\(?(\d+),?(\d+)\)", s)
    for mull_match in mull_matches:
        a = int(mull_match.group(1))
        b = int(mull_match.group(2))
        total += a * b
    return total


def remove_donts(input):
    trimmed = re.sub(r"don't\(\).*?do\(\)", "", input)
    trimmed = re.sub(r"don't\(\).*", "", trimmed)
    return trimmed


if __name__ == "__main__":
    print(remove_donts("don't()mul(1,1)don't()mul(2,2))do()mul(3,3)"))
    # input = advent_utils.get_day_input_as_string(3)
    # print(f"mull totals: {get_mull_match_total(input)}")
    # print(f"trimmed mull totals: {get_mull_match_total(remove_donts(input))}") #74361272
