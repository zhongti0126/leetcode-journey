# Day 7 Notes

## Recursion

### Recursion
- A function that calls itself

Example:

```python
def dfs(node):

    if not node:
        return

    dfs(node.left)

    dfs(node.right)
```

---

## Backtracking

### Core Idea
- Try a choice
- Explore deeper
- Undo the choice
- Try another path

---

## Important Concepts

### path
Stores the current subset

Example:

```python
path = [1,2]
```

Meaning:
- currently selected 1 and 2

---

## Core Operations

### Choose

```python
path.append(nums[i])
```

Add a number into the current path

---

### Explore

```python
backtrack(i + 1)
```

Go to the next level

---

### Undo Choice

```python
path.pop()
```

Remove the last choice

---

## Backtracking Flow

```text
Choose
↓
Recursion
↓
Backtrack (pop)
↓
Try next choice
```

---

## LC 78 - Subsets

### Problem
Return all possible subsets

Example:

```python
nums = [1,2]
```

Output:

```text
[]
[1]
[2]
[1,2]
```

---

## LC 78 Template

```python
class Solution(object):

    def subsets(self, nums):

        result = []
        path = []

        def backtrack(start):

            result.append(path[:])

            for i in range(start, len(nums)):

                path.append(nums[i])

                backtrack(i + 1)

                path.pop()

        backtrack(0)

        return result
```

---

## Important

### path[:]
Copies the current path

Without `[:]`, result may change unexpectedly

---

## What I Learned Today
- recursion
- backtracking
- subsets
- append / pop
- recursive exploration
- path and result

---

- ## NOTES

<img width="2317" height="2925" alt="Day7" src="https://github.com/user-attachments/assets/a7bc485f-99a5-4382-b535-2d27ff28bfef" />
