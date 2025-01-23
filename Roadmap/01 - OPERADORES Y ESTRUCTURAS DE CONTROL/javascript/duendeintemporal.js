/* { RETOS DE PROGRAMACIÓN }  #1 OPERADORES Y ESTRUCTURAS DE CONTROL */
//Note: I use Matt Frisbie book "Professional JavaScript for Web Developers" as a reference to give accurate additional information about the use of some operantors
//I also serch some tips in JavaScript Notes for Professionals from the beautiful people of StackOverflow. You can get it for free in GoalKicker.com

//short for console.log
let log = console.log.bind(console);

/*  OPERATORS  */
//Unary Operators 
        
        //Unary Plus and Minus
/*  When the unary plus is applied to a nonnumeric value, it performs the same conversion as the
Number() casting function: the Boolean values of false and true are converted to 0 and 1, string
values are parsed according to a set of specific rules, and objects have their valueOf() and/or
toString() method called to get a value to convert. */

    let str1 = "03";
    str1 = +str1;
    log(str1) // value becomes numeric 3

    let str2 = "1.4";
    log(str1 + +str2)// 4.4

    str2 = +str2; 
    log(str2) // value becomes numeric 1.4

    let str3 = "zaz";
    str3 = +str3; 
    log(str3) // value becomes NaN

    let bool = true;
    bool = +bool; 
    log(bool) // value becomes numeric 1

    let f_num = 2.8;
    f_num = +f_num; 
    log(f_num) // no change, still 2.8

    let obj = {
        valueOf() {
            return -5;
        }
    };
    obj = +obj; 
    log(obj) // value becomes numeric -5

/* The unary minus operator’s primary use is to negate a numeric value, such as converting 1 into –1. The simple case is illustrated here: */

    let g_actions=50;
    g_actions= -g_actions;
    log(g_actions) // value becomes -50

/* When used on a numeric value, the unary minus simply negates the value. When used on non numeric values, unary minus applies all of the same rules as unary plus and then negates the result */

    str1 = -str1;
    log(str1) // value becomes numeric -3

    str2 = -str2; 
    log(str2) // value becomes numeric -1.4

    str3 = -str3; 
    log(str3) // value becomes NaN

    bool = -bool; 
    log(bool) // value becomes numeric -1

    f_num = -f_num; 
    log(f_num) // no change, still -2.8

    obj = -obj; 
    log(obj) // value becomes numeric 5


     //Increment/Decrement ++ --
     let num1 = 10, num2 = 5, num3, num4;
     num3 = num1++;
     log(num3); // 10
     log(num1); // 11
     num3 = ++num1;
     log(num3); // 12
     log(num1); // 12
     num4 = num2--;
     log(num4); // 5
     log(num2); // 4
     num4 = --num2;
     log(num4); // 3
     log(num2); // 3
     num4++;
     log(num4); // 4


    //Bitwise Operators
/* The next set of operators works with numbers at their very base level, with the bits that represent them in memory. 
When you apply bitwise operators to numbers in ECMAScript, a conversion takes place behind the scenes: the 64-bit number is converted into a 32-bit number, the operation is performed, and then the 32-bit result is stored back into a 64-bit number. */

//Bitwise NOT  ~
//The bitwise NOT is represented by a tilde (~) and simply returns the one’s complement of the number.
let n1 = 25; //  binary 00000000000000000000000000011001
let n2 = ~n1; // binary 11111111111111111111111111100110
log(n2); // -26   it negates the number and subtracts 1
//same to say
n2 = -n1 -1;
//but bitwise operation performs faster cause it works at the lowest lavel of numeric representation.

//Bitwise AND &
//A bitwise AND operation returns 1 if both bits are 1. It returns 0 if any bits are 0.

let n3 = 25 & 3;
log(n3) /* logs: 1 cause the comparation of both binary codes is : 
    25 = 0000 0000 0000 0000 0000 0000 0001 1001
     3 = 0000 0000 0000 0000 0000 0000 0000 0011
    ---------------------------------------------
   AND = 0000 0000 0000 0000 0000 0000 0000 0001   */

//Bitwise OR |
//A bitwise OR operation returns 1 if at least one bit is 1. It returns 0 only if both bits are 0.

n3 = 25 | 3; 
log(n3) /* Logs: 27 cause the comparation of both binary codes is :
    25 = 0000 0000 0000 0000 0000 0000 0001 1001
     3 = 0000 0000 0000 0000 0000 0000 0000 0011
    ---------------------------------------------
    OR = 0000 0000 0000 0000 0000 0000 0001 1011   */

