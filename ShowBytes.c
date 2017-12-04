#include "Csapp.h"

int main(){

	char* str = "Hello linux!";
	show_bytes(str, sizeof(str));

	int a = -1 *pow(2,31) +1;
	show_int(a);

	float f = 1.0f;
	show_float(f);

	double d = 0.1f;
	show_double(d);

	int* pval = &a;
	show_pointer(pval);
	return 0;
}

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

void show_float(float x){

	show_bytes((byte_pointer)&x, sizeof(float));
}

void show_double(double x){

	show_bytes((byte_pointer) &x, sizeof(double));
}

void show_pointer(void *x){

	show_bytes((byte_pointer) &x, sizeof(void *));
}