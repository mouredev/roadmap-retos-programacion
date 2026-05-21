public class Meir {
    public static void main(String[] args) {

        try{
            System.out.println(10/0);
        }catch(ArithmeticException e){
            System.out.println("Error: " + e);
        }


        boolean flagError = false;
        try{
            processParams(new int[]{1, 5,2});
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println("El numero de parametros debe ser mayor a 2");
            flagError = true;
        }catch (ArithmeticException e){
            System.out.println("El segundo parametro no puede ser 0");
            flagError = true;
        }catch (Exception e){
            System.out.println("Error: " + e);
            flagError = true;
        }
        finally{
            if(flagError){
                System.out.println("hubo un error");
            }else{
                System.out.println("No hubo error");
            }
            System.out.println("Finalizo el programa");
        }

    }

    static void processParams(int[] params) {
        if(params.length < 3){
            throw new ArrayIndexOutOfBoundsException();
        } else if (params[1] == 0) {
            throw new ArithmeticException();
        } else if (params.length > 5) {
            throw new ArrayLenghtError("the array can not be more than 5 parameters");
        }

        System.out.println(params[0] / params[1]);
        System.out.println(params[2]);
    }


}



class ArrayLenghtError extends RuntimeException{
    public ArrayLenghtError(String message){
        super(message);
    }
}
