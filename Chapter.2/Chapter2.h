#include <stdio.h>
#include <math.h>

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
