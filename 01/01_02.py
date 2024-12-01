lines = []
lines_split = []
nums = []

with open('input.txt') as file:
    for line in file:
        line.rstrip()
        lines.append(line)

    for line in lines:
        lines_split.append(line.rstrip())

    for line in lines_split:
        nums.append(line.split()[0])
        nums.append(line.split()[1])

left_side = []
right_side = []
distance = 0

for i, num in enumerate(nums):
    if i % 2 == 0:
        left_side.append(int(num))
    else:
        right_side.append(int(num))

left_side.sort()
right_side.sort()

for num in left_side:
    distance += num * right_side.count(num)

print(distance)
