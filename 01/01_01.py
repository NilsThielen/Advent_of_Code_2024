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

for i in range(len(left_side)):
    distance += abs(left_side[0] - right_side[0])
    left_side.pop(0)
    right_side.pop(0)

print(distance)
