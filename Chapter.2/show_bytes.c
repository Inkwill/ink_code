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

