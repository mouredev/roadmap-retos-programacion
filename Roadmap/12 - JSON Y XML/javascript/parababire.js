const fs = require("fs");
const xml2js = require("xml2js");
const parseString = require("xml2js").parseString;
const {Builder} = require("xml2js");
const xmlFile = "parababire.xml";
const jsonFile = "parababire.json";

const persona = {
  nombre: "Ángel",
  edad: 44,
  fechaNacimiento: "16-09-1979",
  lenguajes: {
    item: [
        "JavaScript",
        "Python"
    ]
}
}

//Convirtiendo un objeto en un fichero.xml

function guardarXml() {
  const builder = new Builder();
  const xml = builder.buildObject(persona);

  fs.writeFileSync(xmlFile, xml);
}
guardarXml();

const xmlData = fs.readFileSync(xmlFile, "utf8");
console.log(xmlData);

fs.unlink(xmlFile, err => {
  if (err) throw err;
  console.log("Archivo borrado");
});

//Convirtiendo un objeto a JSON

function crearJson() {
  const string = JSON.stringify(persona);
  fs.writeFileSync(jsonFile, string);
}
crearJson();

const data = fs.readFileSync(jsonFile, "utf8");
console.log(data);

fs.unlink(jsonFile, err => {
  if (err) throw err;
  console.log("Archivo borrado");
});


//Extra
guardarXml();
crearJson();

const parser = new xml2js.Parser();
const objDataFromXml = parseString(xmlData, function (err, result) {
  console.dir(result);
});

const objDataFromJson = JSON.parse(data);
console.log(objDataFromJson);