class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        foundLast = False
        for word in wordList:
            if word == endWord:
                foundLast = True
                break
        if not foundLast:
            return 0

        q2 = [beginWord]
        rest2 = wordList
        level = 1
        while len(q2) > 0:
            q1 = q2
            q2 = []
            rest1 = rest2
            rest2 = []
            level += 1
            for word1 in q1:
                for word2 in rest1:
                    if self.dist(word1, word2) == 1:
                        if word2 == endWord:
                            return level
                        q2.append(word2)
                    else:
                        rest2.append(word2)
        return 0

    def dist(self, w1, w2):
        diff = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return 2
        return diff

def main():

    sol = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    exp = 5
    res = sol.ladderLength(beginWord, endWord, wordList)
    print("exp = {0} result = {1}".format(exp, res))

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    exp = 0
    res = sol.ladderLength(beginWord, endWord, wordList)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()