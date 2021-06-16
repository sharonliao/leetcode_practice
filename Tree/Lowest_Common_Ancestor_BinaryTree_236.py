# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor_topdown(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Time Limit Exceeded   repeated computation
        # top down
        # 1. case 1: when a node, which's left child contains p(or q), and right child contains q(or p), then this node must be the lowestCommonAncestor
        # 2. case 2: when a node, which is p, and its left child or right child contains q , then this node must be the lowestCommonAncestor

        def DFS(root):
            if root is not None:
                if DFS(root.left):
                    return True
                if DFS(root.right):
                    return True
                if root.val == p.val or root.val == q.val:
                    return True

        if root is not None:
            left = DFS(root.left)
            right = DFS(root.right)
            cur = root.val == p.val or root.val == q.val
            if left and right:
                return root
            elif cur and (left or right):
                return root
            elif left:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)


    def lowestCommonAncestor_bottomUp(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # bottom up
        # 1. case 1: when a node, which's left child contains p(or q), and right child contains q(or p), then this node must be the lowestCommonAncestor
        # 2. case 2: when a node, which is p, and its left child or right child contains q , then this node must be the lowestCommonAncestor

        def DFS(root):
            if root is not None:
                left = DFS(root.left)
                right = DFS(root.right)
                cur = root.val == p.val or root.val == q.val
                if left and right:
                    return root
                elif cur and (left or right):
                    return root
                else:
                    return left or right or cur
        DFS(root)













