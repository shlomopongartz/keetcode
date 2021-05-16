class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        lt = len(triangle)
        if lt == 1:
            return triangle[0][0]

        dp = [[0 for j in range(i)] for i in range(1, lt)]
        dp.append(triangle[lt - 1])
        for i in range(lt - 2, -1, -1):
            for j in range(i + 1):
                if dp[i+1][j] < dp[i+1][j+1]:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i + 1][j+1]
                dp[i][j] += triangle[i][j]
        return dp[0][0]

def main():

    sol = Solution()

    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    exp = 11
    res = sol.minimumTotal(triangle)
    print("exp = {0} result = {1}".format(exp, res))

    triangle = [[-10]]
    exp = -10
    res = sol.minimumTotal(triangle)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()