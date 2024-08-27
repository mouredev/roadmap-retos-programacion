public class simonguzman {
    public static void main(String[] args) {

        Persona persona = new Persona();

        persona.setNombre("Simon");
        persona.setApellido("Guzman");
        persona.setEdad(22);
        
        System.out.println(persona.toString());
    }
}

class Persona{
    private String nombre;
    private String apellido;
    private int edad;

    public Persona(){

    }

    public Persona(String nombre, String apellido, int edad){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    
    public String getApellido() {
        return apellido;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return edad;
    }

    @Override
    public String toString() {
        return "Persona: " + "nombre "+ getNombre() + "apellido "+ getApellido() + "edad"+ getEdad() ;
    }
}