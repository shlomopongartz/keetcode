#include <stdio.h>
#include <stdlib.h>

int maxArea(int* height, int heightSize){
	int *l;
	int *r;
	int max;
	int t;
	int area;
	int minh;

	--heightSize;
	l = height;
	r = height + heightSize;

	minh = *l < *r ? *l : *r;
	max = heightSize * minh;
	while (l < r) {
		if (*l < *r) {
			t = *l;
			for (++l; l <= r; ++l)
				if (*l > t)
					break;
		} else if (*l > *r) {
			t = *r;
			for (--r; r >= l; --r)
				if (*r > t)
					break;
		} else {
			t = *l;
			for (++l; l <= r; ++l)
				if (*l > t)
					break;
			t = *r;
			for (--r; r >= l; --r)
				if (*r > t)
					break;
		}
		if (l < r) {
			minh = *l < *r ? *l : *r;
			area = (r - l) * minh;
			if (area > max)
				max = area;
		}
	}
	return max;
}

int main()
{
	{
		int height[] = {1,8,6,2,5,4,8,3,7};
		int Output = 49;
		printf("expected %d got %d\n", Output, maxArea(height, sizeof(height)/sizeof(height[0])));
	}
	{
		int height[] = {1,1};
		int Output = 1;
		printf("expected %d got %d\n", Output, maxArea(height, sizeof(height)/sizeof(height[0])));
	}
	{
		int height[] = {4,3,2,1,4};
		int Output = 16;
		printf("expected %d got %d\n", Output, maxArea(height, sizeof(height)/sizeof(height[0])));
	}
	{
		int height[] = {1,2,1};
		int Output = 2;
		printf("expected %d got %d\n", Output, maxArea(height, sizeof(height)/sizeof(height[0])));
	}

	return 0;
}
