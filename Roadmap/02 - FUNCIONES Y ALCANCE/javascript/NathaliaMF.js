

const nameValue='Nathalia';
let yearBirth =1996;
let today=  new Date();

function greetingMessage() {
    console.log('Hello world this is javascript')
    
};
greetingMessage(); 

function currentAge(param1, param2) {
    let year = param2.getFullYear();
    let ageValue= year -param1;
    return ageValue;
    
}

function introduction(param) {
    console.log(`My name is ${param} and I am ${currentAge(yearBirth, today)} `);

};

introduction(nameValue);

function currentTime(){
     function valueTime(){
        return today.getHours();
    }
    console.log(`The current time is ${valueTime()} `);

}
currentTime();
console.log("Asynchronous");

function two() {
  setTimeout(function () {
    console.log("Two");
  }, 1000);
}

function one() {
  setTimeout(function () {
    console.log("One");
  }, 0);
  two();
  console.log("Three");
}

one();
console.log("End");

/**EJERCICIO EXTRA */

function extraExercise(text1, text2) {
    let value=0;
    for (let index = 0; index <=100 ; index++) {
        if(index % 3 == 0){
            console.log(text1);
        }else if(index % 5 == 0){
            console.log(text2);
        }else if(index % 3 == 0 && index % 5 ==0){
            console.log(`the value of the chains is ${text1} and ${text2} `);
        }else{
            value++;
        }
        
        
    }
    return value

}

console.log(`The value is${extraExercise('Hola','Mundo')}`);