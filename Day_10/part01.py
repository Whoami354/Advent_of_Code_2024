from collections import deque

with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    grid = [list(map(int, line.strip())) for line in lines.readlines()]

rows = len(grid)
cols = len(grid[0])
zeros = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 0]

def count_trails(r: int, c: int):
    queue = deque([(r, c)])
    summits = set()

    while queue:
        r, c = queue.popleft()
        if not grid[r][c] == 9:
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] + 1 == grid[nr][nc]:
                    queue.append((nr, nc))
        else:
            summits.add((r, c))

    return len(summits)

trails = 0
for start in zeros:
    trails += count_trails(*start)

print(trails)
