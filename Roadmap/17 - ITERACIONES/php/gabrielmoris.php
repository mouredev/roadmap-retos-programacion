<?php
/*
* EXERCISE:
* Using your language, employ 3 different mechanisms to print
* numbers from 1 to 10 through iteration.
*/
$count = 0;

do {
    $count++;
    echo "Doing while: $count\n";
} while ($count < 10);

$count = 0;
while ($count < 10) {
    $count++;
    echo "While: $count\n";
}

for ($i = 1; $i < 11; $i++) {
    echo "For loop: $i\n";
}

/*
* EXTRA DIFFICULTY (optional):
* Write the highest number of mechanisms that your language has
* to iterate values. Can you use 5? And 10?
*/

$count = 0;
$limit = 10;

function iterator($count, $limit)
{
    if ($count < $limit) {
        $count++;
        echo "Recursive Fn: $count\n";
        return iterator($count, $limit);
    } else {
        return;
    }
}

iterator($count, $limit);

$numbers = range(1, 10);

foreach ($numbers as $number) {
    echo "Foreach Fn: $number\n";
}
