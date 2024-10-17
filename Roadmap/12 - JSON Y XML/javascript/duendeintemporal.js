/* #12 JSON Y XML */
//bibliography reference
//Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//JavaScript Notes for Professionals (GoalKicker.com) (Z-Library)
//GPT

//Note: We will use Node.js and the xmldom and node-fetch libraries: you can do npm instal xmldom 

//JSON 
/*  JSON stands for "JavaScript Object Notation", but it's not JavaScript. Think of it as just a data serialization format that happens to be directly usable as a JavaScript literal. However, it is not advisable to directly run (i.e. through eval()) JSON that is fetched from an external source. Functionally, JSON isn't very different from XML or YAML – some confusion can be avoided if JSON is just imagined as some serialization format that looks very much like JavaScript.*/
/* Even though the name implies just objects, and even though the majority of use cases through some kind of API always happen to be objects and arrays, JSON is not for just objects or arrays.  */

/* JSON.parse Parse a JSON string
reviver(function) Prescribes a transformation for the input JSON string.
JSON.stringify Serialize a serializable value
replacer(function or String[] or Number[]) Selectively includes certain properties of the value object.
space(String or Number) If a number is provided, then space number of whitespaces will be
inserted of readability. If a string is provided, the string (first 10 characters) will be used as whitespaces. */

// JSON versus JavaScript literals
/*While some JSON is also valid JavaScript and some JavaScript is also valid JSON, there are some subtle differences between both languages and neither language is a subset of the other. */
//JSON
//{"nickname": "mytic.dragon"}

//short for console.log
let log = console.log

//This can be directly inserted into JavaScript. It will be syntactically valid and will yield the correct value:
const nickname = {"nickname": "mytic.dragon"};

//However, we know that "nickname" is a valid identifier name and the quotes around the property name can be omitted:

//const nickname = {nickname: "mytic.dragon"};

//We also know that we can use single quotes instead of double quotes:

//const nickname = {'nickname': 'mytic.dragon'};

//But, if we were to take both of these literals and treat them as JSON, neither will be syntactically valid JSON:

//{nickname: "mytic.dragon"}
//{'nickname': 'mytic.dragon'}

/*JSON strictly requires all property names to be double quoted and string values to be double quoted as well.
 It's common for newcomers to JSON to attempt to use JavaScript object literals as JSON,
 leading to syntax errors when using a JSON parser.*/

 //You will need to add a extension to allow Cross-Origin Resourse Sharing(CORS)
  //  Node.js doesn't implement the fetch API natively. You can install it using: npm install node-fetch. I will coment the next code to avoid conflicts

//  let numberOfParagraphs = 2;
//  let url = `https://baconipsum.com/api/?type=meat-and-filler&paras=${numberOfParagraphs}`;
 
//  fetch(url)
//      .then(response => {
//          if (!response.ok) {
//              throw new Error(`HTTP error! status: ${response.status}`);
//          }
//          return response.json();
//      })
//      .then(loremIpsumTextArray => {
//          log(loremIpsumTextArray); 
//      })
//      .catch(error => {
//          console.error(error); 
//      });
 
/*In the above example, response is a JSON string that is returned by some API. JSON stops at the HTTP response domain.  (could be an object, an array, or even a simple number!)  */


/* Developers often use the phrase "JSON object," which can lead to confusion. 
   A more accurate term is "JSON string," as it refers to the serialized format. 
   After parsing, you end up with a JavaScript value (object, array, etc.). 
   Just like "XML string" or "YAML string," you get a string, parse it, and obtain a value. */

// Parsing with a reviver function. A reviver function can be used to filter or transform the value being parsed.

/*var jsonString = '[{"name":"Kox","age":51},{"name":"Fanny","age":17}]';
var data = JSON.parse(jsonString, function reviver(key, value) {
return key === 'name' ? value.toUpperCase() : value;
});*/

//or with arrow functions

const jsonString = '[{"name":"Kox","age":51},{"name":"Fanny","age":17}]';
const data = JSON.parse(jsonString, (key, value) => key === 'name' ? value.toUpperCase() : value );
log(data); // [{name:"KOX", age:51},{name:"FANNY", age:17}]

/*This is particularly useful when data must be sent that needs to be serialized/encoded when being transmitted with JSON, but one wants to access it deserialized/decoded. In the following example, a date was encoded to its ISO 8601 representation. We use the reviver function to parse this in a JavaScript Date.*/

const jsonString2 = '{"date":"2024-10-12T12:28:40.143Z"}';
const data2 = JSON.parse(jsonString2, (key, value) => key === 'date' ? new Date(value) : value);
log(data2); // {date: 2024-10-12T12:28:40.143Z}

