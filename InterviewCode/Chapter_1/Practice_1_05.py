"""
问题描述：
一个栈中元素的类型为整型，现在想将该栈从顶到底按从大到小的顺序排序，只允许
申请一个栈。除此之外，可以申请新的变量。

解题思路：
借鉴插入排序的思想，让辅助栈 helpStack 中的数据从小到大排序，即每次从初始
栈中弹出元素，插入到辅助栈的指定位置。需要将初始栈中的所有元素都压入 helpStack
中。
"""
from collections import deque


def sortStackByStack(stack):
    helpStack = deque()
    while (stack):
        cur = stack.pop()
        while (helpStack and helpStack[-1] > cur):
            stack.append(helpStack.pop())
        helpStack.append(cur)

    # 将所有元素压回 stack 中
    while (helpStack):
        stack.append(helpStack.pop())


def main():
    newNum = [1, 2, 7, 3, 5, 8, 4]
    stack = deque(newNum)
    print("----未排序的栈----\n{0}".format(stack))
    sortStackByStack(stack)
    print("----排序的栈----\n{0}".format(stack))


if __name__ == "__main__":
    main()
