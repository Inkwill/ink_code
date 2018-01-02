//2.70

#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	int x = 0xFEFFFFFF;
	int n = 26;
	printf("fits_bits(0x%X,%d) -> %d\n" ,x,n,fits_bits(x, n));
	return 0;
}

int fits_bits(int x, int n){

	/*
		Return 1 when x can be represented as an n-bit, 2's-comlement number;0 otherwise
		Assume 1 <= n <= w
	*/
	x >>= n-1;
	//positive : return !0 if all 0;  otherwise 0
	int positive = !x;
	//negative: return !0 if all 1; otherwise 0
	int negative = !(~x);
	return positive || negative;
}
