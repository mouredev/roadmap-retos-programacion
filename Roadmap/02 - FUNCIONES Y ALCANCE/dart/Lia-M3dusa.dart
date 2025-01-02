
void ExamplePrint(){
  print("Hello World");
}

int sum(int a, int b){
  return a + b;
}

int substract(int a, int b){
  return a - b;
}

int twoString(String a, String b){
  int contenoNumeros = 0;

  for(int i=1; i<=100; i++){
    if (i % 3 == 0){
      print(a);
    }else if(i % 3 == 0 && i % 5 == 0){
      print(a + b);

    }
    else if (i % 5 == 0){
      print(b);
    }else{
      print(i);
      contenoNumeros++;
    }
  }
  return contenoNumeros;
}

//variable global
String global = "esto es global";

void main(List<String> args) {
  
  //Variable local
  String local= "esto es local";
  
  //Funcion anidada 
  void fExternal(){
    void fInternal(){
      print("Esto es interna");
    }
    print("Esto es externa");
    fInternal();
  }
  fExternal();

  //Funciones
  ExamplePrint();
  print(sum(5, 5));
  print(substract(5, 5));
  print(global);
  print(local);

  //Funcion que recibe dos strings y un numero
  print(twoString("Fizz", "Buzz"));
}