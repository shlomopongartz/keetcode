class Node(object):
    def __init__(self, isBorser=False):
        self.parent = self
        self.weight = 0
        self.isBorder = isBorder

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows <= 1:
            return board
        cols = len(board[0])
        if cols <= 1:
            return board

        world = Node(True)
        tbl = [[None] * cols] * rows
        for i, c in enumerate(board[0]):
            if c == 'O':
                tbl[0][i] = Node(True)
                self.union(world, tbl[0][i])
        for i, c in enumerate(board[rows-1]):
            if c == 'O':
                tbl[rows-1][i] = Node(True)
                self.union(world, tbl[rows-1][i])
        for i in range(1, rows - 1):
            if tbl[i][0] == '0':
                tbl[i][0] = Node(True)
                self.union(world, tbl[i][0])
            if tbl[i][cols - 1] == '0':
                tbl[i][cols - 1] = Node(True)
                self.union(world, tbl[i][cols - 1])

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if tbl[i][j] == '0':

        for j in range(1, cols - 1):

    def Find(self, x):
        root = x.parent
        while root.parent != root:
            root = root.parent

        while x != root:
            next = x.parent
            x.parent = root
            x = next

    def Union(self, x, y):
        r1 = self.Find(x)
        r2 = self.Find(y)

        if r1 == r2:
            return

        if r1.weight < r2.weight:
            r1, r2 = r2, r1

        r2.parent = r1
        r1.weight += r2.size
        r1.isBorder |= r2.isBorder


def main():
    sol = Solution()

    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    exp   = [['X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X'],
             ['X', 'O', 'X', 'X']]
    exp = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    res = sol.solve(board)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()