public class Danymarsan1 {
    public static void main(String[] args) {
        int a = 4;
        int b = 2;
        System.out.println("Operadores binarios");
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Modulo: " + (a % b));
        System.out.println();

        System.out.println("Operadores unarios");
        System.out.println("Signo positivo: " + (+a));
        System.out.println("Signo negativo: " + (-a));
        System.out.println("Preincremento: " + (++a));
        System.out.println("Postincremento: " + (a++));
        System.out.println("Predecremento: " + (--a));
        System.out.println("Postdecremento: " + (a--));
        System.out.println();

        System.out.println("Operadores de comparación");
        System.out.println("¿4 es mayor que 2? : " +(a>b));
        System.out.println("¿4 es mayor o igual que 2? : " +(a>=b));
        System.out.println("¿4 es menor que 2? : " +(a<b));
        System.out.println("¿4 es menor o igual que 2? : " +(a<=b));
        System.out.println("¿4 es igual que 2? : " + (a==b));
        System.out.println("¿4 es distinto de 2? : " + (a!=b));
        System.out.println();

        boolean v = true;
        boolean f = false;        
        System.out.println("Operadores lógicos");
        
        System.out.println("¿true es igual a false? : " + (v&f));
        System.out.println("¿true es igual a false? : " + (v&&f));
        System.out.println("¿true o false son verdaderas? : " + (v|f));
        System.out.println("¿true o false son verdaderas? : " + (v||f));
        System.out.println("Contrario de true : " + (!v));
        System.out.println();

        int c;
        System.out.println("Operadores de asignación");
        
        System.out.println("Asignamos valor a la variable i = " + (c = 1));
        System.out.println("Suma y asigna: " + (c+=5));
        System.out.println("Resta y asigna: " + (c-=5));
        System.out.println("Multiplica y asigna: " + (c*=5));
        System.out.println("Divide y asigna: " + (c/=5));
        System.out.println();


        System.out.println("Los números del ejercicio de dificultad extra:");
        //Bucle
        for(int i = 10; i < 56; i++){
            //Condicional
            if(i != 16 && i % 3 != 0 && i % 2 == 0){
            System.out.println(i);
            }
        }
    }
}
