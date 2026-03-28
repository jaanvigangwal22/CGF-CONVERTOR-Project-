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


# ------------------ EPSILON REMOVAL ------------------
def remove_epsilon(rules):

    nullable = set()

    for left in rules:
        for prod in rules[left]:
            if prod == "e":
                nullable.add(left)

    new_rules = {}

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


# ------------------ UNIT REMOVAL ------------------
def remove_unit(rules):

    new_rules = {}

    for left in rules:
        new_prods = set()

        for prod in rules[left]:

            # unit production like A -> B
            if len(prod) == 1 and prod.isupper():
                new_prods.update(rules.get(prod, []))
            else:
                new_prods.add(prod)

        new_rules[left] = list(new_prods)

    return new_rules


# ------------------ USELESS REMOVAL (basic) ------------------
def remove_useless(rules):

    useful = set()

    # find symbols producing terminals
    for left in rules:
        for prod in rules[left]:
            if prod.islower():
                useful.add(left)

    new_rules = {}

    for left in rules:
        if left in useful:
            new_rules[left] = rules[left]

    return new_rules


# ------------------ FINAL CNF FORMAT (basic) ------------------
def to_cnf(rules):

    cnf_rules = {}

    for left in rules:

        new_prods = []

        for prod in rules[left]:

            # already valid CNF
            if len(prod) == 2 and prod.isupper():
                new_prods.append(prod)

            elif len(prod) == 1 and prod.islower():
                new_prods.append(prod)

            else:
                new_prods.append(prod)  # keep as is (basic)

        cnf_rules[left] = new_prods

    return cnf_rules