//#32 - BATALLA ENTRE DEADPOOL Y WOLVERINE
/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */

let log = console.log;

class Combatant {
    constructor(name, avatar, life, atkMax, atkMin, def) {
        this.name = name;
        this.avatar = avatar;
        this.life = life;
        this.attackDamageMax = atkMax;
        this.attackDamageMin = atkMin;
        this.defense = def;
        this.attackPotence = atkMax;
    }
}

const WOLVERINE = new Combatant('Wolverine', 'avatar', 100, 120, 10, 20);
const DEADPOOL = new Combatant('Deadpool', 'avatar', 100, 100, 10, 25);

class Battle {
    constructor(c1 = new Combatant(), c2 = new Combatant()) {
        this.combatant1 = c1;
        this.combatant2 = c2;
        this.result = '';
        this.battleInterval = null; 
    }

    startBattle() {
        let isAttacking = false; 

        this.battleInterval = setInterval(() => {
            if (this.combatant1.life <= 0 || this.combatant2.life <= 0) {
                clearInterval(this.battleInterval); 
                return; 
            }

            if (!isAttacking) {
                isAttacking = true; 
                this.round(); 

                setTimeout(() => {
                    isAttacking = false;
                }, 4500); 
            }
        }, 1500);
    }

    attack(attacker, defender) {
        const body = document.body;
        const attackStyle = (attacker === this.combatant1) ? 'wolv_attack' : 'dead_attack';
        let avoidAttack = Math.floor(Math.random() * 101);

        log(`Attacker: ${attacker.name}, Defender: ${defender.name}, Attack Style: ${attackStyle}`);

        
        if (avoidAttack < 101 - defender.defense) {
            // Calculate damage based on attackPotence but within the defined range
            const maxDamage = Math.min(attacker.attackDamageMax, attacker.attackPotence);
            const minDamage = attacker.attackDamageMin; // Keep the minimum damage as defined

            // Calculate the actual damage within the range
            const damage = Math.floor(Math.random() * (maxDamage - minDamage + 1)) + minDamage;

            defender.life -= damage;
            attacker.attackPotence -= 10; // Decrease attackPotence after the attack

            // Update the log container
            logContainer.innerHTML += `<p>${attacker.name} dealt ${damage} damage to ${defender.name}. ${defender.name} has ${defender.life} life left.</p>`;
            
            // Check if the defender's life is less than or equal to zero
            if (defender.life <= 0) {
                this.declareWinner(attacker, defender);
                return; // Exit the attack method
            }

            body.classList.toggle(attackStyle);
            
            // Change background every 1500 milliseconds during the attack
            const changeBackground = () => {
                body.classList.toggle(attackStyle);
                setTimeout(() => {
                    body.classList.toggle(attackStyle);
                }, 500); // Toggle back after 500ms
            };

            // Call changeBackground every 1500ms for a total of 3 times (4.5 seconds)
            const intervalId = setInterval(() => {
                changeBackground();
            }, 1500);

            // Stop changing the background after 4.5 seconds
            setTimeout(() => {
                clearInterval(intervalId);
                body.classList.remove(attackStyle); 
            }, 4500);
            
        } else {
            logContainer.innerHTML += `<p>${defender.name} blocked ${attacker.name}'s attack.</p>`;
        }

        // Ensure attackPotence does not go below a certain threshold
        if (attacker.attackPotence < attacker.attackDamageMin) {
            attacker.attackPotence = attacker.attackDamageMin; // Reset to minimum attack damage if it goes below
        }
    }

    declareWinner(winner, loser) {
        log(`${winner.name} is the winner!`);
        logContainer.innerHTML += `<p>${winner.name} is the winner!</p>`;
        clearInterval(this.battleInterval); 
    }

    round() {
        if (this.combatant1.life > 0 && this.combatant2.life > 0) {
            // Both combatants are alive, proceed with the attack
            let position = Math.floor(Math.random() * 2);
            (position === 1) ? this.attack(this.combatant1, this.combatant2) : this.attack(this.combatant2, this.combatant1);
        } else {
            // One or both combatants are dead, declare the winner
            if (this.combatant1.life <= 0 && this.combatant2.life <= 0) {
                log("It's a draw!");
                logContainer.innerHTML += `<p>It's a draw!</p>`;
            } else if (this.combatant1.life <= 0) {
                this.declareWinner(this.combatant2, this.combatant1);
            } else {
                this.declareWinner(this.combatant1, this.combatant2);
            }
        }
    }
    
    }


const battle1 = new Battle(WOLVERINE, DEADPOOL);

window.addEventListener('load', () => {
    battle1.startBattle();
});

/*
    One Possible Output: 
Wolverine dealt 37 damage to Deadpool. Deadpool has 63 life left.

Deadpool blocked Wolverine's attack.

Deadpool dealt 99 damage to Wolverine. Wolverine has 1 life left.

Deadpool dealt 28 damage to Wolverine. Wolverine has -27 life left.

Deadpool is the winner!

    Another possible Output:
Deadpool blocked Wolverine's attack.

Wolverine blocked Deadpool's attack.

Wolverine dealt 88 damage to Deadpool. Deadpool has 12 life left.

Wolverine dealt 62 damage to Deadpool. Deadpool has -50 life left.

Wolverine is the winner!    

*/


