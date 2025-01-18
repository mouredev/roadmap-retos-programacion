//02 - Java

public class inmortalnight {
    //Sin parámetros ni retorno
    public void hello(){
        System.out.println("Hello World");
    }
    //Con un parámetro
    public void hello(String name){
        System.out.println("Hello " + name);
    }
    //Con varios parámetros
    public void hello(String name, int age){
        System.out.println("Hello " + name + " you are " + age + " years old");
    }
    //Con retorno
    public String hi(){
        return "Hello World";
    }
    //Crear funciones dentro de funciones, no se puede en Java
    //Ejemplo de funciones ya creadas
    public void ejecutar(){
        hello();
        hello("John");
        hello("John", 25);
        System.out.println(hi());
    }
    public String variableGlobal = "Variable global"; //Variable global, se puede usar en cualquier función de esta clase
    public void funcion(){
        String variableLocal = "Variable local"; //Variable local, solo se puede usar en esta función
        System.out.println(variableGlobal);
        System.out.println(variableLocal);
    }
    /*EXTRA:
     *  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
        * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
        * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
        * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    */
    public int funcion(String text1, String text2){
        int count = 0;
        for(int i = 1; i <= 100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                System.out.println(text1 + " " + text2);
            }else if(i % 3 == 0){
                System.out.println(text1);
            }else if(i % 5 == 0){
                System.out.println(text2);
            }else{
                System.out.println(i);
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        //Ejemplo de funciones ya creadas, ejecución
        inmortalnight objeto = new inmortalnight();
        objeto.ejecutar();
        objeto.funcion("Hola", "Mundo");
    }
}
