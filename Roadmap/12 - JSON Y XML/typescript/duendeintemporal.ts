/**
 * #12 { retosparaprogramadores } JSON and XML Handling in TypeScript
 * 
 * Bibliography:
 * - Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
 * - Professional JavaScript for Web Developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
 * - JavaScript Notes for Professionals (GoalKicker.com) (Z-Library)
 * - GPT & Deepseek
 * 
 * Note: We will use Node.js and the `xmldom` and `node-fetch` libraries.
 * You can install them using:
 * npm install xmldom
 * npm install node-fetch
 */

import * as fs from 'fs';
import * as path from 'path';
import { DOMParser } from 'xmldom';

// Short for console.log
const log = console.log;

/**
 * JSON (JavaScript Object Notation)
 * 
 * JSON is a data serialization format that resembles JavaScript object literals.
 * However, it is not JavaScript and should not be directly executed (e.g., using `eval()`).
 * JSON is functionally similar to XML or YAML but is more lightweight and easier to parse.
 * 
 * Key Points:
 * - JSON strictly requires double quotes for property names and string values.
 * - JSON is not limited to objects or arrays; it can represent any serializable value.
 */

/**
 * JSON.parse
 * Parses a JSON string into a JavaScript value.
 * 
 * @param text - The JSON string to parse.
 * @param reviver - A function to transform the parsed value.
 * @returns The parsed JavaScript value.
 */

/**
 * JSON.stringify
 * Serializes a JavaScript value into a JSON string.
 * 
 * @param value - The value to serialize.
 * @param replacer - A function or array to filter or transform properties.
 * @param space - Controls indentation in the output string.
 * @returns The JSON string representation of the value.
 */

// Example: JSON vs JavaScript Literals
const nickname = { "nickname": "mytic.dragon" }; // Valid JSON and JavaScript
// const nickname = { nickname: "mytic.dragon" }; // Valid JavaScript, invalid JSON
// const nickname = { 'nickname': 'mytic.dragon' }; // Valid JavaScript, invalid JSON

/**
 * Parsing JSON with a Reviver Function
 * A reviver function can filter or transform the parsed value.
 */
const jsonString = '[{"name":"Kox","age":51},{"name":"Fanny","age":17}]';
const data = JSON.parse(jsonString, (key, value) => key === 'name' ? value.toUpperCase() : value);
log(data); // [{name: "KOX", age: 51}, {name: "FANNY", age: 17}]

/**
 * Parsing Dates in JSON
 * Dates are often serialized as ISO 8601 strings. Use a reviver to parse them into Date objects.
 */
const jsonString2 = '{"date":"2024-10-12T12:28:40.143Z"}';
const data2 = JSON.parse(jsonString2, (key, value) => key === 'date' ? new Date(value) : value);
log(data2); // { date: 2024-10-12T12:28:40.143Z }

/**
 * JSON.stringify Examples
 */
log(JSON.stringify(true)); // 'true'
log(JSON.stringify(154)); // '154'
log(JSON.stringify('roadmap')); // '"roadmap"'
log(JSON.stringify({})); // '{}'
log(JSON.stringify({ name: 'Any' })); // '{"name": "Any"}'
log(JSON.stringify([41, true, 'System Engineering'])); // '[41, true, "System Engineering"]'
log(JSON.stringify(new Date())); // possible output: '"2025-02-24T09:59:25.526Z"'
log(JSON.stringify({ x: Symbol() })); // '{}'

/**
 * Replacer Function
 * Filters or transforms properties during stringification.
 */
function notStrValues(key: string, value: any): any {
    if (typeof value === "string") {
        return undefined; // Exclude string values
    }
    return value;
}

const crew = { background: "Retosparaprogramadores", model: "weekly", week: 12, language: "javascript", month: 3 };
log(JSON.stringify(crew, notStrValues)); // '{"week": 12, "month": 3}'

/**
 * Replacer as an Array
 * Whitelists specific properties for stringification.
 */
