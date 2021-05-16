class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.hash = {}
        self.hash[""] = 0
        return self.strangePrinterH(s)

    def strangePrinterH(self, s):
        val = self.hash.get(s, -1)
        if val >= 0:
            return val

        if len(s) == 1:
            self.hash[s] = 1
            return 1

        min = 0x7fffffff
        for split in range(1, len(s)):
            if split == 1:
                v1 = 1
            else:
                v1 = self.strangePrinterH(s[:split])
            if split == len(s) - 1:
                v2 = 1
            else:
                v2 = self.strangePrinterH(s[split:])

            t = v1 + v2
            if s[0] == s[-1]:
               t -= 1

            if t < min:
                min = t

        self.hash[s] = min
        return min

def main():

    sol = Solution()

    s = "a"
    res = sol.strangePrinter(s)
    exp = 1
    print("exp = {0} result = {1}".format(exp, res))


    s = "abcabc"
    res = sol.strangePrinter(s)
    exp = 5
    print("exp = {0} result = {1}".format(exp, res))

    s = "aaabbb"
    res = sol.strangePrinter(s)
    exp = 2
    print("exp = {0} result = {1}".format(exp, res))

    s = "aba"
    res = sol.strangePrinter(s)
    exp = 2
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()