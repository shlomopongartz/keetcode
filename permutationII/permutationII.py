class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		ll = len(nums)
		if ll < 1:
			return [nums]
		res = []
		self.tmp = [0] * len(nums)
		nums.sort()
		self.permuteUnique2(nums, 0, res)
		return res

	def permuteUnique2(self, nums, curr, res):
		if len(nums) == 0:
			t = self.tmp[:]
			res.append(t)
			return

		prev = '$'
		for i, val in enumerate(nums):
			if nums[i] == prev:
				continue
			prev = nums[i]
			self.tmp[curr] = nums[i];
			newnums = nums[:i] + nums[i+1:]
			self.permuteUnique2(newnums, curr + 1, res)

		return


def compare(res, exp):
	if len(res) != len(exp):
		print("different size")
		return
	print("same size")

def main():
	s = Solution()

	nums = [1,1,2]
	res = s.permuteUnique(nums)
	exp = [[1,1,2],[1,2,1],[2,1,1]]
	compare(res, exp)
	print(res)
	print(exp)

	nums = [1,2,3]
	res = s.permuteUnique(nums)
	exp = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
	compare(res, exp)
	print(res)
	print(exp)

if __name__ == "__main__":
     main()