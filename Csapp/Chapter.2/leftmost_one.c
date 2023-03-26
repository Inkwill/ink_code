//2.66

#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	unsigned n = 0x80000001;
	printf("0x%X  leftmost_one ? -> 0x%X\n", n,leftmost_one(n));
	return 0;
}

/* 
* Generate mask indicating leftmost 1 in x.
* Assume  sizeof(int) = w = 32
* For example, 0xFF00 -> 0x8000, and 0x6600 -> 0x4000.
* If x = 0, then return 0.
*/
unsigned leftmost_one(unsigned x){

	x |= (x>>1);
	x |= (x>>2);
	x |= (x>>4);
	x |= (x>>8);
	x |= (x>>16);
	x ^= (x>>1);
	return x;
}
