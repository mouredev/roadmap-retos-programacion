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
/** @var object $set1 */
$dataset1 = [["number" => "1", "letter" => "a"], ["number" => "2", "letter" => "b"]];
$dataset2 = [["number" => "2", "letter" => "b"], ["number" => "3", "letter" => "c"], ["number" => "4", "letter" => "d"]];

// 1. Union: combines the two datasets and removes duplicates.
$union = array_merge($dataset1, $dataset2);
$union = array_map("unserialize", array_unique(array_map("serialize", $union)));
echo "Union: ";
var_dump($union);

// 2. Intestection: finds elements that are common to both datasets.
$intersection = array_uintersect($dataset1, $dataset2, 'compare_deep_value');
function compare_deep_value($val1, $val2)
{
    return strcmp(serialize($val1), serialize($val2));
}
echo "Intersection: ";
var_dump($intersection);

// 3. Difference: finds elements that are in the first dataset but not in the second.
$difference = array_udiff($dataset1, $dataset2, 'compare_deep_value');
echo "Difference: ";
var_dump($difference);

// 4. Symmetric difference:  operation finds elements that are in either of the datasets but not in both.ç
$symmetricDifference = array_merge(array_udiff($dataset1, $dataset2, 'compare_deep_value'), array_udiff($dataset2, $dataset1, 'compare_deep_value'));
echo "Symetric difference: ";
var_dump($symmetricDifference);
