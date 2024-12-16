with open("input.txt", "r") as f:
    labour = list(map(list, map(str.strip, f.readlines())))

def get_start():
    for r, row in enumerate(labour):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)

num_rows = len(labour)
num_cols = len(labour[0])

start_y, start_x = get_start()

def check_for_loop():
    y, x = start_y, start_x
    dy, dx = -1, 0
    visited = set()

    while True:
        if (y, x, dy, dx) in visited:
            return True
        visited.add((y, x, dy, dx))
        if not (0 <= y + dy < num_rows and 0 <= x + dx < num_cols):
            return False
        if labour[y + dy][x + dx] == "#":
            dx, dy = -dy, dx
        else:
            y += dy
            x += dx

part2 = 0
for ro in range(num_rows):
    for co in range(num_cols):
        if labour[ro][co] != "#":
            labour[ro][co] = "#"
            if check_for_loop():
                part2 += 1
            labour[ro][co] = "."

print(f"Part 2: {part2}")
