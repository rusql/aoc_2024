import advent_utils


def words_found_at_position(row, col, input, word):
    found = 0
    for rowpos in range(-1, 2):
        for colpos in range(-1, 2):
            if colpos == 0 and rowpos == 0:
                continue
            test_word = ""
            this_row = row
            this_col = col
            for _ in list(word):
                if (
                    this_row > len(input) - 1
                    or this_col > len(input[0]) - 1
                    or this_col < 0
                    or this_row < 0
                ):
                    test_word = ""
                    break
                test_word += input[this_row][this_col]
                this_col += colpos
                this_row += rowpos
            if test_word != "" and word_match(test_word, word):
                found += 1
    return found


def word_match(test_word, target_word):
    if test_word.upper() == target_word.upper():
        return True
    if test_word.upper()[::-1] == target_word.upper():
        return True
    return False


def count_all_positions(input, word):
    if len(input) == 0:
        return 0
    rowpos = 0
    colpos = 0
    found = 0
    while rowpos < len(input):
        while colpos < len(input[0]):
            found += words_found_at_position(rowpos, colpos, input, word)
            colpos += 1
        colpos = 0
        rowpos += 1
    return int(found / 2)


def count_x_mas(input):
    row = 1
    col = 1
    found = 0
    target_word = "MAS"
    while row < len(input) - 1:
        while col < len(input[row]) - 1:
            x1 = f"{input[row-1][col-1]}{input[row][col]}{input[row+1][col+1]}"
            x2 = f"{input[row-1][col+1]}{input[row][col]}{input[row+1][col-1]}"
            if word_match(x1, target_word) and word_match(x2, target_word):
                found += 1
            col += 1
        col = 1
        row += 1
    return found



input = advent_utils.get_day_input_as_los(4)
print(f"day 4 part 1: {count_all_positions(input, 'XMAS')}")
print(f"dat 4 part 2: {count_x_mas(input)}")
