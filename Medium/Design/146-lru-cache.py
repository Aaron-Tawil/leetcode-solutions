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
        

# LeetCode 146: LRU Cache
# Time: O(1) per operation; Space: O(capacity)

class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> Node

        # Sentinels
        self.head = Node()  # most-recent side
        self.tail = Node()  # least-recent side
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Doubly linked list helpers ---
    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_head(self, node: Node) -> None:
        self._remove(node)
        self._add_to_head(node)

    def _pop_tail(self) -> Node:
        node = self.tail.prev
        self._remove(node)
        return node

    # --- API ---
    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
            self._move_to_head(node)
            return

        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_to_head(new_node)

        if len(self.map) > self.cap:
            lru = self._pop_tail()
            del self.map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)