const styles = `
    body {
        background: #000;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: background .5s ease; 
    }

    .contrincants_wrapper {
        display: flex;
        justify-content
        justify-content: center;
        align-items: center;
    }

    .contrincant {
        width: 200px;
        height: 200px;
        border: 1px solid #fff outset;
        object-fit: cover;
        object-position: center center;
    }

    .wolv_attack{
        background: linear-gradient(to top, blue, red);
        background: -webkit-linear-gradient(to top, blue, red); /* For Safari */
        background: -moz-linear-gradient(to top, blue, red); /* For Firefox */
        background: -o-linear-gradient(to top, blue, red); /* For Opera */
        background: -ms-linear-gradient(to top, blue, red);
        background: #0000ff;
    }

    .dead_attack{
        background: linear-gradient(to bottom, green, yellow);
        background: -webkit-linear-gradient(to bottom, green, yellow); /* For Safari */
        background: -moz-linear-gradient(to bottom, green, yellow); /* For Firefox */
        background: -o-linear-gradient(to bottom, green, yellow); /* For Opera */
        background: -ms-linear-gradient(to bottom, green, yellow); /*
        background: #00ff00;
    }

    .log_container {
        background: rgba(0, 0, 0, 0.7); 
        padding: 10px; 
        border-radius: 5px; 
        max-height: 200px; 
        overflow-y: auto; 
        z-index: 1;
        border: 1px solid #fff;
    }

`;

//we use DataURI converted to work with image without files loading.

const deadpool_avatar = `url(data:image/jpeg;base64,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)`;

