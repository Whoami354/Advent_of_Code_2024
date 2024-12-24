import re

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    puzzles = lines.read().split("\n\n")

def solve_puzzle(puzzle, offset):
    a1, a2 = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", puzzle)[0]))

    c1 += offset
    c2 += offset

    # https://de.wikipedia.org/wiki/Cramersche_Regel
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

    if int(x) == x and int(y) == y:
        return tuple(map(int, (x, y)))
    return (0, 0)

part2 = 0

for puzzle in puzzles:
    a, b = solve_puzzle(puzzle, 10000000000000)
    part2 += a * 3 + b

print(part2)





