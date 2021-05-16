#include <stdio.h>

double myPow(double x, int n){

	int res = 1.0; // Initialize result 

	while (n > 0) { 
		// If n is odd, multiply x with result 
		if (n & 1) 
			res = res * x; 

		// n must be even now 
		n = n >> 1; // n = n/2 
		x = x * x; // Change x to x^2 
	} 
	return res; 
}
