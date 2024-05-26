<?php
/*
 * IMPORTANT: You should only upload the code file as part of the exercise.
 *
 * EXERCISE:
 * Develop a program capable of creating a file named after
 * your GitHub username and has the .txt extension.
 * Add several lines to that file:
 * - Your name.
 * - Age.
 * - Favorite programming language.
 * Print the content.
 * Delete the file.
 */


function file_creator($content, $name)
{
    $checkedName = "";

    if (substr($name, -4) !== '.txt') {
        $checkedName =  $name . ".txt";
    } else {
        $checkedName = $name;
    }

    file_put_contents($checkedName, $content, FILE_APPEND | LOCK_EX);
    echo "File " . $checkedName . " created.\n";
}

function file_reader($name)
{
    $checkedName = "";
    if (substr($name, -4) !== '.txt') {
        $checkedName =  $name . ".txt";
    } else {
        $checkedName = $name;
    }

    $contents = file_get_contents($checkedName);
    echo $contents . "\n";
}

function file_deleter($name)
{
    $checkedName = "";
    if (substr($name, -4) !== '.txt') {
        $checkedName =  $name . ".txt";
    } else {
        $checkedName = $name;
    }

    if (file_exists($checkedName)) {
        if (unlink($checkedName)) {
            echo "File " . $checkedName . " deleted.\n";
        } else {
            echo "File " . $checkedName . " couldn't be deleted.\n";
        }
    } else {
        echo "File " . $checkedName . " doens't exist.\n";
    }
}

$content = "Name: Gabriel Moris \nAge: 34\nFavourite programming language: English.";
$fileName = 'gabrielmoris.txt';
file_creator($content, $fileName);
file_reader($fileName);
file_deleter($fileName);


/* EXTRA DIFFICULTY (optional):
 * Develop a sales management program that stores its data in a
 * .txt file.
 * - Each product is saved on a line of the file in the following way:
 *   [product_name], [quantity_sold], [price].
 * - Following that format, and through terminal, it should allow adding, consulting,
 *   updating, deleting products and exiting.
 * - It should also have options to calculate the total sale and by product.
 * - The exit option deletes the .txt.
 */

function sales_management_system()
{
    echo "
    ===== PRINTER =====
     1.- New Document 
     2.- Read Document
     3.- Delete Document
     4.- Exit
    ==================
     \n";

    do {
        $selection = readline("Select an option\n");
        switch ($selection) {
            case 1:
                new_document();
                break;
            case 2:
                read_document();
                break;
            case 3:
                delete_document();
                break;
            case 4:
                echo "\033c";
                echo "Good bye 👋 🌐\n";
                exit;
            default:
                echo "This option doesn't exist.\n";
        }
    } while (true);
}

function new_document()
{
    $name = readline("Write the name of the document without extenstion (.txt only):\n");
    $content = readline("Write the content of the document without extenstion (.txt only):\n");
    file_creator($content, $name);
}

function read_document()
{
    $name = readline("Write the name of the document without extenstion (.txt only):\n");
    file_reader($name);
}

function delete_document()
{
    $name = readline("Write the name of the document without extenstion (.txt only):\n");
    file_deleter($name);
}

sales_management_system();
