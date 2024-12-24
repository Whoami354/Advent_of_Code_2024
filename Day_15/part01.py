with open("input.txt", "r") as f:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    grid_str, moves = f.read().split("\n\n")
grid = [list(row) for row in grid_str.split("\n")]
moves = moves.replace("\n", "")

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            break
    else:
        continue
    break

move_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

for move in moves:
    dr, dc = move_map[move]
    rr, cc = r + dr, c + dc
    do_move = True
    while True:
        if grid[rr][cc] == "#":
            do_move = False
            break
        if grid[rr][cc] == ".":
            break
        if grid[rr][cc] == "O":
            rr, cc = rr + dr, cc + dc
        else:
            assert False

    if not do_move:
        continue
    grid[r][c] = "."

    r, c = r + dr, c + dc

    if grid[r][c] == "O":
        grid[rr][cc] = "O"
    grid[r][c] = "@"

part1 = sum(r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "O")

print(part1)