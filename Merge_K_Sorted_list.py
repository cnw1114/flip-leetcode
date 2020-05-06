class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        all_value = list()
        for node in lists:
            while node:
                all_value.append(node.val)
                node = node.next
        if not all_value: return 
        allnode_new = [ListNode(val) for val in sorted(all_value)]
        Head = copynode = allnode_new[0]
        for idx in range(1,len(allnode_new)):
            copynode.next = allnode_new[idx]
            copynode = copynode.next
        return Head 
