#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *convert(char *s, int numRows)
{
	int len;
	int diag;
	int cycle;
	int cycles;
	int leftover;
	int i, j;
	int target;
	char *res;
	int maxCols;
	char *p;
	char *q;

	fprintf(stderr, "numRows %d\n", numRows);

	if (numRows == 1)
		return strdup(s);

	len = strlen(s);
	if (len < 3)
		return strdup(s);

	/* One extra for '\0' */
	res = malloc(len + 1);
	if (!res) {
		perror("malloc");
		return NULL;
	}
	
	if (numRows == 2) {
		/* Make it works for odd lines */
		q = res;
		p = s;
		for (i = 0; i < (len + 1) / 2 ; ++i) {
			*q++ = *p; p += 2;
		}
		p = s + 1;
		for (i = 0; i < len / 2 ; ++i) {
			*q++ = *p; p += 2;
		}
		*q = '\0';
		return res;
	}

	diag = numRows - 2;
	cycle = numRows + (numRows - 2);
	cycles = len / cycle;
	leftover = len - (cycles * cycle);
	maxCols = (len + cycle - 1) / cycle;
	fprintf(stderr, "len %d cycle %d\n", len, cycle);
	fprintf(stderr, "maxCols %d\n", maxCols);
	fprintf(stderr, "leftover %d\n", leftover);

	res[0] = '\0';

	return res;
}

int main()
{
#if 0
	{
		char *s = "PAYPALISHIRING";
		int numRows = 2;
		char *expect = "PYAIHRNAPLSIIG";
		char *res = convert(s, numRows);
		printf("got %s expects %s cmp %d\n", res, expect, strcmp(expect, res));
	}
	{
		char *s = "PAYPALISHIRIN";
		int numRows = 2;
		char *expect = "PYAIHRNAPLSII";
		char *res = convert(s, numRows);
		printf("got %s expects %s cmp %d\n", res, expect, strcmp(expect, res));
	}
	{
		char *s = "A";
		int numRows = 1;
		char *expect = "A";
		char *res = convert(s, numRows);
		printf("got %s expects %s cmp %d\n", res, expect, strcmp(expect, res));
	}
#endif
	{
		char *s = "PAYPALISHIRING";
		int numRows = 3;
		char *expect = "PAHNAPLSIIGYIR";
		char *res = convert(s, numRows);
		printf("got %s expects %s cmp %d\n", res, expect, strcmp(expect, res));
	}
#if 0
	{
		char *s = "PAYPALISHIRING";
		int numRows = 4;
		char *expect = "PINALSIGYAHRPI";
		char *res = convert(s, numRows);
		printf("got %s expects %s cmp %d\n", res, expect, strcmp(expect, res));
	}
#endif
	return 0;
}
