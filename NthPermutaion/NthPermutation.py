class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = [1,1,2,6,24,120,720,5040,40320,362880]
        perm = [i for i in range(1, n + 1)]
        res = ''
        k -= 1
        for i in range(0, n):
            choice = k // fact[n - 1]
            k = k % fact[n - 1]
            res += chr(perm[choice] + ord('0'))
            perm[choice:] = perm[choice+1:]
            n -= 1

        return res

def main():

    s = Solution()

    n = 3
    k = 3
    res = s.getPermutation(n,k)
    exp = "213"
    print("exp = {0} result = {1}".format(exp, res))

    n = 4
    k = 9
    res = s.getPermutation(n,k)
    exp = "2314"
    print("exp = {0} result = {1}".format(exp, res))

    n = 3
    k = 1
    res = s.getPermutation(n,k)
    exp = "123"
    print("exp = {0} result = {1}".format(exp, res))

    n = 3
    k = 6
    res = s.getPermutation(n,k)
    exp = "321"
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()