/*It is important to make sure the reviver function returns a useful value at the end of each iteration. If the reviver function returns undefined, no value or the execution falls off towards the end of the function, the property is deleted from the object. Otherwise, the property is redefined to be the return value.*/

//A JavaScript value can be converted to a JSON string using the JSON.stringify function.
//JSON.stringify(value[, replacer[, space]])

/* Boolean */
log(JSON.stringify(true)); // 'true'
/* Number */ 
log(JSON.stringify(154)); // '154'
/* String */ 
log(JSON.stringify('roadmap')); // '"roadmap"'
/* Object */ 
log(JSON.stringify({})); // '{}'
log(JSON.stringify({name: 'Any'})); // '{"name": "Any"}'
/* Array */ 
log(JSON.stringify([41, true, 'System Ingeniering'])); // '[41, true, "System Ingeniering"]'
/* Date */ 
log(JSON.stringify(new Date())); // '"2016-08-06T17:25:23.588Z"'
/* Symbol */ 
log(JSON.stringify({x:Symbol()})); // '{}'

/*replacer A function that alters the behaviour of the stringification process or an array of String and Number2. objects that serve as a whitelist for filtering the properties of the value object to be included in the JSON string. If this value is null or is not provided, all properties of the object are included in the resulting JSON string. */
// replacer as a function
function notStrValues (key, value) {
    if (typeof value === "string") {
        return
    } 
    return value
}

let crew = { background: "Retosparaprogramadores", model: "weekly", week: 12, language: "javascript", month: 3 }
log(JSON.stringify(crew, notStrValues)); //  '{"week": 45, "month": 7}'

// replacer as an array
log(JSON.stringify(crew, ['background', 'week', 'month'])); //  '{"background": "Retosparaprogramadores", "week": 12, "month": 3}'
// only the `background`, `week`, and `month` properties are kept

// indentation may be specified as the third parameter.
log(JSON.stringify({x: 4, y: 4}, null, 2)); // 2 space characters will be used for indentation
/* output:
{
  'x': 4,
  'y': 4
}
*/
//Alternatively, a string value can be provided to use for indentation. For example, passing '\t' will cause the tab character to be used for indentation.
log(JSON.stringify({x: 4, y: 4}, null, '\t'));
/* output:
{
    'x': 4,
    'y': 4
}
*/

//Exercises
const fs = require('fs');
const path = require('path');
const { DOMParser } = require('xmldom'); // you need to do a: npm install xmldom

//Note: DOMParser API doesn't have natively implementation on Node.js]

// Data to storage
const data1 = {
    name: "Niko Zen",
    age: 30,
    birthDate: "1983-08-08",
    languages: ["JavaScript", "Python", "Ruby", "Rust", "Bash"]
};

// Function to create a JSON file
function createJSON(data) {
    const jsonData = JSON.stringify(data, null, 2);
    fs.writeFileSync(path.join(__dirname, 'data.json'), jsonData);
    log("Content of the JSON file:");
    log(jsonData);
}

// Function to create an XML file
function createXML(data) {
    const xmlData = `
<person>
    <name>${data.name}</name>
    <age>${data.age}</age>
    <birthDate>${data.birthDate}</birthDate>
    <languages>
        ${data.languages.map(lang => `<language>${lang}</language>`).join('')}
    </languages>
</person>`;
    fs.writeFileSync(path.join(__dirname, 'data.xml'), xmlData);
    log("Content of the XML file:");
    log(xmlData);
}

// Function to delete files
function deleteFiles() {
    fs.unlinkSync(path.join(__dirname, 'data.json'));
    fs.unlinkSync(path.join(__dirname, 'data.xml'));
    log("Files deleted.");
}

// Custom class
class Person {
    constructor(name, age, birthDate, languages) {
        this.name = name;
        this.age = age;
        this.birthDate = birthDate;
        this.languages = languages;
    }
}

// Function to read and transform data
function readAndTransform() {
    const jsonData = JSON.parse(fs.readFileSync(path.join(__dirname, 'data.json')));
    const xmlData = fs.readFileSync(path.join(__dirname, 'data.xml'), 'utf-8');

    // Transform XML to object
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlData, "text/xml");
    const name = xmlDoc.getElementsByTagName("name")[0].textContent;
    const age = parseInt(xmlDoc.getElementsByTagName("age")[0].textContent);
    const birthDate = xmlDoc.getElementsByTagName("birthDate")[0].textContent;
    const languages = Array.from(xmlDoc.getElementsByTagName("language")).map(lang => lang.textContent);

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

