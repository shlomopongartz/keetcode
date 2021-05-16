class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        ls = len(s)
        lt = len(t)

        if ls < lt:
            return 0
        if s == t:
            return 1

        dp = [[0 for j in range(ls + 1)] for i in range(lt + 1)]
        for i in range(ls + 1):
            dp[0][i] = 1
        for i, ct in enumerate(t, 1):
            for j, cs in enumerate(s, 1):
                dp[i][j] = dp[i][j - 1]
                if ct == cs:
                    dp[i][j] += dp[i-1][j-1]

        return dp[lt][ls]


def main():

    sol = Solution()

    s = "b"
    t = "b"
    exp = 1
    res = sol.numDistinct(s, t)
    print("exp = {0} result = {1}".format(exp, res))

    s = "rabbbit"
    t = "rabbit"
    exp = 3
    res = sol.numDistinct(s, t)
    print("exp = {0} result = {1}".format(exp, res))

    s = "babgbag"
    t = "bag"
    exp = 5
    res = sol.numDistinct(s, t)
    print("exp = {0} result = {1}".format(exp, res))

    s = "cbabacbacab"
    t = "abb"
    exp = 4
    res = sol.numDistinct(s, t)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()