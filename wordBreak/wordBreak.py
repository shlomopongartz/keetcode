class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ls = len(s)
        ld = len(wordDict)

        self.ls = ls

        if ls == 0 or ld == 0:
            return []

        dp = [[] for i in range(ls)]
        marked = [False] * ls

        next = [ls]
        while len(next) > 0:
            i = next.pop(0)
            for j, word in enumerate(wordDict):
                start = i - len(word)
                if start >= 0:
                    if word == s[start:i]:
                        #Can reach position start from position i using word j
                        dp[start].append((i,j))
                        if not marked[start]:
                            next.append(start)
                            marked[start] = True

        if len(dp[0]) == 0:
            return []

        self.res = []
        self.tmp = []

        self.doprint(dp, 0, wordDict)

        return self.res

    def doprint(self, dp, ind, wordDict):
        if ind == self.ls:
            self.res.append(" ".join(self.tmp))
            return
        for pos, w in dp[ind]:
            self.tmp.append(wordDict[w])
            self.doprint(dp, pos, wordDict)
            self.tmp.pop()


def main():
    sol = Solution()

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    exp = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    res = sol.wordBreak(s, wordDict)
    print("exp = {0} result = {1}".format(exp, res))

    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    exp = ["cats and dog", "cat sand dog"]

    res = sol.wordBreak(s, wordDict)
    print("exp = {0} result = {1}".format(exp, res))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    exp = []

    res = sol.wordBreak(s, wordDict)
    print("exp = {0} result = {1}".format(exp, res))


    res = sol.wordBreak(s, wordDict)
    print("exp = {0} result = {1}".format(exp, res))


    #root = [-10,9,20,null,null,15,7]

if __name__ == "__main__":
    main()
