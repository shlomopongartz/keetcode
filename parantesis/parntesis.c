#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int catalantbl[9]; /* Input is limited to 8 */

/* Compute Catalan number i.e. (2n)! / (n! * (n + 1)!) */
/* we have ((n+2) * (n+3) *..* (2n)) / (1 * 2 * 3 *..* n)  */
unsigned long int catalan(unsigned int n) 
{
	unsigned long int res = 0; 

	// Base case 
	if (n <= 1) {
		catalantbl[1] = 1;
		return 1;
	}

	if (catalantbl[n] > 0)
		return n;

	// catalan(n) is sum of  
	// catalan(i)*catalan(n-i-1) 
	for (int i = 0; i < n; i++) 
		res += catalan(i) * catalan(n - i - 1); 

	return res; 
}

void generateParenthesis2(int n, int pos, int l, int r, char **out, int *ind)
{
	static char tmp[17]; /* N is limited to 8 */
	if (r == n) {
		memcpy(out[*ind], tmp, n + n);
		out[(*ind)++][n + n] = '\0';
	}
	if (l > r) {
		tmp[pos] = ')';
		generateParenthesis2(n, pos + 1, l, r + 1, out, ind);
	}
	if (l < n) {
		tmp[pos] = '(';
		generateParenthesis2(n, pos + 1, l + 1, r, out, ind);
	}
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** generateParenthesis(int n, int* returnSize){
	unsigned long outsize;
	char **out;
	int i;
	int ind = 0;

	outsize = catalan(n);

	out = malloc(outsize * sizeof(char *));
	if (!out) {
		perror("malloc");
		return NULL;
	}
	for (i = 0; i < outsize; ++i) {
		out[i] = malloc(n + n + 1);
		if (!out[i]) {
			perror("malloc");
			return NULL;
		}
	}

	generateParenthesis2(n, 0, 0, 0, out, &ind);

	*returnSize = outsize;

	return out;
}

void printOut(char **out, int size)
{
	int i;
	printf("[");
	for (i = 0; i < size; ++i) {
		printf("%s,", out[i]);
	}
	printf("]\n");
} 

int main()
{
	{
		char **out;
		int returnSize;
		out = generateParenthesis(1, &returnSize);
		printOut(out, returnSize);
	}
	{
		char **out;
		int returnSize;
		out = generateParenthesis(3, &returnSize);
		printOut(out, returnSize);
	}

	return 0;
}
