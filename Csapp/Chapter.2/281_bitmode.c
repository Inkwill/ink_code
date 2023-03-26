#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int k = 10;
	int j =5;
	printf("A = 0x%X\n",bitmode_A(k));
	show_bit(bitmode_A(k));

	printf("B = 0x%X\n",bitmode_B(k,j));
	show_bit(bitmode_B(k,j));
	return 0;
}

unsigned bitmode_A(unsigned k){

	return -1<<k;
}

unsigned bitmode_B(unsigned j, unsigned k){

	return ((1<<(k+j+1))-1)<<j;
}
