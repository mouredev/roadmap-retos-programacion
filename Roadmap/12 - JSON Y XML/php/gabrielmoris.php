<?php
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


function json_creator()
{
    $array = ["name" => "Gabrielcmoris", "age" => 34, "birthdate" => "15.12.1989", "programming_languages" => ["Javascript", "Typescript", "php", "rust"]];
    $json = json_encode($array, JSON_PRETTY_PRINT);

    file_put_contents('gabrielmoris.json', $json);
}
json_creator();

/* EXTRA DIFFICULTY (optional):
* Using the logic of creating the previous files, create a
* program capable of reading and transforming into a custom class of your
* language the data stored in the XML and JSON.
* Delete the files.
*/