log(JSON.stringify(crew, ['background', 'week', 'month'])); // '{"background": "Retosparaprogramadores", "week": 12, "month": 3}'

/**
 * Indentation in JSON.stringify
 */
log(JSON.stringify({ x: 4, y: 4 }, null, 2)); // Indents with 2 spaces
log(JSON.stringify({ x: 4, y: 4 }, null, '\t')); // Indents with tabs

/*
{
  "x": 4,
  "y": 4
}
{
        "x": 4,
        "y": 4
}
*/
/**
 * Exercises: JSON and XML File Handling
 */

// Data to save
const data1 = {
    name: "Niko Zen",
    age: 30,
    birthDate: "1983-08-08",
    languages: ["JavaScript", "Python", "Ruby", "Rust", "Bash"]
};

/**
 * Creates a JSON file from the given data.
 * @param data - The data to serialize into JSON.
 */
function createJSON(data: any): void {
    const jsonData = JSON.stringify(data, null, 2);
    fs.writeFileSync(path.join(__dirname, 'data.json'), jsonData);
    log("Content of the JSON file:");
    log(jsonData);
}

/**
 * Creates an XML file from the given data.
 * @param data - The data to serialize into XML.
 */
function createXML(data: any): void {
    const xmlData = `
<person>
    <name>${data.name}</name>
    <age>${data.age}</age>
    <birthDate>${data.birthDate}</birthDate>
    <languages>
        ${data.languages.map((lang: string) => `<language>${lang}</language>`).join('')}
    </languages>
</person>`;
    fs.writeFileSync(path.join(__dirname, 'data.xml'), xmlData);
    log("Content of the XML file:");
    log(xmlData);
}

/**
 * Deletes the JSON and XML files.
 */
function deleteFiles(): void {
    fs.unlinkSync(path.join(__dirname, 'data.json'));
    fs.unlinkSync(path.join(__dirname, 'data.xml'));
    log("Files deleted.");
}

/**
 * Custom Person Class
 */
class Person {
    constructor(
        public name: string,
        public age: number,
        public birthDate: string,
        public languages: string[]
    ) {}
}

/**
 * Reads and transforms data from JSON and XML files.
 */
function readAndTransform(): void {
    const jsonData = JSON.parse(fs.readFileSync(path.join(__dirname, 'data.json'), 'utf-8'));
    const xmlData = fs.readFileSync(path.join(__dirname, 'data.xml'), 'utf-8');

    // Transform XML to object
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlData, "text/xml");
    const name = xmlDoc.getElementsByTagName("name")[0].textContent || "";
    const age = parseInt(xmlDoc.getElementsByTagName("age")[0].textContent || "0");
    const birthDate = xmlDoc.getElementsByTagName("birthDate")[0].textContent || "";
    const languages = Array.from(xmlDoc.getElementsByTagName("language")).map(lang => lang.textContent || "");

    // Create an instance of Person
    const person = new Person(name, age, birthDate, languages);
    log("Data transformed to Person class:");
    log(person);
}

// Program execution
createJSON(data1);
createXML(data1);
readAndTransform();
deleteFiles();

/* Output:
Content of the JSON file:
{
  "name": "Niko Zen",
  "age": 30,
  "birthDate": "1983-08-08",
  "languages": [
    "JavaScript",
    "Python",
    "Ruby",
    "Rust",
    "Bash"
  ]
}
Content of the XML file:

<person>
    <name>Niko Zen</name>
    <age>30</age>
    <birthDate>1983-08-08</birthDate>
    <languages>
        <language>JavaScript</language><language>Python</language><language>Ruby</language><language>Rust</language><language>Bash</language>
    </languages>
</person>
Data transformed to Person class:
Person {
  name: 'Niko Zen',
  age: 30,
  birthDate: '1983-08-08',
  languages: [ 'JavaScript', 'Python', 'Ruby', 'Rust', 'Bash' ]
}
Files deleted. */