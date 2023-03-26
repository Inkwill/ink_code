//2.74

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int a = 0;
	int b = 0x80000000;
	printf("tsub_ok(0x%X, 0x%X) ->%d\n",a,b,tsub_ok(a,b) );
	return 0;
}

/* Determine whether arguments can be subtracted without over flow  */
int tsub_ok(int x, int y){
	
	//ok: 1  else  0
	int ok_Tmin = (y & (-y)) && (x>>31);
	//ok: 1 else 0
	int ok_Else = !(y & (-y))  &&  (y ^ (x-y))>>31;
	return ok_Tmin || ok_Else;
}
