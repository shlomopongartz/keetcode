#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum {false, true} bool;

bool isMatch(char * s, char * p){
	int ls, lp;
	char *q;
	char *r;
	char *t;
	char **dp;
	char *flat;
	int tmp;
	int i, j;
	bool res = false;

	ls = strlen(s);
	lp = strlen(p);

	t = malloc(lp + 2);
	if (!t) {
		perror("malloc");
		return false;
	}
	lp = 0;
	for (q = p, r = t; *q; ++q) {
		if (*q == '*') {
			if (*(r - 1) == '.')
				*(r - 1) = '$';
			else
				*(r - 1) = toupper(*(r - 1));
		} else {
			*r = *q;
			r++;
			lp++;
		}
	}

	t[lp] = '&';
	lp++;
	t[lp] = '\0';

	s = strndup(s, ls + 2);
	if (!s) {
		perror("malloc");
		return false;
	}
	s[ls] = '&';
	ls++;
	s[ls] = '\0';

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
	for (i = 0; i < lp; ++i) {
		int ii = i + 1;
		for (j = 0; j < ls; ++j) {
			int jj = j + 1;
			if (s[j] == t[i] || t[i] == '.') {
				if (dp[i][j] == true || dp[i][jj] == 2)
					dp[ii][jj] = true;
			} else {
				if (t[i] == '$') {
					if (dp[i][j] == true || dp[ii][j] == true || dp[i][jj] == 2)
						dp[ii][jj] = true;
				} else {
					if (isupper(t[i])) {
						if (tolower(t[i]) == s[j]) {
							if (dp[i][j] == true || dp[ii][j] == true || dp[i][jj] == 2)
								dp[ii][jj] = true;
						} else {
							if (dp[i][j] == true || dp[i][jj] == 2)
								dp[ii][jj] = 2;
						}
					}
				}
			}
		}
	}
	/* table is (lp + 1) X (ls + 1) */
	res = dp[lp][ls];

	free(s);
	free(t);
	free(flat);
	free(dp);

	return res;
}

int main()
{
	{
		char *s = "aa";
		char *p = "a*";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	{
		char *s = "ab";
		char *p = ".*";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	{
		char *s = "aab";
		char *p = "c*a*b";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	{
		char *s = "mississippi";
		char *p =  "mis*is*p*.";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	{
		char *s = "aaa";
		char *p = "ab*a";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	{
		char *s = "aaba";
		char *p = "ab*a*c*a";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	{
		char *s = "a";
		char *p = "ab*";
		printf("s=[%s] p=[%s], match=%d\n", s, p, isMatch(s, p));
	}
	return 0;
}
