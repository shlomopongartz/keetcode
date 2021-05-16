#include <stdio.h>
#include <stdlib.h>

int regbinsearch(int* nums, int l, int r, int target)
{
	while (l <= r) {
		int m, midval;
		m = (l + r + 1) / 2;
		midval = nums[m];
		if (midval == target)
			return m;
		if (midval < target) {
			l = m + 1;
		} else {
			r = r - 1;
		}
	}
	return -1;
}

int search(int* nums, int numsSize, int target){
	int l, r;

	l = 0;
	r = numsSize - 1;

	if (nums[l] < nums[r]) {
		return regbinsearch(nums, l, r, target);
	}

	while (l <= r) {
		int m, midval;
		m = (l + r + 1) / 2;
		midval = nums[m];
		if (midval == target)
			return m;
		if (nums[l] < midval) {
			/* Left to m are ordered break on the right */
			if (target < midval && nums[l] <= target) {
				return regbinsearch(nums, l, m - 1, target);
			} else {
				l = m + 1;
			}
		} else {
			/* Right ot m are ordered break on the left */
			if (target > midval && target <= nums[r]) {
				return regbinsearch(nums, m + 1, r, target);
			} else {
				r = m - 1;
			}
		}
	}
	return -1;
}

int main()
{
	{
		int nums[] = {4,5,6,7,0,1,2};
		int target = 0;
		int exp = 4;
		printf("exp = %d, res = %d\n", exp, search(nums, sizeof(nums)/sizeof(nums[0]), target));
	}
	{
		int nums[] = {4,5,6,7,0,1,2};
		int target = 3;
		int exp = -1;
		printf("exp = %d, res = %d\n", exp, search(nums, sizeof(nums)/sizeof(nums[0]), target));
	}
	{
		int nums[] = {1};
		int target = 0;
		int exp = -1;
		printf("exp = %d, res = %d\n", exp, search(nums, sizeof(nums)/sizeof(nums[0]), target));
	}
}
