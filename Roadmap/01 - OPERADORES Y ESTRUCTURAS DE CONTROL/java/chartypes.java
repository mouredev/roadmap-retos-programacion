class chartypes{
  public static void main(String[] args){
    operations();
    conditions();
    loops();
    iterNumbers();



  }

  public static void operations(){
    // Asignacion
    int number = 1;
    String phrase = "Hello World";

    // Aritmeticos
    int sum = 1 + 1;
    int sub = 1 - 1;
    int mul = 1 * 1;
    int div = 1 / 1;
    int mod = 1 % 1;

    // Logicos
    boolean isTrue = true;
    boolean isFalse = false;
    boolean and = isTrue && isFalse;
    boolean or = isTrue || isFalse;
    boolean not = !isTrue;

    // Comparacion
    boolean equal = 1 == 1;
    boolean notEqual = 1 != 1;
    boolean greater = 1 > 1;
    boolean less = 1 < 1;
    boolean greaterEqual = 1 >= 1;
    boolean lessEqual = 1 <= 1;

  }

  public static void conditions(){
    int number = 1;
    // If Else
    if(true){
      System.out.println("Is True");
    }else{
      System.out.println("Is False");
    }

    // Switch
    switch(number){
      case 1:
        System.out.println("Is 1");
        break;
      case 2:
        System.out.println("Is 2");
        break;
      default:
        System.out.println("Is not 1 or 2");
    }
  }

  public static void loops(){
    // For
    for(int i = 0; i < 10; i++){
      System.out.println(i);
    }

    // For each
    int[] numbers = {1,2,3,4,5};
    for(int numb : numbers){
      System.out.println(numb);
    }

    // While
    int i = 0;
    while(i < 10){
      System.out.println(i);
      i++;
    }

    // Do While
    i = 0;
    do{
      System.out.println(i);
      i++;
    }while(i < 10);

  }

  public static void iterNumbers(){
    for(int i=10; i<=55; i++){

      if (i % 2 == 0 && i % 3 != 0 && i != 16){
        System.out.println(i);
      }

    }
  }

}

