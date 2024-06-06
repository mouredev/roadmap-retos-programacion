
//Simple
function sayHello(){

    console.log("Hello World!");
}
console.log("Function without parameter and without return");
sayHello();
//With retrun a not parameter
function sayHello2(){
    return "Hello Team!";
}
console.log("Function without parameter and with return");
console.log(sayHello2());
//With parameters not return
function sumNumber(a,b){
    let result = a+b;
    console.log(result)
}
console.log("Function with parameters and not return");
sumNumber(2,3);

//With parameters and return
function multiplyNumbers(a,b){
    return a*b;
}
console.log("Function with parameters and return");
let result = multiplyNumbers(2,3);
console.log(result);

//Function with default parameters
function default_parameter(phrase="Hello world"){

    console.log(phrase);
}

console.log("Function with default parameter");
default_parameter();
default_parameter("This is a function");

//Nested functions
function main_function(){

    function nested_function(){

        console.log("Hello from nested function");
    }

    nested_function();
}

console.log("Nested function");
main_function();

// Javascript functions
let a = 3;
console.log("Function typeof");
console.log(typeof(a));

let string = "This is an string";
let array = string.split(" ");
console.log("Split function");
console.log(array);

let variable = 6

function modify_variable(){

    let variable = 10;
    console.log(variable);
}

modify_variable();
console.log("Original variable " + variable);

//Extra exercise

function print_numbers(string1,string2){

    let numbers = 0;

    for(let i=1;i<=100;i++){

        if(i%3 == 0 && i %5 == 0){
            console.log(string1+string2);
        }
        else if (i%3==0){
            console.log(string1);
        }
        else if (i%5==0){
            console.log(string2);
        }
        else{
            console.log(i);
            numbers++;
        }
    }

    return numbers;
}

let numbers = print_numbers("fizz","buzz");

console.log(numbers);

