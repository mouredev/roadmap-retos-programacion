#include <iostream>
#include <string>
/*
 * FUNCTIONS
 * */

//WITH OUT RETURN - void functions
// Only execute the operations but not return a value
void greeting(){
	std::cout << "Hello" << std::endl;
}
// void function with params

void showMsg(std::string name){
	std::cout << "Hello "  << name << std::endl;
}
int global_res = 0; // global variable.
// WITH RETURN - no void functions

int sum(int n1, int n2){
	int res = n1 + n2;
	std::cout << n1 << " + "<< n2 << " = "<< res << std::endl;
	std::cout << global_res << " global var " << std::endl;
	return res;
}

// Function Overloading: Enable that we have a lot variables with the same name, the diference is the cuantity of params or the type of the same. You can know what function you are using based on the args that you provide.

int sum(double n1, double n2){
	 double res = n1 + n2; // local variable
        std::cout << n1 << " + "<< n2 << " = "<< res << std::endl;
        return res;
}

// FUNCTIONS INSIDE ANOTHER?

// ❌ This is an error, we can't define a function inside in another.
/*
void greetingOutside(){
void greetingInside(){
	std::cout << "Hello, I´m a function inside a function " << std::endl;
}
}
*/
void greetingInside(){
	std::cout << "Hello, I´m a function inside a function " << std::endl;
}

// Here we are using a function inside another.
void greetingOutside(){
	greetingInside();
}


/*
 * EXTRA DIFFICULTY
 * */
//2 params type string
// return int
// f => [1-100]
// print:
// residue betwen 3 = 0 => 1param
// residue betwen 5 = 0 => 2param
// residue betwen 3 = 0 and 5 = 0 => 1param2param (concatenated)
// RETURN: int isn't multiple of 3, 5 and both, number of times.

int exercise(std::string text1, std::string text2){
	int acc = 0;
	for(int i = 1; i <=100; i++){
		std::cout << i <<std::endl;
if(i%3==0 && i%5==0){
			std::cout << text1 << text2 << std::endl;

		}
else if(i%3==0){
			std::cout << text1 << std::endl;
		}
		else if(i%5==0){
			std::cout << text2 << std::endl;
		}
		
		else {
			acc +=1;
		}
	}
	return acc;
}



int main(){
greeting();
showMsg("David");
double res = sum(2.8293,3.4395);
std::cout <<"Out - res SUM DOUBLE: "<< sum(2.8293, 3.4395);
std::cout <<"Out - res SUM INT: "<< sum(1,3);


greetingOutside();
int n = exercise("david", "arroz");
std::cout<<n<<std::endl;
return 0; 
}
