import java.util.HashMap;
import java.util.Map;

public class danhingar {

    public static void main(String[] args) {
        Form1 square = new Square();
        square.draw();

        Form1 circle = new Circle();
        circle.draw();

        Form1 triangle = new Triangle();
        triangle.draw();

        //Extra 
        Calculator calculator = new Calculator();

        calculator.addOperation("addition", new Addition());
        calculator.addOperation("substration", new Substration());
        calculator.addOperation("multiplication", new Multiplication());
        calculator.addOperation("division", new Division());
        calculator.addOperation("power", new Power());

        System.out.printf("Resultado %f\n",calculator.calculate("addition",5.0,3.5));
        System.out.printf("Resultado %f\n",calculator.calculate("substration",10.0,4.0));
        System.out.printf("Resultado %f\n",calculator.calculate("multiplication",5.0,3.0));
        System.out.printf("Resultado %f\n",calculator.calculate("division",20.0,5.0));
        System.out.printf("Resultado %f\n",calculator.calculate("power",2.0,2.0));
        System.out.printf("Resultado %f\n",calculator.calculate("example",2.0,2.0));
    }
    

}

//Incorrecta
class Form {

    public void drawSquare(){
        System.out.println("Dibujar un cuadrado");
    }

    public void drawCircle(){
        System.out.println("Dibujar un círculo");
    }

    public void drawTriangle(){
        System.out.println("Dibujar un círculo");
    }
    
}

//Forma correcta

interface Form1 {

    void draw();
}  


class Square implements Form1 {

    @Override
    public void draw() {
        System.out.println("Dibuja un cuadrado");
    }

    
}

class Circle implements Form1 {

    @Override
    public void draw() {
        System.out.println("Dibuja un círculo");
    }

    
}

class Triangle implements Form1 {

    @Override
    public void draw() {
        System.out.println("Dibuja un triángulo");
    }

    
}



//EXTRA

interface Operation {

    Double operate(Double num1,Double num2);
    
}
    
class Addition implements Operation {

    @Override
    public Double operate(Double num1, Double num2) {
        return num1+num2;
    }
}

class Substration implements Operation {

    @Override
    public Double operate(Double num1, Double num2) {
        return num1-num2;
    }
}

class Multiplication implements Operation {

    @Override
    public Double operate(Double num1, Double num2) {
        return num1*num2;
    }
}

class Division implements Operation {

    @Override
    public Double operate(Double num1, Double num2) {
        return num1/num2;
    }
}

class Power implements Operation {

    @Override
    public Double operate(Double num1, Double num2) {
        return Math.pow(num1, num2);
    }
}

 class Calculator {

    Map<String,Operation> operations;
    
    public Calculator(){
        this.operations = new HashMap<>();
    }

    public void addOperation(String name, Operation operation){
        operations.put(name, operation);
    }

    public double calculate(String name, double num1, double num2){
        if(!operations.containsKey(name)){
            throw new IllegalArgumentException("La operación "+name+" no es válida");
        }
        return operations.get(name).operate(num1, num2);
    }

    
}
