<?php

/*
* Using your language, create a data set and perform the following operations (you must use a structure that supports them):
* Add an element to the end.
* Add an element to the beginning.
* Add multiple elements in a block to the end.
* Add multiple elements in a block to a specific position.
* Delete an element at a specific position.
* Update the value of an element at a specific position.
* Check if an element is in a set.
* Clear the entire contents of the set.
*/
$dataset = [["name" => "Gabriel", "language" => "javascript"], ["name" => "Sascha", "language" => "php"]];
// 1. Add an element to the end.
$dataset[] = ["name" => "Georg", "language" => "deutsch"];
// 2. Add an element to the beginning.
array_unshift($dataset, ["name" => "Matheus", "language" => "Portuguese"]);
// 3. Add multiple elements in a block to the end.
$dataset = array_merge($dataset, [["name" => "Munch", "language" => "paintings"], ["name" => "Juan", "language" => "rust"]]);
// 4. Add multiple elements in a block to a specific position.
$newElements = [["name" => "somebody", "language" => "somelanguage"], ["name" => "Mark", "language" => "C++"]];
array_splice($dataset, 1, 0, $newElements); // (original array, positiontoadd,number of elements to remove before the insertion,elements to add )
// 5. Delete an element at a specific position.
unset($dataset[1]); // this will delete the key an value, but will leave a gap in the order 0,2,3,4,...
$dataset = array_values($dataset); // This would rearange the keys
// 6. Update the value of an element at a specific position.
$dataset[4] = ["name" => "Kent C. Dodds", "language" => "Javascript"];
// 7. Check if an element is in a set.
echo in_array(["name" => "Kent C. Dodds", "language" => "Javascript"], $dataset) . "\n"; // 1 means found
// 8. Clear the entire contents of the set.
$dataset = [];
echo empty($dataset) . "\n"; // to check if it is empty

var_dump($dataset);
/*
* EXTRA DIFFICULTY (optional): 
* Show examples of the following operations with sets:
* Union.
* Intersection.
* Difference.
* Symmetric difference.
*/