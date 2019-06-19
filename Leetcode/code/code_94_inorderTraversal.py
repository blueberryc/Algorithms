from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归形式，分为三步：
        1. 递归遍历左子树；
        2. 增加当前的根的值；
        3. 递归遍历右子树；
    注意：由于要保存遍历的值，所以 ans 也要作为参数传入递归函数
    """

    def inorderTraversal(self, root):
        ans = []
        if (root is None):
            return
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)


class Solution2:
    """
    迭代形式
    """

    def inorderTraversal(self, root):
        ans = []
        stack = deque()
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    solution = Solution2()
    ans = solution.inorderTraversal(node1)
    print(ans)


if __name__ == "__main__":
    main()
