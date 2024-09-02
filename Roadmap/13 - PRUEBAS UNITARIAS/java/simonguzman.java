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
    }    

    public static int sumar(int num1, int num2){
        return num1 + num2;
    }

    
    public static double sumar(double num1, double num2){
        return num1 + num2;
    }
}




