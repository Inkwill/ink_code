//2.68
#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int n = 17;
	//当移位位数超过该数值类型的最大位数时，编译器会用移位位数去模该类型位数，然后按照余数进行移位 n=n mod sizeof(int)
	printf("%X\n", 1<<n );
	//当移位位数小于sizeof(type)时，直接舍去
	printf("%X\n", 1<<(n-1)<<1);

	printf("lower_one_mask(%d) --> 0x%X\n", n, lower_one_mask(n));
	return 0;
}

int lower_one_mask(int n){

	/*
		Mask with least signficant n bits set to 1
		Examples: n = 6 --> 0x3F, n=17 --> 0x1FFFF
		Assume 1 <=n <= w
	*/
	unsigned x = (1<<(n-1)<<1) -1;
	return x;
}
