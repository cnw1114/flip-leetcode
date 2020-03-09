class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue, out = [[root,1]], [[root.val,1]]
        max_lv = 1
        while queue:
            node, lv = queue.pop(0)
            if node:
                queue.append([node.left, lv+1])
                queue.append([node.right, lv+1])
                if node.left:
                    out.append([node.left.val, lv+1])
                    max_lv = lv+1
                if node.right:
                    out.append([node.right.val, lv+1])
                    max_lv = lv+1
        
        output_lv, sum_ = 1, sum(map(lambda y: y[0],list(filter(lambda x: x[1]==1,out))))
        for lv in range(2,max_lv+1):
            if sum_ < sum(map(lambda y: y[0],list(filter(lambda x: x[1]==lv,out)))):
                sum_ = sum(map(lambda y: y[0],list(filter(lambda x: x[1]==lv,out))))
                output_lv = lv
        
        return output_lv
