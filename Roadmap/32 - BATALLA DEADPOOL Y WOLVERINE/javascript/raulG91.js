
const prompt = require('prompt-sync')();

function getRandomNumber(min,max){

    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

let deadpool_life = prompt('Introduce vida maxima para Deadpool ')
if(deadpool_life < 0) {

}
let wolverine_life = prompt('Introduce vida maxima para wolverine ')

if(deadpool_life > 0 && wolverine_life > 0){
    let turn = 1;
    let skip_turn = false;
    while (deadpool_life > 0  && wolverine_life > 0) {
        console.log(`Turno: ${turn}`)
        //Determine who is attacking this turn

        if (turn % 2 != 0){
            //Attack Deadpool
            if(skip_turn){
                console.log("Deadpool no atacara en este turno")
                skip_turn = false
            }
            else{
                let deadpool_attack = getRandomNumber(10,100);
                //Let's see if Wolverine avoid attack
                console.log("Deadpool atacara con: " + String(deadpool_attack))
                let skip = getRandomNumber(0,100);
                if(skip <= 20){
                    console.log("Wolverine esquiva el ataque de Deadpool")
                }
                else{
                    // Check if the damage is the max attack
                    if(deadpool_attack == 100){
                        skip_turn = true
                        console.log("Ataque maximo de Deadpool!")
                    }
                    wolverine_life -= deadpool_attack;
                    
                }
            }
        
        }
        else{
            if(skip_turn){
                console.log("Wolverine no atacara en este turno")
                skip_turn = false;
            }
            else{
                let wolverine_attack = getRandomNumber(10,120)
                console.log(`Wolverine atacara con ${wolverine_attack}`)
                let skip = getRandomNumber(0,100);
                if(skip <= 25){
                    console.log("Deadpool esquiva el ataque de Wolverine")
                }
                else{
                    if(wolverine_attack == 120){
                        skip_turn = true;
                        console.log("Ataque maximo de Wolverine")
                    }
                    deadpool_life -= wolverine_attack;
                }
            }
        }
        if(deadpool_life> 0 && wolverine_life > 0){
            console.log(`Vida de Deadpool tras turno ${turn} es ${deadpool_life}`)
            console.log(`Vida de Wolverine tras turno ${turn} es ${wolverine_life}`)
            turn ++;
        }
        else{
            // One character has died
            if(turn % 2 == 0){
                console.log("Wolverine ha ganado el combate")
            }
            else{
                console.log("Deadpool ha ganado el combate")
            }
        }
    }
} 
else{
    console.log("Vida maxima debe ser mayor que 0")
}