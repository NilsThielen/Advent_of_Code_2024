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

    for rule in rules:
        match = 0

        for n in manual:
            if n in rule:
                match += 1
            if match == 2:
                relevant_rules.append(rule)
                break

    return relevant_rules


def check_manuals(manuals, rules):
    incorrect_manuals = []

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

        if wrong is True:
            incorrect_manuals.append(manual)

    return incorrect_manuals


def correct_manuals(incorrect_manuals, rules):
    corrected_manuals = []

    for manual in incorrect_manuals:

        relevant_rules = find_relevant_rules(rules, manual)
        w_manual = manual.copy()
        found_incorrect = True

        while found_incorrect is True:
            found_incorrect = False
            for rule in relevant_rules:
                order_in_manual = []
                for n in w_manual:
                    if n in rule:
                        order_in_manual.append(n)
                print(rule)
                if rule != order_in_manual:
                    found_incorrect = True
                    i_one = w_manual.index(rule[0])
                    i_two = w_manual.index(rule[1])
                    w_manual[i_one], w_manual[i_two] = w_manual[i_two], w_manual[i_one]

        corrected_manuals.append(w_manual)

    return corrected_manuals


def main():
    input = []

    for line in open('input.txt'):
        input.append(line.strip())

    rules = []
    manuals = []

    split_input(input, rules, manuals)

    rules = process_rules(rules)
    manuals = process_manuals(manuals)

    incorrect_manuals = check_manuals(manuals, rules)
    corrected_manuals = correct_manuals(incorrect_manuals, rules)

    middle_numbers = [int(m[(len(m) - 1) // 2]) for m in corrected_manuals]
    sum_middle_numbers = sum(middle_numbers)

    print(sum_middle_numbers)


if __name__ == "__main__":
    main()
