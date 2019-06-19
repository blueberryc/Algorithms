"""
问题描述：
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
要求 push，pop 和 getMin 操作的时间复杂度都是 O(1).

解题思路：
利用两个栈，stackData用于保存数据，和常规的栈操作一样。而 stackMin 则只用于保存当前的最小值
"""
from collections import deque


class newStack(object):
    def __init__(self):
        self.stackMin = deque()
        self.stackData = deque()

    def push(self, x):
        if (not self.stackMin):
            self.stackMin.append(x)
        elif (x <= self.stackMin[-1]):
            self.stackMin.append(x)
        self.stackData.append(x)

    def pop(self, x):
        if (not self.stackData):
            raise RuntimeError("Your stack is empty")
        value = self.stackData.pop()
        if (value == self.stackMin[-1]):
            self.stackMin.pop()
        return value

    def getMin(self):
        if (not self.stackMin):
            raise RuntimeError("Your stack is empty")
        return self.stackMin[-1]


def main():
    newNum = [3, 4, 5, 1, 2, 1]
    stack = newStack()
    for i in newNum:
        stack.push(i)
        print(stack.getMin())
    print(stack.stackData)
    print(stack.stackMin)


if __name__ == "__main__":
    main()
