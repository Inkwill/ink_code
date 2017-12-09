//2.66

#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	unsigned n = 0x12345678;
	printf("0x%X  leftmost_one ? -> %d\n", n,leftmost_one(n));
	return 0;
}

/* 
* Generate mask indicating leftmost 1 in x.
* Assume  sizeof(int) = w = 32
* For example, 0xFF00 -> 0x8000, and 0x6600 -> 0x4000.
* If x = 0, then return 0.
*/
int leftmost_one(unsigned x){

	
	return 0;
}
