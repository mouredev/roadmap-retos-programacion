import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class mtirador {
    public static void main(String[] args) {


        /*Arrays _Arreglos */

        int[]num={10,3,4,5,6};

            //Para recorrer un array. Los arrays tiene un tamaño fijo
            for(int i=0;i<num.length;i++){
                System.out.println(num[i]);
            }

        /*ArrayList */

        ArrayList<String>name =new ArrayList<String>();

        /*Inserción */
        name.add("Pablo");
        name.add("Pedro");
        name.add("María");
        name.add("Sonia");
        System.out.println(name);

        /*Borrado */
        name.remove("Pablo");

        /*Recorrer un ArrayList */
        for(int i=0;i<name.size();i++){
            System.out.println(name.get(i));
        }

        /* Actualización */
        name.set(2, "Marta");
        System.out.println(name);

        /*Ordenación */
        name.sort(Comparator.naturalOrder());
    
        /*Borrar todos los elementos del ArrayList */
        name.clear();
        System.out.println(name);



    
       
        
       /*Agenda */

        ArrayList<Contacto>agenda=new ArrayList<>();
        Scanner ent =new Scanner(System.in);
        boolean flag=true;



        System.out.println("Agenda(elija una opción)\n1.Buscar\n2.Insertar\n3.Actualizar\n4.Eliminar\n5.Salir");
        String opcion=ent.nextLine();

        while (flag) {
          

            switch (opcion) {
                case "1":
                    opcion = Buscar(agenda, ent);
                    break;
                case "2":
                    opcion = Insertar(agenda, ent);
                    break;
                case "3":
                    opcion = Actualizar(agenda, ent);
                    break;
                
                case "4":
    
                    opcion = Eliminar(agenda, ent);
                    break;
                
                case "5":
                    flag = false;
                    System.out.println("Hasta pronto.");
                    break;
                default:
                    System.out.println("Ingrese una opción válida.");
                    break;
            }
        }

    }//fin main



    private static String Eliminar(ArrayList<Contacto> agenda, Scanner ent) {
        String opcion;
        System.out.println("Ingrese el nombre del contacto a eliminar:");
        String nombreEliminar = ent.nextLine();
        boolean eliminado = false;
            
        for (int i = 0; i < agenda.size(); i++) {
            Contacto contacto = agenda.get(i);
            if (contacto.getNombre().equalsIgnoreCase(nombreEliminar)) {
                agenda.remove(i);
                eliminado = true;
                System.out.println("Contacto eliminado exitosamente.");
                break; 
            }
        }
            
        if (!eliminado) {
            System.out.println("No se encontró ningún contacto con ese nombre.");
        }

        System.out.println("Agenda(elija una opción)\n1.Buscar\n2.Insertar\n3.Actualizar\n4.Eliminar\n5.Salir");
        opcion=ent.nextLine();
        return opcion;
    }



    private static String Actualizar(ArrayList<Contacto> agenda, Scanner ent) {
        String opcion;
        System.out.println("Ingrese el nombre del contacto a actualizar:");
        String nombreActualizar = ent.nextLine();
        boolean actualizado = false;
            
        for (Contacto contacto : agenda) {
            if (contacto.getNombre().equalsIgnoreCase(nombreActualizar)) {
                System.out.println("Ingrese el nuevo número de teléfono para " + nombreActualizar + ":");
                String nuevoTelefono = ent.nextLine();
                contacto.settfno(nuevoTelefono);
                actualizado = true;
                System.out.println("Contacto actualizado exitosamente.");
                break; // Terminamos el bucle ya que encontramos y actualizamos el contacto.
            }
        }
            
        if (!actualizado) {
            System.out.println("No se encontró ningún contacto con ese nombre.");
        }

        System.out.println("Agenda(elija una opción)\n1.Buscar\n2.Insertar\n3.Actualizar\n4.Eliminar\n5.Salir");
        opcion=ent.nextLine();
        return opcion;
    }



    private static String Insertar(ArrayList<Contacto> agenda, Scanner ent) {
        String nombre;
        String tfno;
        String opcion;
        System.out.println("Ingrese el Nombre:");
        nombre = ent.nextLine();
    
        // Validación del número de teléfono
        do {
            System.out.println("Ingrese el teléfono (11 dígitos):");
            tfno = ent.nextLine();
            if (tfno.length() != 11 || !tfno.matches("\\d+")) {
                System.out.println("El número de teléfono debe tener exactamente 11 dígitos.");
            }
        } while (tfno.length() != 11 || !tfno.matches("\\d+")); 
    
        agenda.add(new Contacto(nombre, tfno));
        System.out.println("Contacto añadido exitosamente.");
        System.out.println("Agenda(elija una opción)\n1.Buscar\n2.Insertar\n3.Actualizar\n4.Eliminar\n5.Salir");
        opcion=ent.nextLine();
        return opcion;
    }
    



    private static String Buscar(ArrayList<Contacto> agenda, Scanner ent) {
        String opcion;
        System.out.println("Buscar por nombre:");
        String nombreBuscar = ent.nextLine();
        boolean encontrado = false;
        for (Contacto contacto : agenda) {
            if (contacto.getNombre().equalsIgnoreCase(nombreBuscar)) {
                System.out.println("Contacto encontrado:");
                System.out.println(contacto.toString());
                encontrado = true;
                
                break;
            }
        }
        if (!encontrado) {
            System.out.println("No se encontró ningún contacto con ese nombre.");
            
        }

        System.out.println("Agenda(elija una opción)\n1.Buscar\n2.Insertar\n3.Actualizar\n4.Eliminar\n5.Salir");
        opcion=ent.nextLine();
        return opcion;
    }

    

    public static class Contacto{
        protected String nombre;
        protected String tfno;

        public Contacto(){
            this.nombre="Anónimo";
            this.tfno="null";
        }

        public Contacto(String nombre,String tfno){
            this.nombre=nombre;
            this.tfno=tfno;

        }

        public String getNombre(){
            return nombre;
        }
        public void setnombre(String nombre){
            this.nombre=nombre;
        }

        public String getTfno(){
            return tfno;

        }

        public void settfno(String tfno){
            this.tfno=tfno;
        }

        public String toString(){
            return "Nombre: "+getNombre() +"|| Telefono: "+getTfno();
            
        }
    }//fin contacto


}//fin class





