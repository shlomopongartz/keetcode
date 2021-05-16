#include <stdio.h>

int patrition(int* nums, int numsSize)
{
	int i, j;

	j = 0;
	for (i = 0; i < numsSize; i++) {
		if (nums[i] <= 0) {
			int tmp;
			tmp = nums[i];
			nums[i] = nums[j];
			nums[j] = tmp;
			++j;
		}
	}
	return j;
}

int markAndScan(int* nums, int numsSize)
{
	int i;

	for (i = 0; i < numsSize; ++i) {
		int abs = nums[i] < 0 ? -nums[i] : nums[i];
		int abs_ind = abs - 1;
		if (abs_ind < numsSize && nums[abs_ind] > 0) {
			/* Convert to index */
			nums[abs_ind] = -nums[abs_ind];
		}
	}
	for (i = 0; i < numsSize; ++i) {
		if (nums[i] > 0)
			return i + 1;
	}
	/* All numbers were acounted for return next one */
	return numsSize + 1;
}

int firstMissingPositive(int* nums, int numsSize){
	int numNonPos;

	numNonPos = patrition(nums, numsSize);

	return markAndScan(&nums[numNonPos], numsSize - numNonPos); 
}


int main()
{
	{
		int nums[] = {1, 2, 0};
		int first =  firstMissingPositive(nums, sizeof(nums)/sizeof(nums[0]));
		printf("First is %d\n", first);
	}
	{
		int nums[] = {3, 4, -1, 1};
		int first =  firstMissingPositive(nums, sizeof(nums)/sizeof(nums[0]));
		printf("First is %d\n", first);
	}
	{
		int nums[] = {7, 8, 9, 11, 12};
		int first =  firstMissingPositive(nums, sizeof(nums)/sizeof(nums[0]));
		printf("First is %d\n", first);
	}
	{
		int nums[] = {7, 8, 9, 11, 12, 1, 2, 3, 4, 5, 6};
		int first =  firstMissingPositive(nums, sizeof(nums)/sizeof(nums[0]));
		printf("First is %d\n", first);
	}
	return 0;
}
