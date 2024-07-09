package com.amsoft.roadmap.example27;

import java.util.Map;

public class Example27 {
    public static void main(String[] args) {
        Report report = new HTMLReport();
        report.generate();

        Calculator calculator = new Calculator();
        System.out.println("La suma de 5 + 6 es: " + calculator.calculate(new Addition(),5,6));
        System.out.println("La resta de 10 - 6 es: " + calculator.calculate(new Subtraction(),10,6));
        System.out.println("La multiplicación de 10 * 6 es: " + calculator.calculate(new Multiplication(),10,6));
        System.out.println("La división de 10 / 2 es: " + calculator.calculate(new Division(),10,2));
        System.out.println("La potencia de 9 elevado 3 es: " + calculator.calculate(new Pow(),9,3));
    }
}
//Viola OCP, si queremos agregar un reporte Excel debemos modificar la clase, agregando un if
/*class ReportGenerator{
    public void generateReport(String type){
        if(type.equals("PDF")){
            System.out.println("Generando reporte PDF");
        } else if (type.equals("HTML")) {
            System.out.println("Generando reporte HTML");
        }
    }
}*/


//Cumple OCP, declaramos un interfaz con un método que debe implementar las clases concretas
//Si queremos agregar un reporte Excel simplemente creamos una clase que implementa la interfaz
interface Report{
    void generate();
}

class PDFReport implements Report{

    @Override
    public void generate() {
        System.out.println("Generando reporte PDF");
    }
}

class HTMLReport implements Report{

    @Override
    public void generate() {
        System.out.println("Generando reporte HTML");
    }
}




//EXTRA
interface Operable {
    double calculate(double num1,double num2);
}

class Addition implements Operable {

    @Override
    public double calculate(double num1, double num2) {
        return num1 + num2;
    }
}

class Subtraction implements Operable {

    @Override
    public double calculate(double num1, double num2) {
        return num1 - num2;
    }
}

class Multiplication implements Operable{

    @Override
    public double calculate(double num1, double num2) {
        return num1 * num2;
    }
}

class Division implements Operable {

    @Override
    public double calculate(double num1, double num2) {
        return num1/num2;
    }
}

class Calculator {
    public double calculate(Operable operation, double num1, double num2){
        return operation.calculate(num1,num2);
    }
}
class Pow implements Operable {

    @Override
    public double calculate(double num1, double num2) {
        return Math.pow(num1,num2);
    }
}