//Bitwise XOR
//Bitwise XOR is different from bitwise OR in that it returns 1 only when exactly one bit has a value of 1 (if both bits contain 1, it returns 0).

n3 = 25 ^ 3;
log(n3); /* Logs: 26 cause the comparation of both binary codes is :
    25 = 0000 0000 0000 0000 0000 0000 0001 1001
     3 = 0000 0000 0000 0000 0000 0000 0000 0011
    ---------------------------------------------
   XOR = 0000 0000 0000 0000 0000 0000 0001 1010   */

//Left Shift
//The left shift is represented by two less-than signs (<<) and shifts all bits in a number to the left by the number of positions given

let number = 2; // 10 in binary code
let new_number = number << 6; // 10000000 in binary code wich is decimal 128
log(new_number)// 128

/*  |1|         |0|       |0|       |0|       |0|        |0|       |0|      |0|
(2^7x1)  +  (2^6x0) + (2^5x0) + (2^4x0) + (2^3x0) + (2^2x0) + (2^1x0) + (2^0x0) //here ^ is a powder
 128     +     0    +    0    +    0    +   0     +    0    +    0    +   0    = 128   */

//Signed Right Shift
//The signed right shift is represented by two greater-than signs (>>) and shifts all bits in a 32-bitnumber to the right while preserving the sign (positive or negative). 

number = 128; // 10000000 in binary code
new_number = number >> 6 // 10 in binary code wich is decimal 2
log(new_number)// 2


//Unsigned Right Shift
/* The unsigned right shift is represented by three greater-than signs (>>>) and shifts all bits in a 32-bit number to the right. For numbers that are positive, the effect is the same as a signed right shift. For negative numbers unlike signed right shift, the empty bits get filled with zeros regardless of the sign of the number.*/

number = -64; // equal to binary 11111111111111111111111111000000
new_number = number >>> 5; // equal to decimal 134217726
log(new_number)// 134217726
/* because the unsigned right shift treats this as a positive number, it considers the value to be
4294967232. When this value is shifted to the right by five bits, it becomes 00000111111111111111
111111111110, which is 134217726. */


/* Boolean operators */
//Logical NOT ! 
//can be used in any value. This operator always returns a Boolean value, regardless of the data type it’s used on. The logical NOT operator first converts the operand to a Boolean value and then negates it,

log(!false); // true
log(!"shadow"); // false
log(!0); // true
log(!NaN); // true
log(!""); // true
log(!57344); // false
log(!null) // true
log(!undefined) // true

//it can be used to transform a value into it's boolean equivalent by using two NOT operators in a row

let name = 'Angy';
//name = !!name;
//log(name); // Logs: true

//Note: see that the first negate the value after covert it, the second just convert it to boolean.

//Logical ADN &&
//it operates over two values and return true if both values are true, false otherwise
log(true && name)// Angy
log(false && 'Angy')// false
log(4 < 5 && 8 >6)// true
/* Logical AND can be used with any type of operand, not just Boolean values. When either operand is
not a primitive Boolean, logical AND does not always return a Boolean value; instead, it does one of the following:
➤➤ If the first operand is an object, then the second operand is always returned.
➤➤ If the second operand is an object, then the object is returned only if the first operand evalu-
ates to true.
➤➤ If both operands are objects, then the second operand is returned.
➤➤ If either operand is null, then null is returned.
➤➤ If either operand is NaN, then NaN is returned.
➤➤ If either operand is undefined, then undefined is returned. */



//Logical OR ||
//it operates over two values and return true if both or one of both values are true, false other wise
let empty = '';
log(false || empty)// Logs: <empty string>
log(name || empty)// Angy
log(4 >= 5 || 8 >6)// true 

/* Just like logical AND, if either operand is not a Boolean, logical OR will not always return a Boolean value; instead, it does one of the following:
➤➤ If the first operand is an object, then the first operand is returned.
➤➤ If the first operand evaluates to false, then the second operand is returned.
➤➤ If both operands are objects, then the first operand is returned.
➤➤ If both operands are null, then null is returned.
➤➤ If both operands are NaN, then NaN is returned.
➤➤ If both operands are undefined, then undefined is returned. */

//Note: Both AND and OR are short-circuit operants, this means sometimes only the first operator is evaluated

//Multiplicative Operators
/* There are three multiplicative operators in ECMAScript: multiply, divide, and modulus. These operators work in a manner similar to their counterparts in languages such as Java, C, and Perl, but they also include some automatic type conversions when dealing with nonnumeric values. */

//Multiple Operator *
number = 4 * '8';
log(number)// Logs: 32 cause the above explanation

