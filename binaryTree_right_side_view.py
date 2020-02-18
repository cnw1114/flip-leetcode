class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        node_list, new_list, output = [root], [], []
        while True:
            output.append(node_list[-1].val)
            for node in node_list:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
            node_list = new_list[:]
            new_list = []
            if not node_list:
                break
        
        return output
