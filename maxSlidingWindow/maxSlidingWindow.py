class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = [0] * (len(nums) - k + 1)
        queue = [0]
        for i, n in enumerate(nums[1:k], 1):
            if n <= nums[queue[-1]]:
                queue.append(i)
            else:
                while len(queue) > 0:
                    if nums[queue[-1]] < n:
                        queue.pop()
                    else:
                        break
                queue.append(i)

        res[0] = nums[queue[0]]

        fall_out = 0
        out = 1
        for i, n in enumerate(nums[k:], k):
            if n <= nums[queue[-1]]:
                queue.append(i)
            else:
                while len(queue) > 0:
                    if nums[queue[-1]] < n:
                        queue.pop()
                    else:
                        break
                queue.append(i)
            if queue[0] <= fall_out:
                queue.pop(0)
            fall_out += 1
            res[out] = nums[queue[0]]
            out += 1
        return res

def main():
    s = Solution()

    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    exp = [10,10,9,2]
    res = s.maxSlidingWindow(nums, k)
    print("exp = {0} result = {1}".format(exp, res))

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    exp = [3,3,5,5,6,7]
    res = s.maxSlidingWindow(nums, k)
    print("exp = {0} result = {1}".format(exp, res))

    nums = [1]
    k = 1
    exp = [1]
    res = s.maxSlidingWindow(nums, k)
    print("exp = {0} result = {1}".format(exp, res))

    nums = [1, -1]
    k = 1
    exp = [1, -1]
    res = s.maxSlidingWindow(nums, k)
    print("exp = {0} result = {1}".format(exp, res))

    nums = [9,11]
    k = 2
    exp = [11]
    res = s.maxSlidingWindow(nums, k)
    print("exp = {0} result = {1}".format(exp, res))

    nums = [4,-2]
    k = 2
    exp = [4]
    res = s.maxSlidingWindow(nums, k)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
     main()
