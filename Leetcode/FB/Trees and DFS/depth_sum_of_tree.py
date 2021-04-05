def rangeSumBST(self, root, L, R):
    def dfs(node):
        if node:
            if L <= node.val <= R:
                self.ans += node.val
            if L < node.val:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)

    ans = 0
    dfs(root)
    return ans