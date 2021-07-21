class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        pre : [3,9,20,15,7]  root = 3
        in  : [9,3,15,20,7]  left = [9] right = [15,20,7]

        recursive
        1-pre: [20,15,7] root = 20
        1-in: [15,20,7] left = [15] right = [7]

        Done!

        time complexity : o(n)
        space : O(n)  if use index

        """
        if len(preorder) == 0:
            return None

        root = preorder[0]
        root_node = TreeNode(root)

        index = inorder.index(root)

        left_in = inorder[:index]
        right_in = inorder[index + 1:]

        left_pre = preorder[1:1 + len(left_in)]
        right_pre = preorder[1 + len(left_in):]

        root_node.left = self.buildTree(left_pre, left_in)
        root_node.right = self.buildTree(right_pre, right_in)
        return root_node

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right