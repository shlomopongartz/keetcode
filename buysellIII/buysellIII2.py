class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lp = len(prices)
        if lp == 1:
            return 0
        if lp == 2:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
        dp = [[0 for j in range(lp)] for i in range(3)]
        for trans in range(1, 3):
            prev_max = prices[0] - prices[1]
            for day in range(1, lp):
                #Don't do transaction on "day"
                max = dp[trans][day - 1]
                # Sel stock bought on day "d"
                # But don't sell on day "d"
                prev_max += prices[day] - prices[day-1]
                last_profit = prices[day] - prices[day-1] + dp[trans-1][day-1]
                if last_profit > prev_max:
                        prev_max = last_profit
                if prev_max > max:
                    max = prev_max

                dp[trans][day] = max
        return dp[-1][-1]

def main():

    sol = Solution()

    prices = [1,2,3,4,5]
    exp = 4
    res = sol.maxProfit(prices)
    print("exp = {0} result = {1}".format(exp, res))

    prices = [3,3,5,0,0,3,1,4]
    exp = 6
    res = sol.maxProfit(prices)
    print("exp = {0} result = {1}".format(exp, res))

    prices = [7,6,4,3,1]
    exp = 0
    res = sol.maxProfit(prices)
    print("exp = {0} result = {1}".format(exp, res))

    prices = [1]
    exp = 0
    res = sol.maxProfit(prices)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
     main()