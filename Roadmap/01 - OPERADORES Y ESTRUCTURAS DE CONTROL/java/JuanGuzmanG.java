import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class JuanGuzmanG {

    public static void main(String args[]) {
        //arithmetic
        int additive = 1 + 1;
        int subtraction = 1 - 1;
        int multiplication = 1 * 1;
        float division = 1 / 2;
        float remainder = 1 / 2;
        
        /*
        Unary
        + indica valores positivos
        - indica negativos
        ++ incremente de 1 en 1
        -- decrementa de 1 en 1

        */
        
        //Operadores logicos
        /*
        || or
        && and
        ^ xor
        */
        
        //operadores de comparación
        /*
        == igual a
        != distinto
        > mayor que
        < menos que
        => igual o mayor que
        <= igual o menor que
        */
        
        /*
        = asignacion
        += suma el valor asignado a la variable
        -= resta el valor asignado a la variable
        int b = 9;
        b<<=3;
        System.out.print(b);        
        */
        //condicionales
        int condicion = 1;
        if(condicion==1){
            System.out.print(1);
        } else if(condicion==2){
            System.out.print(2);
        } else{
            System.out.print("mas de 2");
        }
        switch (condicion){
            case 1 -> System.out.print(1);
            case 2 -> System.out.print(2);
        }
        switch (condicion){
            case 1 -> { 
                System.out.println(1);
                System.out.println("fin");
            }
        }
        //iterativas
        System.out.println("while:");
        int count = 2;
        while(count<3){
            count+=1;
            System.out.println("while: "+ count);
        }
        System.out.println("===============");
        int countdo = 6;
        do{
            System.out.println("dowhile: "+ countdo);
            countdo++;
        }while(countdo<6);
        
        //for
        System.out.println("for:");
        int i;
        for(i=0; i<2;i++){
            System.out.println(i);
        }
        System.out.println("foreach:");
        int[] numbers = {1,2,3,4,5};
        for(int num : numbers){
            System.out.println(num);
            if(num == 3){
                break;
            }
        }
        
        System.out.println("try catch:");
        double trydivision;
        try{
            trydivision = 20/0;
            System.out.println(trydivision);
        } catch(ArithmeticException e){
            System.out.println("no se puede dividir por 0");
        } finally{
            System.out.println("fin de division");
        }
         
        System.out.println("dificultad extra");
        List<Integer> lista = IntStream.rangeClosed(10, 55)
                .boxed()
                .collect(Collectors.toList());
        for(Integer num : lista){
            if (num % 2 == 0 && num != 16 && num % 3 != 0) {
              System.out.println(num);
            }
        }
        System.out.println("con streams");
        IntStream.rangeClosed(10,55)
                .filter(n -> n % 2 == 0)
                .filter(n -> n % 3 != 0)
                .filter(n -> n != 16)
                .forEach(System.out::println);
        
    }
}
