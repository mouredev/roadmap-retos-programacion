<?php
    $array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5];
    
    $set = new \Ds\Set($array); // Uso de la clase Set de la extensión PECL Ds

    // https://www.php.net/manual/es/class.ds-set.php
    // En mi caso particular descargue la extensión dll y añadi la extensión en php.ini

    echo "El conjunto tiene ", $set->count(), " elementos\n";
    
    // Añadir un elemento al conjunto

    $set->add(10);

    // Añadir varios elementos al conjunto

    $set->add(11, 12, 13);

    echo "Despues de añadir cuatro elementos el conjunto tiene ahora ", $set->count(), " elementos\n";

    // Verificar si un set contiene un elemento

   echo "El conjunto tiene el número 10: ", $set->contains(10)?"true":"false", " \n";  // true
   echo "El conjunto tiene el número 15: ", $set->contains(15)?"true":"false", " \n";  // false

   // Remover un elemento del conjunto

   $set->remove(0);

   // Remover varios elementos del conjunto

   $set->remove(10, 11, 12, 13); // Tambien se puede $set->remove(...[10, 11, 12, 13])

   echo "Tras eliminar algunos elementos, el conjunto ahora tiene: ", $set->count(), " elementos\n";

   // Eliminar todo el contenido del conjunto

   $set->clear();

   echo "El conjunto después de eliminar todo el contenido tiene ahora ", $set->count(), " elementos\n";

   // RETO EXTRA

   echo "\n*****RETO EXTRA*****\n";

   // Creando dos conjuntos para mostrar varias operaciones con conjuntos
   $M = new \Ds\Set([0, 1, 2, 3, 4, 5]);
   $N = new \Ds\Set([6, 7, 8, 9, 2, 4]);

   echo "\nDado los conjuntos M = {0, 1, 2, 3, 4, 5} y N = {6, 7, 8, 9, 2, 4}\n\n";

   // Diferencia de Conjuntos M \ N
   echo "La diferencia M \ N es: { ", $M->diff($N)->join(","), " }\n";
   echo "La diferencia N \ M es: { ", $N->diff($M)->join(","), " }\n";

   // Intersección de Conjuntos M ∩ N
   echo "La intersección entre los conjuntos es: { ", $M->intersect($N)->join(","), " }\n";

   // Unión de Conjuntos M ∪ N 
   echo "La unión de los conjuntos es: { ", $M->union($N)->join(","), " }\n";

   // Diferencia simétrica de Conjuntos M ⊖ N
   echo "La diferencia simétrica (XOR) de los conjuntos es: { ", $M->xor($N)->join(","), " }\n";
