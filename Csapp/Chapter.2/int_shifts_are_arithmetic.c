//2.62
#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	printf("%d\n", int_shifts_are_arithmetic()); 
	printf("%.8X >>(logically) %d   =  %.8X\n",0x80000000,8,srl(0x80000000,8));
	printf("%.8X >>(arithmetically) %d   =  %.8X\n",0x80000000,8,sra(0x80000000,8));
	return 0;
}

int int_shifts_are_arithmetic(){

	unsigned shift_val = (sizeof(unsigned)<<3)-1;
	int n = 1<<shift_val>>shift_val;
	return !(n+1);
}

//2.63

unsigned srl(unsigned x, int k){
	/* Perform shift arithmetically */

	unsigned xsra = (int) x >> k;
	unsigned mask = 1<< ((sizeof(int)<<3)-k) -1;
	return xsra & mask;
}

unsigned sra(int x, int k){
	/* Perform shift logically */

	int xsrl = (unsigned) x >> k;
	unsigned mask = ((1<< (k+1))-1) << ((sizeof(int)<<3)-k);
	return xsrl | mask;
}
