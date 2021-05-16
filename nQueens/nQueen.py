from copy import deepcopy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 2:
            #return [[".","."],[".","."]]
            return []
        if n == 3:
            #return [[".",".","."],[".",".","."],[".",".","."]]
            return []

        self.solution = [['.' for i in range(n)] for j in range(n)]
        self.res = []
        self.assignment = [0] * n
        self.assignments = []
        perm = [i for i in range(n)]

        self.solveNQueens2(0, n, perm)

        #Convert assignments boards.
        self.buildRes(n)

        return self.res

    def buildRes(self, n):
        for sol in self.assignments:
            t = [''] * n
            for c, r in enumerate(sol):
                s = ''
                for i in range(c):
                    s += '.'
                s += 'Q'
                for i in range(c + 1, n):
                    s += '.'
                t[r] = s
            self.res.append(t)

    def isSafe(self, col, row):
        for c in range(col):
            r = self.assignment[c]
            dx = col - c
            dy = row - r
            if dx == dy or dx == -dy:
                return False
        return True

    def solveNQueens2(self, col, n, perm):
        if n == 0:
            #Deep copy
            t = self.assignment[:]
            self.assignments.append(t)
            return

        for i, h in enumerate(perm):
            if self.isSafe(col, h):
                self.assignment[col] = h
                self.solveNQueens2(col + 1, n - 1, perm[:i] + perm[i+1:])

def main():
    sol = Solution()

    n = 4
    res = sol.solveNQueens(n)
    exp = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print("exp    = {0} \nresult = {1}".format(exp, res))

    n = 1
    res = sol.solveNQueens(n)
    exp = [["Q"]]
    print("exp    = {0} \nresult = {1}".format(exp, res))

if __name__ == "__main__":
    main()