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

    /*  Ejercicio de Agenda de Contactos    */

    echo "Bienvenido a la Agenda de Contactos.\n";
    echo "Las Opciones que se pueden realizar son las siguientes:\n";
    echo "Ver Lista de Contactos. Coloca 1.\n";
    echo "Buscar un Contacto en la Lista. Coloca 2.\n";
    echo "Guardar Contacto. Coloca 3.\n";
    echo "Actualizar Contacto. Coloca 4.\n";
    echo "Eliminar Contacto. Coloca 5.\n";
    echo "Salir de la Agenda. Coloca 6.\n";

    Class Contacto
    {
        public $nombre;
        public $numero;
        public static $agenda;
        public function __construct($nombre, $numero)
        {
            $this->nombre = $nombre;
            $this->numero = $numero;
        }   // Here End Constructor

        // Instancia de SPlobjectStorage
        public static function iniciarAgenda()
        {
            self::$agenda = new SplObjectStorage;
        }   // Here End Function

        // Guarda los Contactos en la Agenda
        public static function guardar($nuevo_contacto)
        {
            self::$agenda->attach($nuevo_contacto);
            echo "Contacto Agregado Correctamente";
        }   // Here End FUnction

        // Actualiza los Contactos en la Agenda
        public function actualizar($nombre_actualizar, $numero_actualizar)
        {
            $this->nombre = $nombre_actualizar;
            $this->numero = $numero_actualizar;
        }   // Here End Function

        // Muestra los Conctactos de la Agenda
        public function getInfo() 
        {
            return "Nombre: $this->nombre, Número: $this->numero";
        }   // Here End Function

        // Buscar un contacto
        public static function find($nombre_buscar)
        {
            self::$agenda->rewind();
            while (self::$agenda->valid()) {
                $contacto = self::$agenda->current();
                if ($contacto->nombre == $nombre_buscar) 
                {
                    return $contacto;
                }   // Here End If
                self::$agenda->next();
            }   // Here End While
            return false;
        }   // Here End Function

        // Mostrar todos los contactos en la agenda
        public static function show()
        {
            self::$agenda->rewind();

            while(self::$agenda->valid())
            {
                $contactos = self::$agenda->current();
                echo $contactos->getInfo() . ".\n";
                self::$agenda->next();
            }   // Here End While
        }   // Here End Function

        // Elimina los Contactos en la Agenda
        public function eliminar()
        { 

        }   // Here End Function
    }   // Here End Class

    // Instancia de Estructura SPLOBJECTSTORAGE
    Contacto::iniciarAgenda();
    $agenda = Contacto::$agenda;

    // Crear Objetos de Contactos
    $contacto_1 = new Contacto("Jeyker", "04245652392");
    $contacto_2 = new Contacto("Maria", "04263318767");
    $contacto_3 = new Contacto("Ramon", "04125618690");
    $contacto_4 = new Contacto("Alejandro", "04164126754");
    $contacto_5 = new Contacto("Fernando", "04148879135");

    // Agregar Contactos a la agenda
    $agenda->attach(object: $contacto_1);
    $agenda->attach(object: $contacto_2);
    $agenda->attach(object: $contacto_3);
    $agenda->attach(object: $contacto_4);
    $agenda->attach(object: $contacto_5);

    // Pedir al usuario ingresar un dato
    $numero =  trim(fgets((STDIN)));

    // Validacion para verificar que el dato ingresado sea numerico
    if(filter_var($numero, FILTER_VALIDATE_INT) === false)
    {
        echo "El Dato a Ingresar Debe Ser un Numero.\n";
        exit;
    }   // Here End If

    // Validacion para que el numero a ingresar sea entre las opciones dadas
    if($numero <= 0 || $numero > 6)
    {
        echo "El Dato a Ingresar Debe Ser Entre las Opciones Dadas.\n";
        exit;
    }   // Here End If

    // Menu de opciones
    switch($numero)
    {
        // Mostras la lista de contactos en la agenda
        case 1:
            echo "Lista de Contactos: \n";
            Contacto::show();
            break;

        // Buscar un contacto en la agenda
        case 2:
            echo "Ingresa El Nombre del Contacto que Buscas:\n";
            $contacto_buscar = trim(fgets(STDIN));
            $contacto = Contacto::find($contacto_buscar);
                if ($contacto) 
                {
                    echo "Contacto encontrado: " . $contacto->getInfo() . "\n";
                }   // Here End If 
                else 
                {
                    echo "No se encontraron contactos.\n";
                }   // Here End Else
            break;

            // Guardar un Contacto
        case 3:
            echo "Escribe un Nombre para el Contacto: . \n";
            $nombre_contacto = trim(fgets(STDIN));

            echo "Escribe un Numero para el Contacto: . \n";
            $numero_contacto = trim(fgets(STDIN));

            $contacto_nuevo = new Contacto($nombre_contacto, $numero_contacto);

            $agenda->attach($contacto_nuevo);

            echo "Contacto Agregado Correctamente.\n";
            break;

        case 4;
            echo "Lista de Contactos: \n";
            Contacto::show();

            echo "Escribe el Nombre del Contacto a Editar: \n";
            $nombre_actualizar = trim(fgets(STDIN));

            $contacto_encontrado = Contacto::find($nombre_actualizar);

            if($contacto_encontrado === false)
            {
                echo "No se Encontraron Contactos con Este Nombre. \n";
            }   // Here End If
            else
            {
                echo "Ingresa un Nuevo Nombre: ";
                $nuevo_nombre = trim(fgets(STDIN));

                echo "Ingresa un Nuevo Numero: ";
                $nuevo_numero = trim(fgets(STDIN));

                $contacto_encontrado->actualizar($nuevo_nombre, $nuevo_numero);
                echo "Contacto Actualizado. \n";
                Contacto::show();
            }   // Here End Else

            break;

        case 5;
        Contacto::show();

        echo "Escribe el Nombre del Contacto que Quieres Eliminar: ";
        $nombre_eliminar = trim(fgets(STDIN));

        $contacto_eliminar = Contacto::find($nombre_eliminar);

        $agenda->offsetUnset($contacto_eliminar);

        Contacto::show();

        echo "Contacto Eliminado Correctamente.\n";
        break;

        case 6:
            echo "Saliendo de la Agenda.\n";
            break;

            default:
            echo "Error Inesperado. Vuelva a Intentar";
            break;
    }   // Here End Switch
?>