//Divide Operator /
number = 10 / 5;
log(number)// Logs: 2
number = 4 / 40;
log(number)// Logs: 0.1 

//Modulus (remainder) Operator %
number = 41 % 5;
log(number)// Logs: 1

//Exponentiation Operator **
number = 4 ** 2;
log(number)// Logs: 16
//same as
log(Math.pow(4,2))// 16

//Add Operator +
number = 76 + 78;
log(number)// 154
log('76' + '78')// 7678 on strings performs as a concatenator

number = BigInt(767867686876876) + BigInt(6757575755);
log(number)// 767874444452631n

//Subtract -
number = 48 - 3;
log(number)// 45

//Note: These operators has a particulary behavior in some cases when are used with Infinity, 0, NaN or a non numeric values, you should search if you want more information.


/* Relatioanl Operators */
/* The less-than (<), greater-than (>), less-than-or-equal-to (<=), and greater-than-or-equal-to (>=) relational operators perform comparisons between values in the same way that you learned in math class. */
let computation = 76 < 4;
log(computation)// false
computation = 87 > 32;
log(computation)// true
computation = 43 <= 43;
log(computation)// true
computation = 44 >= 85;
log(computation)// false

let user ={
    name: 'Clavin & Hobbes'
}

log(user <= 4)// false

log("43" < "8")// true
log("43" < 8)// false

log('DeepState' < 'real people')// true not only cause are more real people, but when we talk about strings the upper characters has lower codes than the regulars ones
console.log('DeepState'.toLowerCase() < 'real people'.toLocaleLowerCase())// true again ... well ummm sometimes we win 

/* As with other operators in ECMAScript, there are some conversions and other oddities that happen
when using different data types. They are as follows:
➤➤ If the operands are numbers, perform a numeric comparison.
➤➤ If the operands are strings, compare the character codes of each corresponding character in
the string.
➤➤ If one operand is a number, convert the other operand to a number and perform a numeric
comparison.
➤➤ If an operand is an object, call valueOf() and use its result to perform the comparison
according to the previous rules. If valueOf() is not available, call toString() and use that
value according to the previous rules.
➤➤ If an operand is a Boolean, convert it to a number and perform the comparison */

//Equality operators
//Determining whether two variables are equivalent is one of the most important operations in programming.

//equal or Equality Operator ==
log(2 == '2')// true
//deep comparation, also comapare types. identically equal or Strict Equality Operator ===
log(2 === '2')// false
//not-equal or Inequality Operator !=
log(2 != '2')// false
//deep comparation, also compare types. identically not-equal or Strict Inequality Operator !==
log(2 !== '2')// true

/* When performing conversions, the equal and not-equal operators follow these basic rules:
➤➤ If an operand is a Boolean value, convert it into a numeric value before checking for
equality. A value of false converts to 0, whereas a value of true converts to 1.
➤➤ If one operand is a string and the other is a number, attempt to convert the string into a
number before checking for equality.
➤➤ If one of the operands is an object and the other is not, the valueOf() method is called on
the object to retrieve a primitive value to compare according to the previous rules.

The operators also follow these rules when making comparisons:
➤➤ Values of null and undefined are equal.
➤➤ Values of null and undefined cannot be converted into any other values for
equality checking.
➤➤ If either operand is NaN, the equal operator returns false and the not-equal operator
returns true. Important note: even if both operands are NaN, the equal operator returns
false because, by rule, NaN is not equal to NaN.
➤➤ If both operands are objects, then they are compared to see if they are the same object. If
both operands point to the same object, then the equal operator returns true. Otherwise,
the two are not equal. */

log(NaN != NaN)// true
log(true == 1)// true
log(null==undefined)// true
log(null===undefined)// false

//Conditional Operator (condition)? true : false;
/* This basically allows a conditional assignment to a variable depending on the evaluation of the
boolean_expression. If it’s true, then true_value is assigned to the variable; if it’s false, then
false_value is assigned to the variabl */


let login = (user.name == 'Nixon')? `Succesfull login, Wellcome ${user.name}` : "Sorry we don't have any user with that name";
log(login)// Sorry we don't have any user with that name

//Assignment Operators

let a = 'a';
a = a + a;
log(a)// aa

number = 8;

/* Compound assignment is done with one of the multiplicative, additive, or bitwise–shift operators
followed by an equal sign (=). These assignments are designed as shorthand for such common situa-
tions as: */

number *= number;
log(number)// 64

number -= 4;
log(number)// 60

