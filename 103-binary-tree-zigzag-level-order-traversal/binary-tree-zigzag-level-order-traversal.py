# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=deque([root])
        left_to_right=True
        ans=[]

        while q:
            level=len(q)
            level_nodes=[]

            for _ in range(level):
                node=q.popleft()
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            if not left_to_right:
                level_nodes.reverse()
            
            ans.append(level_nodes)
            left_to_right=not left_to_right
        return ans

                
            
        return ans