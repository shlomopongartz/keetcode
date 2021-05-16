#include <stdio.h>

void reverse(int* nums, int numsSize)
{
	int i, j;

	i = 0; j = numsSize - 1;
	for (; i < numsSize / 2; ++i, --j) {
		int tmp = nums[i];
		nums[i] = nums[j];
		nums[j] = tmp;
	}
}

void nextPermutation(int* nums, int numsSize)
{
	int i, j, tmp, min, min_ind;

	if (numsSize < 2)
		return;

	/* Find largest decreasing sequence from the end */
	for (i = numsSize - 2; i >= 0; --i) {
		if (nums[i] < nums[i + 1])
			break;
	}
	if (i < 0) {
		/* permutation exausted return reverse of nums */
		reverse(nums, numsSize);
		return;
	}

	/* Find succ of nums[i] */
	min =  0x7fffffff;
	min_ind = i;
	for (j = i + 1; j < numsSize; ++j) {
		if (nums[j] <= nums[i])
			continue;
		if (nums[j] <= min) {
			min = nums[j];
			min_ind = j;
		}
	}

	if (min_ind > i) {
		/* SWAP */
		tmp = nums[i];
		nums[i] = nums[min_ind];
		nums[min_ind] = tmp;
	}

	/* Reverse the rest */
	if (numsSize - i  - 1 > 1) {
		reverse(&nums[i + 1], numsSize - i - 1);
	}

	return;
}

void print_nums(int *nums, long ll, char *term)
{
	long l;
	for (l = 0; l < ll; ++l)
		printf("%d ", nums[l]);
	printf("%s", term);
}

int main()
{
	{
		int nums[] = {2,3,1,3,3};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {1,5,1};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {1,3,2};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {1,2,3};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {3,2,1};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {4,3,2,1};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {1,1,5};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
	{
		int nums[] = {1};
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), " -> ");
		nextPermutation(nums, sizeof(nums)/sizeof(nums[0]));
		print_nums(nums, sizeof(nums)/sizeof(nums[0]), "\n");
	}
}
