class Qv1ko {

    public static void main(String[] args) {
        
        C1 example1 = new C1();
        System.out.println(example1.toString());
        example1.setC1String("Example 1");
        System.out.println(example1.getC1String());

        C2 example2 = new C2();
        System.out.println(example2.toString());
        example2.setC2String("Example 2");
        System.out.println(example2.getC2String());

    }

}

class C1 {

    String c1String;

    C1() {
        this.c1String = "example";
    }

    C1(String value) {
        this.c1String = value;
    }

    public String getC1String() {
        return c1String;
    }

    public void setC1String(String c1String) {
        this.c1String = c1String;
    }

    @Override
    public String toString() {
        return "Class 1 value: " + c1String;
    }
    
}

class C2 {

    String c2String;

    C2() {
        this.c2String = "example";
    }

    C2(String value) {
        this.c2String = value;
    }

    public String getC2String() {
        return c2String;
    }

    public void setC2String(String c2String) {
        this.c2String = c2String;
    }

    @Override
    public String toString() {
        return "Class 2 value: " + c2String;
    }
    
}
