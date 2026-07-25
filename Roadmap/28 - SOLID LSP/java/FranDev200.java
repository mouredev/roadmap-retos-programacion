package com.amsoft.roadmap.example28;

import java.util.ArrayList;

public class FranDev200 {


    abstract static class Vehiculo{

        public void acelerar(){
        }

        public String girar(){ return null; }

    }

    abstract static class VehiculoConMotor extends Vehiculo{

        public void repostar(){ }

    }

    static class Bicicleta extends Vehiculo{

        @Override
        public void acelerar() {
            System.out.println("La bicicleta esta acelerando.");
        }

        @Override
        public String girar() {
            return "La bicicleta ha girado";
        }


    }

    static class Coche extends VehiculoConMotor{

        @Override
        public void acelerar() {
            System.out.println("El coche esta acelerando.");
        }

        @Override
        public String girar() {
            return "El coche ha girado";
        }

        @Override
        public void repostar() {
            System.out.println("El coche esta repostando.");
        }
    }

    static class Furgoneta extends VehiculoConMotor{

        @Override
        public void acelerar() {
            System.out.println("La furgoneta esta acelerando.");
        }

        @Override
        public String girar() {
            return "La furgoneta ha girado";
        }

        @Override
        public void repostar() {
            System.out.println("La furgoneta esta repostando.");
        }

    }

    static class ControlVehiculo{

        public void arrancar(Vehiculo vehiculo){

            vehiculo.acelerar();

        }
        public void girarDerecha(Vehiculo vehiculo){

            System.out.println(vehiculo.girar() + " a la derecha");

        }
        public void girarIzquierda(Vehiculo vehiculo){

            System.out.println(vehiculo.girar() + " a la izquierda");

        }
        public void repostar(VehiculoConMotor vehiculoConMotor){

            vehiculoConMotor.repostar();

        }

    }

    static void main() {

        /*

        EJERCICIO:
         * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
         * y crea un ejemplo simple donde se muestre su funcionamiento
         * de forma correcta e incorrecta.

         */

        ControlVehiculo controlVehiculo = new ControlVehiculo();

        // ACELERRAR
        controlVehiculo.arrancar(new Bicicleta());
        controlVehiculo.arrancar(new Furgoneta());
        controlVehiculo.arrancar(new Coche());
        System.out.println();

        // GIRAR
        controlVehiculo.girarDerecha(new Bicicleta());
        controlVehiculo.girarIzquierda(new Bicicleta());
        controlVehiculo.girarIzquierda(new Coche());
        controlVehiculo.girarDerecha(new Coche());
        controlVehiculo.girarIzquierda(new Furgoneta());
        controlVehiculo.girarDerecha(new Furgoneta());
        System.out.println();

        // REPOSTAR
        controlVehiculo.repostar(new Coche());
        controlVehiculo.repostar(new Furgoneta());
        // controlVehiculo.repostar(new Bicicleta()); // Da error, xq no tiene ese metodo heredado


        /*

        DIFICULTAD EXTRA (opcional):
         * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
         * cumplir el LSP.
         * Instrucciones:
         * 1. Crea la clase Vehículo.
         * 2. Añade tres subclases de Vehículo.
         * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
         * 4. Desarrolla un código que compruebe que se cumple el LSP.

         */
        System.out.println("\n===============");
        System.out.println("EJERCICIO EXTRA");
        System.out.println("===============\n");



        ArrayList<Vehiculo2> vehiculos = new ArrayList<Vehiculo2>();
        for (int i = 0; i < 3; i++) {
            vehiculos.add(new Bici());
            vehiculos.add(new Camion());
            vehiculos.add(new Coche2());
        }

        for(Vehiculo2 vehiculo : vehiculos){
            vehiculo.acelerar();
        }

        System.out.println();

        for(Vehiculo2 vehiculo : vehiculos){
            vehiculo.frenar();
        }

    }

    abstract static class Vehiculo2{

        public void acelerar(){ }
        public void frenar(){ }

    }

    static class Coche2 extends Vehiculo2{

        @Override
        public void acelerar() {
            System.out.println("El coche esta acelerando.");
        }

        @Override
        public void frenar() {
            System.out.println("El coche está frenando.");
        }
    }

    static class Bici extends Vehiculo2{

        @Override
        public void acelerar() {
            System.out.println("La bici esta acelerando.");
        }

        @Override
        public void frenar() {
            System.out.println("La bici está frenando.");
        }
    }

    static class Camion extends Vehiculo2{

        @Override
        public void acelerar() {
            System.out.println("El camion esta acelerando.");
        }

        @Override
        public void frenar() {
            System.out.println("El camion está frenando.");
        }
    }

}
