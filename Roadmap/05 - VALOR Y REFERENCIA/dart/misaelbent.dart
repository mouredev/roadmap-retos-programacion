
void main(List<String> arguments) {
  exchange(1, 2);

  List<int> list1 = [1, 2, 3];
  List<int> list2 = [4, 5, 6];

  exchangeList(list1, list2);
}

//Asignacion por valor Inmutables - aplica a datos primitivos como int, double, String
double c = 0.5;
double d = c;

//Asignar por referencia Mutables - aplica List y mapas
List<int> listA = [1, 2, 3];
List<int> listB = listA;

//EXTRA

//Esta funcion intercambia los valores
void exchange(int a, int b) {
  int temp = a;
  a = b;
  b = temp;
  print('$a y $b');
}

void exchangeList(List<int> a, List<int> b) {
  List<int> temp = a;
  a = b;
  b = temp;
  print('$a y $b');
}
