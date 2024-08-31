//Arimethic operators

let a = 2;
let b = 3;

//Sum 
let sum = a+b;
console.log("Sum: ", sum);

//Diff
let diff = a-b;
console.log("Diff: ", diff);

//Multiply 
let multiply = a*b;
console.log("Mltiply: ",multiply);

//Division 
let division = b/a;
console.log("Division: ",division);

//Remainder
let remainder = b%a;
console.log("Module: ", remainder);

//Pow 
let pow = a**b;
console.log("Pow: ",pow);

//Logical operators
console.log("***Logical operators***");

//And
let and = true && false;
console.log("And: ", and);

//OR
let or = false || true;
console.log("Or: ", or);

//Not
let not = !(true);
console.log("Not: ", not);

//Comparassion
console.log("***Comparassion***");

//Equal 
let equal = a==b;
console.log("Equal: ",equal);

//Not equal
let not_equal = a!=b;
console.log("Not equal: ", not_equal);

//Bigger
let bigger = a > b;
console.log("Bigger: ",bigger);

//Bigger or equal
let bigger_equal = a >= b;
console.log("Bigger or equal: ", bigger_equal);

//Lower 
let lower = a < b;
console.log("Lower: ", lower);

//Lower or equal
let lower_equal = a <= b;
console.log("Lower or equal: ", lower_equal);

//Assignation
let c = 10;
console.log("= ", c);

//Beloning
let array = [3,5,0,1];
let belong = 3 in array;
console.log("IN: ",belong);

//Identity
let identity = a ===b;
console.log("Identity: ",identity);

//Bits 
console.log("***Bits***");

//And
let bits_and = 5 & 3;
console.log("&: ",bits_and);

//Or
let bits_or = 5 | 3;
console.log("|: ", bits_or);

// XOR
let bits_xor = 5 ^ 3;
console.log("^: ",bits_xor);

// Not
let bits_not = ~ 5;
console.log("~: ",bits_not);

// Control 
console.log("***If statements***")
//If
if(a<b){
    console.log("If statement")
}
else{
    console.log("Else statement");
}
//inline if
(a<b)? console.log("If with ?"):console.log("else with ?");

//Switch

let color = "orange";

switch(color){
    case "orange":
        console.log("orange color");
        break;
    case "blue":
        console.log("blue color");
        break;
    default: 
        console.log("Default option") ;
        break;       
}


//Loops
console.log("***While***");

while(true){

    console.log("While loop");
    break;
}

console.log("***for loop***");

for(let i = 0;i<3;i++){

    console.log(i);
}

//Do while loop
console.log("***DO while***");

let j=0;

do{
    console.log(j);
    j++;

}while(j<2);

//Exception  
console.log("***Exception***")
try{

  f
}catch(err){
    console.log(err.message);
}

//Extra exercise

for(let index = 10; index <=55;index++){

    if(index%2==0 && index !=16 && index%3 != 0){
  
      console.log(index);
    }
  }