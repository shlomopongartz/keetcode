class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        lrow = len(matrix)
        lcol = len(matrix[0])

        if lrow == 1:
            for j in range(lcol):
                if matrix[0][j] == "1":
                    return 1
            return 0

        if lcol == 1:
            for i in range(lrow):
                if matrix[i][0] == "1":
                    return 1
            return 0


        dp = [[0 for j in range(lcol + 1)] for i in range(lrow + 1)]

        max = 0;
        for i in range(0, lrow):
            for j in range(0, lcol):
                if matrix[i][j] == "0":
                    dp[i + 1][j + 1] = 0
                else:
                    min = dp[i][j]
                    if dp[i + 1][j] < min:
                        min = dp[i + 1][j]
                    if dp[i][j + 1] < min:
                        min = dp[i][j + 1]
                    min += 1
                    dp[i + 1][j + 1] = min
                    if min > max:
                        max = min
        return max * max


def main():
    s = Solution()

    matrix = [["1", "0"], ["1", "0"]]
    exp = 1
    res = s.maximalSquare(matrix)
    print("exp = {0} result = {1}".format(exp, res))

    matrix = [["0", "1"]]
    exp = 1
    res = s.maximalSquare(matrix)
    print("exp = {0} result = {1}".format(exp, res))

    matrix = [["0"], ["1"]]
    exp = 1
    res = s.maximalSquare(matrix)
    print("exp = {0} result = {1}".format(exp, res))

    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    exp = 4
    res = s.maximalSquare(matrix)
    print("exp = {0} result = {1}".format(exp, res))

    matrix = [["0","1"],["1","0"]]
    exp = 1
    res = s.maximalSquare(matrix)
    print("exp = {0} result = {1}".format(exp, res))

    matrix = matrix = [["0"]]
    exp = 0
    res = s.maximalSquare(matrix)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()
