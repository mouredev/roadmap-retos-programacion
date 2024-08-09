<?php

    $contacts = [];
    $exit = false;

    while (!$exit) {
        echo "\n\n>> Select an option\n1) Search contact\n2) Create contact\n3) Update contact\n4) Delete contact\n0) Exit\n>> ";
        $option = readline();

        switch ($option) {
            case '1':
                if (count($contacts) > 0) {
                    echo "\n>> Type the contact's name\n>> ";
                    $name = readline();
                    if (array_key_exists($name, $contacts)) {
                        echo "\nContact " . $name . " - Phone " . $contacts[$name];
                    } else {
                        echo "\nContact not found";
                    }
                } else {
                    echo "\nNo contacts in the address book";
                }
                break;

            case '2':
                echo "\n>> Enter the name of the new contact\n>> ";
                $name = readline();
                do {
                    echo "\n>> Type the phone number of the new contact (9-11 digits)\n>> ";
                    $phone = readline();
                } while (!(strlen($phone) >= 9 && strlen($phone) <= 11 && ctype_digit($phone)));
                $contacts[$name] = $phone;
                echo "Contact successfully created - " . $name . " (" . $phone . ") ";
                break;

            case '3':
                echo "\n>> Enter the name of the contact to update\n>> ";
                $name = readline();
                if (array_key_exists($name, $contacts)) {
                    do {
                        echo "\n>> Enter the new phone number (9-11 digits)\n>> ";
                        $phone = readline();
                    } while (!(strlen($phone) >= 9 && strlen($phone) <= 11 && ctype_digit($phone)));
                    $contacts[$name] = $phone;
                    echo "Contact " . $name . " updated";
                } else {
                    echo "\nContact not found";
                }
                break;

            case '4':
                echo "\n>> Type the name of the contact you want to delete\n>> ";
                $name = readline();
                if (array_key_exists($name, $contacts)) {
                    unset($contacts[$name]);
                    echo "\nThe contact " . $name . " has been deleted";
                } else {
                    echo "\nContact not found";
                }
                break;

            case '0':
                $exit = true;
                echo "\n>> Exiting...";
                break;

            default:
                echo "\n>> Invalid option";
                break;
        }
    }

?>
