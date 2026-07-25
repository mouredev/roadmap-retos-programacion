class Character {
    constructor(name, hp, regeneration, evasion){
        this.name         = name;
        this.hp           = hp;
        this.regeneration = regeneration;
        this.evasion      = evasion;
        this.damage       = 0;
    }
}

class Battle {

    constructor(){}
    
    regenaration(character){
        let probability = Math.random() * 100 + 1; 
        if(probability <= character.regenaration){
            console.log(`${character.name} esquivo el golpe xD`);
            console.log(`${character.name} se esta regenerando...`);
            character.hp =+ character.regenaration;
            console.log(`${character.name} se regeneró ${character.regenaration}%, su nueva vida: ${character.hp}`);
            return true;
        }
        
        return false;
    }

    fight(){
        console.log("Entreeeee a la batalla");
        let deadpool = new Character("Deadpool", 1000, 25, 25);
        let wolverine = new Character("Wolverine", 1200, 15, 20);
        while(deadpool.hp > 0 && wolverine.hp > 0){
            let random1 = Math.random() * (100 - 10) + 10;
            let random2 = Math.random() * (120 - 10) + 10;
            deadpool.damage = parseInt(random1); 
            wolverine.damage = parseInt(random2);
            let min = 0;
            let max = 2;
            let turn = parseInt(Math.random() * (max - min) + min);
            let regenaration = false;
            if(turn == 0){
                console.log(`Golpea Deadpool con ${deadpool.damage} de daño`);
                regenaration = this.regenaration(deadpool);  
                if(regenaration){
                    min = 1;
                    max = 2;
                } else {
                    wolverine.hp -= deadpool.damage;
                    console.log(`Vida restante de ${wolverine.name}: ${wolverine.hp}`);
                    if(deadpool.damage == 100){       
                        console.log(`${deadpool.name} dio un critico`);
                        min = 0;
                        max = 1;
                    } else {
                        min = 1;
                        max = 2;
                    }
                }
            } else {
                console.log(`Golpea Wolverine con ${deadpool.damage} de daño`);
                regenaration = this.regenaration(wolverine);  
                if(regenaration){
                    min = 0;
                    max = 1;
                } else {
                    deadpool.hp -= wolverine.damage;
                    console.log(`Vida restante de ${deadpool.name}: ${deadpool.hp}`);
                    if(wolverine.damage == 120){       
                        console.log(`${wolverine.name} dio un critico`);
                        min = 1;
                        max = 2;
                    } else {
                        min = 0;
                        max = 1;
                    }
                }
            }
        }

        if(deadpool.hp > 0){
            console.log("----- Deadpool gana -----");
        } else {
            console.log("----- Wolverine gana -----");
        }
    }

}

let battle = new Battle();
battle.fight();
    
