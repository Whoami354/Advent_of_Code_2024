with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    word_searches = lines.read().split("\n")

def solve(words):
    counter = 0
    m_s = {"M", "S"}
    for y in range(1, len(words) - 1):
        for x in range(1, len(words[0]) - 1):
            if words[y][x] == "A":
                if {words[y - 1][x - 1], words[y + 1][x + 1]} == m_s and {words[y - 1][x + 1], words[y + 1][x - 1]} == m_s:
                    counter += 1

    return counter

print(solve(word_searches))
