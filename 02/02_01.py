input = []
for line in open('input.txt'):
    input.append([int(s) for s in line.strip().split(' ')])

print(input)

safe_levels = 0

for line in input:
    print('new line')
    print(line)
    safe = True
    previous_num = 0
    is_positive = False
    is_negative = False
    for i, num in enumerate(line):
        if i == 0:
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
        previous_num = num
    if is_positive is True and is_negative is True:
        safe = False
    if safe is True:
        print('level was safe')
        safe_levels += 1
        print(safe_levels)

print(safe_levels)
