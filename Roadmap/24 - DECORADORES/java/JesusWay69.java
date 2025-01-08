package ejercicio24;

/*
* EJERCICIO:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        Developer frontend = new FrontEndDeveloper();
        frontend.skills();
        System.out.println("\n----------------------------------------------------------------------");

        Developer backend = new BackEndDeveloper(new FrontEndDeveloper());
        backend.skills();
        System.out.println("\n----------------------------------------------------------------------");
        //Podemos instaciar metiendo todas las clases al constructor tal que así:
        Developer fullstack1 = new FullStackDeveloper(new BackEndDeveloper(new FrontEndDeveloper())); 
        
        //O podemos instanciar la última pasándole sólo la primera (la que implementaba el decorador),
        //al guardar con super el método anterior nos ejecutará todos los métodos sobreescritos de todas las clases que haya entre ellas
        Developer fullstack = new FullStackDeveloper(new FrontEndDeveloper());
        fullstack.skills();
        System.out.println("                      |--------------|                      ");
        fullstack1.skills();
        System.out.println("\n----------------------------------------------------------------------");

        Sum sum = new Counter(new MainSum());
        System.out.println(sum.sumtwo(5, 8));
        System.out.println(sum.sumtwo(7, 9));
        System.out.println(sum.sumtwo(3, 1));
        System.out.println(sum.sumtwo(6, 2));
        System.out.println(sum.sumtwo(0, 3));

    }

}

interface Developer {//Declaramos una interfaz

    void skills();// con el método principal que luego sobreescribiremos
}

abstract class DevDecorator implements Developer {//Creamos una clase abstracta para implementar la interfaz

    private final Developer developer;//Convertimos en constante y encapsulamos la interfaz para que no pueda tener subclases

    public DevDecorator(Developer developer) {//Creamos el método decorador
        this.developer = developer;
    }

    @Override
    public void skills() {//Sobreescribimos el método principal
        this.developer.skills();
    }
}

class FrontEndDeveloper implements Developer {//Creamos una clase normal para implementar el decorador de la clase abstracta

    @Override
    public void skills() {//Sobreescribimos el método principal para que empiece a añadir texto
        System.out.print(" El programador frontend tiene conocimientos en: ");
        this.addHTML();
        this.addCSS();
    }

    private void addHTML() {//Creamos más métodos para añadir lenguajes dentro de esta clase frontend
        System.out.print(" HTML ");
    }

    private void addCSS() {
        System.out.print("y CSS");
    }
}

class BackEndDeveloper extends DevDecorator {//Creamos otra clase que hereda de la anterior

    public BackEndDeveloper(Developer developer) {
        super(developer);//Creamos un método de clase propia cuyo argumento de clase Developer pasamos al método de lenguaje super
    }

    @Override
    public void skills() {//Sobreescribimos de nuevo el método skills para añadir otro tipo de programador al texto
        super.skills();//Con super nos aseguramos que el texto del método antes de la sobreescritura se imprima también
        System.out.print("\n El programador backend conoce lenguajes como: ");
        this.addJava();
        this.addPython();
        this.addPhp();
        this.addTypescript();
        this.addJavascript();
    }

    private void addTypescript() {
        System.out.print(", Typescript");
    }

    private void addJavascript() {
        System.out.print(" o Javascript ");
    }

    private void addJava() {
        System.out.print("Java");

    }

    private void addPhp() {
        System.out.print(", PhP");
    }

    private void addPython() {
        System.out.print(", Python");
    }
}

class FullStackDeveloper extends DevDecorator {//Seguimos añadiendo clases heredando del decorador

    public FullStackDeveloper(Developer developer) {
        super(developer);//Si queremos que se ejecuten los métodos anteriores de impresión de texto debemos seguir
        // añadiendo el método de clase propia y añadirle a super nuestro argumento Developer
    }

    @Override
    public void skills() {//Así podemos seguir añadiendo tantas clases como queramos
        super.skills();
        System.out.println("\n El programador senior añade a esos conocimientos los de frameworks como: ");
        this.addAngular();
        this.addReact();
        this.addTailwind();
        this.addSpring();
        this.addDjango();
    }

    private void addAngular() {
        System.out.print(" Angular, ");
    }

    private void addReact() {
        System.out.print("React, ");
    }

    private void addTailwind() {
        System.out.print("Tailwind CSS, ");
    }

    private void addSpring() {
        System.out.print("Spring/SpringBoot, ");
    }

    private void addDjango() {
        System.out.println("o Django");
    }

}

/*
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
 */

interface Sum {

    String sumtwo(int a, int b);
}

abstract class SumDecorator implements Sum {

    private final Sum sum;

    public SumDecorator(Sum sum) {
        this.sum = sum;
    }

    @Override
    public String sumtwo(int a, int b) {

        return this.sum.sumtwo(a, b);

    }
}

class MainSum implements Sum {

    int result;

    @Override
    public String sumtwo(int a, int b) {
        result = a + b;
        return Integer.toString(result);

    }
}

class Counter extends SumDecorator {

    private static int calls = 0;

    public Counter(Sum sum) {
        super(sum);
    }

    @Override
    public String sumtwo(int a, int b) {
        super.sumtwo(a, b);
        ++calls;
        return "Resultado de " + a + " + " + b + " = " + super.sumtwo(a, b) + " , llamada Nº: " + Integer.toString(calls);
        

    }
}
