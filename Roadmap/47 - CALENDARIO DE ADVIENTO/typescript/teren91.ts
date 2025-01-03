/*
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
 */
import * as promptSync from "prompt-sync";

const prompt = promptSync();


function calendario() {
    var dia: number = 0;
    var calendario: string = "";
    var opcion: string | null = "";
    var diaElegido: number = 0;
    var diasRegalos: number[] = [];

    while(opcion != "salir")
    {
        opcion = prompt("¿Qué día quieres descubrir? (1-24). Escribe 'salir' para salir del programa: ");
        
        if(opcion == null)
        {
            console.log("No has introducido ninguna opción, por favor intentalo de nuevo.");
            continue;
        }
        if(opcion == "salir")
        {
            console.log("Hasta pronto!");
            break;
        }

        diaElegido = parseInt(opcion);

        if(isNaN(diaElegido)){ 
            console.log("No has introducido ninguna opción, por favor intentalo de nuevo.");
            continue;
        }

        if(diaElegido < 1 || diaElegido > 24){
            console.log("El día no es correcto, por favor intentalo de nuevo.");
            continue;
        }

        if(diasRegalos.includes(diaElegido)){
            console.log("Ya has descubierto ese día, por favor intentalo de nuevo.");
            continue;
        }

        diasRegalos.push(diaElegido);

        console.log("Enhorabuena!! Has descubierto el día " + diaElegido);

        dia = 0;
        calendario = "";
        for (let i = 0; i < 4; i++) {      
            //Inicio del calendario
            for(let j = 0; j < 6; j++) {
                calendario += "".repeat(j) + "*".repeat(4) + " ";
            }
    
            calendario += "\n";
            for(let j = 0; j < 6; j++) {
                dia++;
                if(diasRegalos.includes(dia))
                {                    
                    calendario += "**** ";                         
                }else
                {
                    if(dia < 10)
                    {
                        calendario += "*" + "".padStart(1, "0") + dia + "* " ;     
                    }
                    else{
                        calendario += "*" + dia + "* "; 
                    }
                }            
            }
            calendario += "\n"
        }
        //Cierre del calendario
        for(let j = 0; j < 6; j++) {
            calendario += "".repeat(j) + "*".repeat(4) + " ";
        }

        calendario += "\n";
        console.log(calendario);
    }
}

calendario();
