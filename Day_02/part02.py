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

def removeSingleElementFromUnsafe(arr):
    i = 0

    while i < len(arr):
        if allIncreasingOrAllDecreasing(arr[:i] + arr[i + 1:]) and differenceAtLeastOneAndAtMostThree(arr[:i] + arr[i + 1:]):
            return True

        i += 1

    return False

def solve(safes):
    counter = 0
    for safe in safes:
        if (allIncreasingOrAllDecreasing(safe) and differenceAtLeastOneAndAtMostThree(safe)) or \
                removeSingleElementFromUnsafe(safe):
            counter += 1

    return counter


print(solve(safes))