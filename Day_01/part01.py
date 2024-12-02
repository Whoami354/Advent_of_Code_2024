with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    location_IDs = lines.read().split("\n")

left_side = []
right_side = []

for id in location_IDs:
    numbers = id.split(" ")
    left_side.append(int(numbers[0]))
    right_side.append(int(numbers[-1]))

def solve(left_numbers, right_numbers):
    sum = 0
    left_len = len(left_numbers)
    right_len = len(right_numbers)

    while left_len > 0 and right_len > 0:
        min_left = min(left_numbers)
        min_right = min(right_numbers)

        sum += (abs(min_left - min_right))

        left_numbers.remove(min_left)
        right_numbers.remove(min_right)

        left_len -= 1
        right_len -= 1

    return sum

print(solve(left_side, right_side))