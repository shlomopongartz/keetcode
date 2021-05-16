# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return
        v = preorder[0]
        root = TreeNode(preorder[0])
        preorder.pop(0)
        ind = inorder.index(v)
        ls = inorder[:ind]
        rs = inorder[ind+1:]
        root.left = self.buildTree(preorder[:len(ls)], ls)
        root.right = self.buildTree(preorder[len(ls):], rs)
        return root

def compareTrees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None != root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return compareTrees(root1.left, root2.left) and compareTrees(root1.right, root2.right)


def main():
    s = Solution()

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n20 = TreeNode(20, n15, n7)
    n3 = TreeNode(3, n9, n20)
    res = s.buildTree(preorder, inorder)
    print("match = {0}".format(compareTrees(res, n3)))

if __name__ == "__main__":
    main()
