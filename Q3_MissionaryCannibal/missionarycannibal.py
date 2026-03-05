from collections import deque

# check if state is valid
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # missionaries eaten on left side
    if m > 0 and m < c:
        return False

    # missionaries eaten on right side
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False

    return True


moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]


# ---------------- BFS ----------------
def bfs():

    start = (3,3,0)
    goal = (0,0,1)

    queue = deque()
    queue.append((start, []))

    visited = set()

    while queue:

        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for move in moves:

            if boat == 0:   # boat on left
                new_state = (m - move[0], c - move[1], 1)
            else:           # boat on right
                new_state = (m + move[0], c + move[1], 0)

            nm, nc, nb = new_state

            if is_valid(nm, nc):
                queue.append((new_state, path + [state]))

    return None


# ---------------- DFS ----------------
def dfs(state, path, visited):

    goal = (0,0,1)

    if state == goal:
        return path + [state]

    if state in visited:
        return None

    visited.add(state)

    m, c, boat = state

    for move in moves:

        if boat == 0:
            new_state = (m - move[0], c - move[1], 1)
        else:
            new_state = (m + move[0], c + move[1], 0)

        nm, nc, nb = new_state

        if is_valid(nm, nc):
            result = dfs(new_state, path + [state], visited)

            if result:
                return result

    return None


# ---------------- MAIN ----------------
print("BFS Solution Path:")
bfs_solution = bfs()

for step in bfs_solution:
    print(step)


print("\nDFS Solution Path:")
dfs_solution = dfs((3,3,0), [], set())

for step in dfs_solution:
    print(step)
