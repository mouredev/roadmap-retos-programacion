#include <iostream>
#include <string>
/*
 * TYPES OF OPERATORS 
 * */

int main(){

int n1=2, n2 = 2;
int res = n1 + n2;

// Arithmetics
std::cout<< "SUM: " << n1+n2 <<std::endl;
std::cout<< "SUBSTACT: " << n1-n2 <<std::endl;
std::cout<< "MULTIPLICATION: " << n1*n2 <<std::endl;
std::cout<< "DIVISION: " << n1/n2 <<std::endl;
std::cout<< "MODULE: " << n1%n2 <<std::endl;

// Assignment:


std::cout << "n1: " << n1 << "n2: " << n2 << std::endl;
n1 += 1; // sum
std::cout << "n1 +=1: " << n1 << std::endl;
n2 -= 1; // substract
std::cout << "n2 -=1: " << n2 << std::endl;
n1 *= 2; //multiplication
std::cout << "n1 *=2 : " << n1 << std::endl;
n1 /= 3; //multiplication
std::cout << "n1 /=3: " << n1 << std::endl;
n1 %= 3; //multiplication
std::cout << "n1%3: " << n1<< std::endl;

// Comparison - Is a boolean value (true or false)


// std::cout << n1==n2 << std::endl; in this case << is left associative and has higher precedence than ==, 0 is equal false and 1 is equal true.
std::cout << (n1==n2) << std::endl;
std::cout << (n1!=n2) << std::endl;
std::cout << (n1>n2) << std::endl;
std::cout << (n1<n2) << std::endl;
std::cout << (n1>=n2) << std::endl;
std::cout << (n1<=n2) << std::endl;

// Logics
bool boolean = true;

if(boolean == true && n1 == 0){
	std::cout << "AND" << std::endl;
}else{

	std::cout << "is not a statment AND" << std::endl;
}


if(boolean == true || n1 == 0){
	std::cout << "OR" << std::endl;
}else{

	std::cout << "is not a statment OR" << std::endl;
}

if(!boolean){
	std::cout <<"NOT - boolean is false"<< std::endl;
}else{

	std::cout << "NOT - boolean is true" << std::endl;
}
// Increase - Decreace

std::cout << "n1: " << n1 << "n2: " << n2 << std::endl;
n1++;
std::cout << n1<< std::endl;
n1--;
std::cout << n1<< std::endl;

//Bitwise bit to bit
/*
 *These operators works with individual bits that make up the integers numbers. (0-1) 
 * */
unsigned int n =  2; // (0010)
unsigned int t = 5; // (0101)
std::cout << "n & t |" << (n & t) << "|  0010 & 0101 = 0000" << std::endl; //AND STATMENT

std::cout << "n | t |" << (n | t) << "|  0010 & 0101 = 0111 (7)" << std::endl; // OR STATMENT

unsigned int y = 7; // 0111
std::cout << "n ^ t |" << (n ^ y) << "|  0010 ^ 0111 = 0101 (5)" << std::endl; // XOR STATMENT
std::cout << "~(n ^ t) |" << (~(n ^ y)) << "|  0010 ^ 0111 = 0101 => ~0101 => 1010 (10)" << std::endl; // NOT STATMENT

std::cout << "|"<< (n<<2) << "|  DISPLACEMENT 2 BITS: n=2 => n=0010 => 1000 (8)"<< std::endl; // LEFT DISPLACEMENT											
std::cout << "|"<< (y>>3) << "|  DISPLACEMENT 3 BITS: y=7 => y=0111 => 0000 (0)"<< std::endl; // RIGHT DISPLACEMENT


/* SIZEOF : 
 * Is an unitary operator that return the size in bytes of a variable or type of data**/
    int miNumero;
    double miDecimal;

    std::cout << "Tamano de int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "Tamano de miNumero: " << sizeof(miNumero) << " bytes" << std::endl;
    std::cout << "Tamano de double: " << sizeof(double) << " bytes" << std::endl;
    std::cout << "Tamano de miDecimal: " << sizeof(miDecimal) << " bytes" << std::endl;

    /*
     * Ternary operator:
     * It is an abbreviated form of the if statement
     * */

    std::string msg;
    int age = 8;

    msg = (age >= 18)? "Adult": "Underage";
    std::cout << " You´re " << msg << std::endl;


    /*
     * CONTROL STRUCTURES
     * */

// Conditionals
// if statment
bool vehicle=true;
    if(vehicle){
	    std::cout <<"It starts"<<std::endl;
}

if(n%2==0){

	    std::cout <<"The number is even"<<std::endl;
}else{

	    std::cout <<"The number is odd"<<std::endl;
}
std::string trafficLight;

trafficLight = "Yellow";

if(trafficLight == "Green"){
	std::cout << "You can go"<<std::endl;
}else if(trafficLight == "Yellow"){
	std::cout << "You coud wait"<<std::endl;

}else if(trafficLight =="Red"){
	std::cout << "Stop"<<std::endl;
}else{
	std::cout << "Something is wrong"<<std::endl;
}

// switch statment:
int number_s = 3;
switch(number_s){
	case 1:
	std::cout << "SWITCH: You can go"<<std::endl;
	break;
	case 2:
	std::cout << "SWITCH: You could wait"<<std::endl;
	break;
	case 3:
	std::cout << "SWITCH: Stop"<<std::endl;
	break;
	default:
	std::cout << "Something is wrong"<<std::endl;
}

// REPETITION STRUCTURES (BUCLES):
int arr[10][2];
// For statment
int bn=1;
for (int i = 0 ; i<10 && i>=0;i++){
	for (int j=0; j<2 && j>=0;j++){
	arr[i][j]=bn++;
			
	std::cout <<"| pos: x:" << i << "y:" << j <<"|  value: "<< arr[i][j] << std::endl;

	}
}
std::cout << arr << std::endl;
//while statment
std::cout << "WHILE" << std::endl;
bool sleap = true;
int time = 0;
while(sleap){
	std::cout <<"zzz"<<std::endl;
if(time == 7){
sleap = false;
}
time++;
}
std::cout << "Already up" << std::endl;

std::cout << "DO WHILE" << std::endl;
bool program = true;
do{
	std::cout<< "Continue learning" <<std::endl;
	break;
}while(program);
std::string days[7] = {"Mon", "Tue", "Wed", "Thu","Fri", "Sat", "Sun"};

for (int i = 0; i<7;i++){
if(days[i] == "Sat" || days[i] == "Sun"){
	// will not run this iterations
continue;
}
	std::cout <<"Today we work: "<< days[i] << std::endl;
}

/*
 ** Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 * */
// A number is even when the remainded in the division is 0
// A number is multiple of 3 when this number divided by 3 the remainded is 0
// no include the integer 16


	std::cout << "EXERCISE" << std::endl;
for (int i = 10; i<56; i++){

	if((i%2==0)&&(i%3==0)&&(i!=16)){
	std::cout << i << std::endl;
}
}
return 0;

}
