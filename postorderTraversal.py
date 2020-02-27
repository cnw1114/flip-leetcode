class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        stack = []
        output = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return output[::-1]
