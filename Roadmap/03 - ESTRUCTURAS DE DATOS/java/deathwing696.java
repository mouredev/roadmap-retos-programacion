
import java.util.HashMap;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

/**
 *
 * @author death
 */
public class deathwing696 {
    public static void main(String[] args)
    {
        int opcion;
        var listin = new HashMap<String, Long>();
        
        do
        {
            opcion = Menu();
            
            switch (opcion) 
            {
                case 0 ->
                {
                    //Salir
                }
                case 1 -> Insertar_nuevo_contacto(listin);
                case 2 -> 
                {
                    Object[] contacto;
                    
                    contacto = Buscar_contacto(listin, null);
                    
                    if (contacto != null)
                        System.out.println("Nombre: " + contacto[0] + " Teléfono: " + contacto[1]);
                    else
                        System.out.println("El contacto buscado no se encuentra en el listín");
                }
                case 3 -> 
                {
                    if (Actualizar_contacto(listin))
                        System.out.println("Contacto actualizado correctamente");
                }
                case 4 -> 
                {
                    if (Eliminar_contacto(listin))
                        System.out.println("Contacto eliminado correctamente");
                    else
                        System.out.println("El contacto buscado no se encuentra en el listín");
                }
                    
                case 5 -> Mostrar_listin(listin);
                default -> throw new AssertionError();
            }
        }while(opcion != 0);
    } 
    
    static private int Menu()
    {
        int opcion;
        Scanner lectura = new Scanner(System.in);
        
        do
        {
        
        System.out.println("**************************************");
        System.out.println("** 1. Insertar nuevo contacto       **");
        System.out.println("** 2. Buscar contacto               **");
        System.out.println("** 3. Actualizar contacto           **");
        System.out.println("** 4. Eliminar contacto             **");
        System.out.println("** 5. Mostrar listín                **");
        System.out.println("** 0. Salir                         **");
        System.out.println("**************************************");
        
        System.out.print("Introduce una opción:");
        
        try
        {
            opcion = lectura.nextInt();
        }
        catch(Exception e)
        {
            System.out.println("Opción incorrecta, por favor introduzca una opción del 0 al 5"); 
            lectura.nextLine();
            opcion = 9;
        }
        
        }while(opcion < 0 || opcion > 5);
        
        return opcion;
    }
    
    static private Long Comprobar_telefono_valido()
    {
        String cadena;
        Scanner lectura = new Scanner(System.in);
        Pattern pattern = Pattern.compile("[0-9]{11}");
        Matcher matcher;
        boolean ok;
        
        do
        {            
            System.out.print("Introduce el número de teléfono:");                        
            cadena = lectura.nextLine();                        
            matcher = pattern.matcher(String.valueOf(cadena));
            ok = matcher.find();
            if (!ok)            
                System.out.println("Formato del teléfono incorrecto, introduzca una secuencia de números de 11 dígitos");
            
        }while(!ok);
        
        return Long.valueOf(cadena);
    }
    
    static private void Insertar_nuevo_contacto(HashMap<String,Long> listin)
    {
        String nombre;
        long telefono;
        Scanner lectura = new Scanner(System.in);
        
        
        System.out.print("Introduce el nombre del contacto:");
        nombre = lectura.nextLine();
        telefono = Comprobar_telefono_valido();
        
        listin.put(nombre, Long.valueOf(String.valueOf(telefono)));
    }
    
    static private Object[] Buscar_contacto(HashMap<String, Long> listin, String key)
    {
        Long value;
        Scanner lectura = new Scanner(System.in);
        
        if (key == null)
        {
            System.out.print("Cuál es el nombre del usuario que desea buscar?");
            key = lectura.nextLine();            
        }
        
        value = listin.get(key);
        
        if (value != null)
            return new Object[]{key, value};
        else
            return null;
    }
    
    static private Boolean Actualizar_contacto(HashMap<String, Long> listin)
    {
        Boolean ok;
        String key;
        Long value;
        Scanner lectura = new Scanner(System.in);
        
        System.out.print("Introduce el nombre del contacto que deseas modificar:");
        key = lectura.nextLine();
        value = listin.get(key);
        
        if (value != null)
        {
            int opcion;
            
            do
            {
                System.out.print("Qué deseas modificar? (0 para nombre, 1 para teléfono)");                
                try
                {
                    opcion = lectura.nextInt();
                    lectura.nextLine();
                }
                catch(Exception e)
                {
                    System.out.println("Opción inválida, por favor introduzca una opción entre 0 y 1");
                    lectura.nextLine();
                    opcion = 9;
                }
            }while (opcion != 0 && opcion != 1);
            
            if (opcion == 0)
            {
                String nombre;
                
                System.out.print("Introduce el nuevo nombre:");
                nombre = lectura.nextLine();
                listin.remove(key);
                listin.put(nombre, value);
            }
            else
            {
                Long telefono;
                                
                telefono = Comprobar_telefono_valido();
                listin.put(key, telefono);
            }
            
            ok = true;
        }
        else
        {
            System.out.println("El contacto buscado no se encuentra en el listín");
            ok = false;
        }
        
        return ok;
    }
    
    static private Boolean Eliminar_contacto(HashMap<String, Long> listin)
    {
        Boolean ok = false;
        String key;
        Long value;
        Scanner lectura = new Scanner(System.in);

        System.out.print("Introduce el nombre del contacto que deseas modificar:");
        key = lectura.nextLine();
        value = listin.get(key);
        
        if (value != null)
        {
            listin.remove(key);
            ok = true;
        }
        
        return ok;
    }
    
    static private void Mostrar_listin(HashMap<String,Long> listin)
    {
        if (!listin.isEmpty())
            listin.forEach((k,v) -> System.out.println("Nombre: " + k + " Teléfono: " + v));
        else
            System.out.println("No hay contactos actualmente en el listín, por favor, introduzca alguno con la opción 1 del menú");
    }
}
