class C1 {

    c1String: string;

    constructor(c1String: string) {
        this.c1String = c1String;
    }

    getC1String() {
        return this.c1String;
    }

    setC1String(c1String: string) {
        this.c1String = c1String;
    }

    toString() {
        return this.c1String;
    }

    print() {
        console.log(this.c1String);
    }

}

class C2 {

    c2String: string;

    constructor(c2String: string) {
        this.c2String = c2String;
    }

    getC2String() {
        return this.c2String;
    }

    setC2String(c2String: string) {
        this.c2String = c2String;
    }

    toString() {
        return this.c2String;
    }

    print() {
        console.log(this.c2String);
    }

}

function main() {
    
    let example1: C1 = new C1("example");
    example1.print();
    example1.setC1String("Example 1");
    console.log(example1.toString());

    let example2: C2 = new C2("example");
    example2.print();
    example2.setC2String("Example 2");
    console.log(example2.toString());

}

main();
