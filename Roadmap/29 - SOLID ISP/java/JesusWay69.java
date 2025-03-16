package ejercicio29;


/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        OstrichISP ostrich = new OstrichISP();
        SwiftISP swift = new SwiftISP();
        PenguinISP penguin = new PenguinISP();
        testBirds(ostrich);
        testBirds(swift);
        testBirds(penguin);
        BwPrinter hpBlackAndWhite = new BwPrinter();
        ColorPrinter xeroxColor = new ColorPrinter();
        MultiPrinter epsonMulti = new MultiPrinter();
        Scanner canonScan = new Scanner();
        testPrinter(hpBlackAndWhite);
        testPrinter(epsonMulti);
        testPrinter(canonScan);
        testPrinter(xeroxColor);

    }

    public static void testBirds(Object object) {
        String name = "";
        boolean feathers = false;
        boolean fly = false;
        boolean swim = false;
        boolean run = false;

        if (object instanceof OstrichISP) {
            feathers = ((OstrichISP) object).haveFeathersISP();
            name = ((OstrichISP) object).birdName();
            run = ((OstrichISP) object).run();
        } else if (object instanceof SwiftISP) {
            feathers = ((SwiftISP) object).haveFeathersISP();
            name = ((SwiftISP) object).birdName();
            fly = ((SwiftISP) object).fliesISP();
        } else if (object instanceof PenguinISP) {
            feathers = ((PenguinISP) object).haveFeathersISP();
            name = ((PenguinISP) object).birdName();
            swim = ((PenguinISP) object).swimsISP();
        }
        System.out.println("\nEspecie de ave: " + name
                + "\n¿tiene plumas?: " + feathers
                + "\n¿Puede volar?: " + fly
                + "\n¿Puede correr?: " + run
                + "\n¿Puede nadar?: " + swim);

    }

    public static void testPrinter(Object printer) {
        boolean canPrint = false;
        String device = "";
        boolean bw = false;
        boolean color = false;
        boolean scan = false;
        boolean fax = false;

        if (printer instanceof BwPrinter) {
            canPrint = ((BwPrinter) printer).printer();
            device = ((BwPrinter) printer).printerModel();
            bw = ((BwPrinter) printer).printBW();
        } else if (printer instanceof ColorPrinter) {
            canPrint = ((ColorPrinter) printer).printer();
            device = ((ColorPrinter) printer).printerModel();
            color = ((ColorPrinter) printer).printColor();
        } else if (printer instanceof MultiPrinter) {
            canPrint = ((MultiPrinter) printer).printer();
            device = ((MultiPrinter) printer).printerModel();
            bw = ((MultiPrinter) printer).printBW();
            color = ((MultiPrinter) printer).printColor();
            scan = ((MultiPrinter) printer).scanner();
            fax = ((MultiPrinter) printer).fax();
        } else if (printer instanceof Scanner) {
            device = ((Scanner) printer).printerModel();
            scan = ((Scanner) printer).scanner();
        }
        System.out.println("\nTipo de dispositivo: " + device
                + "\n¿puede imprimir?: " + canPrint
                + "\n¿Imprime en blanco y negro?: " + bw
                + "\n¿Imprime en color?: " + color
                + "\n¿Escanea Documentos?: " + scan
                + "\n¿Puede enviar/recibir fax?: " + fax);
    }

}

/*
El siguiente código no cumple el principio de segregación de interfaces ya que sólo hay una interface que modela el contenido
de las diferentes clases de aves con todas las características de las cuales solo la primera (tiene plumas)
es común a todas las aves pero no las demás que aun así es obligatorio declarar sus métodos en todas las clases
además la constante que debemos devolver en cada método está seteada en true con lo cual en los métodos cuya
característica no cumpla el ave debemos forzar la salida retornando false.
 */
interface Bird {

    boolean haveFeathers();

    boolean flies();

    boolean swims();

    boolean run();

    final boolean CHARACTERISTIC = true;
}

class Ostrich implements Bird {

    @Override
    public boolean haveFeathers() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean flies() {
        return false;
    }

    @Override
    public boolean swims() {
        return false;
    }

    @Override
    public boolean run() {
        return CHARACTERISTIC;
    }

}

class swift implements Bird {

    @Override
    public boolean haveFeathers() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean flies() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean swims() {
        return false;
    }

