with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    word_searches = lines.read().split("\n")

def around_words(words, x, y):
    up = [(0, 0), (0, 1), (0, 2), (0, 3)]
    up_right = [(0, 0), (1, 1), (2, 2), (3, 3)]
    right = [(0, 0), (1, 0), (2, 0), (3, 0)]
    right_down = [(0, 0), (1, -1), (2, -2), (3, -3)]
    down = [(0, 0), (0, -1), (0, -2), (0, -3)]
    down_left = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    left = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
    left_up = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
    directions = [up, up_right, right, right_down, down, down_left, left, left_up]
    counter = 0

    for direction in directions:
        letters = []
        for dx, dy in direction:
            if (0 <= y + dy < len(words)) and (0 <= x + dx < len(words[0])):
                letters.append(words[y + dy][x + dx])

        xmas = "".join(letters)
        if xmas == "XMAS":
            counter += 1

    return counter

def solve(words):
    counter = 0
    for y in range(len(words)):
        for x in range(len(words[0])):
            counter += around_words(words, x, y)

    return counter

print(solve(word_searches))