/* Compound-assignment operators exist for each of the major mathematical operations and a few
others as well. They are as follows:
➤➤ Multiply/assign (*=)
➤➤ Divide/assign (/=)
➤➤ Modulus/assign (%=)
➤➤ Add/assign (+=)
➤➤ Subtract/assign (-=)
➤➤ Left shift/assign (<<=)
➤➤ Signed right shift/assign (>>=)
➤➤ Unsigned right shift/assign (>>>=)
These operators are designed specifically as shorthand ways of achieving operations. They do not
represent any performance improvement. */

// Membership Operators
// the in operator
let Crows = {
    description: "Mutant fat man lives beyond the margins of the known universe...",
    age: 600,
}

log('description' in Crows)// true
log('location' in Crows)// false

// instanceof operator

class User {
    constructor(name, age, email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }

    greeting() {
        return `Hi ${this.name}. Wellcome to Roadmap Exercise #01.`;
    }
}

const niko_zen = new User('Niko', 41, 'duendeintemporal@hotmail.com');
log(niko_zen.greeting())// 'Hi Niko. Wellcome to Roadmap Exercise #01';

log(niko_zen instanceof User) // true
log(niko_zen instanceof Object) // true
log(4 instanceof Number) // false cause 4 is a primitive value
let four = new Number(4)
log( four instanceof Number)// true

// Type Operators
// we can use instanceof or typeof
log(typeof true)// boolean
log(typeof NaN)// number
log(typeof niko_zen)// object 

//Destructuring Operatorations   spread operator ...
// on arrays
let books = ['Dune', 'Shibumi', 'El Maestro de Esgrima', 'El Perfume'];
let books2 = ['Elocuent javascript', 'You Don’t Know JS ES6 Beyond', 'Linux Command Line An Admin Beginners Guide', 'Learn Bash the Hard Way', 'Programming Algorithms', 'MATLAB Notes for Professionals']
const mix_books = [...books, ...books2];
const [frank_herbert, trevanian] = books;
log(trevanian)//Logs: Shibumi

// on objects
const { email } = niko_zen;
log(email)// duendeintemporal@hotmail.com

const niko_zen_settings ={
    mode: 'dark',
    avatar: 'moebius.svg',
    interfaz: 'compact',
}

const niko_zen_data = { ...niko_zen, ...niko_zen_settings };
log(niko_zen_data)//Logs both objects niko_zen instance and niko_zen_settings

function showUser({name, age, email}){
    log(`User name: ${name}, age: ${age}, email: ${email}`);
}

showUser(niko_zen)// Logs: User name: Niko, age: 41, email: duendeintemporal@hotmail.com

// we can also asign default values in destructuring

const config = { font: 'monospace' };
const { font, mode = 'dark' } = config;

log(font, mode)// monospace dark

//you can use destructuring for exchange values on two or more variables
let ninja1 = 'Hiroshi';
let ninja2 = 'Neko';
let ninja3 = 'Kage';

[ninja1, ninja2, ninja3] = [ninja2, ninja3, ninja1];
log(ninja1)// Neko

// you can copy objects or arrays without modifing the original
const shinobi = {
    skills: ['fast', 'quick', 'precise', 'lethal', 'computational thinking'],
    location: 'no found',
}

const trix = { ...shinobi };
trix.location = 'Bangkok, Thailand';

log(shinobi.location)// no found
log(trix.location)// Bangkok, Thailand

// you can also use spread operator to pass array elements as arguments in functions or methods
nums = [1,3,4,5,6,]
log(Math.max(...nums))// logs: 6

// or to create an array of arguments
const calculateAverage = (...numbers)=> {
    const total = numbers.reduce((sum, num) => sum + num, 0);
    return total / numbers.length;
}

// see that when we call the function all the arguments get holded in numbers
const average = calculateAverage(90, 76, 45, 23, 67);
console.log(average); // 60.2

// you can also use it to convert a string into an array of its individual characters

let maximum = 'in a society that has abolish every kind of adventure, the only adventure that remains is abolish the society'

let maxim_arr = [...maximum];
log(maxim_arr)//  [ "i", "n", " ", "a", " ", "s", "o", "c", "i", "e", … ]

//Comma Operator
//The comma operator allows execution of more than one operation in a single statement, as illustrated here:

let number1 = 1, number2 = 2, number3 = 3, number4;
log(number1, number2, number3, number4)// 1 2 3 undefined

/*Most often, the comma operator is used in the declaration of variables; however, it can also be used to assign values. When used in this way, the comma operator always returns the last item in the
expression, as in the following example: */
number = (225, 14, 40, 8, 220); // num becomes 220
log(number)// 220
/*There aren’t many times when commas are used in this way; however, it is helpful to understand that this behavior exists. */

