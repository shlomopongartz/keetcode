#include <stdio.h>
#include <stdlib.h>

int trap(int* height, int heightSize){

	int *l;
	int *r;
	int max;
	int i;
	int sum;
	int min;

	l = malloc(2 * heightSize * sizeof(int));
	if (!l) {
		perror("malloc");
		return -1;
	}
	r = l + heightSize;

	max = 0;
	for (i = 0; i < heightSize; ++i) {
		if (height[i] > max)
			max = height[i];
		l[i] = max;
	}
	max = 0;
	for (i =  heightSize - 1; i >= 0; --i) {
		if (height[i] > max)
			max = height[i];
		r[i] = max;
	}
	sum = 0;
	for (i = 0; i < heightSize; ++i) {
		min = l[i] < r[i] ? l[i] : r[i];
		sum += min - height[i];
	}

	free(l);

	return sum;
}

int main()
{
	{
		int height[] = {0,1,0,2,1,0,1,3,2,1,2,1};
		int Output = 6;
		printf("expected %d got %d\n", Output, trap(height, sizeof(height)/sizeof(height[0])));
	}
	{
		int height[] = {4,2,0,3,2,5};
		int Output = 9;
		printf("expected %d got %d\n", Output, trap(height, sizeof(height)/sizeof(height[0])));
	}
	{
		int height[] = {4,3,2,1,4};
		int Output = 16;
		printf("expected %d got %d\n", Output, trap(height, sizeof(height)/sizeof(height[0])));
	}

	return 0;
}
