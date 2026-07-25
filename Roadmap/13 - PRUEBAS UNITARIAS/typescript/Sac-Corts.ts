// npm install --save-dev jest
// We name the file with the ending .test.js
// To run the program: npx jest .\Sac-Corts.test.js

function addition(a: number, b: number): number {
    return a + b;
}

test('addition 1 + 2 should be 3', () => {
    expect(addition(1, 2)).toBe(3);
});

test('addition 3 + 7 should be 10', () => {
    expect(addition(3, 7)).toBe(10);
});

// ** Extra Exercise ** //
interface Data {
    name: string;
    age: string;
    birthdate: string;
    programmingLanguages: string[];
}

const data: Data = {
    name: "Isaac",
    age: "22",
    birthdate: "2001-10-21",
    programmingLanguages: ["JavaScript", "Python"]
};

test('It should have all the necessary keys', () => {
    expect(data).toHaveProperty('name');
    expect(data).toHaveProperty('age');
    expect(data).toHaveProperty('birthdate');
    expect(data).toHaveProperty('programmingLanguages');
});

test('It should have the correct data', () => {
    expect(data.name).toBe("Isaac");
    expect(data.age).toBe("22");
    expect(data.birthdate).toBe("2001-10-21");
    expect(data.programmingLanguages).toEqual(["JavaScript", "Python"]);
});
