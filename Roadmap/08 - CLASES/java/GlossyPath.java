import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * 
 *EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 *  @version v1.0
 * 
 *  @since 31/07/2024
 * 
 * @author GlossyPath
 */


public class GlossyPath {
    
    public static void main(String[] args) {
        
        Pila<Empresa> pilaEmpresas = new Pila<>();

        Cola<Empresa> colaEmpresas = new Cola();

        Empresa empresa = new Empresa();

        empresa.setCantidadEmpleados(10);
        empresa.setEsNueva(true);
        empresa.setNombre("Rolan S.L");
        empresa.setUbicadoEnPais("Francia");

        pilaEmpresas.añadirALaPila(empresa);

        colaEmpresas.añadirALaCola(empresa);

        System.out.println(pilaEmpresas);

        System.out.println(colaEmpresas);    
    }
}


class Empresa {

    private String nombre, ubicadoEnPais;
    private int cantidadEmpleados;
    private boolean esNueva;

    public Empresa(){

    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getUbicadoEnPais() {
        return ubicadoEnPais;
    }

    public void setUbicadoEnPais(String ubicadoEnPais) {
        this.ubicadoEnPais = ubicadoEnPais;
    }

    public int getCantidadEmpleados() {
        return cantidadEmpleados;
    }

    public void setCantidadEmpleados(int cantidadEmpleados) {
        this.cantidadEmpleados = cantidadEmpleados;
    }

    public boolean isEsNueva() {
        return esNueva;
    }

    public void setEsNueva(boolean esNueva) {
        this.esNueva = esNueva;
    }

    @Override
    public String toString(){

        String nuevaVieja;

        if(isEsNueva()){
            nuevaVieja = "si";

            } else {
             nuevaVieja = "la empresa es antigua";   
            }

        return "Empresa {" +
                "nombre: " + nombre +
                " ubicada en: " + ubicadoEnPais +
                " cantidad de empleados: " + cantidadEmpleados +
                " la empresa es nueva:" + nuevaVieja + "}";         
            }
                
        }


class Pila<T> {

    private Stack<T> pila;

    public Pila() {
        this.pila = new Stack<>();
    }

    public int cantidadObjetos(){
        return this.pila.size();
    }

    public void añadirALaPila(T o){
        this.pila.add(o);
    }

    public void eliminarDeLaPila(){
        T eliminado = this.pila.pop();

        System.out.println("El elemento eliminado es: " + eliminado);
    }

    @Override
    public String toString(){
        StringBuilder nombreEmpresas = new StringBuilder("\nContenido de la pila: \n");

        @SuppressWarnings("unchecked")
        Stack<T> copiaPila = (Stack<T>) this.pila.clone();
        
        while (!copiaPila.isEmpty()) {
            nombreEmpresas.append(copiaPila.pop().toString()).append("\n");
        }
        
        return nombreEmpresas.toString();
    }
}
 
class Cola<T> {

    private Queue<T> cola;

    public Cola() {
        this.cola= new LinkedList<>();
    }


    public int cantidadObjetos(){
        return this.cola.size();
    }

    public void añadirALaCola(T object){
        this.cola.add(object);
    }

    public void eliminarDeLaCola(int index) throws IndexOutOfBoundsException{
        if(this.cola.size() < index || index < 0){
            throw new IndexOutOfBoundsException("El índice no puede ser superior al tamaño de la cola o negativo.");

        } else {
            this.cola.remove(index);
        }      
    }

    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder("\nContenido de la cola:\n");

        this.cola.forEach(objeto->sb.append(objeto).append("\n"));

        return sb.toString();
        }
    }   

    
