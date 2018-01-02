#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int x = 0xFFFFFFFF;
	printf("%d *3 / 4 = %d\n", x,(int)(x*3/4) );
	printf("%d *3 / 4 = %d\n", x,mul3div4(x) );
	return 0;
}


int mul3div4(int x){

	/*int fix_x = x;
	(fix_x>>31) && (fix_x = fix_x + (1<<2) -1);
	int result = x - (fix_x>>2);*/

	int fix_x = (x<<2) -x;
	(fix_x>>31) && (fix_x = fix_x + (1<<2) -1);
	int result = fix_x>>2;

	return result ;
}
