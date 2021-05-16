class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        i = 1
        while m > 0:
            nr = n & 1
            mr = m & 1
            n = n >> 1
            m = m >> 1
            bit = i
            i = i << 1
            if nr == 0:
                continue
            if mr == 0:
                continue
            if n > m:
                continue
            res |= bit
        return res


def main():
    s = Solution()

    nm = [5, 7]
    exp = 4
    res = s.rangeBitwiseAnd(nm[0], nm[1])
    print("exp = {0} result = {1}".format(exp, res))

    nm = [0, 1]
    exp = 0
    res = s.rangeBitwiseAnd(nm[0], nm[1])
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()