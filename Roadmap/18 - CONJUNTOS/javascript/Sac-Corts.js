let set = [];
set.push(10);
set.unshift(1);
set.push(11, 12);
set.splice(1, 0, 2, 3);
set.splice(2, 1);
set[2] = 5;
let elementExist = set.includes(3);
console.log(elementExist);
console.log(set);
set = [];
console.log(set);

// Extra Exercise //
const setA = new Set([1, 2, 3]);
const setB = new Set([3, 4, 5]);

// Union
const union = new Set([...setA, ...setB]);
console.log(union);

// Intersection
const intersection = new Set([...setA].filter(x => setB.has(x)));
console.log(intersection);

// Difference
const difference = new Set([...setA].filter(x => !setB.has(x)));
console.log(difference);

// Symmetric Difference
const symmetricDifference = new Set([
    ...[...setA].filter(x => !setB.has(x)), 
    ...[...setB].filter(x => !setA.has(x))
]);
console.log(symmetricDifference);