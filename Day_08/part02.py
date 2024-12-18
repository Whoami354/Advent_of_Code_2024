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
        dy = y2 - y1
        dx = x2 - x1
        y, x = y1, x1

        while 0 <= y < num_y and 0 <= x < num_x:
            antinodes.add((y, x))
            y += dy
            x += dx

        y, x = y1, x1

        while 0 <= y < num_y and 0 <= x < num_x:
            antinodes.add((y, x))
            y -= dy
            x -= dx

print(len(antinodes))