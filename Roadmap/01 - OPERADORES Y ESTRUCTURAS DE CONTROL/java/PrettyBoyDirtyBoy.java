/**
 *
 * @author Alan Bautista Desde Colombia
 */
public class PrettyBoyDirtyBoy {

  
    public static void main(String[] args) {

    // Ejemplos de Operadores Aritmeticos
    
    int a = 12;
    int b = 13;
        System.out.println("Aritmeticos");

    
    System.out.println(a + b);
    System.out.println(a - b);
    System.out.println(a * b);  
    System.out.println(a / b);
    System.out.println(a % b);
    
    // Ejemplos operadores Asignacion
    
     System.out.println("Asignacion");  

    
    System.out.println(a += 4);
    System.out.println(a *= 7);  

    // Ejemplos operadores Comparacion
     System.out.println("Comparacion");  
    
    
     int c = 14;
     int d = 15;
     int e = 16;
     int f = 17;
     
      System.out.println(c == d);
      System.out.println(c > d); 
      System.out.println(c < d); 
      System.out.println(c >= d); 
      System.out.println(c <= d);
      
     // Ejemplos operadores Comparacion
     System.out.println("Logicos"); 
     
     System.out.println(c > d || d==2);
     
     System.out.println(c > d); 
     System.out.println(c < d); 
     System.out.println(c >= d); 
     System.out.println(c <= d);
      
     System.out.println("Logicos"); 

     System.out.println("Logicos (o)"); 

     // Or (O)
     System.out.println(c >d || d==15);
     System.out.println(e < f || f!=17); 
     System.out.println(9<= 8 || 450==449 ); 
     System.out.println(7 >= 9 || 22 == d); 

     // And (y)
     System.out.println("Logicos (y)"); 

     System.out.println(49>d && d==15);
     System.out.println(e < f && f!=17); 
     System.out.println(9>= 8 && 450==450 ); 
     System.out.println(7 >= 9 && 22 == d); 

     // Not
     
     System.out.println("Logicos (Not)"); 
     
     System.out.println(!(49>d)&& d==15);
     System.out.println(!(e > f) && f==17); 
     System.out.println(!(9>=8) && 450==450 ); 
     System.out.println(!(7 >= 9) && 22 == 22); 
     
     // urinarios
     
    int g = 18;
    System.out.println(g--);
    System.out.println(--g);
    System.out.println(++g);
    System.out.println(-g);
    System.out.println(g++);
    
    
    if((!(49>d)|| d==15)||(!(9>=8) && 450==450 )){
       System.out.println(" bien");
    }else{System.out.println("Malisimo");
               }  
    
    if( 17 >= 18 || 450==449 ){
       System.out.println("bien");
    }else{System.out.println("Malisimo");
               }  
    
    

    String dia = "Lunes";
    
    switch (dia){
       case "Lunes":
       System.out.println("1"); 
       break;
       case "Martes":
       System.out.println("2");  
       break;
       case "Miercoles":
       System.out.println("3");  
       case "Jueves":
       System.out.println("4");
       case "Viernes":
       System.out.println("5"); 
       break;
   }
    
       int numero = 5;
    
    switch (numero){
       case 1:
       System.out.println("Primero"); 
       break;
       case 2:
       System.out.println("Segundo");  
       break;
       case 3:
       System.out.println("Tercero");  
       case 4:
       System.out.println("Cuarto");
       case 5:
       System.out.println("Quinto"); 
       break;
   }
 
      
    int h = 19;
    int y = 20;
    char operacion ='*';
    
     switch (operacion){
       case '+':
       System.out.println(y + h); 
       break;
       case '-' :
       System.out.println(y - h);  
       break;
       case '*':
       System.out.println(y * h);  
       break;
       case '/':
       System.out.println(y / h);
       break;
   }
    
     int opcion = 99;
     
     switch (opcion){
     case 1:
     System.out.println("Hamburguesa Triple");
     break;
     case 2:
     System.out.println("Pizza Hawaina");
     break;
     case 3:
     System.out.println("Perro suizo");
     break;
     case 4:
     System.out.println("Asado de Pollo");
     break;
     case 5:
     System.out.println("Asado de Cerdo");
     break;
     default:
     System.out.println("Opcion no valida");
     }
     
     
     int numeros = 1;
     
     while(numeros <= 10){
      System.out.println(numeros);
        numeros = numeros + 1;
     } 
        
     System.out.println("Separador");
     int N = 10;
     
     while(N >= 1){
      System.out.println(N);
        N = N - 1;
      
     }
     
    System.out.println("Separador");
     
     
     int Number = 2;
     
      while(Number <= 20){
      System.out.println(Number);
        Number = Number + 2;
     } 
    
      int Numbers = 1;
      int sumaTotal = 0; // El acumulador que guarda la suma simultánea

      
      while(Numbers <= 10){
      System.out.println(Numbers);
        sumaTotal += Numbers;
        Numbers++;
        
      }
      System.out.println("La Suma total es" + " "+ sumaTotal);
       
       System.out.println("ciclo do while");

      int Index = 1;
     
      do{
        System.out.println(Index);
        Index = Index + 1;  
        
      } while(Index <= 10);
      
      int ing = 10;
      
      do{
      System.out.println(ing );
      ing = ing - 1;
     } while(ing >= 1);
      
      
      int rma = 1;
      
      do{
      System.out.println(rma);
      rma = rma + 2;
     }while(rma <= 15);
      
      int Bar = 1;
      int Total= 0;
      
      do{
      System.out.println(Bar);
      Total += Bar;
      Bar++;
      }while (Bar <= 10);
      
      System.out.println("La Suma Total es"+" "+Total);
      
      for(int i = 1; i<=10; i++){
        System.out.println(i);
      }
      
      for(int j = 2; j<=20; j+=2){
        System.out.println(j);
     } 
   
      for(int j = 10; j>=1; j-=1){
        System.out.println(j);
      }
      
      int t = 0;
      for (int i = 1; i<=10; i++){
          t += i;
      
      }
      System.out.println("la suma total es "+ " "+t);
      
      
      String [] empleados = new String [50];
      
      for(int i =0; i <= 49;i++){
      empleados[i] = "Persona " + ( i + 1);  
        
      
      }
      System.out.println(empleados.length);

             
      String [] frutas = {"Durazno","Naranja","Banana","Mango","Lichi"};
      
      boolean encontrado = false;
      
      for (String fruta:frutas){
         if (fruta.equals("Mango")){
         System.out.println("encontre el Mango");   
      } 
      
  }
      int[] C = {12, 5, 27, 8, 31, 4, 19};
      
      int contador = 0;
      
      for (int Co :C){
       if (Co >= 15){
        contador++;
    }
  }
     System.out.println("La Cantidad de numeros mayores que 15 es : "+contador);   
    
              
     String [] names = {"Marcos","Mateo","Lucas","Juan","Sebastian"};
          
     
      String nombreLargo = names[0];
     
      for (String name : names){
        if (name.length()> nombreLargo.length()){
          nombreLargo = name;     
        }  
      }
          System.out.println(nombreLargo);
              
    
      
    String [] productos ={"Arroz","Leche","Cafe","Queso","Huevos"};
       int[] cantidades = {10, 3, 0, 7, 5};
        

      int contar = 0;
       for (int K:cantidades){
        if(K == 0){
       System.out.println(productos[contar]+" Agotado");    
        }  
        contar++;
       }
       
       
       int J = 10;
       int H = 0;
       
       
       try{
         System.out.println(J/H);
          }catch (Exception l) {
           System.out.println("No se puede dividir entre 0" );
       }
       
       String Nume ="Hola";
       
         
       try{
         System.out.println(Nume);
         Integer.parseInt(Nume);
         
          }catch (Exception l) {
           System.out.println("Un numero no una palabra" );
       }
       
       int[] cantidad = {10, 20, 30,40,50};
       
       try{
          System.out.println(cantidad[10]);
       }catch(ArrayIndexOutOfBoundsException p){
           System.out.println("No existe ese elemento");
           
       }
       
       String Digito = "25";
       int[] Digitos = {10,20,30};
       
       try{
        System.out.println(Digito);
         Integer.parseInt(Digito);

        System.out.println(Digitos[10]);
       }catch(NumberFormatException ñ){
             System.out.println("Un numero no una palabra" );
       } catch( ArrayIndexOutOfBoundsException pñ ){
        System.out.println("No existe ese elemento");
     }
   
       // Ejemplo 1 ejercicio adicional
    
    int[] datosConsola = {
    10, 14, 20, 22, 
    26, 28, 32, 34, 38, 40,
    44, 46, 50
};
    
    for( int DC :datosConsola){
     System.out.println(DC);
        
    }
    
    // ejemplo 2
    for (int i = 10; i<=55; i++){ 
       if(i % 2==0 && i != 16 && i % 3 != 0 ){
           System.out.println(i);
       }
        
      }
    
    } 
    
}
   
