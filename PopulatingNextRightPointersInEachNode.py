class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        def Append_val(root):
            if root: ## root가 주어질때 자식노드가 있는지 없는지
                if root.left: ## 왼쪽 자식이 있으면 왼쪽노드를 오른쪽으로 연결
                    root.left.next = root.right
                if root.right: ## 오른쪽 자식이 있으면 
                    if root.next: ##부모노드의 next가 있는지 체크후 
                        root.right.next = root.next.left #왼쪽 노드를 현재 오른쪽 노드와 연결
            if not root.left: #자식이 없으면 가장 말초에 자식 노드이므로 stop
                return
            
            Append_val(root.left)
            Append_val(root.left.next)
            return
        
        Append_val(root)

        return root
