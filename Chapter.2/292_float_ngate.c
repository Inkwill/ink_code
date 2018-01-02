#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	float f = 3.1415927f;
	printf("0x%X\n", float_denorm_zero((float_bits)f2u(f)));
	return 0;
}

float_bits float_negate(float_bits f){
	unsigned sign = f>>31;
	unsigned exp = f>>23 & 0xFF;
	if(exp^0xFF)
		return ~sign<<31 | f<<1>>1;
	else
		return f;
}
