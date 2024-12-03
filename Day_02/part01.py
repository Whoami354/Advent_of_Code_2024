with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    reports = lines.read().split("\n")

safes = []

for report in reports:
    safes.append(list(map(int, report.split(" "))))


def allIncreasingOrAllDecreasing(arr):
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) or \
        all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))


def differenceAtLeastOneAndAtMostThree(arr):
    return all(1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))


def solve(safes):
    counter = 0
    for safe in safes:
        if allIncreasingOrAllDecreasing(safe) and differenceAtLeastOneAndAtMostThree(safe):
            counter += 1

    return counter


print(solve(safes))
