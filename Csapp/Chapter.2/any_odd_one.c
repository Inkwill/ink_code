//2.64
#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	unsigned n = 0xc8888888;
	printf("0x%X  any_odd_one ? -> %d\n", n,any_odd_one(n));
	return 0;
}

// Return 1 when any odd bit of x equals 1; 0 otherwise.
// Assume  sizeof(int) = w = 32
int any_odd_one(unsigned x){

	unsigned mask = x<<1;
	// return 0 if max is true
	return (x&mask)||0;
}
