with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    reports = lines.read().split("\n")

safes = []

for report in reports:
    safes.append(list(map(int, report.split(" "))))

def allIncreasingOrAllDecreasing(arr):
    isIncreasing = True
    isDecreasing = True
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            isIncreasing = False
            break

    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            isDecreasing = False

    return isIncreasing or isDecreasing

def differAtMostThree(arr):
    isMostThree = True
    for i in range(len(arr) - 1):
        differ = abs(arr[i] - arr[i + 1])
        if not 1 <= differ <= 3:
            isMostThree = False
            break

    return isMostThree

def removeSingleElementFromUnsafe(arr):
    i = 0

    while i < len(arr):
        if allIncreasingOrAllDecreasing(arr[:i] + arr[i + 1:]) and differAtMostThree(arr[:i] + arr[i + 1:]):
            return True

        i += 1

    return False

def solve(safes):
    counter = 0
    for safe in safes:
        if (allIncreasingOrAllDecreasing(safe) and differAtMostThree(safe)) or removeSingleElementFromUnsafe(safe):
            counter += 1

    return counter


print(solve(safes))