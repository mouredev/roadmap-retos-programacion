import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;

public class simonguzman {
    public static void main(String[] args) {

        Persona persona = new Persona();

        persona.setNombre("Simon");
        persona.setApellido("Guzman");
        persona.setEdad(22);
        
        System.out.println(persona.toString());

        Pila pila = new Pila();
        pila.agregarElementoPila("Documento1");
        pila.agregarElementoPila("Documento2");
        pila.agregarElementoPila("Documento3");
        System.out.println("************Elementos inciales************");
        pila.verElementosPila(); 
        pila.tamañoPila();
        pila.eliminarElementoPila();
        System.out.println("************Elementos finales************");
        pila.verElementosPila();

        Cola cola = new Cola();
        cola.agregarElementoCola("Documento 1");
        cola.agregarElementoCola("Documento 2");
        cola.agregarElementoCola("Documento 3");
        System.out.println("************Elementos inciales************");
        cola.verElementosCola();
        cola.tamañoCola();
        cola.eliminarElementoCola();
        System.out.println("************Elementos finales************");
        cola.verElementosCola();
    }

    static class Persona{
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
            return "Persona: " + " nombre "+ getNombre() + " apellido "+ getApellido() + " edad "+ getEdad() ;
        }
    }

    static class Pila{
        private Stack<String> pila;
    
        public Pila(){
            this.pila = new Stack<>();
        }
    
        public Pila(Stack<String> pila){
            this.pila = pila;
        }
    
        public void agregarElementoPila(String cadena){
            this.pila.push(cadena);
        }
    
        public void eliminarElementoPila(){
            if(!this.pila.isEmpty()){
                this.pila.pop();
            }else{
                System.out.println("La pila esta vacia");
            }
            
        }
    
        public void verElementosPila(){
            if(!this.pila.isEmpty()){
                for (int i = pila.size() - 1; i >= 0; i--){
                    System.out.println(pila.get(i));
                }
            }else{
                System.out.println("La pila esta vacia");
            }
            
        }
    
        public int tamañoPila(){
            return this.pila.size();
        }
    }

    static class Cola{
        private Queue<String> cola;
    
        public Cola(){
            this.cola = new LinkedList<>();
        }
    
        public Cola(Queue<String> cola){
            this.cola = new LinkedList<>();
        }
    
        public void agregarElementoCola(String cadena){
            this.cola.add(cadena);
        }
    
        public void eliminarElementoCola(){
            if(!this.cola.isEmpty()){
                this.cola.poll();
            }else{
                System.out.println("La cola esta vacia");
            }
            
        }
    
        public void verElementosCola(){
            if(!this.cola.isEmpty()){
                for (String elemento : cola){
                    System.out.println(elemento);
                }
            }else{
                System.out.println("La cola esta vacia");
            }
            
        }
    
        public int tamañoCola(){
            return this.cola.size();
        }
    
    }

}


