#include "show_bytes.c"

/* 
	Y = B2U[k](y) 
	n = 0.yyyyy...
	n<<k  = y.yyyy...  = Y + n
	n<<k - n = Y  ->  n*(2^k-1) = Y
	n =   /(2^k -1)
*/

int main(int argc, char const *argv[])
{
	int x = 0x3;
	infiniteloop_float(x,4);
	return 0;
}

float infiniteloop_float(int x, int k){

	float result = (float)x/(float)(pow(2,k));
	for (int i = 2; i < (52/k); ++i)
	{
		result  += (float)x/(float)(pow(2,k*i));
		printf("%d,%f\n",x, result);
	}
	
	printf("0x%X,0x%X\n", result);
	return result;
}
