<?php
echo "\033c";
/*
* IMPORTANT: You should only upload the code file as part of the exercise.
*
* EXERCISE:
* Develop a program capable of creating an XML and JSON file that saves the
* following data (using the correct syntax in each case):
* - Name
* - Age
* - Date of birth
* - List of programming languages
* Display the content of the files.
* Delete the files.
*/

//············ JSON ············
function json_creator($array)
{

    try {
        $json = json_encode($array, JSON_PRETTY_PRINT);
        file_put_contents('gabrielmoris.json', $json);
        echo "File has been created\n";
    } catch (Exception $e) {
        echo " There was an error creating the JSON file: " .  $e . "\n";
    }
}

function json_reader()
{
    try {
        if (file_exists('gabrielmoris.json')) {
            $json_file = file_get_contents('gabrielmoris.json');
            $data = json_decode($json_file, true);
            echo $json_file . "\n";
            return $data;
        } else {
            throw new Exception("The JSON file 'gabrielmoris.json' does not exist.");
        }
    } catch (Exception $e) {
        echo "Error trying to read the JSON file " . $e . "\n";
    }
}

function json_deleter()
{
    try {
        unlink('gabrielmoris.json');
        echo "JSON Deleted\n";
    } catch (Exception $e) {
        echo "There was an error deleting the JSON file: " .  $e . "\n";
    }
}

//············ XML ············
function xml_creator($array)
{
    try {
        $dom = new DOMDocument('1.0', 'UTF-8');
        $dom->formatOutput = true; // It will format the output
        $root = $dom->createElement('gabrielmoris');
        $dom->appendChild($root);

        foreach ($array as $key => $value) {
            $element = $dom->createElement($key);
            $root->appendChild($element);

            if (is_array($value)) {
                foreach ($value as $language) {
                    $languageElement = $dom->createElement('list', $language);
                    $element->appendChild($languageElement);
                }
            } else {
                $element->textContent = $value;
            }
        }

        $dom->save('gabrielmoris.xml');
        echo "File has been created\n";
    } catch (Exception $e) {
        echo "There was an error creating the XML file: " .  $e . "\n";
    }
}

function xml_reader()
{
    try {
        if (file_exists('gabrielmoris.xml')) {
            $xml_file = file_get_contents('gabrielmoris.xml');
            $xml = simplexml_load_string($xml_file);
            // This function (below) Will iterate over the XML and create an array.
            $array = simpleXmlToArray($xml);
            echo $xml_file . "\n";
            return $array;
        } else {
            throw new Exception("The XML file 'gabrielmoris.xml' does not exist.");
        }
    } catch (Exception $e) {
        echo "Error trying to read the XML file: " . $e->getMessage() . "\n";
    }
}

function simpleXmlToArray($simpleXml)
{
    $array = [];
    foreach ($simpleXml->children() as $child) {
        $childName = $child->getName();
        if ($child->count() > 0) { // Child is gonnna be a List and I have to iterate only if I find a key with a list of values
            $array[$childName] = [];
            foreach ($child->children() as $language) {
                $array[$childName][] = (string) $language;
            }
        } else {
            $array[$childName] = (string) $child;
        }
    }
    return $array;
}

function xml_deleter()
{
    try {
        unlink('gabrielmoris.xml');
        echo "XML Deleted\n";
    } catch (Exception $e) {
        echo "There was an error deleting the XML file: " .  $e . "\n";
    }
}

/* EXTRA DIFFICULTY (optional):
* Using the logic of creating the previous files, create a
* program capable of reading and transforming into a custom class of your
* language the data stored in the XML and JSON.
* Delete the files.
*/

class Person
{
    public $name;
    public $age;
    public $birthDate;
    public $programming_languages;
    public $source;

    public function __construct($data, $source)
    {
        $this->name = $data['name'];
        $this->age = $data['age'];
        $this->birthDate = $data['birthdate'];
        $this->programming_languages = [];
        $this->source = $source;

        foreach ($data["programming_languages"] as $pm) {
            $this->programming_languages[] = $pm;
        }
    }

    public function toString()
    {
        echo "\n\n\n====== FROM " . $this->source . " ======\n";
        echo "Name: " . $this->name . "\n" . "Age: " . $this->age . "\n" . "Birthday: " . $this->birthDate . "\n" . "Programming Languages:\n";
        foreach ($this->programming_languages as $pm) {
            echo "  - " . $pm . "\n";
        }
        echo "======================\n\n\n";
    }
}

function class_from_json_creator($array)
{
    json_creator($array);
    $json = json_reader();
    json_deleter();

    if ($json !== null) {
        return new Person($json, "JSON");
    }
    return null;
}

function class_from_xml_creator($array)
{
    xml_creator($array);
    $xml = xml_reader();
    xml_deleter();

    if ($xml !== null) {
        return new Person($xml, "XML");
    }
    return null;
}

$array = ["name" => "Gabrielcmoris", "age" => 34, "birthdate" => "15.12.1989", "programming_languages" => ["Javascript", "Typescript", "php", "rust"]];
$json_person = class_from_json_creator($array);
$json_person->toString();
$xml_person = class_from_xml_creator($array);
$xml_person->toString();
