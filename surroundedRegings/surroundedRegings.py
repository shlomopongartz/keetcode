class Node(object):
    def __init__(self, isBorder=False):
        self.parent = self
        self.weight = 1
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
        tbl = [[None for j in range(cols)] for i in range(rows)]

        for i, c in enumerate(board[0]):
            if c == 'O':
                tbl[0][i] = Node(True)
                self.Union(world, tbl[0][i])

        for i, c in enumerate(board[rows-1]):
            if c == 'O':
                tbl[rows-1][i] = Node(True)
                self.Union(world, tbl[rows-1][i])

        for i in range(1, rows - 1):
            if board[i][0] == 'O':
                tbl[i][0] = Node(True)
                self.Union(world, tbl[i][0])
            if board[i][cols - 1] == 'O':
                tbl[i][cols - 1] = Node(True)
                self.Union(world, tbl[i][cols - 1])

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if board[i][j] == 'O':
                    tbl[i][j] = Node(False)
                    if board[i-1][j] == 'O':
                        self.Union(tbl[i][j], tbl[i-1][j])
                    if board[i][j-1] == 'O':
                        self.Union(tbl[i][j], tbl[i][j-1])
            if board[i][cols-2] == 'O' and board[i][cols-1] == 'O':
                self.Union(tbl[i][cols-2], tbl[i][cols-1])
        for j in range(1, cols - 1):
            if board[rows-2][j] == 'O' and board[rows-1][j] == 'O':
                self.Union(tbl[rows-2][j], tbl[rows-1][j])

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if tbl[i][j] is not None:
                    parent = self.Find(tbl[i][j])
                    if not parent.isBorder:
                        board[i][j] = 'X'

    def Find(self, x):
        root = x.parent
        while root.parent != root:
            root = root.parent

        while x != root:
            next = x.parent
            x.parent = root
            x = next

        return root

    def Union(self, x, y):
        r1 = self.Find(x)
        r2 = self.Find(y)

        if r1 == r2:
            return

        if r1.weight < r2.weight:
            r1, r2 = r2, r1

        r2.parent = r1
        r1.weight += r2.weight
        r1.isBorder = r1.isBorder or r2.isBorder


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
    res = sol.solve(board)
    print("   exp = {0}\nresult = {1}".format(exp, board))


if __name__ == "__main__":
    main()