import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().warehouseCombination();
    }

    private List<String> validCharacters;
    private String warehouseCode;

    public void warehouseCombination(){
        validCharacters = Arrays.asList("A", "B", "C", "1", "2", "3");
        warehouseCode = generateCode();

        int nTries = 10;
        while(nTries > 0){
            System.out.println("Intentos: " + nTries);
            String userInputCode = askCodeToUser();
            if (warehouseCode.equals(userInputCode))
                break;
            analyzeUserCode(userInputCode);
            nTries--;
        }

        if (nTries == 0)
            System.out.println("¡Has perdido! Papá Noel ya no tiene tiempo para repartir los regalos...");
        else
            System.out.println("¡Felicidades, has acertado el código en " + (11 - nTries) + " intento/s!");
    }

    private String askCodeToUser(){
        Scanner sc = new Scanner(System.in);
        boolean validInput = false;
        String input = "";

        loop:
        while(!validInput){
            System.out.print("Introduzca un código (4 carácteres, solo A-C y 1-3): ");
            input = sc.nextLine().toUpperCase();
            if (input.length() != 4){
                System.out.println("Error. El código debe tener 4 carácteres");
                continue;
            }
            for (String character : input.split("")){
                if (!validCharacters.contains(character)){
                    System.out.println("Error. El código solo puede contener: 'A', 'B', 'C', '1', '2' o '3'");
                    continue loop;
                }
                if (input.indexOf(character) != input.lastIndexOf(character)){
                    System.out.println("Error. El código no puede contener carácteres repetidos");
                    continue loop;
                }
            }
            validInput = true;
        }

        return input;
    }

    private void analyzeUserCode(String code){
        for (String character : code.split("")){
            if (!warehouseCode.contains(character)){
                System.out.println("El carácter '" + character + "' NO EXISTE en el código secreto");
                continue;
            }
            int index = code.indexOf(character);
            if (warehouseCode.indexOf(character) == index){
                System.out.println("El carácter '" + character + "' EXISTE en el código secreto " +
                        "y ESTÁ en el lugar correcto");
                continue;
            }
            System.out.println("El carácter '" + character + "' EXISTE en el código secreto " +
                    "pero NO ESTÁ en el lugar correcto");
        }
        System.out.println();
    }

    private String generateCode(){
        Collections.shuffle(validCharacters);
        return validCharacters.subList(0, 4).stream()
                .reduce(String::concat)
                .get();
    }
}
