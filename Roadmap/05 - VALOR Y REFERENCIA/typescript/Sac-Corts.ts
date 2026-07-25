// By value (with primitive types)
let c: number = 10;
let d: number = c;

d = 20;
console.log(c);
console.log(d);

// By reference (with objects)
let objA = { value: 10 };
let objB = objA;

objB.value = 20;
console.log(objA.value);
console.log(objB.value);

// Function with parameter passed by value
function incrementValue(val: number): void {
    val += 10;
    console.log(`Inside the funcion: ${val}`);
}

let _num = 5;
incrementValue(_num);
console.log(`Outside the function: ${_num}`);

// Function with parameter passed by reference
function incrementObject(obj: { value: number }): void {
    obj.value += 10;
    console.log(`Inside the function: ${obj.value}`);
}

let _myObj = { value: 5 };
incrementObject(_myObj);
console.log(`Outside the function: ${_myObj.value}`);

// *** Extra Exercise *** //
// By value
let parameter1: number = 10;
let parameter2: number = 20;

function exchangeValue(x: number, y: number): number[] {
    let temp = x;
    x = y;
    y = temp;
    return [x, y];
}

let [newValue1, newValue2] = exchangeValue(parameter1, parameter2);
console.log("Swap by value:");
console.log(`Original values: parameter1: ${parameter1} and parameter2: ${parameter2}`);
console.log(`New values: parameter1: ${newValue1} and parameter2: ${newValue2}`);

// By reference
type ValueObject = { value: string }
type Ref = { str1: ValueObject, str2: ValueObject };

let str1: ValueObject = { value: "Object 1" };
let str2: ValueObject = { value: "Object 2" };

let ref: Ref = { str1: str1, str2: str2 };

function exchangeReference(ref: Ref): void {
    let temp = ref.str1;
    ref.str1 = ref.str2;
    ref.str2 = temp;
}

console.log("Swap by reference:");
console.log(`Original values: str1: ${str1.value} and str2: ${str2.value}`);
exchangeReference(ref);
console.log(`New values: str1: ${ref.str1.value} and str2: ${ref.str2.value}`);