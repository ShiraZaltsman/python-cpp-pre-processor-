#include <iostream>

using namespace std;

#include "funcs.h"
#include "defs.h"

int main()
{
	PROGRAM_START

	int num1 = get_num();
	int num2 = get_num();
	int max = get_max(num1, num2);
	int min = get_min(num1, num2);
   
	cout << "The max is " << max << endl;
	cout << "The min is " << min << endl;

	cout << "The factorial of " << num1 << " + " << num2 << "is" << factorial(get_sum(num1, num2)) << endl;
	print_current_time();
   	
   	PROGRAM_END
   	
   	return 0;
}
