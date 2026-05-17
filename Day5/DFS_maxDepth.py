---

## DFS Traversal

```python
def dfs(node):

    if not node:
        return

    print(node.val)

    dfs(node.left)

    dfs(node.right)
```

---

## Important
- recursion = function calls itself
- `if not node` = stop condition
- DFS goes deep first

---

## Maximum Depth of Binary Tree

```python
class Solution(object):

    def maxDepth(self, root):

        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)

        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)
```
