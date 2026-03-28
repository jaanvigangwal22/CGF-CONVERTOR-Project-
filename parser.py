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


# -------- EPSILON REMOVAL --------
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


# -------- UNIT REMOVAL --------
def remove_unit(rules):

    new_rules = {}

    for left in rules:

        new_prods = set()

        for prod in rules[left]:

            if len(prod) == 1 and prod.isupper():
                new_prods.update(rules.get(prod, []))
            else:
                new_prods.add(prod)

        new_rules[left] = list(new_prods)

    return new_rules


# -------- USELESS REMOVAL --------
def remove_useless(rules):

    useful = set()

    for left in rules:
        for prod in rules[left]:
            if prod.islower():
                useful.add(left)

    new_rules = {}

    for left in rules:
        if left in useful:
            new_rules[left] = rules[left]

    return new_rules


# -------- CNF --------
def to_cnf(rules):

    cnf_rules = {}

    for left in rules:

        new_prods = []

        for prod in rules[left]:

            if len(prod) == 2 and prod.isupper():
                new_prods.append(prod)

            elif len(prod) == 1 and prod.islower():
                new_prods.append(prod)

            else:
                new_prods.append(prod)

        cnf_rules[left] = new_prods

    return cnf_rules


# -------- GNF STEP BY STEP --------
def gnf_steps(rules):

    # STEP 1: start from CNF
    step1 = {}
    for left in rules:
        step1[left] = rules[left]


    # STEP 2: replace first variable
    step2 = {}

    for left in step1:

        new_prods = []

        for prod in step1[left]:

            if len(prod) > 0 and prod[0].islower():
                new_prods.append(prod)

            elif len(prod) > 0 and prod[0].isupper():

                first = prod[0]
                rest = prod[1:]

                for rep in step1.get(first, []):
                    new_prods.append(rep + rest)

            else:
                new_prods.append(prod)

        step2[left] = new_prods


    # STEP 3: final GNF (only terminal start)
    final_gnf = {}

    for left in step2:

        new_prods = []

        for prod in step2[left]:

            if len(prod) > 0 and prod[0].islower():
                new_prods.append(prod)

        final_gnf[left] = new_prods

    return step1, step2, final_gnf