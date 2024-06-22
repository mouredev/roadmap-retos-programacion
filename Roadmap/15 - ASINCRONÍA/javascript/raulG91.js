
async function asyncfunction(seconds,name){
    console.log(`Starting async function: ${name}` );
    return new Promise(resolve => setTimeout(function(){
                                console.log(`Ending async function: ${name}`);
                                 resolve()}, 1000*seconds));
    
}

asyncfunction(2,"Function");

/*Extra */ 

async function executePromises(){

    await Promise.all([asyncfunction(3,"C"),asyncfunction(2,"B"),asyncfunction(1,"A")]);
    await asyncfunction(1,"D")
}

executePromises()