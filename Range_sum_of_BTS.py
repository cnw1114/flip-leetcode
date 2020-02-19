class Solution: O(N)/O(N)
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        stack = []
        output_list = []
        
        while True:
            if not stack:
                stack.append(root)
            tmp_tree = stack.pop()
            if tmp_tree:
                output_list.append(tmp_tree.val)
                stack.append(tmp_tree.left)
                stack.append(tmp_tree.right)
            if not stack:
                break
        return sum([item if L<=item<=R else 0 for item in output_list])

class Solution: O(logN)/O(1)
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        def getvalue(root, L, R):
            if root:
                if L <= root.val <= R:
                    self.ans += root.val
                if root.val > L:
                    getvalue(root.left, L, R)
                if root.val < R:
                    getvalue(root.right, L, R)
        getvalue(root, L, R)
        return self.ans
