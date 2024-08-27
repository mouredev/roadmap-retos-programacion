public class simonguzman {
    public static void main(String[] args) {
        Dog dog1 = new Dog("Ares", "Lobo siberiano");
        Cat cat1 = new Cat("Katy", "Carey");
        
        System.out.println("Nombre: "+ dog1.getName() + " Raza: "+dog1.getRaza());
        dog1.hacerSonido();
        System.out.println("Nombre: "+ cat1.getName() + " Raza: "+cat1.getRaza());
        cat1.hacerSonido();
    }

    static class Animal{
        private String name;
        private String raza;
    
        public Animal(){
    
        }
    
        public Animal(String name, String raza){
            this.name = name;
            this.raza = raza;  
        }
    
        public void hacerSonido(){
            
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getRaza() {
            return raza;
        }

        public void setRaza(String raza) {
            this.raza = raza;
        }
    }
    
     static class Dog extends Animal{
    
        public Dog(){
    
        }
    
        public Dog(String name, String raza){
            super(name, raza);
        }
    
        @Override
        public void hacerSonido() {
            System.out.println("Guau");
        }
        
    }
    
    static class Cat extends Animal{
    
        public Cat(){
    
        }
    
        public Cat(String name, String raza){
            super(name, raza);
        }
    
        @Override
        public void hacerSonido() {
            System.out.println("Miau");
        } 
    }

}

