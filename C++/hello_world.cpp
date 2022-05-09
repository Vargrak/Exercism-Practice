#include "hello_world.h"

using namespace std;

namespace hello_world
{
    int main()
    {
        hello_world::hello();
        return 0;
    }
    
    string hello()
    {
        return "Hello, World!";
    }
}
