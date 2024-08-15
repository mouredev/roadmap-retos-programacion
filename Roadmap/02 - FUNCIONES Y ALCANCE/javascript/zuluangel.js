//basic function
function basic() {
    console.log('This is a basic function');    
}
basic();

//function with one parameter
function oneParam(param) {
    console.log(`This is a function with one parameter: ${param}`);
}
oneParam('This is the parameter');
oneParam(2)

//function with two parameters
function twoParams(param1, param2) {
    console.log(`This is a function with two parameters: '${param1}' and '${param2}'`);
}
twoParams('This is the first parameter', 'This is the second parameter');
twoParams(2, 3)

//function with return and two params
function returnFunc(a, b) {
    return `This is a function that returns a value: ${a + b}`;
}
console.log(returnFunc(3, 5));

//function inside another function
function outer() {
    function inner() {
        console.log('This is an inner function');
    }
    console.log(`This is the outer function executing...`)
    inner();
}
outer();

//these are functions created on the javascript environment and we are not able to change them
//we can only use them
// console.log() //is a js function
// alert() //is also a js function

//Local variables are the ones that are inside a specific function or class o little snipet of code.
//They are not accessible from outside the function or class where they are declared.
function local(){
    let x = 10;
    let y = 5
    console.log(x + y);
}
local();

//Global variables are the ones that are accessible from any part of the code.
let z = 20

function globalScope(){
    console.log(z * 5);
}
globalScope();

/* 
EXTRA
*/

function extraFunction(param1, param2) {
    
    let counter = 0
    
    for(i=1; i<=100; i++){   
        if(i%3 == 0 && i%5 == 0) {
            console.log(`${param1} ${param2}`)
        } else if(i%3 == 0) {
            console.log(param1)
        } else if(i%5 == 0) {
            console.log(param2)
        } else {
            console.log(i)
            counter ++
        }
    }
    console.log(`On the whole loop there are a total of ${counter} numbers`)       
}
extraFunction('text1', 'text2')