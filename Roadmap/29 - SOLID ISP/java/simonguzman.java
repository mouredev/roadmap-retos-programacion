public class simonguzman {
    public static void main(String[] args) {
        exampleNoIsp();
    }

    /******************************** Ejercicio adicional con isp ********************************/

    /******************************** Ejercicio adicional sin isp ********************************/

    /******************************** Ejemplo con isp ********************************/

    /******************************** Ejemplo sin isp ********************************/
    static void exampleNoIsp(){
        Worker robot = new Robot();
        robot.work();  // Solo debería trabajar
        robot.eat();
    }

    static interface Worker {
        void work();
        void eat();
    }

    static class Robot implements Worker {
        @Override
        public void work() {
            System.out.println("El robot está trabajando.");
        }

        @Override
        public void eat() {
            // No tiene sentido para un robot
        }
    }

}
