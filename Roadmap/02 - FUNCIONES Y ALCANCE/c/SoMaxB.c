#include <stdio.h>

void	no_param_no_return(void);
int		no_param_with_return(void);
void	param_no_return(int a);
int		param_and_return(int b);
int		extra(char *c, char *d); // Extra

// In C you cannot create functions within functions.

int	global_var = 5; // Global variable.

int	main(void)
{
		int local_var = 10; // Local variable.

		no_param_no_return();
		printf("This function has no param but has return %d\n", no_param_with_return());
		param_no_return(4);
		printf("Function with param and return: %d\n", param_and_return(5));

		// Extra
		extra("Fizz", "Buzz");
    
		int total = extra("Fizz", "Buzz");
    
		printf("The numbers have been printed %d times.\n", total);

		return 0;
}

void	no_param_no_return(void) {
		printf("This function has no parameter or return.\n");
}

int	no_param_with_return(void) {
		int	local = 3; // Local variable.

		return (local += global_var);
}

void	param_no_return(int a) {
		printf("This function has parameter but no return, the parameter is: %d\n", a);
}

int	param_and_return(int b) {
		int total = b + global_var;

		return (total);
}

// Extra function
int	extra(char *c, char *d) {
		int n = 1;
		int count = 0;

		while (n <= 100)
		{
            if (n % 3 == 0 && n % 5 == 0)
                printf("%s%s\n", c, d);
            else if (n % 3 == 0)
                printf("%s\n", c);
            else if (n % 5 == 0)
                printf("%s\n", d);
            else {
                printf("%d\n", n);
                count ++;
            }
            n++;
		}
		return (count);
}
