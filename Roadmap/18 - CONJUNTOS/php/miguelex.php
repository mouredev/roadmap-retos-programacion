<?php

    $conjunto = [1,2,3];

    echo "Vamos a mostrar el conjunto inicial: \n";
    print_r($conjunto);
    echo "\n\n";

    $conjunto[] = 4;
    
    echo "Vamos a mostrar el conjunto tras añadir 4 al final: \n";
    print_r($conjunto);
    echo "\n\n";

    array_unshift($conjunto, 0);

    echo "Vamos a mostrar el conjunto tras añadir 0 al principio: \n";
    print_r($conjunto);
    echo "\n\n";

    $nuevos = [5, 6, 7];
    $conjunto = array_merge($conjunto, $nuevos); 

    echo "Vamos a mostrar el conjunto tras añadir 5, 6 y 7 al final: \n";
    print_r($conjunto);
    echo "\n\n";

    array_splice($conjunto, 2, 0, [0.5, 0.75]);

    echo "Vamos a mostrar el conjunto tras añadir 2.5 y 2.75 en la posición 2: \n";
    print_r($conjunto);
    echo "\n\n";

    unset($conjunto[3]);

    echo "Vamos a mostrar el conjunto tras eliminar el elemento en la posición 3: \n";
    print_r($conjunto);
    echo "\n\n";

    $conjunto[1] = 0.5;
    echo "Cambiamos el valor de la posición 1 por 0.5: \n";
    print_r($conjunto);
    echo "\n\n";

    $elemento = 1.5;
    if (in_array($elemento, $conjunto)) {
        echo "$elemento está en el conjunto.";
    } else {
        echo "$elemento no está en el conjunto.";
    }
    echo "\n\n";

    $conjunto = [];
    echo "Vamos a mostrar el conjunto tras vaciarlo: \n";
    print_r($conjunto);
    echo "\n\n";

    // Extra

    $conjunto1 = [1, 2, 3, 4];
    $conjunto2 = [3, 4, 5, 6];

    // Unión
    $union = array_merge($conjunto1, $conjunto2);
    
    echo "Vamos a mostrar la union de los dos conjuntos: \n";
    print_r($union);
    echo "\n\n";

    // Intersección
    $interseccion = array_intersect($conjunto1, $conjunto2);

    echo "Vamos a mostrar la interseccion de los dos conjuntos: \n";
    print_r($interseccion);
    echo "\n\n";
    // Diferencia
    $diferencia = array_diff($conjunto1, $conjunto2);

    echo "Vamos a mostrar la diferencia de los dos conjuntos: \n";
    print_r($diferencia);
    echo "\n\n";

    // Diferencia simétrica
    $diferencia_simetrica = array_merge(array_diff($conjunto1, $conjunto2), array_diff($conjunto2, $conjunto1));

    echo "Vamos a mostrar la diferencia simetrica de los dos conjuntos: \n";
    print_r($diferencia_simetrica);
    echo "\n\n";


