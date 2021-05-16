class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        if not self.isAnagram(s1, s2):
            return False

        self.cash = set()
        return self.isScramble2(s1, s2)

    def isScramble2(self, s1, s2):
        #s1 and s2 are anagrams
        if s1 == s2:
            self.cash.add(s1 + '-' + s2)
            return True

        if s1 + '-' + s2 in self.cash:
            return True

        for i in range(1, len(s1)):
            #We started from and anagram so it is
            #enugh to check the shorted side
            if i < len(s1) - i:
                isanagram = self.isAnagram(s1[:i], s2[:i])
            else:
                isanagram = self.isAnagram(s1[i:], s2[i:])
            if isanagram:
                if self.isScramble2(s1[:i], s2[:i]) and self.isScramble2(s1[i:], s2[i:]):
                    self.cash.add(s1 + '-' + s2)
                    return True

            if i < len(s1) - i:
                isanagram = self.isAnagram(s1[:i], s2[len(s1) - i:])
            else:
                isanagram = self.isAnagram(s1[i:], s2[:len(s1) - i])
            if isanagram:
                if self.isScramble2(s1[:i], s2[len(s1) - i:]) and self.isScramble2(s1[i:], s2[:len(s1) - i]):
                    self.cash.add(s1 + '-' + s2)
                    return True

        return False

    def hashVal(self, s):
        h = 0
        for c in s:
            t = (ord(c) - ord('a')) * (30 * 26)
            h = (h + t) % 8191
        return h

    def isAnagram(self, s1, s2):
        x = self.hashVal(s1)
        y = self.hashVal(s2)
        if x == y:
            return True
        else:
            return False


def main():

    sol = Solution()

    s1 = "great"
    s2 = "rgeat"
    res = sol.isScramble(s1, s2)
    exp = True
    print("exp = {0} result = {1}".format(exp, res))

    s1 = "abcde"
    s2 = "caebd"
    res = sol.isScramble(s1, s2)
    exp = False
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()