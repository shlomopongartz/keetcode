class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ln = len(nums)
        if ln == 0:
            return [-1, -1]
        if ln == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        l = 0
        r = ln - 1

        while l <= r:
            m = (l + r + 1) // 2
            mval = nums[m]
            if target == mval:
                return [self.findMin(nums, l, m, target), self.findMax(nums, m, r, target)]
            elif mval < target:
                l = m + 1
            else:
                r = m - 1

        return [-1, -1]

    def findMin(self, nums, l, r, target):
        # nums[r] == target
        lastseen = r
        while l <= r:
            m = (l + r + 1) // 2
            if nums[m] < target:
                l = m + 1
            else:
                # nums[m] == target
                lastseen = m
                r = m - 1

        return lastseen

    def findMax(self, nums, l, r, target):
        # nums[l] == target
        lastseen = l
        while l <= r:
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                # nums[m] == target
                lastseen = m
                l = m + 1

        return lastseen



def main():
    s = Solution()

    nums = [1, 3]
    target = 1
    exp = [0, 0]
    print("exp = {0} result = {1}".format(exp, s.searchRange(nums, target)))

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    exp = [3, 4]
    print("exp = {0} result = {1}".format(exp, s.searchRange(nums, target)))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    exp = [-1, -1]
    print("exp = {0} result = {1}".format(exp, s.searchRange(nums, target)))

    nums = []
    target = 0
    exp = [-1, -1]
    print("exp = {0} result = {1}".format(exp, s.searchRange(nums, target)))

if __name__=="__main__":
    main()