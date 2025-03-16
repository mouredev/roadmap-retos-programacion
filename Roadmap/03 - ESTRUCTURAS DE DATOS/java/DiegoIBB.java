package Estructura_Datos_03;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Estructura_Datos {
	public static void main(String[]args) {
		
		//---------------------------------------------------------------
		//---------------------------- ARRAY ----------------------------
		//---------------------------------------------------------------
		
		System.out.println("-------- ARRAY -------- \n");
		
		/*Un Array es una estructura de almacenamiento que guarda
		 *datos del mismo tipo en una sola variable.*/
		
		String [] cars = {"BMW", "Volvo", "Ford", "Mazda"};
		
		//----- 1) Acceder a elementos
		
		System.out.println("Acces to the fisrt item: " + cars[0]);
		
		//Recorrer un array usando ciclos for

		System.out.println("Array Number_1");
		for(int c=0; c<cars.length; c++) {
			System.out.println("Position: " + c + ", Item: " + cars[c]);
		}

		//Recorrer un Array usando For-each
		
		for (String c : cars) { // Con esta forma no necesitamos especificar la longitud del array
			System.out.println(c);
		}
				
		//----- 2) Métodos sobre los elementos
		
		//Cambiar elementos de un array
		cars[2] = "Mercedes Benz";
		System.out.println("Item 2 change it: " + cars[2]);
		
		//Conocer la cantidad de elementos
		System.out.println("Lenght Array Cars: " + cars.length);
		
		
		//--------------------------------------------------------------------
		//---------------------------- ARRAY LIST ----------------------------
		//--------------------------------------------------------------------
		
		/*Un ArrayList es una estructura que nos permite utilizar métodos para insertar
		 *datos, remover o cambiar dentro de un ArrayList.*/
		
		System.out.println("-------- ARRAY LIST -------- \n");
		
		ArrayList<Integer> numbers = new ArrayList<Integer>();

		numbers.add(1);
		numbers.add(2);
		numbers.add(3);
		numbers.add(4);
		numbers.add(5);
		numbers.add(6);
		numbers.add(7);
		
		//Diferentes tipos de datos en arrays
		
		ArrayList<Double> numbers_2 = new ArrayList<Double>();
		ArrayList<Float> numbers_3 = new ArrayList<Float>();
		ArrayList<Character> numbers_4 = new ArrayList<Character>();

		
		//----- 1) Acceder a elementos
		
		System.out.println(numbers); //Acceder a la lista de elementos
		System.out.println("Pos0: " + numbers.get(0) + " Pos5: " + numbers.get(4)); // Acceder a diferentes elementos por su indice
		
		System.out.println("Usando bucle For");
		for(int i =0; i< numbers.size(); i++) { // Acceder a diferentes elementos por medio de un bucle FOR
			System.out.println(numbers.get(i));
		}
		System.out.println("Usando bucle For-each");
		for (Integer i : numbers) {
			System.out.println(i);
		}

		
		//----- 2) Métodos sobre los elementos
		
		//Método de adición
		numbers.add(8);
		System.out.println("Usando add: " + numbers);
		
		// Método para cambiar un elemento
		numbers.set(0, 10); //Especificamos indice y el nuevo valor
		System.out.println("Usando set: " + numbers);
		
		//Método remove
		numbers.remove(0);
		System.out.println("Usando remove: " + numbers);
		
		//Método clear para remover todos los elementos de un array
		numbers.clear();
		System.out.println("Usando clear: " + numbers);
		
		//Método para conocer el largo de un array
		numbers.add(8);
		numbers.add(5);
		numbers.add(1);
		numbers.add(14);
		System.out.println("Usando size: " + numbers.size());

		//Método para ordenar datos de un array (libreria Collections)
		System.out.println("Datos ordenados usando Collections.sort");
		Collections.sort(numbers);
		for(Integer i: numbers) {
			System.out.println(i);
		}
		
		//--------------------------------------------------------------------------------
		//---------------------------- ARRAY MULTIDIMENSIONAL ----------------------------
		//--------------------------------------------------------------------------------
		
		/* Los arrays multidimensionales son usados cuando se quiere
		 * guardar datos en forma de tablas(filas y columnas), la 
		 * sintaxis es añadiendo cada array dentro de uno general*/
		
		//----- Acceder a los elementos de los arrays -----

		int[][] multiArray = {{1,2,3,4,5}, {6,7,8,9}};

		System.out.println(multiArray[1][3]);
		
		/* En el array anterior seleccionamos el segundo elemento del array (1)
		 * y luego accedemos al tercer elemento del array antes seleccionado (2)
		 * NOTA: En los arrays los valores se organizan desde la posición 0 como
		 * valor inicial*/

		//----- Podemos cambiar elementos del array -----
		// En este caso cambiamos el 4 elemento del primer array de valor 4 a 7
		
		System.out.println("Cambio en el valor de un elemento");
		System.out.println(multiArray[0][3]);
		multiArray [0][3] = 7;
		System.out.println(multiArray[0][3]);
		
		
		//--------------------------------------------------------------------
		//----------------------------- HASH SET -----------------------------
		//--------------------------------------------------------------------
		
		System.out.println("-------- HASH SET -------- \n");

		// Un Hash Set es una estructura de datos que no admite elementos duplicados
		
		Set<String> hash_set = new HashSet<String>(); // Creamos el objeto "hash_set" a partir da la clase Set
		
		//Método para añadir elementos a un set
		
		hash_set.add("Australia");
		hash_set.add("Alemania");		
		hash_set.add("Estados Unidos");
		hash_set.add("Chile");
		hash_set.add("Holanda");
		System.out.println(hash_set);

		//----- 1) Acceder a elementos
		
		System.out.println(hash_set.contains("Alemania"));
		
		//----- 2) Métodos sobre los elementos
		
		Set<String> lenguage_set = new HashSet<String>();
		
		//Método ADD, con el podemos agregar elementos a un set
		lenguage_set.add("Java");
		lenguage_set.add("Python");
		lenguage_set.add("SQL");
		lenguage_set.add("Rust");
		lenguage_set.add("C++");
		lenguage_set.add("C");
		lenguage_set.add("Kotlin");
		
		System.out.println(lenguage_set);
		
		// Método REMOVE, con el podemos quitar elementos de un set
		lenguage_set.remove("Kotlin");		
		System.out.println(lenguage_set);
		
		// Método SIZE, con el podemos obtener la cantidad de elementos de un set
		System.out.println(lenguage_set.size());		
		
		Set<String> lenguage_set_2 = new HashSet<String>();

		lenguage_set_2.add("PHP");
		lenguage_set_2.add("React");
		lenguage_set_2.add("R");
		lenguage_set_2.add("JavaScript");
		lenguage_set_2.add("HTML");
		lenguage_set_2.add("CSS");
		
		// Método ITERATOR, con el podemos iterar sobre los elementos de un set
		Iterator<String> it = lenguage_set_2.iterator();
		while(it.hasNext()) { //Usamos un bucle While y el método hasNext
			System.out.println(it.next()); //Retorna un set vacio
		}
		
		// Método CLEAR, con el podemos borrar todos los elementos de un set
		lenguage_set_2.clear();
		System.out.println(lenguage_set_2); //Retorna un set vacio
		
		
		//--------------------------------------------------------------------
		//----------------------------- HASH MAP -----------------------------
		//--------------------------------------------------------------------
		
		System.out.println("-------- HASH MAP -------- \n");
		
		// Un Hash Map es una estructura de datos que toma valores en la forma Key:Values
		// los valores de las values pueden ser de diferentes tipos, no necesariamente string

		HashMap<String, String> capitalCities = new HashMap<String, String>();
		
		//Añadimos elementos usando el método put
		
		capitalCities.put("England", " London");
		capitalCities.put("Germany", " Berlin");		
		capitalCities.put("Norway", " Oslo");		
		capitalCities.put("USA", " Washington DC");
		System.out.println(capitalCities);
		
		//----- 1) Acceder a elementos
		System.out.println(capitalCities.get("England"));
		
		//----- 2) Métodos sobre los elementos
		
		//Método PUT, con el podemos agregar elementos a un HashMap
	    capitalCities.put("USA", "Washington DC");
		
		//Método REMOVE es utilizado para sacar elementos de un HashMap
		capitalCities.remove("England");
		System.out.println(capitalCities);
		
		//Método SIZE, utilizado para conocer la cantidad de parejas que hay en un HashMap
		System.out.println(capitalCities.size());
		
		//Método CLEAR, se utiliza para limpiar un HashMap de todos los elementos que contiene
		capitalCities.clear();
		System.out.println(capitalCities);
		
		
		capitalCities.put("England", "London");
		capitalCities.put("Germany", "Berlin");		
		capitalCities.put("Norway", "Oslo");		
		capitalCities.put("USA", "Washington DC");
		capitalCities.put("Chile", "Santiago");
		capitalCities.put("Australia", "Camberra");
		
		//----- 1) Acceder a elementos usando un loop
		//Este loop lo usamos para obtener la clave (KEY)
		for(String i: capitalCities.keySet()) {
			System.out.println("Key: " + i);
		}
		//Este loop lo usamos para obtener el valor (VALUE)
		for(String i: capitalCities.values()) {
			System.out.println("Value: " + i);
		}
		
		//--------------------------------------------------------------------
		//---------------------------- DICTIONARY ----------------------------
		//--------------------------------------------------------------------
		
		System.out.println("-------- DICTIONARY -------- \n");

		//La clase dictionay nos permite crear diccionarios con una Key y un Value, es similar al Hashmap
		
		Dictionary<String, Integer> dict = new Hashtable<>();
		
		//Método PUT, con el podemos agregar elementos a un dictionary
		dict.put("Porsche", 1931);
		dict.put("Mercedez Benz", 1926);
		dict.put("Ferrari", 1939);
		dict.put("BMW", 1916);
		
		System.out.println(dict);
		
		//----- 1) Acceder a elementos
		System.out.println(dict.get("BMW"));
		
		//----- 2) Métodos sobre los elementos
		
		//Método REMOVE, para remover elementos
		dict.remove("Ferrari");
		System.out.println(dict);

		//Método SIZE, para conocer el largo de una lista
		System.out.println(dict.size());
		

		//--------------------------------------------------------
		//--------------------- LINKEDLIST -----------------------
		//--------------------------------------------------------
		
		System.out.println("-------- LINKEDLIST -------- \n");
		
		//La estructura linked list nos permite crear conjuntos de datos en formato lista
		//puede contener varios objetos del mismo tipo
		
		LinkedList<String> nombres = new LinkedList<String>();
		
		//Método ADD, con el podemos agregar elementos a un LinkedList
		nombres.add("Serena");
		nombres.add("Diego");
		nombres.add("Alan");
		nombres.add("Pablo");
		nombres.add("Andres");
		nombres.add("Ignacio");
		
		System.out.println(nombres);
		
		//----- 1) Acceder a los elementos
		System.out.println(nombres.get(0));
		System.out.println(nombres.get(1));

		
		//----- 2) Métodos sobre los elementos

		//Método addFirst, añade un item al inicio de la lista
		nombres.addFirst("Maria");
		//Método addLast, añade un item al final de la lista
		nombres.addLast("Jose");
		
		System.out.println(nombres);
		
		// Método POP, para remover el primer elemento de una LinkedList
		nombres.pop();
		System.out.println(nombres);
		
		// Método CONTAINS, para saber si un objeto está en la LinkedList
		System.out.println(nombres.contains("Serena"));
		
		//--------------------------------------------------------------------
		//------------------------------- LIST -------------------------------
		//--------------------------------------------------------------------
		System.out.println("-------- LIST -------- \n");
		
		List<String> letters = new ArrayList<String>();
		
		//Método ADD, con el podemos agregar elementos a una List
		letters.add("A");
		letters.add("B");
		letters.add("C");
		letters.add("D");
		letters.add("E");
		
		System.out.println(letters);
		
		//----- 1) Acceder a los elementos
		System.out.println(letters.get(0));
		System.out.println(letters.get(3));
		
		//----- 2) Métodos sobre los elementos
		
		//Método SET, para cambiar elementos a partir del indice
		letters.set(3, "F");
		letters.add(0, "Z");
		
		//Método REMOVE, para remover elementos
		letters.remove("C");
		letters.remove("B");
		
		System.out.println(letters);
		
		//Método SIZE, para conocer sobre la cantidad de elementos que hay en una lista
		System.out.println(letters.size());
		
		// SORT
		Collections.sort(letters); //Usamos la clase collections con el método sort para ordenar los elementos
		System.out.println(letters);
		
		
		
		//--------------------------------------
		//---------- DIFICULTAD EXTRA ----------
		//--------------------------------------
		/*
		DIFICULTAD EXTRA (opcional):
		* Crea una agenda de contactos por terminal.
		* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
		* - Cada contacto debe tener un nombre y un número de teléfono.
		* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
		*   los datos necesarios para llevarla a cabo.
		* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
		*   (o el número de dígitos que quieras)
		* - También se debe proponer una operación de finalización del programa.
		*/
		HashMap<String, Integer> contact_list = new HashMap<String, Integer>();
		int number_contact;
		
		while (true) {
			// Show Options
			System.out.println("----- Options Available -----");
			System.out.println("1_ Add Contact");
			System.out.println("2_ Search Contact");
			System.out.println("3_ Remove Contact");
			System.out.println("4_ Update Contact");
			
			// Create variables of contact and number
			Scanner contact = new Scanner(System.in);
			Scanner number = new Scanner(System.in);
			
			//Create a global variable HashMap contact_list 

			// Select an option
			Scanner options = new Scanner(System.in);
			System.out.print("Select an option: ");
			int option = options.nextInt();
			
			if(option == 1) {
				System.out.println("Option Selected Add Contact");
				System.out.print("Contact Name: ");
				String name_contact = contact.nextLine();
				System.out.println("New Contact Name: " + name_contact);
				
				System.out.print("Phone Number: ");
			    Integer phone_number = number.nextInt();
				System.out.println("New Contact Number: " + phone_number);
				
				// Add the contact to a Hash Map
				contact_list.put(name_contact, phone_number);
				System.out.println(contact_list);
				
			}else if(option == 2) {
				System.out.println("Option Selected Search Contact");
				System.out.print("Contact Name: ");
				String name_contact = contact.nextLine();
				System.out.println("Phone Number: " + contact_list.get(name_contact));

			}else if(option == 3) {
				System.out.println("Option Selected Remove Contact");
				System.out.println("Contact Name: ");
				String name_contact = contact.nextLine();
				System.out.println(contact_list.remove(name_contact) + "Had been Removed");
				
			}else if(option == 4) { // Resolver la actualizacion del contacto y nombre
				System.out.println("Option Selected Update Contact");
				System.out.println("---- Item to Update ----");
				System.out.println("(1) Contact - (2) Number");
				Scanner itemUpdate = new Scanner(System.in);
				int item = itemUpdate.nextInt();
				
				if(item == 1) {
					//Consultar por contacto a modificar
					Scanner contactOld = new Scanner(System.in);
					System.out.print("Contact to change: ");
					String old_contact = contactOld.nextLine();
					//Definir nuevo nombre del contacto
					Scanner contactNew = new Scanner(System.in);
					System.out.print("New Name Contact: ");
					String new_contact = contactNew.nextLine();
					number_contact = contact_list.get(old_contact);
					//Eliminar conacto antiguo y agregar nuevo contacto
					contact_list.remove(old_contact);
					contact_list.put(new_contact, number_contact);
					System.out.println(contact_list);
				}else if(item == 2) {
					//Seleccionar contacto a cambiar el nombre
					Scanner contactNum = new Scanner(System.in);
					System.out.print("Contact to change number: ");
					String contact_num = contactNum.nextLine();
					//Solicitar nuevo número
					System.out.println("Old Number: " + contact_list.get(contact_num));
					Scanner newNumber = new Scanner(System.in);
					System.out.print("New Number: ");
					int number_new = newNumber.nextInt();
					//Quitar contacto con numero antiguo
					contact_list.remove(contact_num);
					// Añadir contacto con nuevo numero
					contact_list.put(contact_num, number_new);
					
				}
			}else {
				System.out.println("Option Not Available");
			}
			
			// Ask for more operations or end the program
			Scanner moreOperations = new Scanner(System.in);
			System.out.print("Another Operation yes(1)/no(2)?: ");
			int mOperation = moreOperations.nextInt();
			
			if (mOperation == 1) {
				continue;
			}else if (mOperation == 2){
				System.out.println("Program Ended");
				System.out.println(contact_list);
				break;
			}else {
				System.out.println("Option not available");
			}
	}
	}
}
