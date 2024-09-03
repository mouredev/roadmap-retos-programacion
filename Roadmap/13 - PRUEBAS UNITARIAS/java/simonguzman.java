
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class simonguzman {
    public static void main(String[] args) {
        assert sumar(10, 5) == 15;
        assert sumar(-10, 5) == -5;
        assert sumar(0, 0) == 0;

        assert Math.abs(sumar(10.5, 5.5) - 16.0) < 0.0001;
        assert Math.abs(sumar(-10.5, 5.5) - (-5.0)) < 0.0001;
        assert Math.abs(sumar(0.0, 0.0)) < 0.0001;

        String numStr1 = "10";
        int num1 = Integer.parseInt(numStr1);
        int resultado1 = sumar(num1, 5);
        assert resultado1 == 15;

        String numStr2 = "10.5";
        double num2 = Double.parseDouble(numStr2);
        double resultado2 = sumar(num2, 5.5);
        assert Math.abs(resultado2 - 16.0) < 0.0001;

        String numStrInvalido = "abc";
        try {
            int numInvalido = Integer.parseInt(numStrInvalido);
            assert false; 
        } catch (NumberFormatException e) {
            assert true;
        }
        System.out.println("Todas las pruebas pasaron correctamente. ");
        pruebaDiccionario();
    }    

    public static int sumar(int num1, int num2){
        return num1 + num2;
    }

    
    public static double sumar(double num1, double num2){
        return num1 + num2;
    }

    static void pruebaDiccionario(){
        Map<String, Object> datosPersona = new HashMap<>();
        datosPersona.put("name", "Simon Guzman");
        datosPersona.put("age", 22);
        datosPersona.put("birth_date", "28-11-2001");
        datosPersona.put("programming_languages", Arrays.asList("Java", "Python","C++"));

        try {
            verificarExistenciaDatos(datosPersona);
            verificarValidezDatos(datosPersona);    
            System.out.println("Todos los datos son validos");
        } catch (AssertionError e) {
            System.out.println("Validacion fallida: "+e.getMessage());
        }
        
    }

    static void verificarExistenciaDatos(Map<String, Object> datos){
        assert datos.containsKey("name") : "El campo 'name' no existe en el diccionario.";
        assert datos.containsKey("age") : "El campo 'age' no existe en el diccionario.";
        assert datos.containsKey("birth_date") : "El campo 'birth_date' no existe en el diccionario.";;
        assert datos.containsKey("programming_languages"): "El campo 'programming_languages' no existe en el diccionario.";;

        System.out.println("Todos los campos existen en el diccionario.");
    }

    static void verificarValidezDatos(Map<String, Object> datos){
        assert datos.get("name").equals("Simon Guzman") : "El valor del campo 'name' no es válido.";
        assert datos.get("age").equals(22) : "El valor del campo 'age' no es válido.";
        assert datos.get("birth_date").equals("28-11-2001") : "El valor del campo 'birth_date' no es válido.";

        List<String> lenguajes = (List<String>) datos.get("programming_languages");
        assert lenguajes.contains("Java") : "El lenguaje 'Java' no está en la lista.";
        assert lenguajes.contains("Python") : "El lenguaje 'Python' no está en la lista.";
        assert lenguajes.contains("C++") : "El lenguaje 'C++' no está en la lista.";

        System.out.println("Todos los datos son validos.");
    }
}




