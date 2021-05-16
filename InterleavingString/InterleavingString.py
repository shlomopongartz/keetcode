class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False

        if len(s3) == 0:
            return True

        #S1 is rows S2 is columns
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i, c in enumerate(s1, 1):
            if c == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for i, c in enumerate(s2, 1):
            if c == s3[i-1]:
                dp[0][i] = dp[0][i-1]

        for i in range(0, len(s1)):
            ind = i
            for j in range(0, len(s2)):
                ind += 1
                if s3[ind] == s2[j] and dp[i+1][j]:
                    dp[i+1][j+1] = True
                if s3[ind] == s1[i] and dp[i][j+1]:
                    dp[i+1][j+1] = True

        return dp[len(s1)][len(s2)]

def main():
    s = Solution()

    s1 = "aab"
    s2 = "axy"
    s3 = "aaxaby"
    exp = True
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

    s1 = "aab"
    s2 = "axy"
    s3 = "aabaaxy"
    exp = False
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

    s1 = "aabd"
    s2 = "abdc"
    s3 = "aabdbadc"
    exp = False
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

    s1 = "aabc"
    s2 = "abad"
    s3=  "aabcabad"
    exp = True
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    exp = True
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    exp = False
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

    s1 = ""
    s2 = ""
    s3 = ""
    exp = True
    res = s.isInterleave(s1, s2, s3)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()
