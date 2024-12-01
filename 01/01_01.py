lines = []

with open('input.txt', 'r') as file:
    for line in file:
        line.replace('\\n', '')
        lines.append(line)

print(lines)
