class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = [root]
        output = []
        while queue:
            node = queue.pop(0)
            # 자식node에 delete가 있는지 없는지 확인(자식 노드 관점)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.left and node.left.val in to_delete:
                node.left = None    
            if node.right and node.right.val in to_delete:
                node.right = None
            # 현재 노드 관점
            if node and node.val in to_delete: #현재 노드가 delete에 포함되면 자식 노드는 따로 분리되어 append
                if node.left and node.left.val not in to_delete:
                    output.append(node.left)
                if node.right and node.right.val not in to_delete:
                    output.append(node.right)
                continue
            
            if not output:
                output.append(node)
        
        return output
