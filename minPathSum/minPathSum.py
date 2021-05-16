class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        if rows == 0:
            return 0;
        cols = len(grid[0])
        if rows == 0:
            return 0;
        if rows == 1 and cols == 1:
            return grid[0][0]

        self.dp = [[-1 for i in range(cols)] for j in range(rows)]

        self.dp[rows-1][cols-1] = grid[rows-1][cols-1]

        self.minPathSumDp(grid, 0, 0, rows - 1, cols - 1)

        return self.dp[0][0]

    def minPathSumDp(self, grid, row, col, rows, cols):
        if self.dp[row][col] > -1:
            return self.dp[row][col]

        min = 0x7fffffff
        if row < rows:
            v1 = self.minPathSumDp(grid, row + 1, col, rows, cols)
            if v1 < min:
                min = v1
        if col < cols:
            v2 = self.minPathSumDp(grid, row, col + 1, rows, cols)
            if v2 < min:
                min = v2

        self.dp[row][col] = grid[row][col] + min
        return self.dp[row][col]





def main():
    s = Solution()

    grid = [[1]]
    exp = 1
    res = s.minPathSum(grid)
    print("exp = {0} result = {1}".format(exp, res))

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    exp = 7
    res = s.minPathSum(grid)
    print("exp = {0} result = {1}".format(exp, res))

    grid = [[1,2,3],[4,5,6]]
    exp = 12
    res = s.minPathSum(grid)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
     main()
