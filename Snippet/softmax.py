import math


def softmax(list1):
    sum1 = sum([math.exp(x) for x in list1])
    ans = []
    for index, val in enumerate(list1):
        ans.append(math.exp(val) / sum1)
    return ans


if __name__ == "__main__":
    list1 = [15, 60, 15, 35]
    print(softmax(list1))
