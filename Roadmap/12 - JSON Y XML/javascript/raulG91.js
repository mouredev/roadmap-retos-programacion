const fs = require('fs').promises
const path = require('path')
const xml2js = require('xml2js')


let json_data = {
    "name": "Raul",
    "age": 33,
    "birth_date": "11/09/1991",
    "languages": ["Python", "Javascript", "Abap"]
};

async function createJSONFile(filename, data) {

    path_file = path.join(__dirname, filename);
    await fs.writeFile(path_file, JSON.stringify(data))

}
async function readJSONFile(filename) {

    let path_file = path.join(__dirname, filename);
    let data = await fs.readFile(path_file);
    object = JSON.parse(String(data))
    return object;
}
async function deleteFile(filename) {

    let path_file = path.join(__dirname, filename);
    await fs.unlink(path_file);
}

async function createXMLfile(filename, data) {

    let path_file = path.join(__dirname, filename);
    await fs.writeFile(path_file, data);
    
}

async function readXMLFile(filename){

    let parser = new xml2js.Parser();
    let path_file = path.join(__dirname, filename);
    let data = await fs.readFile(path_file);
    parser.parseString(data, function (err, result) {
        result_object = Object(result)
        console.log(result_object.Root.name);
    
    });

}

//Create the file
createJSONFile("file.json", json_data).then(function (result) {
    //Read the file once it is created
    readJSONFile("file.json").then(
        function (result) {
            console.log(result)
            //Delete JSON file 
            deleteFile("file.json").then((result) => console.log("JSON file was deleted"),
                (error) => console.log("Error deleting JSON file"));
        }, error => console.log("Error opening JSON file"));

}, error => console.log("Error creating JSON file"));


let xml_data = `<Root>
                    <name>Raul</name>
                    <age>33</age>
                    <birth_date>11/09/1991</birth_date>
                    <languages>
                        <language>
                            <name>Python</name>
                        </language>
                        <language>
                            <name>Javascript</name>
                        </language>     
                        <language>
                            <name>Abap</name>
                        </language>                                            
                    </languages>
                </Root>`;
createXMLfile("file.xml", xml_data).then(function(result){
    readXMLFile("file.xml").then(function(result){
        deleteFile("file.xml").then(result=>console.log("XML file deleted"),
                                    error => console.log("Error deleting xml file"));
    })
}, error => console.log("Error creating XML file"));
   
