let a: number = 3;

main();
console.log("\nNumber of times a text was not printed: " + program("zip", "zap"));

function main() {

    func1();
    console.log(func2());
    func3(a, "\nParameterized and non-return function:\nGlobal variable A: ");
    console.log(func4(-4, "\nFunction with return and with parameters:\nGlobal variable A: "));
    
}

function func1() {
    var b = 3;
    console.log("\nFunction without return and without parameters:\nGlobal variable A: " + a + "\nLocal variable B:" + b);
}

function func2(): string {
    return "\nFunction with return and without parameters:\nGlobal variable A: " + a;
}

function func3(num: number, str: string) {
    console.log(str + num);
}

function func4(num: number, str: string): string {
    return str + a + "\nAbsolute number: " + Math.abs(num);
}

function program(zip: string, zap: string): number {

    console.log("\nProgram:")

    let count: number = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(zip + zap);
        } else if (i % 3 == 0) {
            console.log(zip);
        } else if (i % 5 == 0) {
            console.log(zap);
        } else {
            count++;
        }
    }

    return count;

}
