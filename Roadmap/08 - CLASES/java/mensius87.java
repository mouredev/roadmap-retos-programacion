class PersonaMensius {
    private String nombre;
    private int edad;
    
    public PersonaMensius(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    
    public void imprimirInformacion() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Edad: " + this.edad);
    }

    public static void main(String[] args) {
        // Crear una instancia de la clase Persona
        PersonaMensius persona1 = new PersonaMensius("Juan", 30);

        // Imprimir la información utilizando el método de la clase
        persona1.imprimirInformacion();

        // Modificar los atributos y volver a imprimir la información
        persona1.nombre = "María";
        persona1.edad = 25;
        persona1.imprimirInformacion();
    }
}
