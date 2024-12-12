from collections import defaultdict

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = lines.read().split("\n")

idx = input.index("")
rules = defaultdict(set)

for line in input[:idx]:
    x, y = map(int, line.split("|"))
    rules[x].add(y)

updates = [list(map(int, i.split(","))) for i in input[idx + 1:]]

def is_valid(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True

def fix_update(rules, update):
    filtered_rules = defaultdict(set)

    for i in update:
        filtered_rules[i] = rules[i].intersection(set(update))

    ordered_keys = sorted(filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True)

    return ordered_keys

add_up = 0

for update in updates:
    if not is_valid(rules, update):
        fixed_update = fix_update(rules, update)
        add_up += fixed_update[len(update) // 2]

print(add_up)