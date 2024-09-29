/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

<?php
    /* Primetra Estructura de Datos Listas Enlazadas Clase SplDoublyLinkedList
    --  La clase SplDoublyLinkedList proporciona las principales funcionalidades de una lista doblemente enlazada. */

    $spldll = new SplDoublyLinkedList;

    /* Add A New Value */
    $spldll->add(0, "0");
    $spldll->add(1, "1");
    $spldll->add(2, "3");
    $spldll->add(3, "10");

    /* Update A Value */
    $spldll->offsetSet(2, "2");

    print_r($spldll);

        /* Delete A Value */
    $spldll->offsetUnset(3);
    print_r($spldll);

        /* Segunda Estructura de Datos Listas Enlazadas Clase SplQueue
    --  La clase SplStack proporciona la funcionalidad principal de una pila implementada mediante una lista doblemente enlazada estableciendo el modo iterador a SplDoublyLinkedList::IT_MODE_LIFO. */

    $splstack = new SplStack;

        /* Add A New Value */
    $splstack->add(0, "0");
    $splstack->add(1,"10");
    $splstack->add(2, "20");

    print_r($splstack);

    /* Update A Value */
    $splstack->offsetSet(0, "1");

    print_r($splstack);

    /* Delete A Value */
    $splstack->offsetUnset(2);

    print_r($splstack);

            /* Tercera Estructura de Datos Listas Enlazadas Clase SplStack
    --  La clase SplQueue proporciona las principales funcionalidades de una cola implementada usando una lista doblemente enlazada al estableciendo el modo del iterador a SplDoublyLinkedList::IT_MODE_FIFO. */

    $splqueue = new SplQueue;

        /* Add A New Value */
    $splqueue->add(0, "0");
    $splqueue->add(1,"10");
    $splqueue->add(2, "20");

    print_r($splqueue);

    /* Update A Value */
    $splqueue->offsetSet(0, "1");

    print_r($splqueue);

    /* Delete A Value */
    $splqueue->offsetUnset(2);

    print_r($splqueue);

                /* Cuarta Estructura de Datos Listas Enlazadas Clase SplMaxHeap
    --  La clase SplMaxHeap proporciona la funcionalidad principal de un montículo, manteniendo el máximo en la parte superior. */

    $splmaxheap = new SplMaxHeap;

            /* Add A New Value */
    $splmaxheap->insert("1");
    $splmaxheap->insert("10");
    $splmaxheap->insert("20");

    print_r($splmaxheap);

        /* Delete A Value */
    $splmaxheap->next();

    print_r($splmaxheap);

                    /* Quinta Estructura de Datos Listas Enlazadas Clase SplMinHeap
    --  La clase SplMinHeap proporciona la funcionalidad principal de un montículo, manteniendo el mínimo en la parte superior.. */

    $splminheap = new SplMinHeap;

            /* Add A New Value */
    $splminheap->insert("1");
    $splminheap->insert("10");
    $splminheap->insert("20");

    print_r($splminheap);

        /* Delete A Value */
    $splminheap->next();

    print_r($splminheap);

                    /* Sexta Estructura de Datos Listas Enlazadas Clase SplFixedArray
    --  la clase SplFixedArray proporciona la funcionalidad principal de un array. La principal diferencia entre SplFixedArray y un array normal de PHP es que la clase SplFixedArray es de longitud fija y sólo permite enteros dentro del rango de índices. La ventaja es que usa menos memoría que un array estándar. */

    $splfixedarray = new SplFixedArray(4);

    /* Add a new Value */
    $splfixedarray[0] = 0;
    $splfixedarray[1] = 1;
    $splfixedarray[2] = 2;
    $splfixedarray[3] = 4;

    print_r($splfixedarray);

    /* Update a new Value */
    $splfixedarray->offsetSet(3,3);

    print_r($splfixedarray);

    /* Delete a new Value */
    $splfixedarray->offsetUnset(3);

    print_r($splfixedarray);

                    /* Septima Estructura de Datos Listas Enlazadas Clase SplObjectStorage
    -- La clase SplObjectStorage proporciona una correspondencia de objetos de datos o, ignorando los datos, un conjunto de objetos. Este doble propósito puede ser útil en muchos casos relacionados con la necesidad de identificar objetos de forma única.*/

    $splobjectstorage = new SplObjectStorage;

    $object_1 = new stdClass;
    $object_2 = new stdClass;

    /* Add a new Object */
    $splobjectstorage[$object_1] = array(0,1,2);
    $splobjectstorage->attach($object_2, "Hello");

    print_r($splobjectstorage);

    /* Update a Object */
    $splobjectstorage->offsetSet($object_2, "Hola");

    print_r($splobjectstorage);

    /* Delete a Object */
    $splobjectstorage->offsetUnset($object_2);

    print_r($splobjectstorage);

?>