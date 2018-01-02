#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	float x =  -0.0f;
	float y =  -0.0f;
	printf("float_le(%f,%f) ->%d \n",x,y,float_le(x,y));
	
	float z = pow(2,126);
	printf("f2u(%f) =0x%X\n",z, f2u(z));

	unsigned a = 0x3F800000;
	unsigned b = 0xBF800000;
	unsigned c = 0x40200000;
	printf("u2f(0x%X) =%f\n",a, u2f(a));
	printf("u2f(0x%X) =%f\n",b, u2f(b));
	printf("u2f(0x%X) =%f\n",c, u2f(c));
	printf("%f+%f = 0x%X\n",u2f(a), u2f(b),f2u(u2f(a)+ u2f(b)));
	
	//printf("f2u(%f) =0x%X\n",c, f2u(c));
	return 0;
}

int float_le(float x, float y){

	unsigned ux = f2u(x);
	unsigned uy = f2u(y);

	/* Get the sign bits */
	unsigned sx = ux >>31;
	unsigned sy = uy >>31;

	/* Give an expression using only ux, uy, sx, and sy */
	return (ux == uy) || ((sx^sy)&& sx) || !(sx^sy) && (sx ^ (ux<=uy));
}
