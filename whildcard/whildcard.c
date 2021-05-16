#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isMatch(char * s, char * p){
	int ls, lp;
	bool **dp;
	bool *dpdat;
	int i, j, tmp;
	bool res;

	ls = strlen(s);
	lp = strlen(p);

	if (ls == 0 && lp == 0)
		return true;
	if (ls == 0 || lp == 0)
		return false;

	dp = (bool **) malloc((lp + 1) * sizeof(bool *));
	if (!dp) {
		perror("malloc");
		return false;
	}
	dpdat = (bool *) calloc((lp + 1) * (ls + 1), sizeof(bool));
	if (!dpdat) {
		perror("malloc");
		return false;
	}
	tmp = 0;
	for (i = 0; i <= lp; i++) {
		dp[i] = dpdat + tmp;
		tmp += ls + 1;
	}

	dp[0][0] = true;
	if (p[0] == '*') {
		dp[1][0] = true;
	}

	for (i = 0; i < lp; ++i) {
		char c = p[i];
		for (j = 0; j < ls; ++j) {
			if (c == s[j] || c == '?') {
				dp[i+1][j+1] = dp[i][j];
			} else if (c == '*') {
				dp[i+1][j+1] = dp[i][j] ||
				               dp[i][j+1] ||
				               dp[i+1][j];
			}
		}
	}
	res = dp[lp][ls];

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


	free(dp);
	free(dpdat);

	return res;
}

int main()
{
	char *s;
	char *p;

	{
		s = "";
		p = "******";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), true);
	}
	{
		s = "aab";
		p = "c*a*b";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), false);
	}
	{
		s = "aa";
		p = "a";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), false);
	}
	{
		s = "aa";
		p = "*";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), true);
	}
	{
		s = "cb";
		p = "?a";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), false);
	}
	{
		s = "adceb";
		p = "*a*b";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), true);
	}
	{
		s = "acdcb";
		p = "a*c?b";
		printf("s=[%s] p=[%s] matched=%d expects=%d\n",
			s, p, isMatch(s, p), false);
	}
}
