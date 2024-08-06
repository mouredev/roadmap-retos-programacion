
public class Main {
    public static void main(String[] args) {
        ConcreteComponent component = new ConcreteComponent();
        ConcreteDecoratorA componentDecorateA = new ConcreteDecoratorA(component);
        ConcreteDecoratorB componentDecorateB = new ConcreteDecoratorB(componentDecorateA);
        componentDecorateB.operation();
        System.out.println("EXTRA");
        System.out.println("========================");
        Arithmetic operable = new Arithmetic();
        //Llamada sin el decorador
        double result = operable.sumTwoNumbers(5.6,7.8);
        System.out.println("Resultado llamada sin decorar :" + result);
        //Llamada con decorador
        CountCallDecorator operationDecorated = new CountCallDecorator(operable);
        result = operationDecorated.sumTwoNumbers(2d,4d);
        System.out.println("Resultado llamada con decorador :" + result);
        result = operationDecorated.sumTwoNumbers(4.5,6.7);
        System.out.println("Resultado llamada con decorador :" + result);
    }

}
//Classes Generic
interface Component{
    void operation();
}
class ConcreteComponent implements Component{
    @Override
    public void operation() {
        System.out.println("Concrete Component Operation");
    }
}
abstract class Decorator implements Component{
    protected Component component;
    public Decorator(Component component){
        this.component = component;
    }
    @Override
    public void operation() {
        component.operation();
    }
}
class ConcreteDecoratorA extends Decorator{
    public ConcreteDecoratorA(Component component) {
        super(component);
    }
    protected void otherOperation(){
        System.out.println("Concrete Decorator A");
    }

    @Override
    public void operation() {
        otherOperation();
        super.operation();
    }
}
class ConcreteDecoratorB extends Decorator{
    public ConcreteDecoratorB(Component component) {
        super(component);
    }
    protected void otherOperation(){
        System.out.println("Concrete Decorator B");
    }

    @Override
    public void operation() {
        otherOperation();
        super.operation();
    }
}

//EXTRA
interface Operable{
    double sumTwoNumbers(Double num1, Double num2);
}
class Arithmetic implements Operable {
    @Override
    public double sumTwoNumbers(Double num1, Double num2) {
        return num1 + num2;
    }
}
abstract class OperableDecorator implements Operable{
    protected Operable operable;
    OperableDecorator(Operable operable){
        this.operable = operable;
    }
}

class CountCallDecorator extends OperableDecorator{
    private static int countCall = 0;
    public CountCallDecorator(Operable operable) {
        super(operable);
    }


    @Override
    public double sumTwoNumbers(Double num1, Double num2) {
        countCall++;
        System.out.println("La función se ha llamado : " + countCall + (countCall>1?" veces":" vez"));
        return operable.sumTwoNumbers(num1,num2);
    }
}