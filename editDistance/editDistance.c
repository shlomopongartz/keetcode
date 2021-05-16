#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int minDistance(char * word1, char * word2){

	int l1, l2;
	char **dp;
	char *flat;
	int tmp;
	int i, j, im1, jm1;
	int res = 0;

	l1 = strlen(word1);
	l2 = strlen(word2);

	dp = malloc((l1 + 1) * sizeof(int *));
	if (!dp) {
		perror("malloc");
		return -1;
	}
	flat = calloc((l1 + 1) * (l2 + 1), sizeof(int));
	if (!flat) {
		perror("malloc");
		return -1;
	}

	tmp = 0;
	for (i = 0; i <= l1; ++i) {
		dp[i] = flat + tmp;
		tmp += (l2 + 1) * sizeof(int);
	}

	/* Convert empty string to empty string */
	dp[0][0] = 0;

	for (i = 1; i <= l1; ++i) {
		dp[i][0] = i;
	}
	for (j = 1; j <= l2; ++j) {
		dp[0][j] = j;
	}

	im1 = -1;
	for (i = 1; i <= l1; ++i) {
		++im1;
		jm1 = -1;
		for (j = 1; j <= l2; ++j) {
			++jm1;
			if (word1[im1] == word2[jm1]) {
				dp[i][j] = dp[i-1][j-1];
			} else {
				int min;
				min = dp[i-1][j-1];
				if (dp[i - 1][j] < min)
					min = dp[i-1][j];
				if (dp[i][j - 1] < min)
					min = dp[i][j - 1];
				dp[i][j] = min + 1;
			}
		}
	}

	/* table is (lp + 1) X (ls + 1) */
	res = dp[l1][l2];

	free(flat);
	free(dp);

	return res;
}

int main()
{
	{
		char *word1 = "a";
		char *word2 = "ab";
		int exp = 1;
		printf("word1=[%s] word2=[%s], dist=%d exp=%d\n", word1, word1, minDistance(word1, word2), exp);
	}
	{
		char *word1 = "horse";
		char *word2 = "ros";
		int exp = 3;
		printf("word1=[%s] word2=[%s], dist=%d exp=%d\n", word1, word1, minDistance(word1, word2), exp);
	}
	{
		char *word1 = "intention";
		char *word2 = "execution";
		int exp = 5;
		printf("word1=[%s] word2=[%s], dist=%d exp=%d\n", word1, word1, minDistance(word1, word2), exp);
	}
	return 0;
}
