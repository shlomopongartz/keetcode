#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int num[] = {1,1,3,3,3,3,3,4,3,4};

char tab[][4] = {{'0',0,0,0}   , {'1',0,0,0},
		{'a','b','c',0}, {'d','e','f',0}, {'g','h','i',0},
		{'j','k','l',0}, {'m','n','o',0}, {'p','q','r','s'},
		{'t','u','v',0}, {'w','x','y','z'}};

char ** letterCombinations(char * digits, int* returnSize) {
	int len;
	char c;
	int count;
	int options;
	int cn;
	int i, j, ind;
	int from, to;
	char *p;
	char **ret; 


	len = 0;
	options = 1;
	for (p = digits; *p; ++p) {
		options *= num[*p - '0'];
		++len;
	}

	if (len == 0) {
		*returnSize = 0;
		ret = malloc(sizeof(char *));
		if (!ret) {
			perror("malloc");
			return NULL;
		}
		*ret = NULL;
		return ret;
	}

	/* return size */
	ret = malloc(options * sizeof(char *));
	if (!ret) {
		perror("malloc");
		*returnSize = 0;
		return NULL;
	}

	ind = len - 1;
	cn = digits[ind] - '0';
	for (i = 0; i < num[cn]; ++i) {
		ret[i] = malloc(len + 1);
		ret[i][len] = '\0';
		ret[i][ind] = tab[cn][i];
	}
	count = num[cn];
	for (--ind; ind >= 0; --ind) {
		cn = digits[ind] - '0';
		/* Fill first option */
		for (j = 0; j < count; ++j) {
			ret[j][ind] = tab[cn][0];
		}
		from = 0;
		to = count;
		/* Make (cn - 1) copies of prev "count" entries */
		for (i = 1; i < num[cn]; ++i) {
			for (j = 0; j < count; ++j) {
				ret[to + j] = malloc(len + 1);
				memcpy(ret[to + j], ret[from + j], len + 1);
				/* Add optional char */
				ret[to + j][ind] = tab[cn][i];
			}
			from = to;
			to += count;
		}
		count = to;
	}

	*returnSize = options;

	return ret;
}

void print(char **lstr, int size)
{
	int i;
	printf("size is %d\n", size);
	for (i = 0; i < size; ++i) {
		printf("[%s] ", lstr[i]);
	}
	printf("\n");
}

int main()
{
	int returnSize;
	{
		char *s = "22";
		char **out = letterCombinations(s, &returnSize);
		print(out,  returnSize);
	}
	{
		char *s = "23";
		char **out = letterCombinations(s, &returnSize);
		print(out,  returnSize);
	}
	{
		char *s = "";
		char **out = letterCombinations(s, &returnSize);
		print(out,  returnSize);
	}
	{
		char *s = "2";
		char **out = letterCombinations(s, &returnSize);
		print(out,  returnSize);
	}
	{
		char *s = "5424951";
		char **out = letterCombinations(s, &returnSize);
		print(out,  returnSize);
	}
	return 0;
}
