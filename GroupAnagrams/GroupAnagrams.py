class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 2:
            return [strs]
        hash = {}
        for str in strs:
            c = self.cannon(str)
            entry = hash.get(c, None)
            if entry is None:
                hash[c] = [str]
            else:
                entry.append(str)
        res = []
        for key, item in hash.items():
            res.append(item)
        return res

    def cannon(self, str):
        cnt = [0] * 26
        for a in str:
            cnt[ord(a) - ord('a')] += 1
        s = ""
        for i, n in enumerate(cnt):
            if n > 0:
                s += chr(i + ord('a')) * n
        return s

def main():

    s = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    exp = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print("exp = {0} result = {1}".format(exp, s.groupAnagrams(strs)))

    strs = [""]
    exp = [[""]]
    print("exp = {0} result = {1}".format(exp, s.groupAnagrams(strs)))

    strs = ["a"]
    exp = [["a"]]
    print("exp = {0} result = {1}".format(exp, s.groupAnagrams(strs)))

if __name__ == "__main__":
     main()