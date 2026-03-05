# Missionaries and Cannibals Problem using BFS and DFS (Python)

## Overview

This project implements the classic **Missionaries and Cannibals problem** using **Uninformed Search algorithms** in Artificial Intelligence.

The program demonstrates how **Breadth First Search (BFS)** and **Depth First Search (DFS)** explore the state space to find a valid solution while satisfying constraints.

The implementation is written in **Python** and shows how search algorithms can solve constraint-based problems.

---

# Problem Description

The **Missionaries and Cannibals problem** is a famous Artificial Intelligence problem used to demonstrate **state space search**.

### Initial Situation

* 3 Missionaries
* 3 Cannibals
* All are on the **left side of the river**
* One boat is available

The boat can carry **maximum two people at a time**.

---

# Constraints

1. The boat can carry **one or two people only**.
2. If **cannibals outnumber missionaries on any side**, the missionaries will be eaten.
3. The boat must have **at least one person to move**.

---

# Goal

Move **all missionaries and cannibals safely to the right side of the river**.

Goal State:

```
(0,0,1)
```

---

# State Representation

Each state is represented as:

```
(M_left, C_left, Boat)
```

Where:

* **M_left** = Missionaries on the left side
* **C_left** = Cannibals on the left side
* **Boat** = Position of the boat

Boat values:

```
0 → Left side
1 → Right side
```

Example states:

```
(3,3,0)   Initial State
(3,1,1)
(2,2,0)
(0,0,1)   Goal State
```

---

# Possible Boat Moves

The boat can carry:

```
1 Missionary
2 Missionaries
1 Cannibal
2 Cannibals
1 Missionary + 1 Cannibal
```

These moves are represented in the program as:

```python
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
```

---

# Algorithms Used

## 1. Breadth First Search (BFS)

BFS explores the state space **level by level**.

### Characteristics

* Uses **Queue (FIFO)**
* Guarantees **shortest solution**
* Explores nodes systematically

### Time Complexity

```
O(b^d)
```

Where:

* **b** = branching factor
* **d** = depth of solution

---

## 2. Depth First Search (DFS)

DFS explores nodes **as deep as possible before backtracking**.

### Characteristics

* Uses **Recursion / Stack**
* Lower memory usage
* May not always give optimal solution

### Time Complexity

```
O(b^m)
```

Where:

* **m** = maximum depth of tree

---

# Python Implementation

```python
from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False

    return True


moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]


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

            if boat == 0:
                new_state = (m - move[0], c - move[1], 1)
            else:
                new_state = (m + move[0], c + move[1], 0)

            nm, nc, nb = new_state

            if is_valid(nm, nc):
                queue.append((new_state, path + [state]))

    return None


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


print("BFS Solution Path:")
bfs_solution = bfs()

for step in bfs_solution:
    print(step)


print("\nDFS Solution Path:")
dfs_solution = dfs((3,3,0), [], set())

for step in dfs_solution:
    print(step)
```

---

# Example Output

```
BFS Solution Path:

(3, 3, 0)
(3, 1, 1)
(3, 2, 0)
(3, 0, 1)
(3, 1, 0)
(1, 1, 1)
(2, 2, 0)
(0, 2, 1)
(0, 3, 0)
(0, 1, 1)
(0, 2, 0)
(0, 0, 1)
```

---

# Performance Comparison

| Feature          | BFS    | DFS                  |
| ---------------- | ------ | -------------------- |
| Data Structure   | Queue  | Stack                |
| Completeness     | Yes    | Not always           |
| Optimal Solution | Yes    | No                   |
| Memory Usage     | High   | Low                  |
| Speed            | Slower | Faster in deep trees |

---

# State Space Diagram (Conceptual)

```
           (3,3,L)
         /        \
     (3,1,R)    (2,2,R)
       |           |
     (3,2,L)     (3,2,L)
       |
     (3,0,R)
       |
     (1,1,R)
       |
     (2,2,L)
       |
     (0,2,R)
       |
     (0,0,R)  Goal
```

---

# Applications

The Missionaries and Cannibals problem demonstrates:

* State Space Search
* Constraint Satisfaction
* Graph Traversal Algorithms
* Artificial Intelligence Problem Solving

Similar techniques are used in:

* Robotics planning
* Puzzle solving
* Game AI
* Pathfinding algorithms

---

# Repository Structure

```
Missionaries-Cannibals-AI
│
├── missionaries_cannibals.py
├── README.md
│
└── documentation
    └── report.pdf
```
