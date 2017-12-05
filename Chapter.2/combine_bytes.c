//2.59

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	unsigned x = 0x89ABCDEF;
	int y = 0x76543210;
	combine_bytes((unsigned)x,(unsigned)y);
	return 0;
}

unsigned combine_bytes(unsigned x, unsigned y){

	unsigned mask_x = (1<<8) -1;
	unsigned mask_y =  ((1 << (sizeof(unsigned)*8 - 8)) - 1)<<8;
	//show_int(x);
	//show_int(mask_x);
	x = x & mask_x;
	//show_int(y);
	//show_int(mask_y);
	y = y & mask_y;

	unsigned result = x | y;
	show_int(result);
	return result;
}
