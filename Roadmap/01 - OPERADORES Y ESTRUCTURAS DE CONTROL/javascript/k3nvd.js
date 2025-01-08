//DIFERENTS OPERATORS

// COMPARATORS

let num1 = 10;
let num2 = 10;

let newtype = '10';

console.log(num2 == newtype);       //True
console.log(num2 === newtype);       //False

console.log(num1 != num2);          //False
console.log(num1 !== newtype);      //True for the data Type   

console.log(num1 < 10);             //False
console.log(num1 <= 10);            //True

console.log(num1 > 10);              //False
console.log(num1 >= 10);            //True

if (num1 == num2 ){
    console.log('EQUAL')            //EQUAL
}


// COMPARATOR FOR VALUE AND REFERENCE


//VALUE

let x = 10;
let y = 10;

console.log(x == y);    //True

//reference, we make reference to the memory

let a = {value : 10};
let b = {value : 10};

console.log(a == b );       //False
console.log(a === b );       //False

let c = x;

console.log(c == x);        //True
console.log(c === x);       //True

//ARIMETICS

console.log(4+4);   //8
console.log(4-4);   //0
console.log(4/4);   //1
console.log(4*4);   //16
console.log(4%4);   //0

//LOGICS OPERATORS  && || !

let txt1 = 'JS';
let txt2 = 'C++';
let txt3 = 'Python';

console.log(txt1 === 'JS' && txt1 ==='JS');     //True
console.log(txt1 === 'JS' && txt1 ==='js');     //False

console.log(txt1 === 'JS' || txt1 ==='js');     //True
console.log(txt1 === 'Python' || txt1 ==='js');     //False

console.log(txt1 ==='JS' && txt2 === 'C++' || txt1 === 'Python' && txt3 === 'Python')       //True

let isSunny = false;
if (!isSunny) {
    console.log('It is not sunny');     //It is not sunny
}

console.log(!isSunny);          //True




//CONDITIONALS
//WITH          else if
let minAge = 18
let user1  = 18;
let user2 = 15;
let user3 = 22;

if (user1 => 18){
    console.log('Acces allowed', 'Age is: ' + user1);
}else if (user1 < 18){
    console.log('Sorry, Not Allowed');
}else if (user3 > 18){
    console.log('Allowed');
}else {
    console.log('There is an Error')
}

//CONDITIONALS
//WITH          SWITCH

let administrator = 'Kevin';

switch (administrator)  {
    case 'Peter':
        console.log('Not Allowed');
        break
    case 'Kevin':
        console.log('Congratulations, You are', administrator);
        break
    default:
        console.log('There is an Error here.');
}

//TERNARY OPERATOR

let password = 1234;
let fulacces = password =='1234' ? 'That is correct' : 'The password is not correct';

console.log(fulacces);

//EXEPTIONS 

let id = 12112;


try {
    if(id != 1212) {
        throw "That is not correct,Please try again";
    }
    console.log('That is correct');
}catch (error){
    console.error ('Errorrrrr', error);
}


//EXTRA

let iter = 10;

while (iter <= 55) {
    // console.log(iter);
    iter +=1;
    if (iter % 2 ==0 ) {
        console.log('Is even', iter);
    }else if (iter %3 ==0){
        console.log('This is multiple 3',iter)
    } else if (iter ==16 ) {
        console.log('This numer is 6')

    }
}
//Ouput
/*
Is even 12
Is even 14
This is multiple 3 15
Is even 16
Is even 18
Is even 20
This is multiple 3 21
Is even 22
Is even 24
Is even 26
This is multiple 3 27
Is even 28
Is even 30
Is even 32
This is multiple 3 33
Is even 34
Is even 36
Is even 38
This is multiple 3 39
Is even 40
Is even 42
Is even 44
This is multiple 3 45
Is even 46
Is even 48
Is even 50
This is multiple 3 51
Is even 52
Is even 54
Is even 56
*/
