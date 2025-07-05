# Problem: 133 – clone graph
# Difficulty: Medium
# Link: https://leetcode.com/problems/clone-graph/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clones  = {}
        q = deque()
 
        clones[node] = Node(node.val)
        q.append(node)
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                clones[curr].neighbors.append(clones[nei])
        return clones[node]

        