//Flow Control Statements
//the if statement
if(number){
    number+=4;
    log(number)// 224
}

//the else statement
if(number){
    number+=4;
    log(number)// 228
}else{
   // what ever
}

//the else if statement
if(number > 300){
    number+=4;
    log(number)
}else if(number > 200){
    number+=4;
    log(number)// Logs: 232
}
else{
   //do something
}

// the do-while statement
/* The do-while statement is a post-test loop, meaning that the escape condition is evaluated only after the code inside the loop has been executed. */
let count = 0;
do {
    log("I'm learning a lot in this roadmap for coders, even with these basic exercises")
    count++;
} while (count < 1);

// the while statement
//while(true){
    //do something
    //create an infinite loop cause always evaluate to true
//}

// the for statement
number = 0;
for(let i = 1; i <= 100; i++){
    number += i;
}
log(number)// Logs: 5050

//Nothing can be done with a for loop that can’t be done using a while loop. The for loop simply encapsulates the loop-related code into a single location.

// the for-in statement
// let us iterate over the properties of object elements
let user2 = {
    name: 'Nikita',
    age: 32,
    location: 'No Found',
}

for(let data in user2){
    log(data) // logs only the property 
    log(data, user2[data]) // logs the property and the value
    log(data, eval('user2.' + data)) // the same as before 
}

/* Object properties in ECMAScript are unordered, so the order in which property names are returned
in a for-in statement cannot necessarily be predicted. All enumerable properties will be returned
once, but the order may differ across browsers. */

// the for-of statement
// is thinked to iterate over array elements
let oddNums = [1,3,5,7,9]

for(let num of oddNums){
    log(num)// logs each num
}

/* we can use Object.entries(), Object.keys(), Object.values() to iterate over object f. e.

Object.entries(user2) result in: 
 [
    [ "name", "Nikita" ]
    [ "age", 32 ]
    [ "location", "No Found" ]
 ] */
// so we can just
for(let [key, val] of Object.entries(user2)){
    log(`${key}: ${val}`);
}

// Label statements
outer_loop:for(let i = 0; i <= 10; i++){
    inner_loop:for(let y = 0; y < 5; y++){
             if((i==2) && (y == 4)) break outer_loop;
             if(y==4) break inner_loop;
             log('Is there anybody outthere?')
    }
}

// break and continue statements
/* The break and continue statements provide stricter control over the execution of code in a loop.
The break statement exits the loop immediately, forcing execution to continue with the next state-
ment after the loop. The continue statement, on the other hand, exits the loop immediately, but
execution continues from the top of the loop. Here’s an example: */
number = 0;
while(number < 5){
    if(number == 3) break;
      log(number);
      number++;
}// Logs: number value three times: 0 1 2

number = 0;
while(number < 5){
    if(number == 3){
        number++;
        continue;  
     }
    log(number);
     number++;
}// Logs: number value four times: 0 1 2 4

//The with Statement

/* The with statement was created as a convenience for times when a single object was being coded to over and over again, as in this example: 

let qs = location.search.substring(1);
let hostName = location.hostname;
let url = location.href;

Here, the location object is used on every line. This code can be rewritten using the with statement
as follows: 

with(location) {
let qs = search.substring(1);
let hostName = hostname;
let url = href;
} */

//example
with(user){
    log(name)// Clavin & Hobbes
//    log(age)// thow an error cause age is undefined
}

//Note: the with statement is generally discouraged in modern JavaScript because it can lead to code that is difficult to read and maintain, and it can also cause performance issues.

// The Switch Statement

switch(user.name){
    case 'Nikita': 
        log('Wellcome agent');
        break;
    case 'Calvin &' + 'Hobbes': 
        log('Bring me some cookies');
        break;
    default: 
        log('Turn off that TV'); //log this cause is missing and space in the second case                                  
}

//we can also use an expression that evaluates a string concatenation in a case. The ability to have case expressions also allows you to do things like this:
/*
let num = 25;
switch (true) {
    case num < 0:
        console.log("Less than 0.");
        break;
    case num >= 0 && num <= 10:
        console.log("Between 0 and 10.");
        break;
    case num > 10 && num <= 20:
        console.log("Between 10 and 20.");
        break;
    default:
        console.log("More than 20.");
} */

// Extra dificulty: Create a program that prints the even numbers from 10 to 55 inclusive and avoids printing the numbers if they are equal to 16 or multiples of 3

for(let i = 10; i <= 55; i++ ){
    if(i % 3 == 0 || i == 16) continue;
    if(i % 2 == 0) log(i);
}