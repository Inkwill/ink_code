#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	// A. (x<y) == (-x>-y)
	int x = 0x80000000;
	int y = 0xFFFFFFFF;
	char expression[100] = "A. (x<y) == (-x>-y)";
	printf("%s->%d (x=0x%X, y=0x%X)\n",expression,(x<y)==(-x>-y),x,y);
	//B. ((x+y) << 4) + y-x == 17*y + 15*x
	x = 0x80000000;
	y = 0x00000000;
	strcpy(expression,"B. ((x+y) << 4) + y-x == 17*y + 15*x");
	printf("%s->%d (x=0x%X, y=0x%X)\n",expression, ((x+y) << 4) + y-x == 17*y + 15*x,x,y);
	//C. ~x+ (~y) + 1 == ~(x+y)
	//~x +1 = -x, ~y+1 = -y, ~(x+y)+1 = -x-y
	x = 0x80000000;
	y = 0x80000000;
	strcpy(expression,"C. ~x+ (~y) + 1 == ~(x+y)");
	printf("%s->%d (x=0x%X, y=0x%X)\n",expression, ~x+ (~y) + 1 == ~(x+y),x,y);
	//D. (ux - uy) == -(unsigned)(y-x)
	//(unsigned) don't change bit value
	x = 0x7FFFFFFF;
	y = 0x80000000;
	unsigned ux = (unsigned)x;
	unsigned uy = (unsigned)y;
	strcpy(expression,"D. (ux - uy) == -(unsigned)(y-x)");
	printf("%s->%d (x=0x%X, y=0x%X)\n",expression, (ux - uy) == -(unsigned)(y-x),x,y);
	//E. ((x>>2)<<2) <= x
	//
	x = 0x80000000;
	y = 0x80000000;
	strcpy(expression,"E. ((x>>2)<<2) <= x");
	printf("%s->%d (x=0x%X, y=0x%X)\n",expression, ((x>>2)<<2) <= x,x,y);
	return 0;
}
