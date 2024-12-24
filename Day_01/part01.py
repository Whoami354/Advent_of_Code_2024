with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    location_IDs = lines.read().split("\n")

left_side = [int(number.split("   ")[0]) for number in location_IDs]
right_side = [int(number.split("   ")[1]) for number in location_IDs]

def solve(left_numbers, right_numbers):
    sum = 0

    while len(left_numbers) > 0 and len(right_numbers) > 0:
        min_left = min(left_numbers)
        min_right = min(right_numbers)

        sum += (abs(min_left - min_right))

        left_numbers.remove(min_left)
        right_numbers.remove(min_right)

    return sum

print(solve(left_side, right_side))