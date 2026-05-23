class Solution(object):

    def maxDepth(self, root):

        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)

        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)
