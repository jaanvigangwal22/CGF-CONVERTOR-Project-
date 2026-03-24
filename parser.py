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