#include <iostream>
//#include <string>
// strings don't work

//g++ -fPIC -shared -o cpplibrary.so cpplibrary.cpp

void func()
{
    std::cout << "function without parameters" << '\n';
}

void func(int a)
{
    std::cout << "Function with an int parameter: " << a << '\n';
}

void func(char* a)
{
    std::cout << "Function with a string parameter: " << a << '\n';
}

extern "C"
{
    void func_v()
    {
        func();
    }

    void func_i(int a)
    {
        func(a);
    }

    void func_s(char* a)
    {
        func(a);
    }
}