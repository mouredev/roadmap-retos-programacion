
try{    
   myFunctionUndefined()
}catch(error){
    console.log("There is an error")
    console.log(error.name)
}

class CustomError extends Error{

    constructor(){

        super("Custom message");
    
    }
}


function myFunction(param1,param2){
    if(param1 <= 3){
        throw new CustomError();
    }
    else if (typeof(param2)!= "number"){
        throw TypeError("Int was expected");  
    }
    else if(param2>= 6){
        throw Error("Value bigger than 6");
    }
}

try{
        //myFunction(1,4);
        //myFunction(8,"ed");
        myFunction(8,16);

}catch(err){

    console.log("Exception name ", err.name);
    console.log("Exception message ", err.message);
}

console.log("Execution finished ")