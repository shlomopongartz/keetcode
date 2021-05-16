#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize){
	int i, j, k, len;
	int *list;
	int bit, l;

	len = 1 << n;
	list = malloc(len * sizeof(int));
	if (! list) {
		perror("malloc");
		*returnSize = 0;
		return NULL;
	}
	*returnSize = len;

	list[0] = 0;
	bit = 1;
	l = 2;
	for (i = 0; i < n; ++i) {
		j = 0;
		k = l - 1;
		while (j < k) {
			list[k] = list[j] | bit;
			++j;
			--k;
		}
		bit <<= 1;
		l <<= 1;
	}
	return list;
}

void print(int *list, int len)
{
	int i;
	printf("[");
	for (i = 0; i < len; ++i)
		printf("%d, ", list[i]);
	printf("]\n");
}

int main()
{
	int retSize;
	int *res;

	{
		res = grayCode(2, &retSize);
		print(res, retSize);
		free(res);
	}

	{
		res = grayCode(1, &retSize);
		print(res, retSize);
		free(res);
	}
	return 0;
}
