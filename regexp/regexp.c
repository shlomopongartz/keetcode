#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum {false, true} bool;

bool isMatch(char * s, char * p){
	int ls, lp;
	char **dp;
	char *flat;
	int tmp;
	int i, j;
	bool res = false;

	ls = strlen(s);
	lp = strlen(p);

	dp = malloc((lp + 1) * sizeof(char *));
	if (!dp) {
		perror("malloc");
		return false;
	}
	flat = calloc((lp + 1) * (ls + 1), sizeof(char));
	if (!flat) {
		perror("malloc");
		return false;
	}

	tmp = 0;
	for (i = 0; i <= lp; ++i) {
		dp[i] = flat + tmp;
		tmp += (ls + 1);
	}

	/* Empty string match with empty string */
	dp[0][0] = true;
	/* Deals with patterns like a* or a*b* or a*b*c* */
	for (i = 1; i < lp; ++i) {
		int ii = i + 1;
		if (p[i] == '*')
			dp[ii][0] = dp[i - 1][0];
	}

	for (i = 0; i < lp; ++i) {
		int ii = i + 1;
		switch (p[i]) {
		case '*':
			for (j = 0; j < ls; ++j) {
				int jj = j + 1;
				/* Zero occrence of X* */
				dp[ii][jj] = dp[i-1][jj];
				/* another occurence */
				if (p[i-1] == '.' || p[i - 1] == s[j]) {
					dp[ii][jj] = dp[ii][jj] || dp[ii][j];
				}
			}
			break;
		case '.':
			for (j = 0; j < ls; ++j) {
				int jj = j + 1;
				dp[ii][jj] = dp[i][j];
			}
			break;
		default:
			for (j = 0; j < ls; ++j) {
				int jj = j + 1;
				if (s[j] == p[i]) {
					dp[ii][jj] = dp[i][j];
				}
			}
			break;
		}
	}

	printf("    ");
	for (j = 0; j < ls; ++j)
		printf("%c ", s[j]);
	printf("\n  ");
	for (j = 0; j <= ls; ++j) {
		printf("%d ", dp[0][j]);
	}
	printf("\n");
	for (i = 1; i <= lp; ++i) {
		printf("%c ", p[i-1]);
		for (j = 0; j <= ls; ++j) {
			printf("%d ", dp[i][j]);
		}
		printf("\n");
	}

	/* table is (lp + 1) X (ls + 1) */
	res = dp[lp][ls];

	free(flat);
	free(dp);

	return res;
}

int main()
{
	{
		char *s = "aa";
		char *p = "a*";
		int exp = 1;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "ab";
		char *p = ".*";
		int exp = 1;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "aab";
		char *p = "c*a*b";
		int exp = 1;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "mississippi";
		char *p =  "mis*is*p*.";
		int exp = 0;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "aaa";
		char *p = "ab*a";
		int exp = 0;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "aaba";
		char *p = "ab*a*c*a";
		int exp = 0;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "a";
		char *p = "ab*";
		int exp = 1;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	{
		char *s = "bbbba";
		char *p = ".*a*a";
		int exp = 1;
		printf("s=[%s] p=[%s], match=%d exp=%d\n", s, p, isMatch(s, p), exp);
	}
	return 0;
}
