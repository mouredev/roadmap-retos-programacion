import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().sortingHat();
    }

    private House hWarrior = new House("Guerrero");
    private House hRogue = new House("Pícaro");
    private House hWizard = new House("Mago");
    private House hBard = new House("Bardo");

    private List<House> houseList = Arrays.asList(hWarrior, hRogue, hWizard, hBard);
    private List<Question> questionList = new ArrayList<>();
    final private Scanner sc = new Scanner(System.in);
    private String[] letters = new String[] {"a", "b", "c", "d"};

    private boolean was_tied = false;

    public void sortingHat(){
        initQuestions();

        try(sc){
            System.out.println("Bienvenido/a al sombrero seleccionador, donde se " +
                    "elegirá la casa a la que pertenecerás. Para ello deberás responder " +
                    "10 preguntas");
            System.out.print("Introduce tu nombre: ");
            String userName = sc.nextLine();

            Collections.shuffle(questionList);
            int counter = 1;
            for (Question q : questionList){
                Answer answer = askQuestion(q, counter++);
                hWarrior.addAffPoints(answer.getWARRIOR_HOUSE_POINTS());
                hRogue.addAffPoints(answer.getROGUE_HOUSE_POINTS());
                hWizard.addAffPoints(answer.getWIZARD_HOUSE_POINTS());
                hBard.addAffPoints(answer.getBARD_HOUSE_POINTS());
            }

            House chosenHouse = chooseHouse();
            if (was_tied)
                System.out.println("La desición ha sido muy complicada, pero...");

            System.out.println(userName + ", tu casa será.... ¡La casa del " + chosenHouse.getNAME() + "!");
            System.out.println("\nResultados: ");
            for (House house : houseList)
                System.out.println("Casa del " + house.getNAME() + ": " + house.getAffinityPoints());
        }


    }

    private void initQuestions(){
        //Pregunta 1
        Question question = new Question("¿Si fueras un animal, cuál serías?");
        Answer answer1 = new Answer("Un león", 2, 0, 0,1);
        Answer answer2 = new Answer("Un ratón", 0, 2, 0,0);
        Answer answer3 = new Answer("Un cuervo", 0, 0, 2,0);
        Answer answer4 = new Answer("Un grillo", 0, 1, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 2
        question = new Question("¿Qué atributo valoras mas?");
        answer1 = new Answer("La fuerza", 2, 1, 0,0);
        answer2 = new Answer("La destreza", 1, 2, 0,0);
        answer3 = new Answer("La inteligencia", 0, 0, 2,1);
        answer4 = new Answer("El carisma", 0, 0, 1,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 3
        question = new Question("¿Cuál es tu comida favorita?");
        answer1 = new Answer("Pollo con patatas", 2, 0, 0,0);
        answer2 = new Answer("Una ensalada ligera", 0, 2, 0,0);
        answer3 = new Answer("Bacalao con costra de mahonesa de pera", 0, 0, 2,0);
        answer4 = new Answer("Lo que sea pero con cerveza", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 4
        question = new Question("¿Dónde irías de viaje?");
        answer1 = new Answer("A la montaña", 2, 0, 0,0);
        answer2 = new Answer("Al bosque", 0, 2, 0,0);
        answer3 = new Answer("A la playa", 0, 0, 2,0);
        answer4 = new Answer("A una gran capital", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 5
        question = new Question("¿Qué arma pillarías si hay una emergencia y te tienes que equipar rápido?");
        answer1 = new Answer("Un martillo a dos manos", 2, 0, 0,0);
        answer2 = new Answer("Un arco", 0, 2, 0,0);
        answer3 = new Answer("Una varita", 0, 0, 2,0);
        answer4 = new Answer("Una espada a una mano", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 6
        question = new Question("¿Cuál es tu película favorita?");
        answer1 = new Answer("Gladiator", 2, 0, 0,0);
        answer2 = new Answer("Robin Hood", 0, 2, 0,0);
        answer3 = new Answer("Harry Potter", 0, 0, 2,0);
        answer4 = new Answer("La La Land", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 7
        question = new Question("Hay una puerta cerrada, ¿Cómo la abres?");
        answer1 = new Answer("Con una patada", 2, 0, 0,0);
        answer2 = new Answer("Uso unas ganzuas", 0, 2, 0,0);
        answer3 = new Answer("Uso un hechizo", 0, 0, 2,0);
        answer4 = new Answer("Busco a alguien que tenga la llave y lo convenzo", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);

        //Pregunta 8
        question = new Question("¿Qué lugar se te viene a la mente al decir <<Hogar>>?");
        answer1 = new Answer("Cualquier sitio con una buena cama limpia, como un hostal", 2, 0, 0,0);
        answer2 = new Answer("Un sitio cómodo y sin miradas indiscretas, como un callejón", 0, 2, 0,0);
        answer3 = new Answer("Una torre, donde estar tranquilo", 0, 0, 2,0);
        answer4 = new Answer("Una taverna, y si hay mucha gente, mejor", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);


        //Pregunta 9
        question = new Question("Tienes que obtener un objeto que está en posesión de una" +
                " persona ¿Cómo lo consigues?");
        answer1 = new Answer("Noqueo al que tiene el objeto y lo pillo", 2, 0, 0,0);
        answer2 = new Answer("Uso el sigilo y lo robo sin que se de cuenta", 0, 2, 0,0);
        answer3 = new Answer("Uso un hechizo para dormir a la persona y pillo el objeto", 0, 0, 2,0);
        answer4 = new Answer("Hablo con él y lo convenzo de que el objeto está mejor conmigo", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);


        //Pregunta 10
        question = new Question("Necesitas dinero rápido ¿Cómo lo ganas?");
        answer1 = new Answer("Ayudo a cualquier comercio llevando carga", 2, 0, 0,0);
        answer2 = new Answer("Lo robo a alguna persona pudiente", 0, 2, 0,0);
        answer3 = new Answer("Creo alguna poción y la vendo en el mercado", 0, 0, 2,0);
        answer4 = new Answer("Interpreto en la plaza con mi laud", 0, 0, 0,2);
        question.setAnswerList(Arrays.asList(answer1, answer2, answer3, answer4));
        questionList.add(question);
    }

    private Answer askQuestion(Question question, int qCounter){
        System.out.println("---Pregunta " + qCounter + "---");
        System.out.println(question.getText());

        List<Answer> answerList = question.getAnswerList();
        Collections.shuffle(answerList);
        int counter = 0;
        for (Answer a : answerList){
            System.out.println(letters[counter++] + ". " + a.getText());
        }

        String userAnswer = askValidAnswerToUser();
        System.out.println("------------------");
        return answerList.get(Arrays.asList(letters).indexOf(userAnswer));
    }

    private String askValidAnswerToUser(){
        boolean validAnswer = false;
        String userAnswer = null;
        while(!validAnswer){
            System.out.print("Respuesta: ");
            userAnswer = sc.nextLine().strip().toLowerCase();

            switch (userAnswer){
                case "a": case "b":case "c": case "d":
                    validAnswer = true;
                    break;
                default:
                    System.out.println("Error. Elija una opción válida (a-d)");
            }
        }

        return userAnswer;
    }

    private House chooseHouse(){
        House chosenHouse = null;
        Set<House> tiedHouses = new HashSet<>();
        for (House house : houseList){
            if (chosenHouse == null){
                chosenHouse = house;
                continue;
            }
            if (house.getAffinityPoints() < chosenHouse.getAffinityPoints())
                continue;
            if (house.getAffinityPoints() == chosenHouse.getAffinityPoints()){
                tiedHouses.add(house);
                tiedHouses.add(chosenHouse);
                continue;
            }
            chosenHouse = house;
            tiedHouses.clear();
        }
        if (!tiedHouses.isEmpty()){
            was_tied = true;
            Random rnd = new Random();
            chosenHouse = List.copyOf(tiedHouses).get(rnd.nextInt(tiedHouses.size()));
        }

        return chosenHouse;
    }

    public class House{
        final private String NAME;
        private int affinityPoints;

        public House(String name) {
            this.NAME = name;
            affinityPoints = 0;
        }

        public String getNAME() {
            return NAME;
        }

        public int getAffinityPoints() {
            return affinityPoints;
        }

        public void addAffPoints(int amount){
            affinityPoints += amount;
        }
    }

    public class Question{
        private String text;
        private List<Answer> answerList;

        public Question(String text) {
            this.text = text;
        }

        public Question(String text, List<Answer> answerList) {
            this.text = text;
            this.answerList = answerList;
        }

        public String getText() {
            return text;
        }

        public List<Answer> getAnswerList() {
            return answerList;
        }

        public void setAnswerList(List<Answer> answerList) {
            this.answerList = answerList;
        }
    }
    public class Answer{
        private String text;
        final private int WARRIOR_HOUSE_POINTS;
        final private int ROGUE_HOUSE_POINTS;
        final private int WIZARD_HOUSE_POINTS;
        final private int BARD_HOUSE_POINTS;

        public Answer(String text, int WARRIOR_HOUSE_POINTS, int ROGUE_HOUSE_POINTS,
                      int WIZARD_HOUSE_POINTS, int BARD_HOUSE_POINTS) {
            this.WARRIOR_HOUSE_POINTS = WARRIOR_HOUSE_POINTS;
            this.ROGUE_HOUSE_POINTS = ROGUE_HOUSE_POINTS;
            this.WIZARD_HOUSE_POINTS = WIZARD_HOUSE_POINTS;
            this.BARD_HOUSE_POINTS = BARD_HOUSE_POINTS;
            this.text = text;
        }

        public String getText() {
            return text;
        }

        public int getWARRIOR_HOUSE_POINTS() {
            return WARRIOR_HOUSE_POINTS;
        }

        public int getROGUE_HOUSE_POINTS() {
            return ROGUE_HOUSE_POINTS;
        }

        public int getWIZARD_HOUSE_POINTS() {
            return WIZARD_HOUSE_POINTS;
        }

        public int getBARD_HOUSE_POINTS() {
            return BARD_HOUSE_POINTS;
        }
    }
}
