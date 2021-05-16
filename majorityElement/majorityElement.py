class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            else:
                return nums

        (cand1, cand2) = self.findCands(nums)
        (valid1, valid2) = self.validate(nums, cand1, cand2)
        if valid1 and valid2:
            return [cand1, cand2]
        if valid1:
            return [cand1]
        if valid2:
            return [cand2]
        return []

    def findCands(self, nums):
        cand1 = 10000000000
        cand2 = 10000000000
        count1 = 0
        count2 = 0
        for i in nums:
            if i == cand1:
                count1 += 1
            elif i == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = i
                count1 = 1
            elif count2 == 0:
                cand2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return (cand1, cand2)

    def validate(self, nums, cand1, cand2):
        count1 = 0
        count2 = 0
        for i in nums:
            if i == cand1:
                count1 += 1
            elif i == cand2:
                count2 += 1

        threshold = len(nums) // 3

        return (count1 > threshold , count2 > threshold)

def main():
    sol = Solution()

    nums = [3,2,3]
    exp = [3]
    res = sol.majorityElement(nums)
    print("   exp = {0}\nresult = {1}".format(exp, res))

    nums = [1]
    exp = [1]
    res = sol.majorityElement(nums)
    print("   exp = {0}\nresult = {1}".format(exp, res))

    nums = [1,2]
    exp = [1,2]
    res = sol.majorityElement(nums)
    print("   exp = {0}\nresult = {1}".format(exp, res))


if __name__ == "__main__":
    main()
