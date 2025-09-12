
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
 * - Muestra ejemplos de creaci�n de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserci�n, borrado, actualizaci�n y ordenaci�n.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de b�squeda, inserci�n, actualizaci�n y eliminaci�n de contactos.
 * - Cada contacto debe tener un nombre y un n�mero de tel�fono.
 * - El programa solicita en primer lugar cu�l es la operaci�n que se quiere realizar, y a continuaci�n
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir n�meros de tel�fono no n�mericos y con m�s de 11 d�gitos.
 *   (o el n�mero de d�gitos que quieras)
 * - Tambi�n se debe proponer una operaci�n de finalizaci�n del programa.
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
                        System.out.println("Nombre: " + contacto[0] + " Tel�fono: " + contacto[1]);
                    else
                        System.out.println("El contacto buscado no se encuentra en el list�n");
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
                        System.out.println("El contacto buscado no se encuentra en el list�n");
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
        System.out.println("** 5. Mostrar list�n                **");
        System.out.println("** 0. Salir                         **");
        System.out.println("**************************************");
        
        System.out.print("Introduce una opci�n:");
        
        try
        {
            opcion = lectura.nextInt();
        }
        catch(Exception e)
        {
            System.out.println("Opci�n incorrecta, por favor introduzca una opci�n del 0 al 5"); 
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
            System.out.print("Introduce el n�mero de tel�fono:");                        
            cadena = lectura.nextLine();                        
            matcher = pattern.matcher(String.valueOf(cadena));
            ok = matcher.find();
            if (!ok)            
                System.out.println("Formato del tel�fono incorrecto, introduzca una secuencia de n�meros de 11 d�gitos");
            
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
            System.out.print("Cu�l es el nombre del usuario que desea buscar?");
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
                System.out.print("Qu� deseas modificar? (0 para nombre, 1 para tel�fono)");                
                try
                {
                    opcion = lectura.nextInt();
                    lectura.nextLine();
                }
                catch(Exception e)
                {
                    System.out.println("Opci�n inv�lida, por favor introduzca una opci�n entre 0 y 1");
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
            System.out.println("El contacto buscado no se encuentra en el list�n");
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
            listin.forEach((k,v) -> System.out.println("Nombre: " + k + " Tel�fono: " + v));
        else
            System.out.println("No hay contactos actualmente en el list�n, por favor, introduzca alguno con la opci�n 1 del men�");
    }
}
