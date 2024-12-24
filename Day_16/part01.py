import heapq

with open("input.txt", "r") as f:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    grid = list(map(str.strip, f.readlines()))

def get_started(grid):
    for r in range(len(grid)):
        if "S" in grid[r]:
            return r, grid[r].index("S")

start = get_started(grid)

queue = [(0, *start, 0, 1, [start])]
seen = {(*start, 0, 1)}
part1 = None
best_cost = float("inf")

while queue:
    cost, r, c, dr, dc, path = heapq.heappop(queue)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        if not part1:
            part1 = cost
        if cost <= best_cost:
            best_cost = cost
        else:
            break
    if grid[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
        heapq.heappush(
            queue, (cost + 1, r + dr, c + dc, dr, dc, path + [(r + dr, c + dc)])
        )
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen and grid[r + ndr][c + ndc] != "#":
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))

print(part1)