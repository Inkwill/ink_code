//2.75

#include "show_bytes.c"
#include <inttypes.h>

int main(int argc, char const *argv[])
{
	unsigned a = 0xFFFFFFFF;
	unsigned b = 0xFFFFFFFF;
	//printf("unsigned_high_prod(0x%X, 0x%X) ->0x%X\n",a,b,unsigned_high_prod(a,b) );
	printf("unsign_multiplication(0x%X, 0x%X) ->0x%X\n",a,b,unsign_multiplication(a,b) );
	printf("unsign_multiplication(0x%X, 0x%X) ->0x%X\n",a,b,a*b );
	printf("unsigned_high_prod(0x%X, 0x%X) ->0x%X\n",a,b,unsigned_high_prod(a,b) );
	printf("signed_high_prod(0x%X, 0x%X) ->0x%X\n",a,b,signed_high_prod(a,b) );
	return 0;
}

unsigned unsigned_high_prod(unsigned x, unsigned y){
	
	int highbit_x = x>>31;
	int highbit_y = y>>31;
	unsigned reslut = signed_high_prod(x, y) + highbit_x *y + highbit_y *x;
	//reslut  += ((highbit_x*highbit_y)<<31<<1 ); 
	return reslut;
}

int signed_high_prod(int x, int y){
	
	int64_t mul = (int64_t) (x*y);
	return  mul>>32;
}
