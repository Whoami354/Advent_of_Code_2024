with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    location_IDs = lines.read().split("\n")

left_side = [int(number.split("   ")[0]) for number in location_IDs]
right_side = [int(number.split("   ")[1]) for number in location_IDs]

def solve(left_numbers, right_numbers):
    sum = 0

    for left_number in left_numbers:
        right_common = right_numbers.count(left_number)

        sum += left_number * right_common

    return sum


print(solve(left_side, right_side))
