
<?php 

/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */



 //Tipo de dato por valor 

    $a = 5;
    $b = $a;
    $b = 10;

    print $a; 
    print $b;


    //Tipo de dato por referencia

    $colores = ["rojo", "azul", "verde"];
    $colores2 = &$colores;
    $colores2[0] = "amarillo";
    print_r($colores);
    print_r($colores2);


    //Funciones con datos por valor
    $my_variable = 4;

    function my_function($my_variable){
        $my_variable = 8 ."\n";
        print $my_variable;
    }

    my_function($my_variable);
    print($my_variable);



    //Funciones con datos por referencia
    $my_list = [1, 2, 3];

    function my_function2(&$my_list){
        $my_list[] = 4;
        $my_list_2 = &$my_list;
        $my_list_2[] = 5;
        print_r($my_list);
    }

    my_function2($my_list);
    print_r($my_list);


    //Extra

    //Por valor 
    $var_1 = 10;
    $var_2 = 20;

    function values($var_1, $var_2){
        $temp = $var_1;
        $var_1 = $var_2;
        $var_2 = $temp;
        return [$var_1, $var_2];
    }

print_r(values($var_1, $var_2));
print("Valor1=".$var_1.", Valor2=". $var_2);


 //Por referncia
    $list_1 = ["azul","rojo","verde"];
    $list_2 = ["amarillo","naranja","morado"];

    function values_list($list_1, $list_2){
        $temp = $list_1;
        $list_1 = $list_2;
        $list_2 = $temp;
        return [$list_1, $list_2];
    }

    print_r(values_list($list_1, $list_2));
    print_r($list_1);
    print_r($list_2);
