// "Los clientes no deben ser forzados a depender de interfaces que no utilizan."
// En JavaScript, al no tener interfaces nativas, nos referimos a un contrato implícito o a una clase base abstracta}


class ControGeneral {
    tvOn(){console.log("Encendiendo la TV")}
    tvOff(){console.log("Apagando la TV")}
    tvSubirVolume(){ console.log("Subiendo vol")}
    tvBajarVolume(){console.log("Bajando vol") }
    tvCanalMas(){console.log("Subiendo de Canal")}
    tvCanalMenos(){ console.log("Bajando de Canal")}
    airOn(){console.log("Prendiendo el Aire Acondicionado")}
    airOff(){console.log("Apagando el Aire Acondicionado")}
    airSubirTem(){console.log("Subiendo la temperatura")}
    airBajarTem(){console.log("Bajando la temperatura") }
    luzOn(){console.log("Luz Encendia")}
    luzOff(){console.log("Luz Apagada")}
    luzTenue(){console.log("Atenuar Luz")}
    
}

const controlGeneral = new ControGeneral() 
controlGeneral.airOn()
controlGeneral.tvBajarVolume()

class Tv extends ControGeneral{
    prender(){console.log("encender la tele")}
    apagar(){console.log("apagar la tele")}
    volMas(){console.log("Subir Volimen")}
    volMenos(){console.log("Bajar Volumen")}
}
class Air extends ControGeneral{
    prender(){console.log("prender Aire acondicionado")}
    apagar(){console.log("apagar Aire acondicionado")}
    subir(){console.log("subir temperatura")}
    bajar(){console.log("bajar temperatura")}
}

class Luz extends ControGeneral{
    prender(){console.log("prender luz")}
    apagar(){console.log("apagar luz")}
}

const tv = new Tv()
tv.prender()
const luz = new Luz()
luz.apagar()

/*

 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */

class Impresora{
   
}

class BlackWhite extends Impresora{
    imprimir(){console.log("Estoy imprimiendo en blanco y negro")}
}

class Color extends Impresora{
    imprimir(){console.log("Estoy imprimiendo a color")}
}

class Multifuncion extends Impresora{
    imprimirBlancoNegro(){console.log("imprimiendo en Blanco y Negro")}
    imprimirColor(){console.log("imprimiendo en Color")}
    escanear(){console.log("Escaneando documento")}
    faxSend(){console.log("Enviando Fax")}
}

