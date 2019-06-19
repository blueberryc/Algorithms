class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        if n <= 0:
            return [[]]
        return self.createSubTree(1, n)

    def createSubTree(self, start, end):
        res = []
        if (end < start):
            return None
        for i in range(start, end+1):
            for l in self.createSubTree(start, i) or [None]:
                for r in self.createSubTree(i+1, end+1) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    res.append(node)
        return res
