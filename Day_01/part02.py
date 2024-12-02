with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    location_IDs = lines.read().split("\n")

left_side = []
right_side = []

for id in location_IDs:
    numbers = id.split("   ")
    left_side.append(int(numbers[0]))
    right_side.append(int(numbers[1]))

def solve(left_numbers, right_numbers):
    sum = 0

    for left_number in left_numbers:
        right_common = right_numbers.count(left_number)

        sum += left_number * right_common

    return sum


print(solve(left_side, right_side))