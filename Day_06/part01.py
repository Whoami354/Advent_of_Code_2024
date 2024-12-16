with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    lab = lines.read().split("\n")

x = -1
y = 0

while x == -1:
    if "^" in lab[y]:
        x = lab[y].index("^")
    else:
        y += 1

direction = lab[y][x]
lab[y].replace('^', '.')

def rotate_right(guard):
    match guard:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'

len_lab = len(lab)
visited_places = set()

while 0 <= y < len(lab) and 0 <= x < len(lab[0]):
    visited_places.add((x, y))

    if direction == "^" and lab[y - 1][x] != "#":
        y -= 1
    elif direction == "v" and lab[(y + 1) % len_lab][x] != '#':
        y += 1
    elif direction == ">" and lab[y][(x + 1) % len(lab[0])] != '#':
        x += 1
    elif direction == "<" and lab[y][x - 1] != '#':
        x -= 1
    else:
        direction = rotate_right(direction)

print(len(visited_places))