# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Node val min value is -1000
        self.result = -1000000

        self.maxPathSum2(root)

        return self.result

    def maxPathSum2(self, root):
        if root is None:
            return 0

        lval = self.maxPathSum2(root.left)
        rval = self.maxPathSum2(root.right)
        straight_max = root.val
        sval = lval if lval > rval else rval
        if sval > 0:
            straight_max += sval
        as_root_val = lval + root.val + rval
        if straight_max > self.result:
            self.result = straight_max
        if as_root_val > self.result:
            self.result = as_root_val
        return straight_max


def main():
    s = Solution()

    #root = [1,2,3]
    two = TreeNode(2, None, None)
    three = TreeNode(3, None, None)
    one = TreeNode(1, two, three)
    exp = 6
    res = s.maxPathSum(one)
    print("exp = {0} result = {1}".format(exp, res))

    #root = [-10,9,20,null,null,15,7]
    seven = TreeNode(7, None, None)
    fifteen = TreeNode(15, None, None)
    twenty = TreeNode(20, fifteen, seven)
    nine = TreeNode(9, None, None)
    minusten = TreeNode(-10, nine, twenty)
    exp = 42
    res = s.maxPathSum(minusten)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
    main()
