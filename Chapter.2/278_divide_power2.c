#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	int x = 0x80000000;
	int k = 3;
	printf("0x%X / power(2, %d) = 0x%X\n", x,k,divide_power2(x, k));
	printf("0x%X / power(2, %d) = 0x%X\n", x,k, x/(1<<k));
	return 0;
}

/* Divide by power of 2.
 	Assume 0 <= k < w-1 */

int divide_power2(int x, int k){

	int fix_x = x;
	(x>>31) && (fix_x = x + (1<<k)-1);
	return fix_x>>k;
}
