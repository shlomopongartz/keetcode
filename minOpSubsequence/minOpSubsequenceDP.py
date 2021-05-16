class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        lt = len(target)
        la = len(arr)

        if lt == 0:
            return 0
        if la == 0:
            return lt

        dp = [[0 for j in range(la + 1)] for i in range(lt + 1)]
        for i in range(lt + 1):
            dp[i][0] = i

        for i in range(1, lt + 1):
            for j in range(1, la + 1):
                if target[i - 1] == arr[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    x = dp[i-1][j] + 1
                    y = dp[i][j-1]
                    dp[i][j] = x if x < y else y

        return dp[lt][la]


def main():
    s = Solution()

    target = [5,1,3]
    arr = [9,4,2,3,4]
    exp = 2
    res = s.minOperations(target, arr)
    print("exp = {0} result = {1}".format(exp, res))

    target = [6,4,8,1,3,2]
    arr = [4,7,6,2,3,8,6,1]
    exp = 3
    res = s.minOperations(target, arr)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()
