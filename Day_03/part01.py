import re

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    numbers = lines.read()

matches = re.findall(r"mul\(\d+,\d+\)", numbers)
sum = 0

for match in matches:
    mul = match.split("mul(")
    mulNumbers = mul[1].split(",")
    sum += int(mulNumbers[0]) * int(mulNumbers[1][:-1])

print(sum)
