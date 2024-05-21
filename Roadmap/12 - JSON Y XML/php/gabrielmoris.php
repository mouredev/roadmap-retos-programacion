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
        $json_file = file_get_contents('gabrielmoris.json');

        echo $json_file . "\n";
        return $json_file;
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

        $xml_file = file_get_contents('gabrielmoris.xml');

        echo $xml_file . "\n";
        return $xml_file;
    } catch (Exception $e) {
        echo "Error trying to read the XML file: " . $e . "\n";
    }
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


$array = ["name" => "Gabrielcmoris", "age" => 34, "birthdate" => "15.12.1989", "programming_languages" => ["Javascript", "Typescript", "php", "rust"]];

json_creator($array);
json_reader();
json_deleter();
xml_creator($array);
xml_reader();
xml_deleter();

/* EXTRA DIFFICULTY (optional):
* Using the logic of creating the previous files, create a
* program capable of reading and transforming into a custom class of your
* language the data stored in the XML and JSON.
* Delete the files.
*/


function class_creator()
{
}

class_creator();
