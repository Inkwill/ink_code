//2.58

#include "Chapter2.h"

int main(int argc, char const *argv[])
{
	printf("%d\n", is_little_endian());
	return 0;
}

int is_little_endian(){

	int n = 1;
	char* start = (char*)&n;
	return start[0] >0; 
}
