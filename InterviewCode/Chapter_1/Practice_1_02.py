"""
问题描述：
编写一个类，用两个栈实现队列，支持队列的基本操作（add，poll，peek）

解题思路：
首先明确队列的特点是先进先出，而栈的特点是先进后出。
因此，在出队操作时需要将原先压入的序列反转过来。
具体来说，设计两个栈 stackPush 和 stackPop 。
第一个栈只负责接收压入的数据，而每次遇到弹出操作时，如果 stackPop 为空，
则需要将 stackPush 中的所有数据压入到 stackPop 中
"""
from collections import deque


class TwoStackQueue(object):
    def __init__(self):
        self.stackPush = deque()
        self.stackPop = deque()

    def add(self, x):
        self.stackPush.append(x)

    def poll(self):
        if (not self.stackPop and not self.stackPush):  # 两个栈都为空，则队列为空
            raise RuntimeError("Queue is empty")
        if (not self.stackPop):  # stackPop 为空
            while (self.stackPush):
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):
        if (not self.stackPop and not self.stackPush):  # 两个栈都为空，则队列为空
            raise RuntimeError("Queue is empty")
        if (not self.stackPop):  # stackPop 为空
            while (self.stackPush):
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop[-1]

    def empty(self):
        if (not self.stackPop and not self.stackPush):  # 两个栈都为空，则队列为空
            return True
        else:
            return False


def main():
    newNum = [1, 2, 3, 4, 5]
    queue = TwoStackQueue()
    for item in newNum:
        queue.add(item)
    while (not queue.empty()):
        print(queue.poll(), end=" ")


if __name__ == "__main__":
    main()
