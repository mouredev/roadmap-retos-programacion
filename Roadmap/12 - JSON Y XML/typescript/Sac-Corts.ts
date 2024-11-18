import * as fs from 'fs';

interface PersonData {
    name: string;
    age: number;
    birthdate: string;
    programmingLanguage: string[];
}

const data: PersonData = {
    name: 'Isaac Cortés',
    age: 22,
    birthdate: "2001-10-21",
    programmingLanguage: ["JavaScript", "Python"]
};

fs.writeFileSync('data.json', JSON.stringify(data, null, 4));

let xmlData2 = `<?xml version ="1.0" encoding="UTF-8"?>
<person>
    <name>${data.name}</name>
    <age>${data.age}</age>
    <birthdate>${data.birthdate}</birthdate>
    <programmingLanguage>${data.programmingLanguage.map(lang => `<language>${lang}</language>`).join('\n     ')}</programmingLanguage>
</person>`;

fs.writeFileSync('data.xml', xmlData2);

console.log("Content of data.json:");
console.log(fs.readFileSync('data.json', 'utf8'));

console.log("\nContent of data.xml:");
console.log(fs.readFileSync('data.xml', 'utf8'));

// ** Extra Exercise ** //

class Person {
    name: string;
    age: number;
    birthdate: string;
    programmingLanguage: string[];

    constructor(name: string, age: number, birthdate: string, programmingLanguage: string[]) {
        this.name = name;
        this.age = age;
        this.birthdate = birthdate;
        this.programmingLanguage = programmingLanguage;
    }

    showData(): void {
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
        console.log(`Birthdate: ${this.birthdate}`);
        console.log(`Programming Language: ${this.programmingLanguage.join(', ')}`);
    }
}

// Read JSON and XML file
const jsonContent: string = fs.readFileSync('data.json', 'utf-8');
const xmlContent: string = fs.readFileSync('data.xml', 'utf-8');

// Parse JSON and XML in JavaScript
const jsonData: PersonData = JSON.parse(jsonContent);

function parseXML(xml: string): PersonData {
    const name = xml.match(/<name>(.*?)<\/name>/)![1];
    const age = parseInt(xml.match(/<age>(.*?)<\/age>/)![1], 10);
    const birthdate = xml.match(/<birthdate>(.*?)<\/birthdate>/)![1];
    const languagesMatches = xml.match(/<language>(.*?)<\/language>/g);
    const programmingLanguage = languagesMatches!.map(lang => lang.replace(/<\/?language>/g,  ''));

    return {
        name,
        age,
        birthdate,
        programmingLanguage
    };
}

const xmlData: PersonData = parseXML(xmlContent);

// Create instances of the class with the read data
const personFromJson = new Person(
    jsonData.name,
    jsonData.age,
    jsonData.birthdate,
    jsonData.programmingLanguage
);

const personFromXml = new Person(
    xmlData.name,
    xmlData.age,
    xmlData.birthdate,
    xmlData.programmingLanguage
);

// Show data for class instances
console.log("Data from JSON:");
personFromJson.showData();

console.log("\nData from XML:");
personFromXml.showData();

// Delete the files
fs.unlinkSync('data.json');
fs.unlinkSync('data.xml');
console.log("\nDeleted files.");
