class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = {}
        for x in nums:
            if x in ht:
                continue
            l = ht.get(x - 1, [x])
            r = ht.get(x + 1, [x])
            min = l[0]
            max = r[-1]
            ht[min] = [min, max]
            ht[max] = [min, max]
            ht[x] = [min, max]

        max = -1
        for v in ht.values():
            diff = v[1] - v[0]
            if diff > max:
                max = diff
        return max+1


def main():
    s = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    exp = 4
    res = s.longestConsecutive(nums)
    print("exp = {0} result = {1}".format(exp, res))

    nums = [0,3,7,2,5,8,4,6,0,1]
    exp = 9
    res = s.longestConsecutive(nums)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
    main()
