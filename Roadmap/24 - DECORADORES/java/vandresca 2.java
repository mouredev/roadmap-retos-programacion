public class vandresca {
    public static void main(String[] args) {

        //EJERCICIO
        Insurance myInsurance = new FloodFareDecorator(new FireFareDecorator(new ThirdPartyInsurance()));
        System.out.println("COST -> "+ myInsurance.getPrice());
        System.out.println();
        System.out.println("==============================");
        System.out.println();

        //EXTRA
        Operable sum = new Sum();
        CountDecorator counter = new CountDecorator(sum);
        System.out.println("\tSUM--> "+sum.operation());
        System.out.println("\tSUM--> "+sum.operation());
        System.out.println("COUNT_DECORATOR-> "+counter.operation());
        System.out.println("\tSUM--> "+sum.operation());
        System.out.println("COUNT_DECORATOR-> "+counter.operation());
        System.out.println("\tSUM--> "+sum.operation());
        System.out.println("COUNT_DECORATOR-> "+counter.operation());
        System.out.println("\tSUM--> "+sum.operation());
        System.out.println("COUNT_DECORATOR-> "+counter.operation());
        System.out.println("COUNT_DECORATOR-> "+counter.operation());
        System.out.println("\tSUM--> "+sum.operation());
    }
}


////////////////////
//                //
//   EJERCICIO    //
//                //
////////////////////

interface Insurance{
    double getPrice();
}

class ThirdPartyInsurance implements Insurance{
    double price;

    @Override
    public double getPrice(){
        return 100.0;
    }
}

abstract class AbstractInsuranceDecorator implements Insurance{
    protected Insurance component;

    public AbstractInsuranceDecorator(Insurance component){
        this.component = component;
    }

    @Override
    public double getPrice(){
        return this.component.getPrice();
    }
}

class FireFareDecorator extends AbstractInsuranceDecorator{
    public FireFareDecorator(Insurance component){
        super(component);
    }

    @Override
    public double getPrice() {
        return component.getPrice() + 50.0;
    }
}

class FloodFareDecorator extends AbstractInsuranceDecorator{
    public FloodFareDecorator(Insurance component){
        super(component);
    }

    @Override
    public double getPrice() {
        return component.getPrice() + 30.0;
    }
}

/////////////////////////
//                     //
//       EXTRA         //
//                     //
/////////////////////////


interface Operable{
    int operation();
}

class Sum implements Operable{
    private static int c;
    int a=4;

    @Override
    public int operation() {
        c = c + a;
        return c;
    }
}

abstract class AbstractOperationDecorator implements Operable{
    Operable component;
    public AbstractOperationDecorator(Operable component){
        this.component = component;
    }
}

class CountDecorator extends AbstractOperationDecorator{

    private static int countNumExecOp = 0;

    public CountDecorator(Operable component){
        super(component);
    }

    @Override
    public int operation() {
        component.operation();
        countNumExecOp++;
        return countNumExecOp;
    }
}
