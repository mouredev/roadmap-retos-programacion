/*
* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*/
#include<iostream>
#include <cstring> // copiar, concatenar, mayuscula_strupr, minuscula_strlwr
#include <string.h> // comparar
#include <algorithm> // reverse_cadena
#include <cctype> // tolower
#include <ctype.h> // toupper


using namespace std;

void copiar_strcpy();
void comparar_strcmp();
void concatenar_strcat();
void mayusculas_strupr();
void minuscula_strlwr();
void reverse_cadena();
//* extra
string tolower_p(string);
string eliminar_espacios(string);
void respuesta_solo(string, string);
void respuesta_duo(string, string, string);
void ejercicio_extra();
bool palindromo(string);
bool anagrama(string, string);
bool isograma(string);

int main(){

  copiar_strcpy();
  comparar_strcmp();
  concatenar_strcat();
  mayusculas_strupr();
  minuscula_strlwr();
  reverse_cadena();

  ejercicio_extra();

  return 0;
}

void copiar_strcpy(){
  //? strcpy copiar una cadena de caracteres de una úbicación a otra
  //! sintaxis:  char *strcpy(char *destino, const char *origen);

  cout << "\n\t---------------- strcpy (copiar)-------------\n";
  char origen[] = "hola mundo"; // cadena origen
  char destino[strlen(origen + 1)]; // el puntero destino tine que tener espacio para la cadena origen, mas caracter final nulo
  strcpy(destino, origen); // desdpues de esto, la variable destino tambien tendrá el valor "hola mundo"
  cout << "origen: " << origen << endl;
  cout << "destino: " << destino << endl;
}

void comparar_strcmp(){
  //? strcmp compara uno a uno los caracteres de las cadenas hasta encontrarlas o encontrar una diferencia
  //* devuelve 0 si ambas cadenas son iguales
  //* devuelve un valor negativo si la primera cadena es menor a la segunda en valor lexicografico
  //* devuelve un valor positivo si la primera es mayor a la segunda en valor lexicografico
  //! sintaxis: int strcmp(const char *s1, const char *s2);
  //* s1 y s2 son los punteros a las cadenas a las cuales se desea comparar

  cout << "\n\t ----------------strcmp (comparar)--------------\n";
  char str1[] = "hola";
  char str2[] = "mundo";
  int resultado = strcmp(str1, str2);
  cout << "resultado: " << resultado << endl;
  if(resultado ==0){
    cout << "ambas cadenas son iguales" << endl;
  }else if(resultado > 0){
    cout << "la primera cadena es mayor" << endl;
  }else{
    cout << "la segunda cadena es mayor" << endl;
  }
}

void concatenar_strcat(){
  //? strcat se utiliza para concatenar cadenas, agrega una copia de la cadena origen al final de la cadena destino
  //? y devuelve la direccion a la que apunta la variable destino
  //! sintaxis: strcat(char *destino, const char *fuente)
  //* es importante que la cadena destino deve ser los suficiente grande para contener la cadena resultante 
  //* incluyendo el valor nulo del final
  cout << "\n\t --------------strcat (concatenar)-----------\n";

  char cadena_1[20] = "Esta cadena";
  char cadena_2[20] = "ocupa 2";
  char cadena_3[20] = "hola";

  strcat(cadena_1, cadena_2);
  strcat(cadena_3, " como estas?");

  cout<< "cadena 1: " << cadena_1 << endl;
  cout << "cadena 3: " << cadena_3 << endl;
}

void mayusculas_strupr(){
  //? strupr convierte las letras contenidas en la cadena en mayusculas y devuelve el puntero a la cadena
  //* strupr no esta en todas las implementaciones, pero se puede usar _strupr_s en visual , este requiere
  //* el tamaño del array como segundo argumento o un array de tamaño conocido en tiempo de compilacion.

  cout << "\n\t ------------strupr (mayusculas)-----------\n";
  char texto[] = "hola lector";
  cout << "cadena original: " << texto << endl;
  strupr(texto); // al parecer si se puedo :v
  // _strupr_s(texto, sizeof(texto));
  cout << "el texto en mayuscula es: " << texto << endl;

  //* usando toupper
  char a = 'a';
  cout << a << endl;
  a = toupper(a);
  cout << "toupper char: " << a << endl;

  //* usando trannsform 
  string tex = "hola";
  transform(tex.begin(), tex.end(), tex.begin(), ::toupper);
  cout << "toupper string: " << tex << endl;
}

