"""
Insert Delete GetRandom O(1)
！！： time : o(1)
dict里有数字的idx，用idx去访问对应的list里的数字，
we need combine list, dict to achieve this goal,
dict[val]: val's index in list
list[i]: i's val in list
交换位置，需要把删掉元素的idx换成最后一位的idx，且交换位置
删掉元素的idx ： dict[删掉元素]
最后一位的idx： tail = list[-1], dict[tail]
"""
from random import choice


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.vals)
        self.vals.append(val)
        return True
        # put the number into the dict,

    def remove(self, val: int) -> bool:
        if val in self.dict:
            tail, idx = self.vals[-1], self.dict[val]
            self.vals[idx], self.dict[tail] = tail, idx
            self.vals.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.vals)
#time/space: o(1), o(n)