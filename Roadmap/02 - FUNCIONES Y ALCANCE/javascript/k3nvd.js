//F U N C T I O N S

//Basic Function            'Function to add two numbers'

let varInitial = 3;                 //we declared a var Inital

function addNumbers(){              
    varInitial += 7;
    // varInitial = varInitial + 7;         //Another way to do that                
    console.log(varInitial);
}

addNumbers();           //10                          //we call the function
addNumbers();           //17                          //we call the function
addNumbers();           //24                          //we call the function


//With 'retunr' and 'Parameters and arguments'

function add2numbers (a,b){
    console.log(a + b);
    return add2numbers;
}

rer = add2numbers(1,4);         //5
rer = add2numbers(1,7);         //8
rer = add2numbers(1,5);         //6

//Add differents arguments

function manyArguments(){
    let valueInitial = 0;
    for (let eachValue of arguments){
        valueInitial += eachValue;
        // console.log(addOfArguments); 
    }
    return valueInitial;
}
console.log(manyArguments(1,2,3));



//Declarate a function and function expretion;

//when we declarate a function

function declarateFunction(){
    console.log('This is a declaration');
}

let varDeclaration = function(){
    console.log('This is Expretion');
}

declarateFunction();            //This is a declaration
varDeclaration();              //Thus is a Expretion


//FUNCTIONS USING 'RETURN'


let user1 = {
    name: 'Ana',
    age: 22,
    city:'Mexico City',
    phone:5512123434
};

// function changeMyage(objectt){
//     objectt.age = 23;                   //With this, I change the original object
// }
// changeMyage(user1);
// console.log(user1);    

//This is object copy, so the original object not change

function changeMyage(objectt){
    let copyy = JSON.parse(JSON.stringify(objectt));         //This is doing a copy
    copyy.age = 23; 
    return copyy;                  
}
console.log(user1);                         //print the orignal object

console.log(changeMyage(user1));            //Print the copy object

//METHODS IN A FUNCTION

let newObjt = {
    favoritecolor:'Blue',
    favoriteCity:'Mexico',
    favariteFood: 'Pizza',
    hobby:function(){
        console.log('I like to play videogames');
    }
};

newObjt.hobby();                            //It is show 'I like to play videogames'


//SCOOP


var var1 = 10;                      //global scoope

function inside(){
    // var var1 = 20;                  //local scoope

    //now, if we delete the 'var' in our local variable
    var1 = 20;    // this would change the gloabal var 'var var1 = 10'

    console.log(var1);
}   

//When we put var, this means that is a new declaration. That's why that variable changes

inside();                           //20
console.log(var1);                  //10
console.log(var1);                  //20    This is wiith de local variable without 'var'


//var works in the scoop of the function
//let workd in the scoop of the block, for example  let xVariable={         }

//CALLBACK

function sayHiAfterTwoSeconds(){
    console.log('Hi');

}
setTimeout(sayHiAfterTwoSeconds,2000); 
console.log('This well print Immediately');   

//another way

function llamar(callbackk){
    callbackk();
}

llamar(function(){console.log(3); });

//ANOTHER WAY 


function varification(t, f){
        //####t or f
    let validation = true;

    if (validation){
        t();
    }else {
        f();
    }

}
varification(
    () => console.log('Welcome'),
    () => console.log('Error')
)

/*
function t(){
    console.log('Welcome');
}
function f(){
    console.log('Sorry, Could there an Error');
}


varification(t,f);
*/
//CHALLENGE         

let adder = 1;
function soap(txt11,txt22){
    console.log(txt11 + txt22);

    while (adder<=99){
        // console.log(adder);
        adder+=1;

        if (adder %3 ==0 && adder %5 ==0){//
            console.log(txt11 +' '+ txt22);

        }else if(adder %5 ==0){
            console.log(txt22);
           

        }else if (adder %3 ==0){
            console.log(txt11);
        

        }else {
            console.log(adder);
        }
    }

    

}
soap('Hello','World');

  


  

