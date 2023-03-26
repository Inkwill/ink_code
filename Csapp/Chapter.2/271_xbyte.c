//2.71

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	packed_t word = 0xE2345678;
	int bytenum = 3;
	printf("xybe(0x%X, %d) -> 0x%X\n",word, bytenum, xbyte(word, bytenum)); 
	return 0;
}

int xbyte(packed_t word, int bytenum){

	/* Extract byte from word. Return as signed integer */
	/* Failed attempt:  equal zero extension*/
	//return (word >> (bytenum << 3)) & 0xFF;
	unsigned shift_val = (bytenum -3)<<3;
	int result = (int)(word<<shift_val)>>24;
	return result;
}
