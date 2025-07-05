# Problem: 146 – lru cache
# Difficulty: Medium
# Link: https://leetcode.com/problems/lru-cache/


from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]
    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic)> self.cap:
            self.dic.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)