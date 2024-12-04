def check_list(input):
    count = 0

    for line in input:
        char_buffer = ''
        for char in line:
            char_buffer += char
            if len(char_buffer) > 4:
                char_buffer = char_buffer[1:]
            if char_buffer == 'XMAS' or char_buffer == 'SAMX':
                print(char_buffer)
                count += 1

    return count


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


def main():
    input = []
    for line in open('input.txt'):
        input.append(line.strip())

    xmas_count = 0

    xmas_count += check_list(input)
    print(xmas_count)

    input_vertical = turn_vertical(input)
    xmas_count += check_list(input_vertical)
    print(xmas_count)

    input_shift_left = shift_list(input, 'left')
    input_vertical_shift_left = turn_vertical(input_shift_left)

    input_shift_right = shift_list(input, 'right')
    input_vertical_shift_right = turn_vertical(input_shift_right)

    xmas_count += check_list(input_vertical_shift_left)
    print(xmas_count)
    xmas_count += check_list(input_vertical_shift_right)
    print(xmas_count)


if __name__ == "__main__":
    main()