    @Override
    public boolean run() {
        return false;

    }
}

class Penguin implements Bird {

    @Override
    public boolean haveFeathers() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean flies() {
        return false;
    }

    @Override
    public boolean swims() {
        return CHARACTERISTIC;
    }

    @Override
    public boolean run() {
        return true;
    }
}

/*
En el siguiente código aplicamos el principio de segregación de interfaces dividiendo en diferentes interfaces
los métodos que devuelven la característica verdadera, en el primero declaramos el método "tiene plumas" común
a todas las aves y el método que devuelve el nombre del ave así como la constante general de característica
seteado en true, después creamos una interface por cada característica para declarar dentro su método de característica 
que no es común a todas las aves, volar, correr y nadar, luego creamos las clases que modelen cada especie de ave heredando
en cada una de ellas las interfaces que se correspondan con sus características particulares (Java no permite la 
herencia múltiple de superclases ni clases abstractas pero sí permite heredar de varias interfaces), despues dentro
de la clase principal del fichero creamos un método que reciba un objeto, seteamos todas las características en false
y mediante condicionales aplicamos para cada tipo de objeto/ave sus correspondientes características que sean verdaderas,
creamos una salida que muestre todas las características y en cada ave mostrará true si esa característica está en el
modelado de su objeto o false, que es el valor por defecto que declaramos si no cumple dicha característica.
 */
interface BirdISP {

    boolean haveFeathersISP();

    String birdName();
    final boolean CHARACTERISTICISP = true;

}

interface FlyingBirdISP {

    boolean fliesISP();
}

interface SwimmingBirdISP {

    boolean swimsISP();
}

interface RunnerBirdISP {

    boolean run();
}

class OstrichISP implements BirdISP, RunnerBirdISP {

    @Override
    public boolean run() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean haveFeathersISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public String birdName() {
        return "Avestruz";
    }

}

class PenguinISP implements BirdISP, SwimmingBirdISP, RunnerBirdISP {

    @Override
    public boolean haveFeathersISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean swimsISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean run() {
        return CHARACTERISTICISP;
    }

    @Override
    public String birdName() {
        return "Pingüino";
    }

}

class SwiftISP implements BirdISP, FlyingBirdISP {

    @Override
    public boolean haveFeathersISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public boolean fliesISP() {
        return CHARACTERISTICISP;
    }

    @Override
    public String birdName() {
        return "Vencejo";
    }

}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 *  Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */
interface Printer {

    boolean printer();

    String printerModel();
    final boolean FEATUREPRINTER = true;
}

interface BlackAndWhite {

    boolean printBW();
}

interface Color {

    boolean printColor();
}

interface Scan {

    boolean scanner();
}

interface Fax {

    boolean fax();
}

class BwPrinter implements Printer, BlackAndWhite {

    @Override
    public boolean printer() {
        return FEATUREPRINTER;
    }

    @Override
    public String printerModel() {
        return "Impresora en blanco y negro";
    }

    @Override
    public boolean printBW() {
        return FEATUREPRINTER;
    }

}

class ColorPrinter implements Printer, Color {

    @Override
    public boolean printer() {
        return FEATUREPRINTER;
    }

    @Override
    public String printerModel() {
        return "Impresora a color";
    }

    @Override
    public boolean printColor() {
        return FEATUREPRINTER;
    }

}

class MultiPrinter implements Printer, Color, Scan, Fax, BlackAndWhite {

    @Override
    public boolean printer() {
        return FEATUREPRINTER;
    }

    @Override
    public String printerModel() {
        return "Dispositivo multifunción";
    }

    @Override
    public boolean printColor() {
        return FEATUREPRINTER;
    }

    @Override
    public boolean scanner() {
        return FEATUREPRINTER;
    }

    @Override
    public boolean fax() {
        return FEATUREPRINTER;
    }

    @Override
    public boolean printBW() {
        return FEATUREPRINTER;
    }

}

class Scanner implements Printer, Scan {

    @Override
    public boolean printer() {
        return FEATUREPRINTER;
    }

    @Override
    public String printerModel() {
        return "Dispositivo exclusivo de escaneo";
    }

    @Override
    public boolean scanner() {
        return FEATUREPRINTER;
    }

}
