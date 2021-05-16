#include <stdio.h>

void rotate(int** matrix, int matrixSize, int* matrixColSize)
{
	int i, j, t;

	*matrixColSize = matrixSize;
	if (matrixSize <= 1)
		return;
	// Transpos
	for (i = 0; i < matrixSize - 1; ++i) {
		for (j = i + 1; j < matrixSize; ++j) {
			t = matrix[i][j];
			matrix[i][j] = matrix[j][i];
			matrix[j][i] = t;
		}
	}
	// Mirror
	for (i = 0; i < matrixSize; ++i) {
		for (j = 0; j < (matrixSize + 1) / 2; ++j) {
			t = matrix[i][j];
			matrix[i][j] = matrix[i][matrixSize - j - 1];
			matrix[i][matrixSize - j - 1] = t;
		}
	}
}

void compare(int **m1, int **m2, int lm)
{
	int i, j;

	for (i = 0; i < lm; ++i) {
		for (j = 0; j < lm; ++j) {
			if (m1[i][j] != m2[i][j]) {
				printf("not match\n");
				return;
			}
		}
	}
	printf("match\n");
}

int main()
{
	int matrixColSize;
	{
		int matrix[4][4] = {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
		int exp[4][4] = {{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}};
		rotate((int **)matrix, 4, &matrixColSize);
		compare((int **)matrix, (int **)exp, 4);
	}
	{
		int matrix[1][1] = {{1}};
		int exp[1][1] = {{1}};
		rotate((int **)matrix, 1, &matrixColSize);
		compare((int **)matrix, (int **)exp, 1);
	}
	{
		int matrix[2][2] = {{1, 2}, {3, 4}};
		int exp[2][2] = {{3, 1}, {4, 2}};
		rotate((int **)matrix, 2, &matrixColSize);
		compare((int **)matrix, (int **)exp, 2);
	}
	return 0;
}
