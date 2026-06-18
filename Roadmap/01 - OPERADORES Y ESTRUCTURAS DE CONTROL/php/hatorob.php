<?php

$a = 20;
$b = "20";
$c = 20;
$isAdmin = false;
// igualdad
if($a == $b) echo "open in If -> true";
// identico
if($a === $c) echo "open in If -> true";
// menor
if($a < 30) echo "is less value";
// menor o igual
if($a <= 20) echo "is less or equal value";
// mayor
if($a > 10) echo "is more value";
// mayor o igual
if($a >= 10) echo "is more or equal value";

//isTrue
if($isAdmin) echo "is true";
// !
if(!$isAdmin) echo "false";

// and
if($a >= 20 && $c<= 20) echo " is and";
// or
if($a >= 20 || $c<= 20) echo " is or";

// if / else

if($a === $b) echo "true";
else echo "false";

// if /elseif / else
if($a >= $c) echo "option 1";
elseif($a === $c) echo "option 2";
else echo "option 3";

$i=1;
// while
while($i <= 10) {
    echo "number -> $i";
    $i++;
}

// do while -> al menos una vez
$i = 0;
do {
    echo $i;
} while ($i > 0);


// match
$fruit = "manzana";

$returnValue = match($fruit) {
    "manzana" => "manzana",
    "pera" => "pera",
};

echo $returnValue;

// switch

switch ($fruit) {
    case 'mazana':
        echo "option apple";
        break;
    case 'pera':
        echo "option pera";
        break;
    default:
        echo "any fruit";
        break;
}

