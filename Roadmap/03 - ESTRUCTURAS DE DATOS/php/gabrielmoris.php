<?php
/*
 * EXERCISE:
 * - Show examples of creating all default-supported structures in your language.
 * - Use insertion, deletion, update, and sorting operations.
 */

// ARRAY
$arr = array(1, 2, 3, 4);
$arr[] = 9; // insertion
unset($arr[1]); // deletion
$arr[1] = 33; // Update
sort($arr); // sorting
var_dump($arr);

// ASSOCIATIVE ARRAY
$asociative_Arr = array("name" => "Gabriel", "age" => 34);
$asociative_Arr["age"] = 35; // update
$asociative_Arr["email"] = "gabriel@example.com"; // insert
ksort($asociative_Arr); // sorting
unset($asociative_Arr["email"]); // delete

// USING: Standard PHP Library (SPL)
// DOUBLY LINKED LIST: list of nodes linked in both directions. Efficient for stacks and queries.
$dll = new SplDoublyLinkedList();
$dll->push(1); //push
$dll->push(2);
$dll->pop(); //deletion
$dll->offsetSet(0, 99); //update


// HEAPS: tree-like structures where each node is greater than or equal to its children.
$heap = new SplMaxHeap();
$heap->insert(1); // insertion
$heap->extract(); //deletion


// PRIORITY QUEUE: priority queue based on a heap. Elements are ordered by priority.
$pq = new SplPriorityQueue();
$pq->insert('A', 1); // Insertion
$pq->insert('B', 1); // Insertion
$pq->insert('C', 1); // Insertion
$pq->extract(); // Deletion
$pq->insert('B', 2); // Update

// MAP: maps from integers/strings to values. SPL provides a map from objects to data.
$map = new SplObjectStorage();
$obj1 = new stdClass();
$obj2 = new stdClass();
$map->attach($obj1, 'Value1'); // Insertion
$map->attach($obj2, 'Value2'); // Insertion
$map->detach($obj2); // Deletion
$map[$obj1] = 'UpdatedValue'; // Update

/*
 * EXTRA CHALLENGE (optional):
 * Create a terminal-based contact agenda.
 * - Implement functionalities for search, insertion, update, and deletion of contacts.
 * - Each contact should have a name and a phone number.
 * - The program first prompts for the desired operation, followed by necessary data.
 * - The program should reject non-numeric phone numbers with more than 11 digits (or any other desired digit count).
 * - Also, provide an option to exit the program.
 */


function agenda($agenda)
{
    echo "\033c";
    echo "
    =====AGENDA=====
    1.- New Contact 
    2.- Search Contact
    3.- Update contact
    4.- Delete Contact
    5.- Exit
    ================
     \n";

    do {
        $selection = readline("Select an option\n");
        switch ($selection) {
            case 1:
                add_contact($agenda);
                break;
            case 2:
                find_contact($agenda);
                break;
            case 3:
                update_contact($agenda);
                break;
            case 4:
                delete_contact($agenda);
                break;
            case 5:
                echo "\033c";
                echo "Good bye 👋📞\n";
                exit;
            default:
                echo "This option doesn't exist.\n";
        }
    } while (true);
};

// I need to pass by reference the agenda
function add_contact(&$agenda)
{
    $name = readline("Write the name:");
    $number = readline("Write the number:");

    if (strlen($number) > 11) {
        echo "The number must be less than 11 digits.\n";
        return;
    } else {
        $agenda[$name] = $number;
    }
};
function find_contact(&$agenda)
{
    $name = readline("Write the name:");
    if (!array_key_exists($name, $agenda)) {
        echo "This contact doesn`t exist\n";
        return;
    } else {
        $number = $agenda[$name];
        echo "The number of " . $name . " is " . $number . "\n";
    }
};
function update_contact(&$agenda)
{
    $name = readline("Write the name:");
    $newName = readline("Write the new name:");
    $newNumber = readline("Write the new number:");
    unset($agenda[$name]);
    $agenda[$newName] = $newNumber;
};
function delete_contact(&$agenda)
{
    $name = readline("Write the name to DELETE:");
    unset($agenda[$name]);
};

$contacts = [];
agenda($contacts);
