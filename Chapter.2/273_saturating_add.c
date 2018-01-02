//2.73

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int a = 0xFFFFFFFF;
	int b = 0x80000000;
	printf("saturating_add(0x%X, 0x%X) -> 0x%X\n",a,b,saturating_add(a,b) );
	return 0;
}

/* Addition that saturates to TMin or TMax */
int saturating_add(int x, int y){

	int sum = x + y;
	//pos: Tmax  else:Tmin
	int  T = (y>>31) ^ 0x7FFFFFFF;
	//over: -1    else  0
	int over =(((x + y)^x) & ((x+y)^y))>>31;
	over && (sum = T);
	return sum;
}
