from collections import defaultdict
from itertools import combinations

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = lines.read().split("\n")

antenna = defaultdict(set)
num_y = len(input)
num_x = len(input[0])

for y, line in enumerate(input):
    for x, val in enumerate(line):
        if val != '.':
            antenna[val].add((x, y))

antinodes = set()

for freq in antenna:
    for (y1, x1), (y2, x2) in combinations(antenna[freq], 2):
        antinodes.add((2 * y1 - y2, 2 * x1 - x2))
        antinodes.add((2 * y2 - y1, 2 * x2 - x1))

sum = len([1 for y, x in antinodes if 0 <= y < num_y and 0 <= x < num_x])

print(sum)