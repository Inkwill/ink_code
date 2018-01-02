/*  Create some arbitrary values */
int x = random();
int y = random();
int z = random();
/* Convert to double */
double dx = (double) x;
double dy = (double) y;
double dz = (double) z;

A.(float)x == (float) dx
/* right : 丢失的精度相同*/

B. dx-dy == (double)(x-y)
/*wrong : y=INT_MIN    x-y = x + y   dx-dy != dx + dy*/

C. (dx+dy)+dz == dx + (dy+dz)
/*right */

D. (dx*dy)*dz == dx*(dy*dz)
/*wring: dx*dy溢出, dy*dz变小*/

E. dx/dy == dz/dz
/*right*/
