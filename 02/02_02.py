def main():

    input = []
    for line in open('input.txt'):
        input.append([int(s) for s in line.strip().split(' ')])

    safe_levels = 0

    for line in input:
        print('new line')
        print(line)
        print('check')
        checks = []
        checks.append(check_line(line))

        for i in range(len(line)):
            print('check')
            shortened_line = line.copy()
            shortened_line.pop(i)
            checks.append(check_line(shortened_line))

        for c in checks:
            if c is True:
                safe_levels += 1
                print('level was safe')
                break

        print(safe_levels)


def check_line(line) -> None:
    safe = True
    previous_num = 0
    is_positive = False
    is_negative = False

    for i, num in enumerate(line):

        if i == 0:
            previous_num = num
            continue
        print(abs(num - previous_num))
        if num - previous_num < 0:
            is_negative = True
        if num - previous_num > 0:
            is_positive = True
        if abs(num - previous_num) > 3:
            safe = False
            break
        if abs(num - previous_num) == 0:
            safe = False
            break
        if is_positive is True and is_negative is True:
            safe = False
            break
        previous_num = num
    return safe


if __name__ == "__main__":
    main()

