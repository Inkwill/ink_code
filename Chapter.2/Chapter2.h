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
