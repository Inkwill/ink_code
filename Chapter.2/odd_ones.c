#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	unsigned n = 0x3;
	//odd_ones(n) && printf("0x%X  contains an odd number of 1s. \n", n);
	printf("0x%X  odd_ones ? -> %d\n", n,odd_ones(n));
	return 0;
}

// Return 1 when x contains an odd number of 1s; 0 otherwise.
// Assume  sizeof(int) = w = 32
// exclusive OR all bits of x, the final result  is  the result of  if x contains an odd number of 1s
int odd_ones(unsigned x){

	x ^= x>>16;
	x^= x>>8;
	x^= x>>4;
	x^= x>>2;
	x^= x>>1;
	return x&1;
}
