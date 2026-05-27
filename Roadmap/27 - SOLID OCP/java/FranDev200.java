package com.amsoft.roadmap.example27;

public class FranDev200 {


    interface MetodoPago{
        public void pago();
    }

    static class PagoBizum implements MetodoPago{
        public void pago(){
            System.out.println("Pagando con bizum.");
        }
    }

    static class PagoTarjeta implements MetodoPago{
        public void pago(){
            System.out.println("Pagando con tarjeta.");
        }
    }

    static class PagoPayPal implements MetodoPago{
        public void pago(){
            System.out.println("Pagando con paypal.");
        }
    }

    static class PagoTransaccion implements MetodoPago{
        public void pago(){
            System.out.println("Pagando con transaccion.");
        }
    }

    static class Datafono{

        public void pagar(MetodoPago metodoPago){
            metodoPago.pago();
        }

    }

    static void main() {

        /*

        EJERCICIO:
         * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
         * y crea un ejemplo simple donde se muestre su funcionamiento
         * de forma correcta e incorrecta.

         */

        Datafono df = new Datafono();
        df.pagar(new PagoBizum());
        df.pagar(new PagoTarjeta());
        df.pagar(new PagoPayPal());

        // AÑADO UN METODO MÁS DE PAGO. SOLO TENGO QUE AÑADIR UNA CLASE QUE IMPLEMENTE LA INTERFAZ, CUMPLO OCP
        df.pagar(new PagoTransaccion());


        /*

            DIFICULTAD EXTRA (opcional):
             * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
             * Requisitos:
             * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
             * Instrucciones:
             * 1. Implementa las operaciones de suma, resta, multiplicación y división.
             * 2. Comprueba que el sistema funciona.
             * 3. Agrega una quinta operación para calcular potencias.
             * 4. Comprueba que se cumple el OCP.

         */

        Calculadora calculadora = new Calculadora();

        System.out.println("\n===============");
        System.out.println("EJERCICIO EXTRA");
        System.out.println("===============");

        System.out.println("-SUMA");
        System.out.println("-----------");
        System.out.println("4 + 7 = " + calculadora.calcular(new Suma(), 4, 7));
        System.out.println("===========");
        System.out.println("-RESTA");
        System.out.println("-----------");
        System.out.println("4 - 7 = " + calculadora.calcular(new Resta(), 4, 7));
        System.out.println("===========");
        System.out.println("-MULTIPLICACION");
        System.out.println("-----------");
        System.out.println("4 * 7 = " + calculadora.calcular(new Multiplicacion(), 4, 7));
        System.out.println("===========");
        System.out.println("-DIVISION");
        System.out.println("-----------");
        System.out.println("7 / 4 = " + calculadora.calcular(new Division(), 7, 4));
        System.out.println("===========");
        System.out.println("-POTENCIA");
        System.out.println("-----------");
        System.out.println("2 ^ 3 = " + calculadora.calcular(new Potencia(), 2, 3));
        System.out.println("===========");

    }

    interface Calculo{
        public double calcular(int a,  int b);
    }

    static class Suma implements Calculo{
        @Override
        public double calcular(int a, int b) {
            return a + b;
        }
    }

    static class Resta implements Calculo{
        @Override
        public double calcular(int a, int b) {
            return a - b;
        }
    }

    static class Multiplicacion implements Calculo{
        @Override
        public double calcular(int a, int b) {
            return a * b;
        }
    }

    static class Division implements Calculo{
        @Override
        public double calcular(int a, int b) {
            return (double) a / b;
        }
    }

    static class Potencia implements Calculo{
        @Override
        public double calcular(int a, int b) {
            return Math.pow(a, b);
        }
    }

    static class Calculadora{

        public double calcular(Calculo calculo, int a, int b) {
            return calculo.calcular(a, b);
        }

    }

}
