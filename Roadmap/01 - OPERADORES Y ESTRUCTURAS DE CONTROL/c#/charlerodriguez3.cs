/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */
 
 
int num1 = 5;
 int num2 = 3;
 int num3;

 // unary operators. Only one variable is in use
 num3 = -num1; //NEGATIVE OPERATOR. Implicity if it's a number is that number times minus one
 Console.WriteLine("num3 is {0}", num3);

 bool isSunny = true;
 Console.WriteLine("is it sunny? {0}", !isSunny);//NEGATION OPERATOR IS USED WITH BOOL VARIABLES
 //SO THE NEGATION OF TRUE WILL BE FALSE AND VICEVERSA

 // increment operators
 int num = 0;
 num++;
 Console.WriteLine("num is {0}", num);
 Console.WriteLine("num is {0}", num++);// increment operator, first assign or print of the variable and then the decrement operation will take action
 // pre increment
 Console.WriteLine("num is {0}", ++num);//before printing the value the increment will take action

 // decrement opertor
 num--;
 Console.WriteLine("num is {0}", num);
 Console.WriteLine("num is {0}", num--);// same as increment in this line
 // pre decrement
 Console.WriteLine("num is {0}", --num); //same as increment

 int result;

 result = num1 + num2; //SUM
 Console.WriteLine("result of num1 + num2 is {0}", result);
 result = num1 - num2;//SUSTRACTION
 Console.WriteLine("result of num1 - num2 is {0}", result);
 result = num1 / num2; //DIVIDE
 Console.WriteLine("result of num1 / num2 is {0}", result);
 result = num1 * num2; //MULTIPLY
 Console.WriteLine("result of num1 * num2 is {0}", result);
 result = num1 % num2; // MODULE
 Console.WriteLine("result of num1 % num2 is {0}", result);

 // relational and type operators
 bool isLower;
 isLower = num1 < num2;// LESS THAN 
 Console.WriteLine("result of num1 < num2 is {0}", isLower);
//OTHER RELATIONAL OPERATORS
/*
> GREATER THAN
<= LESS OR EQUAL THAN
>= GREATER OR EQUAL THAN

*/


 // equality operator
 bool isEqual;
 isEqual = num1 == num2;
 Console.WriteLine("result of num1 == num2 is {0}", isEqual);

 isEqual = num1 != num2; //DIFFERENT OR NOT EQUAL OPERATOR
 Console.WriteLine("result of num1 != num2 is {0}", isEqual);

 // conditional operators
 bool isLowerAndSunny;
 // condition1 AND condition2
 isLowerAndSunny = isLower && isSunny; // AND OPERATOR: BOTH SENTENCES HAVE TO BE TRUE
 Console.WriteLine("result of isLower && isSunny is {0}", isLowerAndSunny);

 // condition1 OR condition2
 isLowerAndSunny = isLower || isSunny; // OR OPERATOR: EITHER ONE OR THE OTHER SENTENCES HAS TO BE TRUE SO THAT THE EXPRESSION IT IS TRUE
 Console.WriteLine("result of isLower || isSunny is {0}", isLowerAndSunny);
 Console.ReadKey();

 //ternary operator
// Assigns the variable of side left or right, having as a reference the ":" symbol. If the condition between parenthesis is true, the left value will be assigned to the variable
//if not the right value will be the selected.
num3 = (num1 > num3) ? num1 : num2;

//CONDITIONALS

isLowerAndSunny = false;
num1 = 5;
num2 = 3;

//conditional if else


if(isLowerAndSunny)
{
    num1 = num2;
}
else
{
    num2 = num1;
}
Console.WriteLine("Values num2: {0} num1: {1}",num2,num1);

//loop do while
// do something until the condition express Truth
// First you do something before checking the condition if it is true or false
do
{
    num2++;
} while (num2 >= num1);
Console.WriteLine(num2);

//loop while
//first you check the condition and depends on its result, it will execute the code between the curly brackets
while (num1 > 50)
{
    num1 += 5;
}
Console.WriteLine(num1);
//loop for
//You decide when to start (paramter 1), when to stop the loop (parameter 2) and how much you will go forward between the beginning
// and the finish of the loop
for (int i = 0; i < num1; i++)
{
    Console.WriteLine("Number: {0}", i);
}

//foreach loop
// Another way to go over a variable.
//the expression variable1 IN variable2 decides to divide variable 2 into little pieces and assign them into
//variable 1 which are going to change their value throughout the loop
string word = "Greetings";

foreach (char c in word)
{
    Console.WriteLine(c);
}


int num3 = 0;

//switch
//given a value, the switch will validate through all the cases, and the selected case will execute its code
//until the break statement
//If none of the cases satisfy the condition, the default case will take action

switch (num3)
{
    case 0:
        Console.WriteLine("The value of num3 is 0");
        break;
    case 1:
        Console.WriteLine("The value of num3 is 0");
        break;
    default:
        Console.WriteLine("Default option. It works as and else condition");
        break;
}


          
//Exception
//When a error ocurrs and in pro of the direction of not stopping the program.
//We will throw and exception, which it could be created by us or defined by the programming language
try
{
    Console.WriteLine(num2 / num3);
}catch (DivideByZeroException ex) {
    throw new Exception ($"You can't divide by zero {ex.Message}");
}

 /*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seg

 */
 for(int i = 10; i < 56; i++)
 {
     if(i % 2 == 0 && i != 16 && i % 3 != 0)
     Console.WriteLine(i);
 }

