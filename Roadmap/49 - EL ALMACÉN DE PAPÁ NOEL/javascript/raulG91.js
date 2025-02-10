const prompt = require('prompt-sync')();

const CHAR_SET = ['A', 'B', 'C', "1", "2", "3"];

function getRandomNumber(min, max) {

    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

function generateCode() {

    let char_set_string = CHAR_SET.join("")
    let i = 0;
    let final_code = ""

    while (i < 4) {
        let pos = getRandomNumber(0, char_set_string.length - 1)
        final_code += char_set_string.charAt(pos)
        char_set_string = char_set_string.slice(0, pos) + char_set_string.slice(pos + 1)
        i++
    }
    return final_code
}

function check_input(input) {

    let correct = true

    //First check if the length of the input is 4
    if (input.length != 4) {
        console.log("El codigo debe tener una longitud de 4 caracteres")
        correct = false
    }
    else {
        //Check if the input contains non allowed characters
        for (let char of input) {
            if (!(CHAR_SET.includes(char))) {
                console.log(`Caracter ${char} no esta permitido`)
                correct = false
                break
               
            }
            else {
                //Count if the char appears more than 1
                let count = (input.match(new RegExp(char, "g")) || []).length;
                if (count > 1) {
                    console.log(`Caracter ${char} esta duplicado`)
                    correct = false
                    break
                  
                }
            }
        }
    }
    return correct
}

function main() {
    let code = generateCode()
    let tries = 0;
    let exit = false

    console.log(code)
    while (tries < 10 && !exit) {
        console.log(`Numero de intentos restantes ${10 - tries}`)
        //User imput
        let input = prompt('Introduce codigo de entrada ')
        //If length is different to 4 throw an error
        if (check_input(input)) {
            // Check if the code entered by the user is the one that we are looking for
            if (input === code) {
                exit = true
                console.log("El codigo es correcto ")
            }
            else {
                // Checks how many characters the user input correctly
                for (let i = 0; i < input.length; i++) {
                    if (input.at(i) == code.at(i)) {
                        //Char is in the same position
                        console.log(`Caracter ${input.at(i)} es Correcto`)
                    }
                    else {
                        let current_char = input.at(i)
                        if (code.includes(current_char)) {
                            //Char exist in the code but the position is not correct
                            console.log(`Caracter ${current_char}  esta presente`)
                        }
                        else {
                            console.log(`Caracter ${current_char} es Incorrecto`)
                        }
                    }
                } 

            }
        }

        tries++

    }
}

main()