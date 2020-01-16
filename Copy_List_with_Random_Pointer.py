"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head:'node')->'node':
        d = {None:None}
        nodeC = nodeP = head ## old node를 저장하기 위하여
        while nodeC: #copy nodes
            d[nodeC] = Node(nodeC.val) # 구노드의 키값에 새노드를 mapping
            nodeC = nodeC.next

        while nodeP: #copy random pointers and next pointers
            d[nodeP].random = d[nodeP.random] #dictionary must have None for this
            d[nodeP].next = d[nodeP.next]
            nodeP = nodeP.next

        return d[head]
