func(0);

console.log("---");

console.log(fact(12));

console.log("---");

console.log(fib(12));

function func(num: number) {

    console.log(num);

    num = num + 1;

    if (num <= 100) {
        func(num);
    }

}

function fact(num: number): number {
    if (num <= 0) {
        return 0;
    } else if (num == 1) {
        return 1;
    } else {
        return num * fact(num - 1);
    }
}

function fib(pos: number): number {
    if (pos <= 1) {
        return 0;
    } else if (pos == 2 || pos == 3) {
        return 1;
    } else {
        return fib(pos - 1) + fib(pos - 2);
    }
}
