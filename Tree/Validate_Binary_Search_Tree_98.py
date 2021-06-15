# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.checkRange(root)
        if result is False:
            return False
        else:
            return True

    def checkRange(self, root):
        # DFS
        # bottom up
        left_range = None
        right_range = None
        # leaf node, return range
        if root.left is None and root.right is None:
            return tuple([root.val, root.val])

        # check left subtree
        if root.left is not None:
            left_range = self.checkRange(root.left)
            if left_range is False:
                return False
        # check right subtree
        if root.right is not None:
            right_range = self.checkRange(root.right)
            if right_range is False:
                return False

        # left substree is none
        if left_range is None:
            if root.val < right_range[0]:
                return tuple([root.val, right_range[1]])
            else:
                return False
        # right substree is none
        elif right_range is None:
            if root.val > left_range[1]:
                return tuple([left_range[0], root.val])
            else:
                return False
        #left and right subtree is not none
        else:
            if left_range[1] < root.val and right_range[0] > root.val:
                return tuple([left_range[0], right_range[1]])
            else:
                return False

        def isValidBST(self, root):
            # DFS
            # top down
            import math
            def validate(node, low=-math.inf, high=math.inf):
                # Empty trees are valid BSTs.
                if not node:
                    return True
                # The current node's value must be between low and high.
                if node.val <= low or node.val >= high:
                    return False

                # The left and right subtree must also be valid.
                return (validate(node.right, node.val, high) and
                        validate(node.left, low, node.val))

            return validate(root)


