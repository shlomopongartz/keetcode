class Solution(object):
    tmp = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candsNum = len(candidates)
        self.tmp = [0] * candsNum
        self.combinationSum2(candidates, candsNum, target, res)
        return res

    def combinationSum2(self, candidates, candsNum, target, res):
        if target == 0:
            self.buildresult(candidates, res)
            return
        if candsNum == 0:
            return

        biggest = candidates[candsNum - 1]
        max = target // biggest
        t = target - max * biggest
        for rep in range(max, -1, -1):
            self.tmp[candsNum - 1] = rep
            self.combinationSum2(candidates, candsNum - 1, t, res)
            t += biggest

    def buildresult(self, candidates, res):
        l = []
        for cand, rep in enumerate(self.tmp):
            val = candidates[cand]
            for i in range(rep):
                l.append(val)
        if len(l) > 0:
            res.append(l)

def main():

    s = Solution()

    candidates = [2, 3, 6, 7]
    target = 7
    exp = [[2, 2, 3], [7]]
    print("exp = {0} result = {1}".format(exp, s.combinationSum(candidates, target)))

    candidates = [2, 3, 5]
    target = 8
    exp = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print("exp = {0} result = {1}".format(exp, s.combinationSum(candidates, target)))

    candidates = [2]
    target = 1
    exp = []
    print("exp = {0} result = {1}".format(exp, s.combinationSum(candidates, target)))

    candidates = [1]
    target = 1
    exp = [[1]]
    print("exp = {0} result = {1}".format(exp, s.combinationSum(candidates, target)))

    candidates = [1]
    target = 2
    exp = [[1, 1]]
    print("exp = {0} result = {1}".format(exp, s.combinationSum(candidates, target)))

if __name__ == "__main__":
     main()