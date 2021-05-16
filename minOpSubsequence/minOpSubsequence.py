import bisect

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        lt = len(target)
        la = len(arr)

        if lt == 0:
            return 0
        if la == 0:
            return lt

        pos = {x:i for i,x in enumerate(target)}
        xs = [pos[i] for i in arr if i in pos]

        return lt - self.LIS(xs)

    def LIS(self, xs):
        l = len(xs)
        if l == 0:
            return 0
        if l == 1:
            return 1

        cand = []

        cand.append(xs[0])
        for i in range(1, l):
            if xs[i] > cand[-1]:
                cand.append(xs[i])
            else:
                cand[bisect.bisect_left(cand, xs[i])] = xs[i]

        return len(cand)


def main():
    s = Solution()

    target = [5,1,3]
    arr = [9,4,2,3,4]
    exp = 2
    res = s.minOperations(target, arr)
    print("exp = {0} result = {1}".format(exp, res))

    target = [6,4,8,1,3,2]
    arr = [4,7,6,2,3,8,6,1]
    exp = 3
    res = s.minOperations(target, arr)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()
