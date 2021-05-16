class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        ret = 0
        i = 1
        while i <= n:
            div = n // i
            curr_digit = div % 10
            if curr_digit == 0:
                ret += (div // 10) * i
            elif curr_digit == 1:
                mod = n % i
                ret += (div // 10) * i + (mod + 1)
            else:
                ret += (div // 10 + 1) * i
            i = i * 10


        return ret

def main():
    sol = Solution()

    n = 13
    exp = 6
    res = sol.countDigitOne(n)
    print("   exp = {0}\nresult = {1}".format(exp, res))

    n = 0
    exp = 0
    res = sol.countDigitOne(n)
    print("   exp = {0}\nresult = {1}".format(exp, res))

    n = 100
    exp = 21
    res = sol.countDigitOne(n)
    print("   exp = {0}\nresult = {1}".format(exp, res))

if __name__ == "__main__":
    main()
