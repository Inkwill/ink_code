//2.55~2.57

#include "Chapter2.h"

/*int main(int argc, char const *argv[])
{
	char* str = "Hello World!";
	show_bytes(str, sizeof(str));

	
	int a = -1 *pow(2,31) +1;
	printf("Show int %d: " ,a);
	show_int(a);

	float f = 1.0f;
	printf("Show float %f:",f );
	show_float(f);

	double d = 0.1f;
	printf("Show double %f:",d );
	show_double(d);

	int* pval = &a;
	printf("Show pointer %p:",pval );
	show_pointer(pval);

	unsigned x = 0xFFFFFFFF;
	char str[] = "";
	set_bit_array(x,str);
	return 0;
}*/

void show_bytes(byte_pointer start, int len){

	for (int i = 0; i < len; ++i)
	{
		printf("%.2x ",start[i]);
	}
	printf("\n");
}

void show_int(int x){

	show_bytes((byte_pointer)&x, sizeof(int));
}

void show_short(short x){

	show_bytes((byte_pointer)&x, sizeof(short));
}

void show_long(long x){

	show_bytes((byte_pointer)&x, sizeof(long));
}

void show_float(float x){

	show_bytes((byte_pointer)&x, sizeof(float));
}

void show_double(double x){

	show_bytes((byte_pointer) &x, sizeof(double));
}

void show_pointer(void *x){

	show_bytes((byte_pointer) &x, sizeof(void *));
}

void show_bit(unsigned x){

	int size = sizeof(unsigned)<<3;
	int num_1 = 0;
	int num_0 = 0;
	for (int i = size-1; i >=0; --i)
	{
		int bit = (x>>i) & 1;
		printf("%d", bit );
		if(bit)
			num_1 ++;
		else
			num_0 ++;
	}
	printf("\n =%d bit,1=%d, 0=%d\n",size,num_1, num_0);
}

unsigned unsign_multiplication(unsigned x, unsigned y){

	int size = sizeof(unsigned)<<3;
	unsigned result = 0;
	for (int i = 0; i < size; ++i)
	{
		if(y&1)
			result += (x<<i);
		printf("%X-%X,result = %X\n",y,y&1,result);
		y  >>= 1;
	}
	return result;
}

unsigned f2u(float x){

	unsigned result =  *((unsigned*)&x);
	//printf("f2u(%f) = 0x%X\n", x,result);

	return result;
}

float u2f(unsigned x){

	float result = *((float*)&x);
	//printf("u2f(%u) = %f\n", x,result);

	return result;
}

/* If f is denorm, return 0. Otherwise, return f */
float_bits float_denorm_zero(float_bits f){

	/* Decompose bit representation into parts */
	unsigned sign = f>>31;
	unsigned exp = f>>23 & 0xFF;
	unsigned frac = f & 0x7FFFFF;
	if( exp == 0){
		/* Denormalized. Set fraction to 0 */
		frac = 0;
	}
	/* Reassemble bits */
	return (sign<<31) | (exp << 23) | frac;
}
