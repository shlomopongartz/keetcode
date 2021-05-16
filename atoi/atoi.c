#include <stdio.h>
#include <ctype.h>

int myAtoi(char * s){
	unsigned int val = 0;
	int neg = 0;
	while (*s) {
		if (isspace(*s)) {
			s++;
			continue;
		}
		break;
	}
	if (!*s)
		return 0;
	if (*s == '+') {
		s++;
	} else if (*s == '-') {
		neg = 1;
		s++;
	}
	if (!isdigit(*s))
		return 0;
	val = *s - '0';
	s++;
	while (*s) {
		if (!isdigit(*s))
			break;
		val <<= 1;
		val += (val << 2) + *(s++) - '0';
		if (val > 0x7fffffff) {
			if (!neg)
				return 0x7fffffff;
			if (val > 0x80000000)
				return 0x80000000;
			}
		}
		if (neg) {
		if (val > 0x80000000)
			return 0x80000000;
			val = -val;
	    } else {
		if (val > 0x7fffffff)
			return 0x7fffffff;
	}
	return val;
}

int main()
{
	printf("%s %d\n", "42", myAtoi("42"));
	printf("%s %d\n", "-42", myAtoi("-42"));
	printf("%s %d\n", "-91283472332", myAtoi("-91283472332"));
	return 0;
}
