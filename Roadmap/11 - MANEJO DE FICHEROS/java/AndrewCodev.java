import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.Scanner;

public class AndrewCodev {
	public static void main(String[] args) {
        //Los ejercicios estan separados para seleccionar entre uno y otro comentar y descomentar cada uno.
		//ejemploManejoArchivos();
		gestionVentas();
	}

	// DIFICULTAD EXTRA
	public static void gestionVentas() {
		String nombreArchivo = "GestionVentas.txt";
		Scanner scanner = new Scanner(System.in);
		List<String> contenidoArchivo;
		try {
			crearArchivo(nombreArchivo);

			contenidoArchivo = new ArrayList<>(Files.readAllLines(Paths.get(nombreArchivo)));

			System.out.println("\nGESTOR DE VENTAS\n");
			System.out.println("1 AGREGAR PRODUCTO");
			System.out.println("2 LEER EL ARCHIVO");
			System.out.println("3 MODIFICAR PRODUCTO");
			System.out.println("4 CALCULAR TOTAL DE PRECIOS");
			System.out.println("5 ELIMINAR PRODRUCTO");
			System.out.println("6 CERRAR APLICACIÓN");

			String opcionMenu = recibirScanner(scanner);

			switch (opcionMenu) {
			case "1": {
				String detalleProducto = lineaArchivo(scanner, contenidoArchivo, nombreArchivo, 
						contenidoArchivo.size());
				anexarArchivo(nombreArchivo, detalleProducto);
				gestionVentas();
				break;
			}
			case "2": {
				System.out.println("\nDETALLE DE VENTAS\n");
				leerArchivo(nombreArchivo);
				// REVISAR SUBMENU
				gestionVentas();
				break;
			}
			case "3": {
				// Pasamos las filas al una lista para modificar
				try {

					leerArchivo(nombreArchivo);					
					
					if (contenidoArchivo.size() > 1) {
						System.out.println(
								"Escribe un número del 0 al " + (contenidoArchivo.size() - 1) + " la fila a Modificar");
					} else if (contenidoArchivo.size() == 1) {
						System.out.println(
								"Escribe un número: " + (contenidoArchivo.size() - 1) + " para modificar la linea");
					} else {
						System.out.println("El archivo no tiene productos");
					}
					
					
					int idEditado = Integer.parseInt(recibirScanner(scanner));

					String detalleProducto = lineaArchivo(scanner, contenidoArchivo, nombreArchivo, 
							idEditado);
					leerArchivo(nombreArchivo);

					contenidoArchivo.set((idEditado), detalleProducto);

					Files.write(Paths.get(nombreArchivo), contenidoArchivo);
					gestionVentas();
				} catch (IOException e) {
					e.printStackTrace();
				}
				break;
			}
			case "4": {
				double sumTotalPrecios = 0;
				String inputString = "";
				for (int i = 0; i < contenidoArchivo.size(); i++) {
					inputString = contenidoArchivo.get(i).replace("[", "").replace("]", "");
					
					String array[] = inputString.split(",");
					sumTotalPrecios = sumTotalPrecios + Double.parseDouble(array[4]);
				}
				leerArchivo(nombreArchivo);
				System.out.println("PRECIO TOTAL: " + sumTotalPrecios);
				gestionVentas();
				break;
			}
			case "5": {
				try {
					leerArchivo(nombreArchivo);
					if (contenidoArchivo.size() > 1) {
						System.out.println(
								"Escribe un número del 0 al " + (contenidoArchivo.size() - 1) + " la fila a eliminar");
					} else if (contenidoArchivo.size() == 1) {
						System.out.println(
								"Escribe un número: " + (contenidoArchivo.size() - 1) + " para eliminar la linea");
					} else {
						System.out.println("El archivo no tiene productos");
					}

					int idELiminado = Integer.parseInt(recibirScanner(scanner));

					if (idELiminado >= 0 && idELiminado < contenidoArchivo.size()) {
						// Eliminar la línea específica
						contenidoArchivo.remove(idELiminado);

						// Escribir el contenido modificado de nuevo en el archivo
						Files.write(Paths.get(nombreArchivo), contenidoArchivo);
						System.out.println("La línea ha sido eliminada exitosamente.");
					} else {
						System.out.println("Número de línea fuera de rango.");
					}

					gestionVentas();
				} catch (IOException e) {
					e.printStackTrace();
				}
				break;
			}
			case "6": {
				eliminarArchivo(nombreArchivo);
				break;
			}
			default:
				System.err.println("La opción no es valida, intentelo de nuevo");
				gestionVentas();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static String recibirScanner(Scanner scanner) {
		String dato = scanner.nextLine();
		return dato;
	}

	public static String lineaArchivo(Scanner scanner, List<String> contenidoArchivo, String nombreArchivo,
			int idProducto) {
		String lineaArchivo = "";
		try {
			String nombreproducto;
			int cantidad;
			double precio;
			double totalPrecio;
			//int idProducto = 0;

			//idProducto = contenidoArchivo.size();
			System.out.println("Ingresa el nombre del producto");
			nombreproducto = recibirScanner(scanner);
			System.out.println("Ingresa la cantidad");
			cantidad = Integer.parseInt(recibirScanner(scanner));
			System.out.println("Ingresa el precio unidad");
			precio = Integer.parseInt(recibirScanner(scanner));
			totalPrecio = precio * cantidad;
			lineaArchivo = "[" + idProducto + "]," +"[" + nombreproducto + "],[" + cantidad + "],[" + precio + "],[" + totalPrecio + "]";
			
			return lineaArchivo;
		} catch (Exception e) {
			System.err.println("La opción no es valida está debe escribir la opción númerica");
		}
		return lineaArchivo;
	}

	public static void ejemploManejoArchivos() {
		String nombreArchivo = "AndrewCodev.txt";

		crearArchivo(nombreArchivo);

		anexarArchivo(nombreArchivo, "Nombre: AndrewCodev");
		anexarArchivo(nombreArchivo, "Edad: 30");
		anexarArchivo(nombreArchivo, "Lenguaje: Java");

		leerArchivo(nombreArchivo);
		eliminarArchivo(nombreArchivo);
	}

	// CREAMOS EL ARCHIVO
	public static void crearArchivo(String nombreArchivo) {
		File archivo = new File(nombreArchivo);

		try {
			if (!archivo.exists()) {
				PrintWriter salida = new PrintWriter(archivo);
				salida.close();
				System.out.println("Se ha creado el archivo: " + nombreArchivo);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	// ESCRIBIR ARCHIVO
	public static void escribirArchivo(String nombreArchivo, String contenido) {
		File archivo = new File(nombreArchivo);

		try {
			PrintWriter salida = new PrintWriter(archivo);
			salida.println(contenido);
			salida.close();
			System.out.println("Se ha escrito en el archivo: " + nombreArchivo);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	// ANEXAR INFORMACIÓN
	public static void anexarArchivo(String nombreArchivo, String contenido) {
		File archivo = new File(nombreArchivo);

		try {
			PrintWriter salida = new PrintWriter(new FileWriter(archivo, true));
			salida.println(contenido);
			salida.close();
			System.out.println("Se ha anexado información en el archivo: " + nombreArchivo);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	// LEER ARCHIVO
	public static void leerArchivo(String nombreArchivo) {
		File archivo = new File(nombreArchivo);
		BufferedReader entrada = null;
		try {
			entrada = new BufferedReader(new FileReader(archivo));
			String lectura = entrada.readLine();

			while (lectura != null) {
				System.out.println(lectura);
				lectura = entrada.readLine();
			}
			//entrada.close();

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// Cerrar el BufferedReader
			if (entrada != null) {
				try {
					entrada.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}

	public static void eliminarArchivo(String nombreArchivo) {
		File archivo = new File(nombreArchivo);

		Path ruta = Path.of(archivo.getPath());

		try {
			Files.delete(ruta);
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("Archivo eliminado: " + nombreArchivo);
	}
}
