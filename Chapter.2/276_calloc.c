#include "show_bytes.c"
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	void* p = another_calloc(SIZE_MAX,2);
	printf("%p\n",p );
	//assert(p != NULL);
	//free(p);

	/*p = another_calloc(SIZE_MAX, 2);
	assert(p == NULL);
	free(p);*/

	return 0;
}

void * another_calloc(size_t nmemb, size_t size){

	size_t callsize = nmemb * size;
	void *result = NULL;
	if(!nmemb && !size  && callsize/nmemb == size){
		result = malloc(callsize);
	}
	if(result == NULL)
		return NULL;
	else
		return memset(result, 0, callsize);;
}

/*void * malloc(size_t size){


}

void * memset(void *s, int c, size_t n){

	
}*/
