public class simonguzman {
    public static void main(String[] args) {
        exampleNoIsp();
        exampleIsp();
    }

    /******************************** Ejercicio adicional con isp ********************************/

    /******************************** Ejercicio adicional sin isp ********************************/

    /******************************** Ejemplo con isp ********************************/
    static void exampleIsp(){
        Workable robotIsp = new RobotIsp();
        robotIsp.work();

        Employee employee = new Employee();
        employee.work();
        employee.eat();
    }

    static interface Workable {
        void work();
    }

    static interface Eatable {
        void eat();
    }

    static class RobotIsp implements Workable {
        @Override
        public void work() {
            System.out.println("El robot está trabajando.");
        }
    }

    static class Employee implements Workable, Eatable {
        @Override
        public void work() {
            System.out.println("El empleado está trabajando.");
        }

        @Override
        public void eat() {
            System.out.println("El empleado está comiendo.");
        }
    }
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
