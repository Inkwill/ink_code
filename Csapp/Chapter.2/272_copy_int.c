//2.72

#include "show_bytes.c"

int main(int argc, char const *argv[])
{
	int n = 0x12345678;
	int maxbytes = 2;
	void* buf = (void*) &maxbytes;
	copy_int(n, buf, maxbytes);
	return 0;
}

void copy_int(int val, void *buf, int maxbytes){

	/* Copy integer into buffer if space is available */
	/*sizeof(val) return a size_t(unsigned) type
	if (maxbytes - sizeof(val) >= 0)
	*/
	if(maxbytes >= sizeof(val))
		memcpy(buf, (void*) &val, sizeof(val));
		printf("Copying...\n");
}