void minuscula_strlwr(){
  //? strlwr convierte a las letras de la cadena de caracteres en minusculas y devuleve un puntero a la cadena
  cout << "\n\t ----------strlwr (minusculas)------------\n";
  char texto[] = "HOLA LECTOR";
  cout << "texto original: " << texto<<endl;
  strlwr(texto);
  cout << "texto en minusculas es: " << texto << endl;

  //* usando tolower
  char a = 'A';
  cout << a<<endl;
  a = tolower(a);
  cout << "tolower en char: " << a << endl;

  //* usando transform, para combertir todos los caracteres de una cadena en minuscula
  string str = "HOLA";
  cout << str << endl;
  transform(str.begin(), str.end(),str.begin(), ::tolower);
  cout << "tolower con trasform: " << str << endl;
}

void reverse_cadena(){
  cout << "\n\t ------------reverse------------------\n";
  string texto = "hola mundo";
  cout << "el texto original es: " << texto << endl;
  reverse(texto.begin(), texto.end());
  cout << "el texto invertido es: " << texto << endl;
}

/*
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
*/


string tolower_p(string palabra){
   transform(palabra.begin(), palabra.end(), palabra.begin(), ::tolower);
   return palabra;
}

string eliminar_espacios(string palabra){
 
  palabra.erase(remove(palabra.begin(), palabra.end(), ' '), palabra.end());
  return palabra;
}

bool palindromo(string palabra){
  //? palabra que se lee igual en ambos sentidos
  //! ejemplo renoconocer, Dábale arroz a la zorra el abad
  palabra = tolower_p(palabra);
  string copia = palabra;
  reverse(palabra.begin(), palabra.end());
  return palabra == copia;
}

bool anagrama(string palabra_1, string palabra_2){
  //? palabra o frase formada al reordenar las letras de una palabra o oracion original
  //! ejemplo de GOTA, sale GATO
  //* no puede ser un anagrama si los tamaños son diferentes
  if(palabra_1.size() != palabra_2.size()){
    return false;
  }

  //* ordenar ambas palabras
  sort(palabra_1.begin(), palabra_1.end());
  sort(palabra_2.begin(), palabra_2.end());

  return palabra_1 == palabra_2;
}

bool isograma(string palabra){
  //? es un tipo de diagrama que representa cualidades o circunstancias iguales referidas a cosas distintas
  //! También se refiere a una palabra en la cual ninguna letra se repite

  for (size_t i = 0; i < palabra.size() - 1;i++){
    if(palabra[i]== palabra[i+1]){
      return false;
    }
  }

  return true;
}
//* respusta de una palabra , con el tipo
void respuesta_solo(string palabra, string mensaje){
  cout << "la palabra: " << palabra << mensaje << endl;
  cout << endl;
}

void respuesta_duo(string palabra_1, string palabra_2,string texto){
  cout << "la palabra: " << palabra_1 << " y la palaba: " << palabra_2 << texto << endl;
  cout << endl;
}

//* funcion principal 
void ejercicio_extra(){

  string palabra_1;
  string palabra_2;
  
  bool respuesta_1, respuesta_2,respuesta_anagrama;
  cout << "ingrese la primera palabra: ";
  getline(cin, palabra_1);
  cout << "ingrese la segunda palabra: ";
  getline(cin, palabra_2);
  
  string compacto_1= eliminar_espacios(palabra_1);
  string compacto_2= eliminar_espacios(palabra_2);

  respuesta_1 = palindromo(compacto_1);
  respuesta_2 = palindromo(compacto_2);

  //* ver si las palabras son palindroma, anagrama o isograma

 if(respuesta_1){
   respuesta_solo(palabra_1, " es palindromo");
 }else{
   respuesta_1 = isograma(compacto_1);
   if(respuesta_1){
     respuesta_solo(palabra_1, " es isograma");
   }
 }

 if(respuesta_2){
   respuesta_solo(palabra_2, " es palindromo");
 }else{
   respuesta_2 = isograma(compacto_2);
   if(respuesta_2){
     respuesta_solo(palabra_2, " es isograma");
   }
 }

 respuesta_anagrama=anagrama(compacto_1, compacto_2);
 if(respuesta_anagrama){
   respuesta_duo(palabra_1, palabra_2, " ambas son anagramas");
 }
}