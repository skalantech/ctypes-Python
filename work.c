#include <stdio.h>
#include <stdlib.h>

long double* data;  // Declare a pointer to long double

long double* work(int n)
{
    // Allocate memory for the data array
    data = (long double*)malloc(sizeof(long double) * n);
    if (data == NULL) {
        perror("Failed to allocate memory");
        exit(1);
    }

    for (int i = 0; i < n; ++i)
    {
        data[i] = (long double)(i * i);
    }
    return data;
}

int main()
{
    int n = 100000000;
    long double* result = work(n);

    // Now you can use the 'result' pointer to access the data array.

    // Don't forget to free the dynamically allocated memory when you're done with it.
    free(result);
    return 0;
}