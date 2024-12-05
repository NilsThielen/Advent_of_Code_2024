def check_list(input, x_counts):
    print(input)
    counts = x_counts.copy()

    for y, line in enumerate(input):
        char_buffer = ''
        for x, char in enumerate(line):
            char_buffer += char
            if len(char_buffer) > 3:
                char_buffer = char_buffer[1:]
            if char_buffer == 'MAS' or char_buffer == 'SAM':
                print(char_buffer)
                counts[y][x - 1] += 1

    return counts


def shift_list(input, direction):
    list_height = len(input) - 1
    shift_amt = 0
    new_list = []

    for line in input:
        if direction == 'right':
            new_list.append(('_' * shift_amt) + line + ('_' * list_height))
        if direction == 'left':
            new_list.append(('_' * list_height) + line + ('_' * shift_amt))
        shift_amt += 1
        list_height -= 1

    return new_list


def shift_list_count(input, direction):
    list_height = len(input) - 1
    shift_amt = 0
    new_list = []

    for line in input:
        if direction == 'right':
            new_list.append([9 for i in range(shift_amt)] + line + [9 for i in range(list_height)])
        if direction == 'left':
            new_list.append([9 for i in range(list_height)] + line + [9 for i in range(shift_amt)])
        shift_amt += 1
        list_height -= 1

    return new_list


def turn_vertical(input):
    x = 0
    y = 0
    line_length = len(input[0])
    line_height = len(input)
    new_line = ''
    new_list = []

    while True:
        new_line += input[y][x]
        y += 1
        if y == line_height:
            y = 0
            x += 1
            new_list.append(new_line)
            new_line = ''
        if x == line_length:
            break

    return new_list


def turn_vertical_counts(input):
    x = 0
    y = 0
    line_length = len(input[0])
    line_height = len(input)
    new_line = []
    new_list = []

    while True:
        new_line.append(input[y][x])
        y += 1
        if y == line_height:
            y = 0
            x += 1
            new_list.append(new_line)
            new_line = []
        if x == line_length:
            break

    return new_list


def remove_placeholders(input):
    new_list = []
    for line in input:
        new_line = []
        for entry in line:
            if entry != 9:
                new_line.append(entry)
        new_list.append(new_line)
    return new_list


def add_matricies(left, right):
    sum_matrix = []
    for y, line in enumerate(left):
        new_line = []
        for x, n in enumerate(line):
            new_line.append(left[y][x] + right[y][x])
        sum_matrix.append(new_line)

    return sum_matrix


def count_full_crosses(counts):
    amt = 0
    for line in counts:
        for n in line:
            if n == 2:
                amt += 1
    return amt


def main():
    input = []

    for line in open('input.txt'):
        input.append(line.strip())

    x_counts = [[0 for j in range(0, len(input[0]))] for i in range(0, len(input))]

    input_shift_left = shift_list(input, 'left')
    input_vertical_shift_left = turn_vertical(input_shift_left)
    x_counts_shift_left = shift_list_count(x_counts, 'left')
    x_counts_vertical_shift_left = turn_vertical_counts(x_counts_shift_left)

    input_shift_right = shift_list(input, 'right')
    input_vertical_shift_right = turn_vertical(input_shift_right)
    x_counts_shift_right = shift_list_count(x_counts, 'right')
    x_counts_vertical_shift_right = turn_vertical_counts(x_counts_shift_right)

    x_counts_left = check_list(input_vertical_shift_left, x_counts_vertical_shift_left)
    x_counts_right = check_list(input_vertical_shift_right, x_counts_vertical_shift_right)
    print(x_counts_left)
    print(x_counts_right)

    x_counts_left = turn_vertical_counts(x_counts_left)
    x_counts_left = turn_vertical_counts(x_counts_left)
    x_counts_left = turn_vertical_counts(x_counts_left)

    x_counts_right = turn_vertical_counts(x_counts_right)
    x_counts_right = turn_vertical_counts(x_counts_right)
    x_counts_right = turn_vertical_counts(x_counts_right)

    x_counts_left = remove_placeholders(x_counts_left)
    x_counts_right = remove_placeholders(x_counts_right)
    print(x_counts_left)
    print(x_counts_right)
    x_counts = add_matricies(x_counts_left, x_counts_right)

    amt = count_full_crosses(x_counts)
    print(amt)


if __name__ == "__main__":
    main()
