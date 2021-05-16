class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        if ln == 1:
            return nums
        if ln == 2:
            if nums[0] <= nums[1]:
                return nums
            else:
                if ln == 2:
                    if nums[0] <= nums[1]:
                        return
                    else:
                        nums[0], nums[1] = nums[1], nums[0]
                        return

        l = -1
        r = ln
        x = 0
        while x < r:
            if nums[x] == 0:
                l += 1
                nums[l],nums[x] = nums[x],nums[l]
                #nums[l] was 1
                x += 1
            elif nums[x] == 1:
                x += 1
            else:
                r -= 1
                nums[r],nums[x] = nums[x],nums[r]
                #Don't increment x
        return nums

def main():
    s = Solution()

    nums = [0, 1]
    exp = [0,1]
    s.sortColors(nums)
    print("exp = {0} result = {1}".format(nums, exp))

    nums = [1, 0]
    exp = [0,1]
    s.sortColors(nums)
    print("exp = {0} result = {1}".format(nums, exp))

    nums = [2, 0, 2, 1, 1, 0]
    exp = [0,0,1,1,2,2]
    s.sortColors(nums)
    print("exp = {0} result = {1}".format(nums, exp))

    nums = [2, 0, 1]
    exp = [0,1,2]
    s.sortColors(nums)
    print("exp = {0} result = {1}".format(nums, exp))

    nums = [2, 1, 0]
    exp = [0,1,2]
    s.sortColors(nums)
    print("exp = {0} result = {1}".format(nums, exp))

    nums = [0]
    exp = [0]
    s.sortColors(nums)
    print("exp = {0} result = {1}".format(nums, exp))


if __name__ == "__main__":
     main()
