# Day 6 Notes

## Graph Basics

### Graph
- A graph is a collection of:
  - nodes
  - edges

Example:

```text
0 — 1 — 2
```

---

## Important Concepts

### Node
- A point in the graph

### Edge
- A connection between two nodes

### Neighbor
- Connected node

---

## Adjacency List

```python
graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}
```

Meaning:
- 0 connects to 1
- 1 connects to 0 and 2
- 2 connects to 1

---

## BFS (Breadth First Search)

### Core Idea
- Explore level by level
- Use Queue
- Use visited set

---

## Queue Setup

```python
from collections import deque

queue = deque()
visited = set()
```

---

## BFS Template

```python
queue.append(source)
visited.add(source)

while queue:

    node = queue.popleft()

    if node == destination:
        return True

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.add(neighbor)

            queue.append(neighbor)
```

---

## Important

### queue
Stores nodes to visit later

### visited
Prevents infinite loops

### graph[node]
Gets all neighbors of a node

---

## BFS Flow

```text
Take one node
↓
Check neighbors
↓
Add unvisited neighbors to queue
↓
Repeat
```

---

## LeetCode

### LC 1971
Find if Path Exists in Graph

---

## What I Learned Today
- Graph basics
- BFS on graph
- queue + visited
- adjacency list
- graph traversal

---

- ## NOTES
<img width="2637" height="2646" alt="Day6" src="https://github.com/user-attachments/assets/d5e00c74-d700-45c2-9ee4-3916b3c3920a" />

