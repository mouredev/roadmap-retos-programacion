public class Animal {
	
//	Atributos que van a heredar todos los animales
	
	protected String nombre;
	protected int numPatas;
	protected int edad;
	protected boolean cola;
	protected int numVacunas;
	
//	Metodos de la superclase Animal
	public Animal(String nombre, int numPatas, int edad, boolean cola, int numVacunas) {
		this.nombre = nombre;
		this.numPatas = numPatas;
		this.edad = edad;
		this.cola = cola;
		this.numVacunas = numVacunas;
	}
	
//	Metodo sin parametros para la superclase Animal
	public Animal(){
		this.nombre="";
		this.numPatas=0;
		this.edad=0;
		this.cola=false;
		this.numVacunas=0;
	}

	
//	Getters and setters
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getNumPatas() {
		return numPatas;
	}

	public void setNumPatas(int numPatas) {
		this.numPatas = numPatas;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public boolean isCola() {
		return cola;
	}

	public void setCola(boolean cola) {
		this.cola = cola;
	}

	public int getNumVacunas() {
		return numVacunas;
	}

	public void setNumVacunas(int numVacunas) {
		this.numVacunas = numVacunas;
	}
}

------------- CLASS DOG -----------
public class Perro extends Animal{
	
	private String ladrido;

	
//	Constructor con todos los parametros de la superclase Animal
	public Perro(String nombre, int numPatas, int edad, boolean cola, int numVacunas, String ladrido) {
		super(nombre, numPatas, edad, cola, numVacunas);
		this.ladrido = ladrido;
	}
	
	public Perro() {
		this.ladrido="";
	}

	
//	Getters and setters
	public String getLadrido() {
		return ladrido;
	}

	public void setLadrido(String ladrido) {
		this.ladrido = ladrido;
	}
	
	
//	Metodo para ver el sonido del animal
	
	public void ladrido() {
		Scanner sn=new Scanner(System.in);
		System.out.println("Que sonido hace el perro?");
		this.setLadrido(sn.next());
		
		System.out.println("El perro hace: "+this.getLadrido());
	}
	
//	Main para realizar las pruebas 
	public static void main(String[] args) {
		Perro p=new Perro();
		p.ladrido();
	} 
	
}
-----------CLASS CAT--------------
public class Gato extends Animal{
	
	private String mauyido;

	
//	Constructor con todos los parametros de la superclase Animal
	public Gato(String nombre, int numPatas, int edad, boolean cola, int numVacunas, String mauyido) {
		super(nombre, numPatas, edad, cola, numVacunas);
		this.mauyido = mauyido;
	}
	
//	Constructor sin parametros
	
	public Gato() {
		this.mauyido="";
	}

	
//	Getters and setters
	public String getMauyido() {
		return mauyido;
	}

	public void setMauyido(String mauyido) {
		this.mauyido = mauyido;
	}
	
//	Metodo para ver el sonido del animal
	
	public void mauyido() {
		Scanner sn=new Scanner(System.in);
		System.out.println("Que sonido hace el gato?");
		this.setMauyido(sn.next());
		
		System.out.println("El gato hace: "+this.getMauyido());
	}
	
//	Main para realizar las pruebas
	
	public static void main(String[] args) {
		Gato g= new Gato();
		g.mauyido();
		
	}
}
