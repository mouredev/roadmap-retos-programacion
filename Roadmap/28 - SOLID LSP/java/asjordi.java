/*
    El Principio de Sustitución de Liskov (LSP) establece que las subclases deben ser sustituibles por sus clases base.
    Es decir, dado que la clase B es una subclase de la clase A, deberíamos poder pasar un objeto de la clase B a cualquier método que espere un objeto de la clase A sin que se produzca un error.
    Este es el comportamiento esperado, dado que cuando se utiliza la herencia se asume que la subclase hereda todos los comportamientos de la superclase.
    La subclase extiende el comportamiento, pero nunca lo reduce.
 */

public class Main {

    public static void main(String[] args) {
        // Comprobación LSP
        Vehiculo vehiculoDeportivo = new VehiculoDeportivo();
        Vehiculo vehiculoFamiliar = new VehiculoFamiliar();
        Vehiculo vehiculoCarga = new VehiculoCarga();

        vehiculoDeportivo.acelerar();
        vehiculoDeportivo.frenar();

        vehiculoFamiliar.acelerar();
        vehiculoFamiliar.frenar();

        vehiculoCarga.acelerar();
        vehiculoCarga.frenar();
    }

    /*
        EJERCICIO:
        Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
        y crea un ejemplo simple donde se muestre su funcionamiento
        de forma correcta e incorrecta.
     */

    interface Animal {
        void comer();
        void nadar();
    }

    static class Jirafa implements Animal {
        @Override
        public void comer() {
            System.out.println("La jirafa come hojas de los árboles");
        }

        @Override
        public void nadar() {
            throw new UnsupportedOperationException("La jirafa no puede nadar");
        }
    }

    static class Pato implements Animal {
        @Override
        public void comer() {
            System.out.println("El pato come pan");
        }

        @Override
        public void nadar() {
            System.out.println("El pato nada en el agua");
        }
    }

    /*
        En este caso, la clase Jirafa no puede nadar, por lo que se lanza una excepción UnsupportedOperationException.
        Esto viola el principio de sustitución de Liskov, ya que la clase Jirafa no puede ser sustituida por la clase Animal.
        Para solucionar este problema, se puede crear una interfaz separada para los animales que pueden nadar, y hacer que la clase Pato implemente esa interfaz. Mientras que la clase Jirafa no implementará la interfaz AnimalAcuatico, pero sí la interfaz Animal.
     */

    interface Animal2 {
        void comer();
    }

    interface AnimalAcuatico extends Animal2 {
        void nadar();
    }

    static class Jirafa2 implements Animal2 {
        @Override
        public void comer() {
            System.out.println("La jirafa come hojas de los árboles");
        }
    }

    static class Pato2 implements AnimalAcuatico {
        @Override
        public void comer() {
            System.out.println("El pato come pan");
        }

        @Override
        public void nadar() {
            System.out.println("El pato nada en el agua");
        }
    }

    /*
        DIFICULTAD EXTRA (opcional):
        Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como cumplir el LSP.
        Instrucciones:
        1. Crea la clase Vehículo.
        2. Añade tres subclases de Vehículo.
        3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
        4. Desarrolla un código que compruebe que se cumple el LSP.
     */

    abstract static class Vehiculo {
        abstract void acelerar();
        abstract void frenar();
    }

    static class VehiculoDeportivo extends Vehiculo {
        @Override
        void acelerar() {
            System.out.println("El vehículo deportivo acelera rápidamente");
        }

        @Override
        void frenar() {
            System.out.println("El vehículo deportivo frena bruscamente");
        }
    }

    static class VehiculoFamiliar extends Vehiculo {
        @Override
        void acelerar() {
            System.out.println("El vehículo familiar acelera suavemente");
        }

        @Override
        void frenar() {
            System.out.println("El vehículo familiar frena de forma segura");
        }
    }

    static class VehiculoCarga extends Vehiculo {
        @Override
        void acelerar() {
            System.out.println("El vehículo de carga acelera lentamente");
        }

        @Override
        void frenar() {
            System.out.println("El vehículo de carga frena con precaución");
        }
    }

}
