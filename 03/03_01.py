import re

def main():

    input = []
    for line in open('input.txt'):
        input.append(line.strip())

    mults = []

    for line in input:
        line_mults = []
        line_mults.append(re.findall('mul\(\d*,\d*\)', line))
        for mult in line_mults:
            for m in mult:
                mults.append(m)

    print(mults)
    nums = []

    for mul in mults:
        lis = re.findall('\d*,\d*', mul)
        for l in lis:
            bips = l.split(',')
            nums.append([int(b) for b in bips])

    solution = 0
    for n in nums:
        solution += n[0] * n[1]


    print(solution)

if __name__ == "__main__":
    main()
