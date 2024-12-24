import math
import re

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    puzzles = list(map(str.strip, lines.readlines()))

def safety_score(robots):
    q = [0] * 4
    for xf, yf in robots:
        midw, midh = width // 2, height // 2
        if xf < midw:
            if yf < midh:
                q[0] += 1
            if yf > midh:
                q[1] += 1
        elif xf > midw:
            if yf < midh:
                q[2] += 1
            if yf > midh:
                q[3] += 1
    return math.prod(q)

width, height = 101, 103

robots = []
for line in puzzles:
    x, y, dx, dy = tuple(map(int, re.findall(r"-?\d+", line)))
    robots.append((x, y, dx, dy))


part1_robots = []
for x, y, dx, dy in robots:
    xf = (x + (dx * 100)) % width
    yf = (y + (dy * 100)) % height
    part1_robots.append((xf, yf))

part1 = safety_score(part1_robots)

print(part1)