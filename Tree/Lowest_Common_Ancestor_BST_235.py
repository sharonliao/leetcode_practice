
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # top down
        # if a node which value is between q and p, then this node is the lca
        # if a node which value is q or p, then this node is the lca
        def topD(root):
            if root is not None:
                if root.val > p.val and root.val > q.val:
                    return topD(root.left)
                elif root.val < p.val and root.val < q.val:
                    return topD(root.right)
                else:
                    return root
        topD(root)




