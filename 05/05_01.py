def split_input(input, rules, manuals):
    for line in input:
        if len(line) < 4:
            continue
        if len(line) > 5:
            manuals.append(line)
        else:
            rules.append(line)


def process_rules(rules):
    processed_rules = []
    for rule in rules:
        processed_rules.append(rule.split('|'))
    return processed_rules


def process_manuals(manuals):
    processed_manuals = []
    for manual in manuals:
        processed_manuals.append(manual.split(','))
    return processed_manuals


def find_relevant_rules(rules, manual):
    relevant_rules = []
    print('manual: ', manual)
    for rule in rules:
        match = 0
        for n in manual:
            if n in rule:
                match += 1
            if match == 2:
                relevant_rules.append(rule)
                break
    print('relevant rules: ', relevant_rules)
    return relevant_rules


def check_manuals(manuals, rules):
    correct_manuals = []
    for manual in manuals:
        wrong = False
        relevant_rules = find_relevant_rules(rules, manual)
        for rule in relevant_rules:
            for n in manual:
                if n == rule[0]:
                    break
                if n == rule[1]:
                    wrong = True
                    break
        if wrong is False:
            correct_manuals.append(manual)
    return correct_manuals


def main():
    input = []
    for line in open('input.txt'):
        input.append(line.strip())

    rules = []
    manuals = []

    split_input(input, rules, manuals)

    rules = process_rules(rules)
    manuals = process_manuals(manuals)
    correct_manuals = check_manuals(manuals, rules)

    middle_numbers = [int(m[(len(m) - 1) // 2]) for m in correct_manuals]
    sum_middle_numbers = sum(middle_numbers)

    print(sum_middle_numbers)


if __name__ == "__main__":
    main()
