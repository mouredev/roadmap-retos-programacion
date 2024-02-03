<?php

declare(strict_types = 1);

/*
    Array
*/

$data = ['fname', 'surname', 'chile', 'america'];

# Insert
array_unshift($data, 'man'); // insert elements to the begin
array_push($data, 'july'); // insert elements to the end
$data[5] = 'php';

echo 'insert', PHP_EOL;
echo var_dump($data);

# Update
$data[5] = 'php?';

echo 'update', PHP_EOL;
echo var_dump($data);

# Delete
array_shift($data); // delete elements to the begin
array_pop($data); // delete elements to the end
unset($data[5]);

echo 'delete', PHP_EOL;
echo var_dump($data);

# Order

$data = array_reverse($data); // reverse
echo 'reverse', PHP_EOL;
echo var_dump($data);

asort($data); // ascending by value
echo 'ascending by value', PHP_EOL;
echo var_dump($data);

arsort($data); // descending by value
echo 'descending by value', PHP_EOL;
echo var_dump($data);

sort($data); // ascending by index
echo 'ascending by index', PHP_EOL;
echo var_dump($data);

rsort($data); // descending by index
echo 'descending by index', PHP_EOL;
echo var_dump($data);

natsort($data); // by natural order
echo 'by natural order', PHP_EOL;
echo var_dump($data);

natcasesort($data); // by natural order case insensitive
echo 'by natural order case insensitive', PHP_EOL;
echo var_dump($data);

/*
    Array  associative
*/

$data2 = ['fname' => 'fname', 'surname' => 'surname', 'country' => 'chile', 'continent' => 'america'];

# Insert
$data2['kode'] = 'php';

echo 'insert', PHP_EOL;
echo var_dump($data2);

# Update
$data2['kode'] = 'php?';

echo 'update', PHP_EOL;
echo var_dump($data2);

# Delete
unset($data2['kode']);

echo 'delete', PHP_EOL;
echo var_dump($data2);

# Order

$data2 = array_reverse($data2); // reverse
echo 'reverse', PHP_EOL;
echo var_dump($data2);

asort($data2); // ascending by value
echo 'ascending by value', PHP_EOL;
echo var_dump($data2);

arsort($data2); // descending by value
echo 'descending by value', PHP_EOL;
echo var_dump($data2);

ksort($data2); // ascending by index
echo 'ascending by index', PHP_EOL;
echo var_dump($data2);

krsort($data2); // descending by index
echo 'descending by index', PHP_EOL;
echo var_dump($data2);

natsort($data2); // by natural order
echo 'by natural order', PHP_EOL;
echo var_dump($data2);

natcasesort($data2); // by natural order case insensitive
echo 'by natural order case insensitive', PHP_EOL;
echo var_dump($data2);

/*
    Exercise
*/

$option = 0;
$data = [];

function save($array, $number): bool {
    $isNumber = ctype_alpha($number) ? true : false;

    if (strlen($number) <= 11 and $isNumber) {
        $array[$name] = $number;

        return true;
    }

    return false;
}

while ($option != 5) {

    echo "\033c";

    echo '1. search'. PHP_EOL;
    echo '2. add'. PHP_EOL;
    echo '3. edit'. PHP_EOL;
    echo '4. delete'. PHP_EOL;
    echo '5. exit'. PHP_EOL;

    $option = readline('choose an option: ');

    switch ($option) {
        case 1:
            $name = readline('name: ');

            echo $name, PHP_EOL;
            echo $data[$name];

            sleep(5);
            break;
        case 2:
            $name = readline('name: ');
            $number = readline('number: ');

            save($data, $number);
            break;
        case 3:
            $name = readline('name: ');
            $number = readline('number: ');

            save($data, $number);
            break;
        case 4:
            $name = readline('name: ');

            unset($data[$name]);
            break;
        default:
            # code...
            break;
    }
}