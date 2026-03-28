def parse_grammar(grammar_text):

    rules = {}

    lines = grammar_text.strip().split("\n")

    for line in lines:

        if "->" not in line:
            continue

        left, right = line.split("->")

        left = left.strip()
        right = right.strip()

        productions = [p.strip() for p in right.split("|")]

        rules[left] = productions

    return rules


def remove_epsilon(rules):

    nullable = set()

    # Step 1: find nullable variables
    for left in rules:
        for prod in rules[left]:
            if prod == "e":
                nullable.add(left)

    new_rules = {}

    # Step 2: create new productions
    for left in rules:

        new_prods = set()

        for prod in rules[left]:

            if prod == "e":
                continue

            new_prods.add(prod)

            for var in nullable:
                if var in prod:
                    new_prods.add(prod.replace(var, ""))

        new_rules[left] = list(new_prods)

    return new_rules