# Definition for a binary tree node.
import copy

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        res = []

        q2 = [root]
        i = 0
        while len(q2) > 0:
            q1 = q2
            q2 = []
            t = []
            for node in q1:
                t.append(node.val)
                if node.left is not None:
                    q2.append(node.left)
                if node.right is not None:
                    q2.append(node.right)
            if i == 1:
                t.reverse()
                res.append(t)
            else:
                res.append(t)
            i = 1 - i

        return res

def main():
    s = Solution()

    # tree [3,9,20,null,null,15,7]
    seven = TreeNode(7, None, None)
    fifteen = TreeNode(15, None, None)
    twentee = TreeNode(20, fifteen, seven)
    nine = TreeNode(9, None, None)
    three = TreeNode(3, nine, twentee)
    exp = [[3],[20,9],[15,7]]
    res = s.levelOrder(three)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
    main()
