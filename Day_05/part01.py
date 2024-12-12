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

add_up = 0

for update in updates:
    if is_valid(rules, update):
        add_up += update[len(update) // 2]

print(add_up)