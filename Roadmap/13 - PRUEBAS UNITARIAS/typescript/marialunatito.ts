/**
 * Steps for test
 * 1. Copy tests in other file called `marialunatito.test.ts`
 * 2. Install npm init
 * 3. Install npm i jest
 * 4. Install npm i --save-dev @types/jest for run test
 * 5. in package.json set this script "test": "jest"
 * 6. descomment the import
 *  - `import { addition } from './marialunatito'`
 *  - `import { generateUser } from './marialunatito'`
 * 4. run command `npm run test marialunatito.test.ts`
 */

///////////////////////// EJERCICIO DE SUMA /////////////////////////

export function addition(a: number, b: number) {
  return a + b;
}

// import { addition } from './marialunatito'

describe("Addition", () => {
  it("Should calculate of addition successful", () => {
    const mockA = Math.random() * 10;
    const mockB = Math.random() * 10;

    const result = addition(mockA, mockB);

    expect(result).toEqual(result);
  });
});

///////////////////////// DIFICULTAD EXTRA /////////////////////////

interface User {
  name: string;
  age: number;
  birth_date: Date;
  programming_languages: string[];
}

export function generateUser(user: User) {
  return user;
}

// import { generateUser } from './marialunatito'

describe("Validate dictionary", () => {
  it("Should validate all fields exist", () => {
    const mockUser = {
      name: "Maria",
      age: 32,
      birth_date: new Date("02/04/1992"),
      programming_languages: [
        "C#",
        "C++",
        "Go",
        "Java",
        "Javascript",
        "Python",
        "Ruby",
      ],
    };

    const user = generateUser(mockUser);
    expect(user.name).toBeDefined();
    expect(user.age).toBeDefined();
    expect(user.birth_date).toBeDefined();
    expect(user.programming_languages).toBeDefined();
  });

  it("Should validate successful all fields of dictionary are correctly", () => {
    const mockUser = {
      name: "Maria",
      age: 32,
      birth_date: new Date("02/04/1992"),
      programming_languages: [
        "C#",
        "C++",
        "Go",
        "Java",
        "Javascript",
        "Python",
        "Ruby",
      ],
    };

    const user = generateUser(mockUser);
    expect(user).toBe(mockUser);
  });
});
