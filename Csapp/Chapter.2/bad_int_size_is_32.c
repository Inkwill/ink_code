//2.67

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	bad_int_size_is_32() && printf("this machine is 32 bit.\n");
	return 0;
}

int bad_int_size_is_32(){

	int set_msb = 1 <<31;
	/*
		can't shift a value to its max bit
		int beyond_msb = 1 << 32;
	*/
	int beyond_msb = set_msb <<1;

	/*
		set_msb is nonzero when word size >=32
		beyond_msb is zero when word size <=32
	*/
	return set_msb && !beyond_msb;
}
