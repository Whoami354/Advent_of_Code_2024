import re

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    numbers = lines.read()

matches = re.findall(r"mul\(\d+,\d+\)", numbers)
mulNums = []

for match in matches:
    mul = match.split("mul(")
    mulNumbers = mul[1].split(",")
    mulNums.append((int(mulNumbers[0]), int(mulNumbers[1][:-1])))

def solve(mulitypliNums):
    sum = 0

    for multiNum in mulitypliNums:
        sum += multiNum[0] * multiNum[1]

    return sum

print(solve(mulNums))