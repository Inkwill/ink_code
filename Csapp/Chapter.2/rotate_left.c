//2.69
#include "show_bytes.c"

int main(int argc, char const *argv[])
{	
	int n = 3;
	unsigned x = 0x12345678;
	printf("rotate_left(0x%X, %d) -> 0x%X\n", x, n ,rotate_left(x, n));
	return 0;
}

unsigned rotate_left(unsigned x, int n){
/*
	Do ratating left shift. Assume 0 <= n < w
	Examples when x = 0x12345678 and w =32:
		n=4 -> 0x23456781, n=20 -> 0x67812345
*/
	int	w = 32;
	unsigned y = x>>(w-n -1) >> 1;
	return (x<<n) | y;
}

