import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().mouredevPro();
    }

    final private File file = new File("Josegs95.csv");

    public void mouredevPro(){
        initCSVFile();

        selectWinners(getSubListFromCSVFile());

        deleteFile();
    }

    private void selectWinners(List<String> subscriberList){
        if (subscriberList.size() < 3){
            System.out.println("No hay suficientes participantes para el sorteo");
            return;
        }

        Collections.shuffle(subscriberList);
        List<String> winners = subscriberList.subList(0, 3);

        String[] twitchSubWinner = winners.get(0).split(",");
        String[] discountWinner = winners.get(1).split(",");
        String[] bookWinner = winners.get(2).split(",");
        System.out.println("El usuario con id:" + twitchSubWinner[0] + " e email: "
                + twitchSubWinner[1] + " ha ganado una subscripción a Twitch!");
        System.out.println("El usuario con id:" + discountWinner[0] + " e email: "
                + discountWinner[1] + " ha ganado un descuento en la web!");
        System.out.println("El usuario con id:" + bookWinner[0] + " e email: "
                + bookWinner[1] + " ha ganado un libro de programación!");
    }

    private void initCSVFile(){
        try {
            if (!file.createNewFile())
                return;

            List<String> subscriberList = new ArrayList<>();
            subscriberList.add("1,ejemplo@gmail.com,activo");
            subscriberList.add("2,ejemplo2@gmail.com,inactivo");
            subscriberList.add("3,ejemplo3@gmail.com,activo");
            subscriberList.add("4,ejemplo4@gmail.com,activo");
            subscriberList.add("5,ejemplo5@gmail.com,inactivo");
            subscriberList.add("6,ejemplo6@gmail.com,activo");
            subscriberList.add("7,ejemplo7@gmail.com,activo");


            Files.writeString(file.toPath(), "id,email,status" + System.lineSeparator(),
                    StandardCharsets.UTF_8);
            populateFile(subscriberList);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void populateFile(List<String> dataList){
        try{
            for (String dataLine : dataList){
                Files.writeString(file.toPath(), dataLine + System.lineSeparator(),
                        StandardCharsets.UTF_8, StandardOpenOption.APPEND);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

    private List<String> getSubListFromCSVFile(){
        try{
            List<String> readList = Files.readAllLines(file.toPath());
            List<String> subList = new ArrayList<>();
            for (int i = 1; i < readList.size(); i++){
                if (!readList.get(i).contains("inactivo"))
                    subList.add(readList.get(i));
            }

            return subList;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void deleteFile(){
        if (file.delete())
            System.out.println("Archivo " + file.getName() + " borrado correctamente");
        else
            System.out.println("Error al intentar borrar el archivo " + file.getName());
    }
}
