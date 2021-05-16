class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        letters = [0] * (ord('z') + 1)
        counts = [0] * (ord('z')+ 1)
        for l in t:
            letters[ord(l)] += 1
        l = 0
        r = 0

        min = len(s) + 1
        res = ""
        count = 0
        while l < len(s):
            while (count < len(t) and r < len(s)):
                ind = ord(s[r])
                if letters[ind] > 0:
                    if counts[ind] < letters[ind]:
                        count += 1
                    counts[ind] += 1
                r += 1

            #Expanded till return last min
            if count < len(t):
                return res

            while (l < r):
                ind = ord(s[l])
                if letters[ind] > 0:
                    counts[ind] -= 1
                    if counts[ind] < letters[ind]:
                        if count == len(t):
                            tmp = s[l:r]
                            if len(tmp) < min:
                                res = tmp
                                min = len(tmp)
                        count -= 1
                        #Need to extend again
                        l += 1
                        break
                l += 1

        return res

def main():

    sol = Solution()

    s = "bdab"
    t = "ab"
    res = sol.minWindow(s, t)
    exp = "ab"
    print("exp = {0} result = {1}".format(exp, res))


    s = "aa"
    t = "aa"
    res = sol.minWindow(s, t)
    exp = "aa"
    print("exp = {0} result = {1}".format(exp, res))

    s = "ADOBECODEBANC"
    t = "ABC"
    res = sol.minWindow(s, t)
    exp = "BANC"
    print("exp = {0} result = {1}".format(exp, res))

    s = "a"
    t = "a"
    res = sol.minWindow(s, t)
    exp = "a"
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()