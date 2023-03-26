#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int x = -126;
	float f = fpwr2(x);
	printf("%f\n", f );
	show_float(f);
	return 0;
}

float fpwr2(int x){

	/* Result exponent and fraction */
	unsigned exp, frac;
	unsigned u;

	if(x < -149){
		/* Too small. Return 0.0 */
		exp = 0x0;
		frac = 0x0;
	}
	else if (x < -126){
		/* Denormalized result */
		exp = 0x0;
		frac = 1<<(149+x);
	}
	else if (x < 128){
		/* Normalized result.*/
		exp = x+127;
		frac = 0x0;
	}
	else {
		/* Too big. Return +oo */
		exp = (1<<9)-1;
		frac = 0x0;
	}

	/*  Pack exp and frac into 32 bits*/
	u = exp <<23 | frac;
	/* Return as float */
	return u2f(u);
}
