"""
问题描述：
实现一种猫狗队列的结构，要求如下：
- 调用 add 方法将 cat 类和 dog 类放入队列中；
- 调用 pollAll 方法，将队列中所有的实例按照进队列的先后顺序依次弹出；
- 调用 pollDog 方法，将队列中 dog 类的实例按照进列队先后顺序依次弹出；
- 调用 pollCat 方法，将队列中 dog 类的实例按照进列队先后顺序依次弹出；
- 调用 isEmpty 方法，检查队列中是否还有 dog 和 cat 的实例；
- 调用 isDogEmpty 方法，检查队列中是否还有 dog 的实例；
- 调用 isCatEmpty 方法，检查队列中是否还有 cat 的实例；

解题思路：
该题的关键地点是如何设计来对整个队列进行出队操作，因此需要设计一个数据结构
存储猫狗实例的入队次序，即增加一个时间戳变量。
"""
from collections import deque


class Pet:
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type

    def __repr__(self):
        return "This is a {0} instance".format(self.type)


class Dog(Pet):
    def __init__(self):
        super().__init__("dog")


class Cat(Pet):
    def __init__(self):
        super().__init__("cat")


class PetEnterQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

    def getEnterPetType(self):
        return self.pet.getPetType()


class DogCatQueue:
    def __init__(self):
        self.dogQ = deque()
        self.catQ = deque()
        self.count = 0

    def add(self, pet):
        if (pet.getPetType() == "dog"):
            self.count += 1
            self.dogQ.append(PetEnterQueue(pet, self.count))
        elif (pet.getPetType() == "cat"):
            self.count += 1
            self.catQ.append(PetEnterQueue(pet, self.count))
        else:
            raise ValueError("err, not dog or cat")

    def pollAll(self):
        if (self.dogQ and self.catQ):
            # 按照 count 从小到大的顺序输出
            if (self.dogQ[0].getCount() < self.catQ[0].getCount()):
                return self.dogQ.popleft().getPet()
            else:
                return self.catQ.popleft().getPet()
        elif (self.dogQ):
            return self.dogQ.popleft().getPet()
        elif (self.catQ):
            return self.catQ.popleft().getPet()
        else:
            raise RuntimeError("err, queue is empty")

    def pollDog(self):
        if (self.dogQ):
            return self.dogQ.popleft().getPet()
        else:
            raise RuntimeError("err, dog queue is empty")

    def pollCat(self):
        if (self.catQ):
            return self.catQ.popleft().getPet()
        else:
            raise RuntimeError("err, cat queue is empty")

    def isEmpty(self):
        return self.dogQ and self.catQ

    def isDogQueueEmpty(self):
        return self.dogQ

    def isCatQueueEmpty(self):
        return self.catQ


def main():
    dog1 = Dog()
    dog2 = Dog()
    cat1 = Cat()
    cat2 = Cat()
    cat3 = Cat()
    queue = DogCatQueue()
    queue.add(dog1)
    queue.add(cat1)
    queue.add(cat3)
    queue.add(dog2)
    queue.add(cat2)
    print(queue.pollAll())
    print(queue.pollAll())
    print(queue.pollAll())
    print(queue.pollAll())
    print(queue.pollAll())


if __name__ == "__main__":
    main()
