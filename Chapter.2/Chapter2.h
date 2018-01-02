#include <stdio.h>
#include <math.h>
#include <string.h>

typedef unsigned char* byte_pointer;
void show_bytes(byte_pointer start, int len);
void show_int(int x);
void show_short(short x);
void show_long(long x);
void show_float(float x);
void show_pointer(void *x);
void show_double(double x);

int is_little_endian();

unsigned combine_bytes(unsigned x, unsigned y);

unsigned replace_byte(unsigned x, int i, unsigned char b);

int int_shifts_are_arithmetic();

unsigned srl(unsigned x, int k);
unsigned sra(int x, int k);
int any_odd_one(unsigned x);
int odd_ones(unsigned x);
int bad_int_size_is_32();
int lower_one_mask(int n);
unsigned rotate_left(unsigned x, int n);
int fits_bits(int x, int n);
unsigned leftmost_one(unsigned x);

typedef unsigned packed_t;
int xbyte(packed_t word, int bytenum);
void copy_int(int val, void *buf, int maxbytes);

int saturating_add(int x, int y);

int tsub_ok(int x, int y);

int signed_high_prod(int x, int y);
unsigned unsigned_high_prod(unsigned x, unsigned y);
void show_bit(unsigned x);
unsigned unsign_multiplication(unsigned x, unsigned y);

void * another_calloc(size_t nmemb, size_t size);
/*void * malloc(size_t size);
void * memset(void *s, int c, size_t n);*/

int divide_power2(int x, int k);
int mul3div4(int x);
int threefourths(int x);
unsigned bitmode_A(unsigned k);
unsigned bitmode_B(unsigned j, unsigned k);

float infiniteloop_float(int x, int k);
int float_le(float x, float y);
unsigned f2u(float x);
float u2f(unsigned x);

float fpwr2(int x);
typedef unsigned float_bits;
float_bits float_denorm_zero(float_bits f);

float_bits float_negate(float_bits f);
