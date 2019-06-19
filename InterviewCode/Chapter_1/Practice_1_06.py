"""
问题描述：生成窗口最大值数组
有一个整型数组 arr 和一个大小为 w 的窗口从数组的最左边滑到最右边，
窗口每次向右移动一个位置。例如，数组为 [4, 3, 5, 4, 3, 3, 6, 7]，
窗口大小为 3 时：

[4 3 5] 4 3 3 6 7    -- 最大值 5
4 [3 5 4] 3 3 6 7    -- 最大值 5
4 3 [5 4 3] 3 6 7    -- 最大值 5
4 3 5 [4 3 3] 6 7    -- 最大值 4
4 3 5 4 [3 3 6] 7    -- 最大值 6
4 3 5 4 3 [3 6 7]    -- 最大值 7

可以发现，一共产生 n-w+1 个最大值，要求返回这些最大值。

解题思路：
最暴力的方法就是双层循环，时间复杂度为 O(n*w)
但是我们可以知道，一个窗口的最大值的左侧的数据是不会有成为最大值的可能的，
所以这部分的数据并不需要遍历。而对于右边即将新加入的元素，如果大于队尾的元
素，则队尾的元素也没有可能再成为最大值，所以也可以去掉。显然，这里需要在队
头和队尾都能对序列进行处理，所以采用双端队列。

参考资料：http://blog.itpub.net/31561266/viewspace-2286701/
"""
from collections import deque


def getMaxWindow(arr, w):
    if (not arr or w < 1 or len(arr) < w):
        return None
    qmax = deque()
    res = []  # 保存最大窗口的元素
    for index, val in enumerate(arr):
        # 队列不为空，且新元素大于队尾元素，队尾不可能成为最大值
        while(qmax and arr[qmax[-1]] <= val):
            qmax.pop()
        # 将当前元素加入队列，使用下标是为了判断窗口是否过期
        qmax.append(index)
        if (qmax[0] == index - w):  # 最大元素过期
            qmax.popleft()
        if (index >= w - 1):
            res.append(arr[qmax[0]])
    return res


def main():
    arr = [4, 3, 1, 5, 4, 3, 7, 5]
    w = 3
    print(getMaxWindow(arr, w))


if __name__ == "__main__":
    main()
