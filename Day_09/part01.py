with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    data = list(map(int, lines.read().strip()))

disk = []
for i in range(0, len(data), 2):
    disk.extend(data[i] * [i // 2])
    if i + 1 < len(data):
        disk.extend(data[i + 1] * [-1])

empties = [i for i, val in enumerate(disk) if val == -1]

i = 0

while True:
    while disk[-1] == -1:
        disk.pop()
    target = empties[i]
    if target >= len(disk):
        break

    disk[target] = disk.pop()

    i += 1

print(sum(i * val for i, val in enumerate(disk)))