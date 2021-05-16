#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char * s)
{
	char *table[0x100];
	char *p;
	char *q;
	int len;
	int max = 0;

	memset(table, 0, sizeof(table));

	q = s;
	for (p = s; *p; p++) {
		if (table[*p]) {
			/* repeated char string ended */
			len = p - q;
			if (len > max)
				max = len;
			for (; q <= table[*p]; q++)
				table[*q] = 0;
		}
		table[*p] = p;
	}
	len = p - q;
	if (len > max)
		max = len;

	return max;
}

int main()
{
	char *s;

	s = "abcabcbb";
	printf("lenght is %d\n", lengthOfLongestSubstring(s));

	s = "bbbbb";
	printf("lenght is %d\n", lengthOfLongestSubstring(s));

	s = "pwwkew";
	printf("lenght is %d\n", lengthOfLongestSubstring(s));

	s = "";
	printf("lenght is %d\n", lengthOfLongestSubstring(s));

	return 0;
}
