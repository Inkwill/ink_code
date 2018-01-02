#include "show_bytes.c"

int	main(int argc, char const *argv[])
{
	int x = 0x12345678;
	/* K = 17 */
	printf("%d*17 = 0x%X(0x%X)\n",x, x + (x<<4), x*17);
	/* K= -7 */
	printf("%d*(-7) = 0x%X(0x%X)\n",x, (-x<<3)+x, x*(-7));
	/*  K＝60*/
	printf("%d*(60) = 0x%X(0x%X)\n",x, (x<<6)-(x<<2), x*(60));
	/*  K＝-112*/
	printf("%d*(-112) = 0x%X(0x%X)\n",x, (-x<<7)+(x<<4), x*(-112));
	return 0;
}

