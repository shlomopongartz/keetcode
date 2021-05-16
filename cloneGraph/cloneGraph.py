# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        self.dfs1(node)
        t = node.neighbors[-1]
        self.dfs2(node)
        self.dfs3(node)
        return t

    def dfs1(self, node):
        if node.val > 100:
            return
        node.val = node.val + 100
        for n in node.neighbors:
            self.dfs1(n)
        node.neighbors.append(Node(node.val - 100, node.neighbors[:]))

    def dfs2(self, node):
        if node.val > 200:
            return
        node.val = node.val + 100
        clone = node.neighbors[-1]
        for i, n in enumerate(node.neighbors[0:-1]):
            clone.neighbors[i] = n.neighbors[-1]
        for n in node.neighbors[0:-1]:
            self.dfs2(n)

    def dfs3(self, node):
        if node.val < 200:
            return
        node.val = node.val - 200
        node.neighbors.pop()
        for n in node.neighbors:
            self.dfs3(n)

def main():
    s = Solution()

    #x = [1,null,3,null,2]
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.neighbors.append(two)
    one.neighbors.append(four)
    two.neighbors.append(one)
    two.neighbors.append(three)
    three.neighbors.append(two)
    three.neighbors.append(four)
    four.neighbors.append(one)
    four.neighbors.append(three)
    #exp = [1,None,2,None,3]
    s.cloneGraph(one)
    #res = printTree(root)
    #print("exp = {0} result = {1}".format(exp, res[:-2]))

if __name__ == "__main__":
    main()
