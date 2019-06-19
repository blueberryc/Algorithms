"""
问题描述：
一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。
将这个栈转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的
逆序，但是只能用递归函数来实现。

解题思路：
当栈中只有两个个元素时，很显然获取栈底元素，并将其从栈中移除，然后将
得到的值压入栈中，就相当于逆序了栈。同理，对高度为n的栈进行操作时，
可以将栈底的元素和其上的所有部分看成是两个元素，这就相当于完成两个元
素的逆序。而 n-1 个元素可以进行递归处理。
"""
from collections import deque


def reverse(stack: deque):
    if (not stack):
        return
    value = stack.popleft()  # 获取队列左端元素，即栈底元素
    reverse(stack)
    stack.append(value)


def main():
    newNum = [1, 2, 3, 4, 5]
    stack = deque()
    for item in newNum:
        stack.append(item)
    reverse(stack)
    for item in newNum:
        print(stack.pop(), end=" ")


if __name__ == "__main__":
    main()
