# LeetCode Journey (Python)

This repository documents my learning journey in Data Structures and Algorithms using Python.

The goal is not only to solve problems, but also to build a stronger foundation in computer science, including problem-solving logic, time complexity analysis, and algorithmic thinking.

---

## Current Learning Focus

- Data Structures and Algorithms
- Python problem-solving
- Stack / Queue
- Linked List
- Binary Search
- Tree / Graph
- BFS / DFS
- Recursion & Backtracking
- Dynamic Programming

---

## Learning Roadmap

| Topic | Status | Practice Problems |
|---|---|---|
| Stack | Completed | LC 20 Valid Parentheses, LC 155 Min Stack |
| Queue | Completed | Queue Basics, BFS Introduction |
| Linked List | Completed | LC 206 Reverse Linked List |
| Binary Search | Completed | LC 704 Binary Search |
| Tree | Completed | LC 104 Maximum Depth of Binary Tree |
| Graph Basics | Completed | LC 1971 Find if Path Exists in Graph |
| Recursion & Backtracking | In Progress | LC 78 Subsets |
| Heap / Priority Queue | LC 215 Kth Largest Element in an Array |
| Sliding Window | Coming Soon | - |
| Two Pointers | Coming Soon | - |
| Prefix Sum | Coming Soon | - |
| Matrix / Grid BFS | Coming Soon | - |
| Monotonic Stack | Coming Soon | - |
| Dynamic Programming | Coming Soon | - |
| Greedy Algorithms | Coming Soon | - |
| Trie / String Search | Coming Soon | - |

---

## Topic Notes

### Stack

#### LC 20 - Valid Parentheses

**What I Learned**
- How to use a stack to match pairs
- How to use a HashMap to store bracket relationships
- Why stack is useful for “last in, first out” problems

**Key Idea**
Push opening brackets into the stack.  
When a closing bracket appears, check whether it matches the latest opening bracket.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

### Queue / BFS

**What I Learned**
- Queue follows FIFO: first in, first out
- BFS uses a queue to explore nodes level by level
- `collections.deque` is useful for efficient queue operations in Python

---

### Linked List

#### LC 206 - Reverse Linked List

**What I Learned**
- How pointers move in a linked list
- How to reverse links step by step
- Why `prev`, `curr`, and `next` are important variables

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

### Binary Search

#### LC 704 - Binary Search

**What I Learned**
- How to reduce the search range by half each time
- Why `left <= right` is important
- How logarithmic time complexity improves efficiency

**Key Idea**
Compare the target with the middle value.  
If the target is smaller, search the left half.  
If the target is larger, search the right half.

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

---

### Tree

#### LC 104 - Maximum Depth of Binary Tree

**What I Learned**
- Basic tree traversal
- Recursive thinking
- How to break a problem into left subtree and right subtree

---

### Graph / BFS / DFS

#### LC 1971 - Find if Path Exists in Graph

**What I Learned**
- How to build an adjacency list
- How to use BFS or DFS to search a graph
- Why a `visited` set is necessary to avoid repeated traversal

---

### Recursion & Backtracking

#### LC 78 - Subsets

**What I Learned**
- How recursion explores different choices
- How backtracking builds possible combinations
- How to think about “choose” and “not choose”

---
### Heap / Priority Queue

#### LC 215 - Kth Largest Element in an Array

**What I Learned**
- How a Min Heap works
- How to maintain only k largest elements
- Why Heap is faster than sorting in some cases

**Key Idea**
Keep a heap of size k.
When the heap size exceeds k, remove the smallest element.

At the end:

```python
return heap[0]
```

is the kth largest element.

**Time Complexity:** O(n log k)
**Space Complexity:** O(k)

---
## Growth Reflection

At the beginning, I mainly focused on solving problems by intuition.  
Through continuous practice, I started to understand the importance of data structures, algorithm patterns, and time complexity.

This repository helps me record not only solved problems, but also the learning process behind each topic.

---

## Goals

- Strengthen computer science fundamentals
- Improve algorithmic thinking
- Build consistent problem-solving habits
- Prepare for future software engineering studies
- Connect coding practice with real project development

---

## Language

- Python
