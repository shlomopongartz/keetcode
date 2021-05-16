# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first_node = None
        self.second_node = None
        self.last_visited = None

        self.recoverTree2(root)
        if self.first_node is not None:
            self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    def recoverTree2(self, root):
        if root.left is not None:
            self.recoverTree2(root.left)
        if self.last_visited is not None:
            if self.last_visited.val > root.val:
                if self.first_node is None:
                    self.first_node = self.last_visited
                self.second_node = root
        self.last_visited = root
        if root.right is not None:
            self.recoverTree2(root.right)


def printTree(root):
    res = []
    q2 = [root]
    while (len(q2) > 0):
        q1 = q2
        q2 = []
        while (len(q1) > 0):
            node = q1.pop(0)
            if node == None:
                res.append(None)
            else:
                res.append(node.val)
                q2.append(node.left)
                q2.append(node.right)
    return res

def main():
    s = Solution()

    #x = [1,null,3,null,2]
    two = TreeNode(2, None, None)
    three = TreeNode(3, None, two)
    root = TreeNode(1, None, three)
    exp = [1,None,2,None,3]
    s.recoverTree(root)
    res = printTree(root)
    print("exp = {0} result = {1}".format(exp, res[:-2]))

    #x = [3,null,2,null,1]
    one = TreeNode(1, None, None)
    two = TreeNode(2, None, one)
    root = TreeNode(3, None, two)
    exp = [1,None,2,None,3]
    s.recoverTree(root)
    res = printTree(root)
    print("exp = {0} result = {1}".format(exp, res[:-2]))

    #x = [2,1,3]
    one = TreeNode(1, None, None)
    three = TreeNode(3, None, None)
    root = TreeNode(2, one, three)
    exp = [2,1,3]
    s.recoverTree(root)
    res = printTree(root)
    print("exp = {0} result = {1}".format(exp, res[:-2]))

    #x = [2,3,1]
    one = TreeNode(1, None, None)
    three = TreeNode(3, None, None)
    root = TreeNode(2, three, one)
    exp = [2,1,3]
    s.recoverTree(root)
    res = printTree(root)
    print("exp = {0} result = {1}".format(exp, res[:-2]))

    #x = [1,3,None,None,2]
    two = TreeNode(2, None, None)
    three = TreeNode(3, None, two)
    root = TreeNode(1, three, None)
    exp = [3,1,None,None,2]
    s.recoverTree(root)
    res = printTree(root)
    print("exp = {0} result = {1}".format(exp, res[:-2]))

    #x = [3,1,4,None,None,2]
    one = TreeNode(1, None, None)
    two = TreeNode(2, None, None)
    four = TreeNode(4, two, None)
    root = TreeNode(3, one, four)
    exp = [2,1,4,None,None,3]
    s.recoverTree(root)
    res = printTree(root)
    print("exp = {0} result = {1}".format(exp, res[:-2]))

if __name__ == "__main__":
    main()
