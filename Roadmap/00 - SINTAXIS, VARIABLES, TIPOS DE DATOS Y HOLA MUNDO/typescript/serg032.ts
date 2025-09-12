// Typescript: https://www.typescriptlang.org/

/*
Other way to create comments with Typescript
/

/**
 * @author Sergio Radigales
 */

let firstVariable = "First variable";
const firstConstant = "First Constant";
const numberVariable: number = 1993;
const stringVariable: string = "Software development";
const booleanVariable: boolean = true;
const nullVariable: null = null;
const undefinedVariable: undefined = undefined;
const bigIntvariable: bigint = 10n;
const symbolVariable = Symbol("My symbol");
const arrayVaraible: [] = [];
const array2Variable: Array<number> = [1, 2, 3, 4, 5];
const multitypeVariable: boolean | number = 4;
enum Techs {
  Typescript,
  Node,
}

const tech: Techs = Techs.Typescript;
const tupleVariable: [number, Techs] = [55, Techs.Node];

const helloTech = (tech: string): string => `Hola, ${tech}`;
console.log(helloTech("Typescript"));
