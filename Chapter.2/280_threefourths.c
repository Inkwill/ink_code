#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int x = 0x12345678;
	printf("%d *3 / 4 = %d\n", x,(int)(x*3/4) );
	printf("%d *3 / 4 = %d\n", x,threefourths(x) );
	return 0;
}

int threefourths(int x){

	int is_neg = x >>31;
	//  every int x, equals f(first 30 bit number) plus l(last 2 bit number)
	int f = x & ~0x3;
	int l = x & 0x3;

	//f doesn't care about round at all, we just care about rounding from l*3/4
	int fd4 = f >> 2;
	int fd4m3 = (fd4 << 1) + fd4;

	int lm3 = (l << 1) + l;
	int bias = (1 << 2) - 1;
	(is_neg && (lm3 += bias));
	int lm3d4 = lm3 >> 2;

	return fd4m3 + lm3d4;
}
