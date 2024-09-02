let a: number = 3;
let b: number = 4;
const xy = {x: 5, y: 6};

function program1(a: number, b: number): number[] {

    var tmp = a;

    a = b;
    b = tmp;

    return [a, b];

}

function program2(ref: { x: number, y: number }): number[] {

    var tmp = ref.x;

    ref.x = ref.y;
    ref.y = tmp;

    return [ref.x, ref.y];

}

let newAB = program1(a, b);
let newXY = program2(xy);

console.log("A value: " + a);
console.log("New A value: " + newAB[0]);
console.log("B value: " + b);
console.log("New B value: " + newAB[1]);
console.log("X value: " + xy.x);
console.log("New X value: " + newXY[0]);
console.log("Y value: " + xy.y);
console.log("New Y value: " + newXY[1]);
