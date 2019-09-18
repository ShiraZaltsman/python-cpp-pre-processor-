#include <ctime>
#include <iostream>

using namespace std;

void print_current_time() 
{
   time_t curtime;
   time(&curtime);

   cout << "Current time and date: " << ctime(&curtime);
}
