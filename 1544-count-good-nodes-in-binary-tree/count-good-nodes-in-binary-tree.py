class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        st = [(root,root.val)]
        while st:
            x, m = st.pop()
            if x.val >= m:
                ans += 1
            if x.left:
                st.append((x.left, max(m, x.val)))
            if x.right:
                st.append((x.right, max(m, x.val)))
        return ans