const wolverine_avatar = `url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQA/gMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAFBgQHAAIDAQj/xABFEAABAwMCAwUGBAQEBAQHAAABAgMEAAUREiEGMUETIlFhcQcUMoGRoSNCscEVUtHwJGKS4TNDgsJTcrLxFhc0RGOiw//EABoBAAIDAQEAAAAAAAAAAAAAAAQFAgMGAQD/xAAxEQACAgEEAQMBBwMFAQAAAAABAgADEQQSITFBEyJRBRQyYXGBobFCkfAjUsHR4ST/2gAMAwEAAhEDEQA/AKhbjrdUlDaSXFKCUjGxJ2H61dnDnAXDzkVa5ttbf7JAClqUrvEDc86ReELR7zemNae4zlwjHUcvvV1LAg8O61JwVAqOPrV617Rg+YK1mX48SvJHDPDcdmfNetrSY0ZKlBOVY7o36+O1JtpYsz9xtJet6ewfQWJHeJQHfyqznY9MGnXjlRicIiJqIdlrAVg8xkKV+w+dV5BaNrR79MGWHAQ1HJ3k+Z8EDx68hUNQmfaOJPT2EDd3LKRwbw52faOWxrB+HdW/3rm5wfw8Bk2tgZ5AFX9aFWfiNxGFynwHnEAtxHvyjpuPhGOQOaKpv8N9Wl51TDyuQe7uo+SuSvkaQXafV1ngkj845pv09nBAB/GArxw5aO3hwocJDb0l3mknutp3WefhgfOm9jgfhlm0mVLtLRUo9wlStk+POoPCcP8AjN6euAAKVK7Bk+DaT3iPVX6U0cZSg2huG1y06ceQ5/tT3R1FKVD8seYp1du60lOAOIkMcN8OsxJ1xmW1oRo6SrSSrHiBz/vNVM4QpalJQG0kkhA5JHhVr+0KQYdii2do4ckjt3/JA/qSB8jVUqGDgjfwqVpG7AnKQduTJVtchNOn3+P2zauWD8NMUD/4YkvCOY2CrZJOpOT5b0r9gvB0oUogZVpGdIrQZzsSPMULYm7yRCUs2+MiWzbuEuH3WxmC05j+YqB/Wip4H4bU0dNrbBxzSpWR96WuHLz7rHP8ScQ2ezzqCshzHUeNOsK9QnoxfD2EIR2qsg/D5ePypBqDqEf2scRqi1MuSBE9nhuySGYsFNua9+bWRLWknICDg9fznHyNNMngXhiFA1SbSyt7H8yuf1qZwjbdbz1zkshp19faLT/LthIPTupAHrXa5PJnTShSgmOykrXqOAEjc/30rU6an06gH77Mz11pewlOvETJfC1lSuJGRbW+3fParwpWUo30pAz+Y/YGiaOBuH2IqQ9bWnVgbuFR5n510sUxp69O3GSnQqS2Vs6xhSUA40jPIgAZHnTRJCXbd7w0nCSkKAI6VmPqmts9fahwI70tCog3DJMq/jPh+0Q7XBTboCESpcoISpJOdIyT18qjxuF4T7awiGlZR8eCTgeNEr1JD0mKpY7kGKvSnwcWogH/AEhX1FR2JS4kdw9sUdqNLigcAJ5nJ+laT6Wm2gGzkxN9Sc+qVTgD4gmVaLTGQVraQlCPiVqO2aDTG7a+UqhMBtpnd1xWcHyqdxHGmvwW5i2+xgBwNspXsXVEE6seGB1oJHYfcDKXArsCsqA5ZwNzj6VfY4LYA4lVSMFyxh632uG4louwh38aSScn/agN6iph3R9hCdKQoYT4DFO8IpchvOKaUVYAScHCQDsBSxxckqnNScZ1t6VHxUDv+tetTFYnKrN1h5gNDZcOlIAA3z4Dxo1brKiYn3h9fu0JI+M/E55gVLtXDEx6yN3xbaVwFOEKCVd/Y4yR4Z8PKol7updUY8fCW0gAn+lD1vWcnOcQmwOOJ5dn7MB2VugjCNi6pZKlHxNBSAd8AelZWGvMS3idUATEd1WdKVeShkUYkSYMplli32lJmu4GASrCv8ozvQb7VZXsy91ehKTDjBVwQT2iiMYBOxKvDyoXU2ipPUPiEULvbaTibweErRa7S2u9RxIlqxlJPU/lGPpXJjhiM9rdNtjNtqOUF1agn5b7+tNU9q2W5Zm3OS2+8znvOKwyzn/1HypRn8bPzpamrHb1TVp7ynVg7p8k9BSyq2+0Eqf1PX6Q0itcAgRx4LsjkYulxACnFhKFJOQpPiD4U7X9vWlqKPh2yPL+xWcLwDEhR23UnW2nOD0J3olKijtC8sZI+EVp3cepxM9VUfS57Mq/jtpkSmXJQC22m/wowO7iidyrwSPvypJuA92e96uIDs1wAoaI7rI/KSPLon5nnT7xKhLMx2Y4kLlLOW0q3DQHIkePgKQLilSyta1FS1HKlHmT1oi2rKboLRf/AKhQxWnIeRKU444pa1HX2hPx/wCap1tnT5MhqE3hwvnQMjx8vrXZtlD4MZ3ugnLbh/Io/sev19W32a8MOu3hbzzOlTR7JGf5jzP0/WgVQk/hGTOMZ8y0eC7Q3arR2gThDbYQ2PIc/qaDrSbletat0JPXwB/qab76REtiIzG2RpGOmBSRfZSrDwvOnISfeXQGmABkqUrYAD1q4NwWlJXGElX8eqkXa9y7g2SqOF9g0hPPQjIzjzJJ+dLrn+ECUuYMoDGOfZD91fpy57BzhuMsxgySlUvSEujIPY7cvNXj0HnS9erC9HHvUYKdjr5gc0H+lVNX/UvMtS0D2niB48h2M6HmHFJcHXPP1pms7Fmvr5TKbUxJV8XZHGT/ADAdfSlTlzG9dIxUmQ0UPFpYUNLn8nnQli5HBwYUj7Tz1LZtHD8i0KaVpbuFvKgQ4npv1FGbhAjTL5FjwG0owQ64lIwnf4R9d/lQezXKbboOu46VpQjPvDGSlfkU9FfUU7cHwFIjruUwYfeUVqH8pxyHkBhI9KA0VD2aj1LOl/eEatxXUEXsyXcHEWq2oYaxqxjGPiNJd1lJjtxIy9OZ74DpVy7IHKgf/MRj0zRy4vquNx0BQSgHBUTgDHM58qr7iqcpxLdxUlbKFzWQyhXRhO6FEdM7nx3pzqn217fJ4i7TIGfPgRkuiFx3FIlslmGmSUrcWR3tS9vTpv503PXBEmxIUhITqOE48P7FV/cuIEXNm2WM6lrkuCS6TnCW85A/SiXFV2Fq4efdaxqCeyZSORcVsD8tz8qyVunawopHJP7R8CpG49CJtzfS37w52hKXJOrxykKAAHj1pz4Q4PkXRAm3FBbjp+BCv36Up2NVuhx27hdJbCG2SG4za91KWB3l6ee3IfOiF49qrotyoNjbWkY09u6nAGfBPP61rlIRQvxM+VLsSRI3tPnMOX2DZ4qgWoZ1vBH8x6fIZ+tDbY+Jl0kPpQlLaO42MbDlSkXFvP6tSu0UclSlcz1JNM1ncYixUtocSVHfnXa2y2TOXJhMCN1zmJMSLFbShKQjLgTtqWetI/F4KO6UnSoBxB88YP8AflRxpxLq8heo56VE4oQDCakEZ93cSsjHTIyP0+lE2+6skQOn2WqDH+xobbsEViOtpyOGgAEKBAqruN7ImzXf8BBEV9Opo5zpP5h9d/nVjRkwoDaX0R3kMr7xWyfw/mKh8QSOFrrDMW43cx0jCk91JWg+W/7VkNNY1V5IBKnuazUIr1AHuVGa3baceWEMtqcWeSEJyT8qZ51r4ZiupMG6+/NEb6hpWk+B6H1FcF8QMQmy1Z46Ws7FzG5880/qCuocnAiR2ZTtAnJnh1yOA5dliOBv2QUNfz8KkwuIFWt1TVjSdb47PCDjUo7D1NAZEqXPeJWXHVk8gCam2+13FiUxKCOwLK0uJLu24OalYAylQvE9XlWDM3MY4/CN2vK0PX2YplsfCwjBKflyH3qwODOFIdojuloLWXDutfxK/wBvKgfCcq73+epUhtDENGUJSg7uK8c+A3/sVaEaOEthI2SBttWc1H2iyz0M4H4dCM2NSJuXknzCVtTiOCQdhgZr24vFqG4UjC9J0+tclvqh29rVutQHPzoHxPcz7jhB/F+LSDvgbk/KtTWhZ4ntsFdZzEy/OZQvUcnfOfGk2YAcij9zmC4IUpBAeRkqQPzp/mHn4j50tOuhS8femVzAJtiXSqWtLzSPF7RWMZJ2FXtwNaRCgM6wO0bbAKupJ51VnBsMS7qzqTlDf4is/arxtqA1BQeWregrgFUARlpyXck9CR7gz7w7uOWw9arP2qz/AHdyNboqQHmUFxTp37PVsMDocZ38DVsuONpaUrblVE8ZSRNusmQrfUo4Pl0rlKbwc9CS1NgqZQOzEKNINvlhZ+BWQv8ArT1Y5Ud1RiyyQy9yXj4D0PpSDcsa6n2m+RIkVpmRqQpAxr086hS+xsSd9e9QQIbu/CzMmWtCMMu5+NONJ8zS5P4XuMJZStKVJ/mHhTNHu0aWhOJIVtjBQdxWzvbsqIQJD8YjU2sJKgnyqyxK2GRKq7LUODCXBjU24Bq3PIStppaXFOdVH8o+2fkKtG9vJttuEdojONIIod7PbB/DYJkSUgPK77m2wWRyHoMCuV6Ls+4hsbJ1aR/WqaalTKj8/wBYTbYW9x88RfuS2mbWpl9ZHvuUK08+yG7mPUd35mo3GzEGXEYeDiUx3WTGLvxBCighClfMiljiO9ok8SOutBCIsApaZklWwAJCyfNRyMDngVvAmJmW2RDWotxH+1EZBOVIRpJ1nw3Bx4ZpZrVZ7lcHgQ7ShVr2+TIMqWxF4gg3FIUlkRg05q/5biTuk/SoXF1/N9W23GSv3dglRx1Vjn9K8ukdmXHiyVLhqf0aZLnbaSFA4yQOZI/SosaBJgrjrUjS3JcGhKtlrRkblPTPPHhU66kLBj2OJKyx1UicYrTM5BHZrW8OehQBx5eIrwxrYwvRLemtg8x2YpitdltyHgue0olZOCdt/Khl6gMLX+A6ltQPwuNHP+oUwNZC7jFq2qzbRN2JHCsZGzD7ywNlOlf6YArvCuEWQsiJBfWfHswEgeZzSyy6qO6SENqUOqk5qU7eZi29CnEoQOiE6a4LQJJqcxkXMDKd20JOeQVk58MCuzyFPw1oe3U40fkahxbcYUWGxLCjcpoEhaVf/bx/yDH8yzlR8EpHiaMOI0hAPLNXVEuCYPaBWwHmAeGeI71Y20FtlcmCcgtqTqG22Aflyp5gJ4H4waPbW9MWYdlFs9k4k0O9nLyW4s6JpyuNLUO9tqSd8fY/WmW93e12SbEcm25r3d7uh8oBLS+eFf30rLax8XFEUhvkGaCtAalLHIMDSfY5D7XXGvUhDBGyVtJUry3GNqSLraYHDsxUS6IXIfAyAjZK09CP72q5lXtmQ0golNdmod3QcUge0Wyv3hMedbGFvOMgocCRjUk9R47/AK1H6brdQLNt54/KRv0ea8iJx4mkstlq2R2YKPFtA1/WhT0yXJcBckOuLJ/MrrWsuLIhPdjLYWw7jOlwY2qdZLa5KkocWnDaDn/zVolLOcAxYQqAx34GuTtgltOLC3YjgCZCBupP+dI8RzI6jPlVzOup7NsIVqSoagpPIg1UkVCbdbXp6sdpgtxweiiN1fIE/PFH/Z9fDKgOW59RU5Dx2ZVk5bOcfTl9KXfWqWopNlI9x7ndHcbW2nrxHe/Pj3llkHkc/QZ/pVbceXZTV0jNtrUlTKAoEHko06XR8uXtQz8CCT8zj9BQK3W2JxAid79GLjL0hYC88tHdGCNxyJphqdWujqFjSlKPtFjL4lfzJiXUmdE7i0Y7ZCfyH+YDwP2oc4+l/wDHbwlWcuoB5HxHkf76UzTPZ3eod+jot0hDsRw7ynB/w0dQ4nrtttz8qI3PgO02mC/KYcmuyAPwwXQBqOwTgDlkgb5/eqD9VodlCnJPxL00RVTxwJO9nMQqjpewdchYCc/yg4qzrlLEUMsIAACcn0pf4Gt6IxabbCdEdoA7cjywPLnWtzmGTenEJOUhWj5CmDe58fEDTKV5+TJHE11MCxvOpXpdVhCMeKqp+8yA+hT7aQFDZ1sHOk+I8j9j92v2i3dtuVBt5UBsXF+p2T+9IN4U+ysSY/e0jvDHP18RVm8JXgSr0zZeGaLs5zWvFS+Hbz/CJZfMOPLQpOl1p1I3/wAyT0NQZWlz8ZkYaVzSOaFeB8vA1FFAnuM5cXDPFXDMpYMtBjkfkfTp+42P98qc2ptr4hlsQ7Uw0qKwQ48tCcDI+EZxvv8ApVA2tIynKk8/A19Ceze1iDakFxADih2ru3JR5D5Cr1IK5MGcEPtEZ3GhHiBlPPG+BSbxViBZZj4dDLridCHOqc8yB1OM07hxt5SgpWBVX+06Uh+UiM2vKWcjT5nrU6ELnEr1VgqXdKmlNlxKmmYzSYjOMJcOSnzJyMqPj9Nq7xHESGkwWXvdgO6EvtFSHOhSVpJx866NIacuAjvt9qh8dkEjY6j8O/riodkdftt0U62C4yw6Q+0djpHXT5eNAXcEiMqGyBHm22FyXJYjyWmtSSgMpabSlvKuayATqKRkjJxmpvG1ptsBoJtzYRJ1ICNRypwgjJ+YyCac+FolvXGQ8wnvpRkeAqJIhaX5cmTpSkt6ELV+RO5UfTYfSs39sf1wSevHzGPpKwKyq47gVIJddQVKOUpUrfH0otc4EJ8JCVqUCkZyPLxoTDMU3aS92SX2t0o1pOFDJ3xXeY/GhtlzWptBOEIB1HPgkftW2qYGvLTMXIVt2oYGncOpB1xnN87gjauvCvDi5VyS9PS4i3tKwp9CdSdYxhP9a43afLivoYkRZEfXhRDqdKlI/wAvr49Kufhe625+wxkWpLaIWkBLPMJPnnfNLdVYqj2CNNHS7Nh+4lcRsra4rtz8qQh9D8QtpcScghCtvMY19c1l4jll7TjCdIKf61L9o9vZaVarjEGlXvCm1JGdPeSTy9UAVz94TcLWlt0Dtm091R548KO+nPvogH1RNl+Ys2S5sWbieaia8lpl8JKSrlnbn9TVg3GDGv8AaghxoSmF4OG1gFXUd7PPz86rmPeoll4kkuz4632nGmwUoCSQfHemmN7TbDGbShqBNSnHIBAx9KQfUaLWv31LzHWiuUUBXML2Oxv22MWbHw2p8oWSTMnJGhX3xsfAVBurfGUyUI7qrdaIhJ1PIdDqkD7ZP0oFM9q0lTr3ultAaWQcuPaSdgNwB+9Ls/jS7XEpQ2GmlK2HZJKlKNQTTXk5YDPyeZI3J1u4+BGriFixxIXYFaZ00kFTzqgpaiNyc9BtyoPw0p+aO3eSEtrIDbYHIVpZOCbxMbcuMlspWkFSWlnC3D1B88Z28aKRXUsNAtp0lIwARjB8KcfSwgJUNkjuKvqZsKg7cZm3EcnLqYrZBaYGnbqep+tKjl/kW2VqtSwl0JKVOeRxt9hXt/uC0EtNqwpW6vKl1Qq7UOHJU9SGmr2KCJ9ByZaW5FymLIw0Duf8qSf1pB9m/EM+A8r3pTi4by9bgG5QSckgHp6b0x3h5Q4UnEq70r8MHr3yB+5oJZmUsyEoQkBI2A8anbpU1K+m/Up+0NQCy9y2mpbb7KXGihbagMLSdsY6f70t8QPreuECA0rSlSlPv7fElIwkeXeIP/TUCXPVapRRE0lHNxonZR8vA1pZHjdp8icArStYZbSeYSn/AHKqRaP6G2l1oPajqMG19dumYDhusSwLPot1ikTVDGUlWT5cqVLK4t6W4+sg47xJ8Sf/AHpg43f/AIbw8xDbOC6oJI8gMmlWK97nY5UofEUKKfXGB960CHOXMBcdIIhXVa+JuK7w00f+DHcLJ8NBSB+9Q7C//EI6mHhl5B0qBprYsaLNeZ8xteyYSI+w+JxRyfn3QfnS5dbI7wy1DuatWZMpaHQrokgFH0IV9aV6fWo12CeDGN+lIpyOxAV5tK7e4p5lOWV/Gg0HYbbW+lC1lCDzUBmrEnrQuIl/s+2iuDCwPynrSXe7aiN/iYp1RVdRvp/2o+6vByIHTZkbWjTwhw6HL2grc7VhpIcUNON+g+ufpV8HTarQhKwQpW68c8+FI3sosa0QWHZbeHVAPO5zkfyp+Qx880e4pnqkXH3ZpWyNj5mpgDIWV5Iy00m3n3K3PTFkd0YQD+ZR5VV9yuZuAIeVl7mhRPxeR/ap3tMvHuz0O1NL2bR2rgHnsM/eq+kTdQ5n5VM3hAQJUNMXIZvE8nyFayQShQVnOe8Ff1olcXveY7PEsZRTO7cNygnGjX4kdNQ6UEfd9576hl0DBP8AP5+oqVYZrMeSY1wBXbpQDUpAPIflWPNJ3+tAWc8xlWce2W7wHxI3KjtkNhlwJwWvAeXiKY78nt0xghRLbru+PAAkj0OMfOq4slrcscv3WQ4X44OqPJSd0hXL1B5Y86siC+2uEWlkKVjIV+9ZXWoqW716jqsMVDHuVxIiFi5S0r+FLmR02O9OPBHCMMvNXq7I7WUpOqOyvGlhOeeOqj1PnQ2Zb2rneUlLuIraQiTp/OQThIP6nyxTQ864GtadWAO6lAGemw/X5U/Ot36dEHfmLU0LC57D56nPjW1Wi/xVR5Ucr07trQQkoOOaT+3XwqrbEqXwdxAiHKc7S2TiEhxXRXT0NGOIuMZFrWWTamSkHV+JMCnPpg4+RqILlbOLYEhlKVNyw2DoWd0qG4Uk+teQMB7ujLfb/SfcIe44WV8NrI7xjyGlj01YP2JoBAQ62h5w4U0TqGDunPr51OQ65ceDpSXQO193UFjwUj/2ofCfCrco5+JKcfWmH08gAiLvqo3MrDzBloYs1zvVyg3klLjugMrSd0EJ3waPQPZvGjKcXPb/AIjGKgpmQ24oEJ8FJB50mXG3LNiavKAQpUtwLVj8qlEJP1T96mcPcfXezLGt1UhoDGlRGceHnS3VJfYWehv0/wCoZSUrCq45EsGFwjYQpY/hMRRSditGQR471NFqsdsc96aYt0R5A2dQ2lJHzpcd9o9imalSrZpcVzUnWCfXSRQWTxJwk6oq/gTa1E/nSs5+ppatGoY/6gb/AD9YZ61ePaBDs/iyG3NNvtijLluuBLZSSUpyBuceHUCjfF/C2ix/xmGlQktJ1ykfzt8yceKfuM+VQfZpJtt1mKcgcOR4jaB/9UltIJPgDjP3qx7nK92ZKNidJGMZrwuTS25UYx+8ou3XAI3OZ8sXBztpzqknu6ilO/QVGo3xna0WjiGTHYTojq/EZT0Sk9B6Gghp8rixQw6MAZNvtMt3iNfZ2i3sj87usjyAJqFa3gzIQpe4SrO9bcYOrTPgsMt6+zZUTlWANwN/lmhjbctTPaaWlA9Erwr5A86Zq3ui2xcrzJl2uB0SJLnxYKtqe/Z7bwlUFo5PZt61+Zxn9TVYqKJk6HC7wU6+nWlSSCEpyo8/THzq7uB2ghiRKWMHYA+Q3Ned+CZ6qoBgIA9o0wv3hqKk5THb3HmaG3MoZjWuEvAS9ISpzJwNCAVn7pSPnUZ93+J8QOvHJDr2R6D/AGoB7Q/eLnfrfaYSyHSjmDjTqOT+iaHuAXTnJxxCKffeIxRpSbvc3nWwDb4S0qfI5KVyA8zjJPgB50J9qUr33hSC8RpDqy6lPgMgJx8s114hda4e4cas9u5tJy4oc3FnmSfEn9Kh+07Sf4LZknOexaJHTx/UVlqEBuRl6yf7CPbmJUg94i5wrcu1ZXCkHOBt5jof2qZbrO47xCzHbJ9xd/Efb6YHh4ZOKVZDT9jvbsZWoORnihW2Mjp9RVu+zaCq5vomKTlLxARn/wANJyT8zk+mK1Vbh15iKxGR8jzLFtyU2fh9Uhey1IKzn7CkmK+CqTcJSjpQC4s/ej/HlwH4UBs8zkgeA/v7GlG6XCJbVWi3TFhPvr4177YG+/lq0j517OFLmd27mCCVNxNImSb/AD3rghTclTx1Nq5pHJI/04oZk1ZXtViNtNNSUtI1rcBKykahtyzSbcLCqHZIFyQtTiJKQpadP/Dzyx40CtocZh9lJrO0QOMg5B36VmM8/pXtZU5VGeFxpLjQ2I7sNp8so0JWpwgkYxvtRyycXXC66oERlLCtOVP69XZp5befhVeDJISkEqPJI5n0FN3DXDnFDrLjtutf4ThBLjqsbDoE6gfHnQ76aph1CE1Dg98RzbkRbH2pW+lqA2kEuLVuHDzA8T1rk9drzf2349iYVGaDeVPvbOrHLuDPdJ6US4X4MTciJt8SZamVFtphxrQ2349zGPHc5pvas8OzQXFFaW2irYLIGOQSkfYCvCkA58yb6kkbR1Kgf4DYagx57r76m1PIL/bDCuzUcE56HNLfD0lFv4pZU2Sprt1Mgk80kkA/pVn8WXZmd7MZMxLamirtYq21EZStLoTVW3NmBCZthhP9tL7y5C0kaRuNI+yjRBGRBVOGBljW+Mptu8RSpRSl1YQkgAd5AO31pUivFFsyT8LWT8hTnbndct/tc6n2W1BI8BlJP3FI0hPu0OYyf+UpxHyBIqOkbDGWa1QyqY2Q7UZfCRtYHecjAAn+bGR96qyVEkw5BjTI7jEgf8paSFH0HUelNnDXHc23Ftia2qU1kJSUDDnljxp8ie0DhqUpCJxLLyNkqeZIWkn150tLajTMx2bgfiEuKrlBU4IlWWzhG/XRaRHtj6UE/wDEfT2afvvT3w57NITTiXr5JEnBz2LZ0I28T1/SmW/RuIJsMOWq8MNtrTqQFxsEjp6fSk1jhriedckIvtyWYOfxEsSCNQHTAAwKpbVveh94T8u/3nVo29KT/EuC1sQokRLcBptthOwDYAG23+1QLw8V5wrfGPKuMV0RYqGUEhCRhKc7AeAqHJd1k+FZ5FbfycjMLrow2TKp9pFuuLc1udJUl2Kr8NtSU40dcHx9aSzVy8Zw1XLh2c0hOSy32ySBzUnfA+4+dU1sd61+gt9SkDyIu1deyyNntDmuniRSG3VJDcdAIBxvuf3FRYfEIZYCXWypzOCrbFR+Mlhzie5EKyA4lGfRI/eg1MjYQ5xAPTVlAMsXhx83C5CTpIS0zgDzUf6D71brrv8ACuB33M6XFN6R5lRAH61VHs1hKVb2z+aQ99s4FWJx/J7K3wYCTgKVrPoNh+tEZLIM+YOMIxMXeHWsvlWN0j9aBmShniW531aEuJjZaQkqwfAlPiRp5Uz21AiwXH1EJBBXk9AKrCa7KnWoIbjuN9ortCpQzkHc8t/tXL0V1KN8TtDsjArMRLd4n4rhMKUvsFyEnRy2BySfpUri+V73xxEGvUll1vSc9NQP6AVrwGkRru/OlDSpiOsJ1D4lHqPQZ+tDLY7/ABDi5l4jIVIKvpmk7JtsPHCrGwYuuT2TLT9pMRNxtEZhpLfaSJLaVOADUoevkBTlwbDbt1qcfQgIShIbbHTAH9/Sk9Kl3G9tR2jqZhJGO7sHVjlt4JI/1048TyU2mxIhtnvlOnHmev61f9LpNelAPZ/iCaywNefhf5io44bne3HicoSru58B/U7/ADqsOM5arzxA+SSGk/hRFHYKCeePU5P0qwJ8pNn4dekuKSh10dmjJxgq2H9aU5cJqdDDY7pSkaFp8ByIpm6bhtHiBCzYdx8yf2z3FPAuXCFzIiS28OupPI/MCly7Sy7wjalsqAT2SWT3uqdjt/fOpvD1yXZZzkiQnDSwGZyAnkOjo8vGhvEENVplzLa6QYsgiTFdG6c+A/T6Ur2bH2+OxG/qb03DvowFEivzJCI0Rpbry8hCE8zgEn7A02cL8EI4gtbjiZa2JneCG1JGMjof3pThyH4spqREdU282oFtaTuDTnaOKLzZJyZl5grTDdUFOFtATg89Y3Iz4jrVpgwlk2DhG3O26JDkwWGZTKRh1oYWhYG5Ch15+tN9qhs2xCYodCihO+tQCiPGq54w4jktP2y9WKW0AFdnIb20KUoZRrHNIPLPQkc6r3i5q63e5ru8rtVplN9xRGNKBnuHHUHbzr2J2XRxh7R+HuH3OwDqZsnSSWoqkrKD4KI5Heqv9ol7m3kJntvEMobjSozI/wCWnBO+PNWf+iq/KOzyjGCOmKboL8OVw7bm3dfbsurhualfEhYUpH/9Ejw2ronpG4ovD7sc29lX+DlyE3Eb8ypAGPTOT6mmC98L2+x8Iq96dQZMlKHWQlRUtSx8RIHIYwPD60lzo60WhtLmA9b5K4ru3NKsrQfqlwfSrq/gsBnhBhpMtMiMqAhCQpZJCu8Svwxy28q4Z6DS3GTb7TPtzodadGlw9QrG4I9RSfdY6F3yXEeB7J6Un/SsJJ/U0YhJbHD9vcaGShhGpYGSdjuDjGNvuKDcQuOO3pgNuNtOOtsrC14IScrAPP8Ay/eqEPubELtGUGfkQ1buHoFtmB+BAW64nqqSnH3FE0oubcszYvDERUo40vPSEqV9TnFJdxgcXx5KWkQnZBcGpt2DqWhwDfbCuflQiWeJkqKJLV4ZztoU06Mn6eNBije2S4P+fnLTegGAuP7SzJ0vjuSApLFtZUrfvySo/pRmIhUWK0ibJQ5I05ccyACrrjypC4b9m17uqRJusqREQrcI7QqXjz329KfbZ7M+HoidT8QSlZ3W+ckn50u1Z049oPI/2j/nMnXcy8n+f/Jo7cre1sqfFT5F5P8AWp0JtqSyX0KS430KTkUbi2e3QkgRIUdkDl2bYFey0gJIwKVWOvSgy0andxAj7SAnSEgCvn3iCH/DLxNiaNKW3lBA/wAp3T9q+hZB51UXtQiBm+MSkoz27OD6pP8AvTf6Nbi0p8ynWJuQGK14c7a7z3P55Lp//Y1EPlW+7z3d5uLJ+ppqatDLUWMgoSXHXUN6hzwVDUfpmtOqFySIoawIBLF9n8EMMxEadmmQT6kf71K43d7e9Ntf+C0E/WiPCbelCl+JH2oLdMyb2+odXAn6UbjkCBDomacRLLHDMltJwpxtLKT4FZCf3oTabM27r7V4IQ23lTiwQnPgKI8WOfg29jbvyNZB8EpJ/UpoUtwlO/TlV9ag5JgeodgQo6g24Wxl7X2aiD+ZQOx+vOl+3xv4RfmVOg6EpURjfptj9KZnnemknzGK4xY6bldobWnUlpReWSOQGwHzJH0oe+lH4helusTkywvZ/blAtvSB+IMvOq8Vq6f34V5xTKNyvQZT8DXM+Z/oMUeh6bXYVvrHeWNR/Yf340qQxpL8x8jmVKV0HUn7VxVGePEsJOPz5iN7VLhrkQ7W2ruMp7V4D+YjCR9Mn5ila0Xh23kIVlbOeWd0+lEOMEy3Vpmzoqozr0hfxc1pISps/wCjA+VLe/Tn6UH6u5iywv0gFCtHhRZmoEphSFahjPQjwNSWYLd5ta7M8T2zCSq3ur6D+Q+n6UkW+c7Bd1NnKD8aDyNNMSch8tyIq8LQoKG+ClX9/WpPi0fjI1k0N+ET32HI7y2JCNDiFYUk9KbeHeHU8QW0PuXN4OJdDagtZKWhnnv5UV4ltTd+gpuMNGJqdloSPiIG4z+lQ7sjhuy2mzO25+Y4+8tL8hkk6VBJAUFJO2RuB54odXzx5hT17eR1I3ENrctSH4Wt5S4ONDpbKRJj5HyOhRHpmmyyXuFdrAbY4lsyT329XNSgN0/Mb+oo005ZuJ4Vthx5jIZjv9oHkrC17ghSFA7jUDjHnVW8Y2KVwdxGuF2hS2D2kVwHcp6fMVOVQXeQ2JjhR8Oa2siDIVLhD45DJ7HHMuoOtOPXCk/9Vb3lovttXZpI7GUrS7/+N7GVJ8sjvDxFQIklcKUzKbJC2VhYx1wc4rs9GKW2qd2ymQSbnbw+nAzqeZIOw8SAcD/NVmNNW4+z+3M2xfaR1wFKeUk5KlAcj4EHIoNw/wAMSXb3Gke6k2ZqT72zICk6SFpJU3zz1A2H5RTRd4q3kNsx+zZDzv4qUJAHZ4JXy67DfzFRZgBJKpY4EWbagN8OsRiCOxYQgnG+dIOfvSZxqUrbiqAH4iSCEnYaVZx8tdWNck/4d1fRStQSkEbYA/akO829y4uW1hH4YWpwKUpJxnu9PlQdLDO6MNQh2hYK4ZvV9iy2I1pfcVk40cwPHV5Cr9skqW5HAmYUrSNZA21dceVI/B3DzFuTpjpKlk991QGVHz8KfYqNKUoR86QfVtQljYQfrLa6jXX7uz+0NxglQBwAPSvX1pJ7nw1yQVBsDNcHngPWoLrUq0+wDmBlCW4nrjgSD40NlPqXnbat3VlWT4VBkL0jJPypcGaw5MLqrkZ886r/ANqEQvwIjzZ76HtO3gQT/wBtOkl9SshP+kUNlwhMQEvpJAOdh1plo81WB5fam6siVRw3CDiw+vGEjbxpigupl8QRWNWQ0C5geQ0j/wBX2ocXBb7aA2O9p2xzJohwVBU1dHXXiFPFsFR8Mnl9q3K+FEy785cy2rAjs4ZPmTQVlAXNLn8zhV96OxCGrYtXgkmhsJsahnGQPvV57laD2xZ4vUXLpFY2wiOtSuvxKA/7aELShI2HqRU3iF0K4hlnOyG22wPA4JP61AAJ7yth51JDxB7F92ZotelslSu7+vlR/wBnluMtbkotlBlO4APRtOQPvqPzFLryVrACE5cUQhsY5FRwP78qtnhG3Nw4acDAbQEJ+m9RY4OZYgyMTOKXzoZgtcjuoDy2/v0pT4pfMKze7so1rfUGgjVgqTzV9gaYJyzJujjvLoPQUq3q4NquzrBbS4I7ASkn8q17/ZIT/qqIXIx8yxzt90Bccvf/ABI/Zo9uB1vr0hOMdngYIPmKERuBbg9fJMF1JZiRjl2SrGMeA8zj9+tMNhYbVxPFdXjdK+fLIwc48dsfIVM9od7ujSREt0dXZLwVupGwzWdsNmnuGlr6x3HVRW+oXNK1vseJEuj7EBxS2EHAKvGosWS5FdDjR3HMdD61qtGXlpDgcwT3x1865+lMVyAPmCtgk/EsDhq9Np1acll0aVpP5FVw45tvvEWPLhx1a2dfbpAwQCRj1O1JsWS7FdDjKsEcweRHnVqcPTIc7h7t2VFx8EofbX+QAZHL16c6jbx7xLaPcPTbrxK/4U4kk8N3ESo47RtXdWjOD6g9DVwWG9Wfi+yqXdoCHC6lbSycKW18+nrVVcWWAQlqlQsFnOVgH4T0PpXCx3aK1JCpC3oTxGn3iMvH1HI9OYrwYMMyLIVODLDt/s/hxYEmMb0zKYkIUlcdxBSDhWW1BYzhSfHB5mvf/lXw63AWr324S5GnZWpKUBXkB09a34cuCUwwn+J+8NrcKx2oQo7nkMAdaNpmhkvdpKeeDnwo7qQ2D0GBn71W1yr3LF0zt1Ozl3aRZmWLI21LdCAzHixlhSUqGxCiOSR1Pl41IWHmmQ04WnJryQHFN5DaAOYHlud+tQbZAaiNYjMx7ZEUe+pCPxF58f8Ac/KjUhNttbC1ofLjqgSVFWcacZH36UPba1gwo4hFVS0t7uTFTiZ4R0OJUBpSNjzH08aS47naybcEBOpc1SkkklRGkjfPIUx8SLVc31pYWkJx8ZGOWfrzI22/YNw25bpd2BLyGvcm9Lba1ZLiid1g45dB8/GuAbKSZY5L2ASxLa0mOyEJ3J5misdwJI3oPHcBGQoEeIqWhZrKWKS2TDWXMMe9AI2O9RlOZHPPnUTtDXKRI0DGf96r9PJlIq54nR+TpSdJ+dDVuqcJwcDqTXN15JOpxYSkeJ2rRtUiUsNwGSc/8xQ2+Q6+pwPWjKqQJbxWJ7JdjwWC9JcS2gfmUefp4n0pem3O9TVFVrYahxwrCXZKdS3PRPQeu/lTUuzIaw/MUXX+mT8Pp4fKoMggKwkDbzomvUIpwgyfxlePU8yrB+I8nXvoRqA89hTNwoM3CZ5KbA9MV7WVta/vTMWdSw3SRaFY/wAv61GidflWVlXt2ZWnUr2eSu/XXVv/AIj/ALU1xbKnHw2pR0eAwKysrydSqzuEbS0l3iGA2sqKEhxwDP5gAAfuattgBu0Eo2OgGsrKjZJ0dReAH4h67VWzjy1y5Tijlbkl0qPorSPskVlZXR2JK7qbxnVt3iDoOMFZ+xpYuvEt0elSmFPJCO0UjZAzjlzr2spVqAPtRP4CMdKf/mH5wIlwtoW0kDCyMnG/LxrXoPMA1lZUxOGZRrg+dIh3+GlleESHgy6g8lJO313rKyuP90ydX3xGyYP8Q4jP4a3OzLfQDf8ApSJI0w7irsm0KSFgaFjIINe1lV1S7UdiP8S129tSFIhMpKgFHSCnfB8D5U1W2KyyAppASSOfP9aysoO6H09Ty4ynUoYCVY7RSkkjwxQeVJdU/oz3NIUU+Jr2srtf3ZGz70jXUh1VrhlKQ1JaU84QO9lJT3QeicnOKP2/h22XBoqlRkKKN07AY2z4VlZQutdlxtOJ5OiYQbhMQQEMJOP8xzUkHasrKSuYaOpsCajyzlQFZWVFO5EdzpAhMPuBTqdWPGjraUsNFTSUp8gK8rK6pO4/lA9QfdAlzkOaM55nFDSgE71lZUqOUBhFX3J//9k=)`

// Create a <style> element and append the styles
let styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);

// Create the combatants' wrapper
let div_wrapper = document.createElement('div');
div_wrapper.classList.add('contrincants_wrapper');

// Create the first combatant (Wolverine)
let div1 = document.createElement('div');
div1.classList.add('contrincant');
div1.style.setProperty('background', wolverine_avatar);
div1.style.backgroundSize = 'cover'; // Ensure the background covers the div
div_wrapper.appendChild(div1);

// Create the second combatant (Deadpool)
let div2 = document.createElement('div');
div2.classList.add('contrincant');
div2.style.setProperty('background', deadpool_avatar);
div2.style.backgroundSize = 'cover'; 
div_wrapper.appendChild(div2);

// Create the log container
let logContainer = document.createElement('div');
logContainer.classList.add('log_container');
logContainer.style.color = '#fff';
logContainer.style.marginTop = '20px'; 
logContainer.style.width = '100%'; 
logContainer.style.textAlign = 'center'; 
div_wrapper.appendChild(logContainer);


// Append the wrapper to the body
document.body.appendChild(div_wrapper);
