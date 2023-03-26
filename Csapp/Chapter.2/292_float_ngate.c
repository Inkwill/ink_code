#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	for (unsigned i = 0; i < (unsigned)-1; ++i)
	{
		if(float_negate((float_bits)i)^f2u((-u2f(i)))){
			printf("0x%X: 0x%X,%f\n", i,float_negate((float_bits)(i)),u2f(i));
			break;
		}
	}
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
