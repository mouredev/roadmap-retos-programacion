import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.TemporalAdjusters;
import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().batmanDay();
    }

    private int[][] gothamMap = new int[20][20];

    public void batmanDay(){
        //Reto 1
        System.out.println("Reto 1:");
        calculateFutureBatmanDays();

        //Reto 2
        System.out.println("\nReto2:");
        List<Integer[]> sensorList = createRandomSensors(25);
        putSensorOnMap(sensorList);
        Map<String, Integer> mostDangerousAreaData = identifyMostDangerousArea();

        int xCoord = mostDangerousAreaData.get("X");
        int yCoord = mostDangerousAreaData.get("Y");
        int dangerLevel = mostDangerousAreaData.get("dangerLevel");
        System.out.println("Zona mas peligrosa");
        System.out.print("X: " + xCoord + ", ");
        System.out.print("Y: " + yCoord + ", ");
        System.out.println("Nivel de peligro: " + dangerLevel);
        System.out.println((dangerLevel > 19 ? "Se" : "No se") + " debe activar el protocolo de seguridad");
        System.out.println("Distancia a la Batcueva: " + (xCoord + yCoord) + " casillas.");
    }

    //Reto 1
    private void calculateFutureBatmanDays(){
        LocalDate date = LocalDate.of(2024, 9, 1);
        int anniversaryCount = 85;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd 'de' LLLL 'del' yyyy");
        while(anniversaryCount <= 100){
            date = date.with(TemporalAdjusters.dayOfWeekInMonth(3, DayOfWeek.SATURDAY));
            System.out.println("El aniversario nª" + anniversaryCount + " será el: " + date.format(formatter));

            date = date.plusYears(1);
            anniversaryCount++;
        }
    }

    //Reto 2
    private List<Integer[]> createRandomSensors(int sensorCount){
        Random rnd = new Random();
        List<Integer[]> sensorList = new ArrayList<>();
        int[][] aux = new int[gothamMap.length][gothamMap[0].length];

        Arrays.stream(aux).forEach(row -> Arrays.fill(row, -1));

        for (int i = 0; i < sensorCount; i++){
            int x = rnd.nextInt(aux.length);
            int y = rnd.nextInt(aux.length);
            if (aux[x][y] != -1){
                i--;
                continue;
            }

            int value = rnd.nextInt(11);
            sensorList.add(new Integer[] {x, y, value});
            aux[x][y] = value;
        }

        return sensorList;
    }

    private void putSensorOnMap(List<Integer[]> sensors){
        for (Integer[] sensor : sensors){
            gothamMap[sensor[0]][sensor[1]] = sensor[2];
        }
    }

    private Map<String, Integer> identifyMostDangerousArea(){
        int coordX = 0;
        int coordY = 0;
        int mostDangerLevel = 0;
        for (int i = 0; i < gothamMap.length - 2; i++){
            for (int j = 0; j < gothamMap[0].length - 2; j++){
                int[][] area = getSubmatrixFromMatrix(gothamMap, i, j);
                int dangerLevel = Arrays.stream(area)
                        .map(row -> Arrays.stream(row).sum())
                        .reduce(Integer::sum)
                        .get();

                if (dangerLevel > mostDangerLevel){
                    coordX = i + 1;
                    coordY = j + 1;
                    mostDangerLevel = dangerLevel;
                }
            }
        }
        Map<String, Integer> data = new HashMap<>();
        data.put("X", coordX);
        data.put("Y", coordY);
        data.put("dangerLevel", mostDangerLevel);

        return data;
    }

    private int[][] getSubmatrixFromMatrix(int[][] matrix, int xCoord, int yCoord, Integer... size){
        int length = size.length != 0 ? size[0] : 3;

        return Arrays.stream(Arrays.copyOfRange(matrix, yCoord, yCoord + length))
                .map(row -> Arrays.copyOfRange(row, xCoord, xCoord + length))
                .toArray(int[][]::new);
    }

    private void printMatrix(int[][] matrix){
        Arrays.stream(matrix)
                .map(Arrays::toString)
                .forEach(System.out::println);
    }
}
