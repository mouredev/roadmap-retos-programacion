// Exercise //

// Variable Assignment 
// By value
let a = 10;
let b = a;
b = 20;

console.log(a);
console.log(b);

// By reference
let obj1 = { value: 10 };
let obj2 = obj1;
obj2.value = 20;

console.log(obj1.value);
console.log(obj2.value);

// Passing from Parameters to Functions
// By value
function changeValue(x) {
    x = 30;
    return x;
}

let num = 10;
console.log(changeValue(num));
console.log(num);

// By reference
function changeObj(obj) {
    obj.value = 60;
    return obj;
}

let myObj = { value: 50 };
console.log(changeObj(myObj));
console.log(myObj);

// Extra Exercise //
let str1 = "Hello";
let str2 = "World";

// By value
function swapByValue(x, y) {
    let temp = x;
    x = y;
    y = temp;
    return [x, y];
}

// By reference
function swapByReference(ref) {
    let temp = ref.str1;
    ref.str1 = ref.str2;
    ref.str2 = temp;
}   

let [newStr1, newStr2] = swapByValue(str1, str2);
console.log("Swap by value:");
console.log("Original values: str1 = ", str1, " str2 = ", str2);
console.log("New values: nweStr1 = ", newStr1, " newStr2 = ", newStr2);

let ref = {str1: str1, str2: str2};
swapByReference(ref);
console.log("Swap by reference");
console.log("Original values: str1 = ", str1, " str2 = ", str2);
console.log("New values: ref.str1 = ", ref.str1, " ref.str2 = ", ref.str2);