import re

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    numbers = lines.read()

matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", numbers)

sum = 0
state = True

for match in matches:
    if match[2] == "do()":
        state = True
    elif match[3] == "don't()":
        state = False
    elif state:
        sum += int(match[0]) * int(match[1])

print(sum)
