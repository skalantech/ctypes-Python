#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

char* display(char* str, int age)
{
    printf("My name is %s and my age is %d\n", str, age);
    return "Completed";
}

// Compile into a .so file
// gcc -fPIC -shared -o clibrary.so clibrary.c

int add(int num1, int num2)
{
    return num1 + num2;
}

void show(char* str)
{
    printf("%s", str);
}

char* alloc_memory()
{
    char* str = strdup("Hello again world or pointers");
//    char* str = (char*)malloc(sizeof(char) * 50);
//    str = "Hello again world or pointers\n";
    printf("Memory allocated...\n");
    return str;
}

void free_memory(char* str)
{
    printf("Memory string char* freed!...\n");
    free(str);
}

int* work(int n)
{
    int* data = (int*)malloc(sizeof(int) * n);
    if (data == NULL) {
        perror("Failed to allocate memory");
        exit(1);
    }

    for (int i = 0; i < n; ++i)
    {
        data[i] = (int)i * i;
    }
    return data;
}

void free_array(int* arr)
{
    printf("Memory array freed!...\n");
    free(arr);
}

int sumArray(int* arr, int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}

int* incArray(int* arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        arr[i] += 5;
    }
    return arr;
}

struct Point
{
    int x;
    int y;
};

void printPoint(struct Point p)
{
    printf("x: %d y: %d\n", p.x, p.y);
}

struct Point* getPoint()
{
    struct Point* p;
    p->x = 10;
    p->y = 20;
    return p;
}

struct Student
{
    char* name;
};

void printStudentDetails(struct Student s)
{
    printf("%s\n", s.name);
}

struct Student* getStudent()
{
    struct Student* s = malloc(sizeof(struct Student));
    s->name = strdup("Carlos Escalante");
    return s;
}

void free_struct(struct Student* s) {
    printf("Memory struct freed!...\n");
    free(s->name);
    free(s);
}

struct PointArray
{
    struct Point points[3];
};

void printPointArray(struct PointArray pa)
{
    for (int i = 0; i < 3; i++)
    {
        printf("%d %d\n", pa.points[i].x, pa.points[i].y);
    }
}

int main()
{
    int n = 100000000;
    clock_t t;
    t = clock();
    int* result = work(n);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("\nTime taken = %f", time_taken);
//    for (int i = 0; i < n; ++i)
//        printf("%d ", result[i]);
    // Now you can use the 'result' pointer to access the data array.

    // Don't forget to free the dynamically allocated memory when you're done with it.
    free(result);
    return 0;
}