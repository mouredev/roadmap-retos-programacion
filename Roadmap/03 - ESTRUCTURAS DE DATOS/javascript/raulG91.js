//Array
console.log("***Array***");
let array = [6,4,23,3,4];

//Add element 
array.push(10);
console.log("Add element: ",array);

//Delete last element
array.pop();
console.log("Remove last element: ",array);

//Delete specific element
array.splice(1,1) //Removes element at position 1
console.log("Remove specific element: ",array);

//Update element at position 0 
array[0] = 5;
console.log("Update element at pos 0: ",array);

//Order array
function compareNumeric(a, b) {
    if (a > b) return 1;
    if (a == b) return 0;
    if (a < b) return -1;
  }
array.sort(compareNumeric);
console.log("Sort array: ",array);

//MAP
console.log("***Map***");
let map = new Map();

//Add values to the map
map.set(1,"one");
map.set(2,"two");
console.log("Adding element: ",map);

//Update value
map.set(2,"dos");
console.log("Update value: ",map);

//Borrado 
map.delete(2) //Delete element with key
console.log("Delete element: ",map);

//Set 
console.log("***Set***");

let set = new Set();
//Add element
set.add(1);
set.add(2);
set.add(10)
console.log("Add elements: ", set);

//Delete element
set.delete(10)
console.log("Delete elements: ",set);

// Objects
console.log("***Object***");
my_object = {

    name:"Raul",
    last_name:"last name"
}

// Add element
my_object.age = 14;
console.log("Adding element: ",my_object);

//Update element
my_object.age = 32;
console.log("Update object: ", my_object);

//Delete element
delete my_object.last_name;
console.log("Delete element: ", my_object);

//Extra exercise
const  readline = require('node:readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });

let contact_agenda = {};

function agenda(){
        show_menu();
        readline.question("Insert operation: ",(operation)=>{
            operation = parseInt(operation);
            switch(operation){
                case 1: //Insert
                    readline.question("Insert user name: ",(name)=>{
                        if(contact_agenda[name]){
                            console.log("User already exist");
                            agenda()
                        }
                        else{
                            readline.question('Insert number: ',(number)=>{
                                phone = parseInt(number);
                                if(validate_number(phone)){
                                    contact_agenda[name] = phone;
                                }
                                else{
                                    console.log("Invalid phone number");
                                }
                                
                                agenda()
                            });
                        }
                       
                    });
                    break;
                case 2: //Update
                    readline.question('Insert user name: ',(name)=>{
                        if(contact_agenda[name]){
                            //User already exist
                            readline.question('Insert new phone number: ',(number)=>{
                                phone = parseInt(number);
                                if(validate_number(phone)){
                                    contact_agenda[name] = phone;
                                }
                                else{
                                    console.log("Invalid phone number");
                                }
                                agenda()
                            })
                        }   
                        else{
                            console.log("User doesn't exist");
                            agenda()

                        }
                    });
                    break;   
                case 3: //Delete user
                    readline.question('Insert user name: ',(name)=>{
                        if(contact_agenda[name]){
                            delete contact_agenda[name];
                        }
                        else{

                            console.log("User doesn't exist");
                        }
                        agenda();
                    });
                    break;
                case 4: //Show user phone
                    readline.question('Insert user name: ',(name)=>{
                        if(contact_agenda[name]){
                          console.log(`Phone number for ${name} is ${contact_agenda[name]}`);
                        }
                        else{
                            console.log("User doesn't exist");
                        }
                        agenda();
                    });
                    break;  
                case 5: //Exit program 
                    readline.close();
                    break
                }
        })

}
function show_menu(){

    console.log("Insert 1 to create user");
    console.log("Insert 2 to update user");
    console.log("Insert 3 to delete user");
    console.log("Insert 4 to look for a user");
    console.log("Insert 5 to exit");
}
function validate_number(number){

    return /^\d{9}$/.test(number)
}
agenda();