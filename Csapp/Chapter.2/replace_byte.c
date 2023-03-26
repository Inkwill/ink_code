//2.60

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	unsigned a = 0x12345678;
	int index = 0;
	unsigned b = 0xAB;
	printf("replace_byte(%X  ,%d,%X)--> %X \n", a,index,b,replace_byte(a,index,b));

	//2.61
	//A.  return 1  if  the value of every bit equal 1  else 0
	printf("%X -->%d\n", 0xffafffff, !(0xffafffff + 1));
	//B.  return 1  if  the value of every bit equal 0  else 0
	printf("%X -->%d\n", 0x00010000, !(0x00010000));
	//C. return 1  if  the value of lowest bit equal 1  else 0
	int shift_val = (sizeof(int)-1)<<3;
	printf("%X -->%d\n", 0x010000ff, !((0x010000ff<<shift_val>>shift_val) +1));
	//D. return 1  if  the value of highest bit equal 0  else 0
	printf("%X -->%d\n", 0x00ffff00, !(0x00ffff00>>shift_val<<shift_val));
	return 0;
}


unsigned replace_byte(unsigned x, int i, unsigned char b){

	byte_pointer start = (byte_pointer) &x;
	unsigned mask = ((1<<8) -1)<< (i*8);
	unsigned result = x&(~mask)| (b<<(i*8));
	return result;
}
