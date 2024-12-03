import re
import math

def main():

    input = []
    for line in open('input.txt'):
        input.append(line.strip())

    instructions = []

    for line in input:
        instructions.append(re.findall('do\(\)|don\'t\(\)|mul\(\d*,\d*\)', line))

    print(instructions)

    solution = 0
    activated = True

    for line in instructions:
        for i in line:
            print(i)
            if 'do()' in i:
                print('do found')
                activated = True
            elif 'don\'t()' in i:
                print('dont found')
                activated = False
            elif 'mul' in i and activated is True:
                print('mul found')
                nums = re.search('\d*,\d*', i).group()
                solution += math.prod([int(n) for n in nums.split(',')])
                print(math.prod([int(n) for n in nums.split(',')]))

    print(solution)


if __name__ == "__main__":
    main()
