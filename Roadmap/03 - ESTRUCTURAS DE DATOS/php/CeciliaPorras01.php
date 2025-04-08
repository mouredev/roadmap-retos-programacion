<?php /*
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */


 //Listas 

 $my_lists = array("Cecilia", "Porras", "Gonzalez", "Porras", "Torres");
 print_r($my_lists);

 array_push($my_lists, "Martha");//Inserción
print_r($my_lists);

unset($my_lists[2]); // Eliminación
print_r($my_lists);

$my_lists[1] = "Porrasssss"; // Actualización
print_r($my_lists);

print_r($my_lists[5]);//Acceso

sort($my_lists); //Ordenación
print_r($my_lists);


//Tuplas
$my_tuples = array("Cecilia", "Porras", "@porrasceci", "23");
print_r($my_tuples[3]);//Acceso

sort($my_tuples);//Ordenación
print_r($my_tuples);



//Diccionarios
$my_dict = array("Nombre" => "Cecilia", "Apellido" => "Porras", "Edad" => "23", "Twitter" => "@porrasceci");
print_r($my_dict["Edad"]);//Acceso

$my_dict["Edad"] = "24";//Actualización
print_r($my_dict["Edad"]);

unset($my_dict["Twitter"]);//Eliminación
print_r($my_dict);

$my_dict["Telefono"] = "1234567890";//Inserción
print_r($my_dict);




//Extra 

$agenda =[];

    function contacts(){

        global $agenda;

        while (true) {
         
        print "Bienvenido a la agenda de contactos 📕\n  ";
        print "Selecciona una opción:\n";
        print "1.- Buscar contacto 🔎\n";
        print "2.- Insertar contacto ➕\n";
        print "3.- Actualizar contacto 👲🏽\n";
        print "4.- Eliminar contacto 🗑️\n";
        print "5.- Salir\n";

        $option = readline("Opción: "); 

            switch($option){
                case 1:     
                    print  "Has elegido: Buscar contacto 🔎\n";
                        searchContact($agenda);
                    break;
                case 2:
                    print  "Has elegido: Insertar contacto ➕\n";
                        addContact($agenda);
                    break;
                case 3:
                    print  "Has elegido: Actualizar contacto 👲🏽\n";
                        updContact($agenda);
                    break;
                case 4:
                    print  "Has elegido: Eliminar contacto 🗑️\n";
                    break;
                case 5:
                    print  "Saliendo... 👋\n";
                    exit;
                default:
                    print  "❌ Opción no válida. Inténtalo de nuevo.\n";
                    break;
            }
        }
    }

    function getContactInfo() {
        print "Introduce el nombre del contacto: ";
        $name = readline();
        print "Introduce el número de teléfono: ";
        $phone = readline();

        if ($name == "" || !preg_match("/^[a-zA-Z\s]+$/", $name)) {
            print "❌ Debes introducir un nombre válido (solo letras y espacios).\n";
            return null;
        } elseif ($phone == "" || !is_numeric($phone) || strlen($phone) != 10) {
            print "❌ Debes introducir un número de teléfono válido (10 dígitos).\n";
            return null;
        } else {
            return ['name' => $name, 'phone' => $phone];
        }
    }


    function searchContact($agenda) {
        $contact = getContactInfo();
        if ($contact) {
            foreach($agenda as $entry) {
                if ($entry['name'] == $contact['name'] && $contact['phone'] == $contact['phone']) {
                    print  "Contacto encontrado: \n";
                    print  "Nombre: " . $contact['name'] . "\n";
                    print  "Teléfono: " . $contact['phone'] . "\n";
                }

            }
      
            print  " ❌ Contacto no encontrado\n";
        }
    }

    function addContact($agenda) {
        $contact = getContactInfo();
        $agenda[] = $contact;
        if ($contact) {
            print  "Contacto añadido: \n";
            print  "Nombre: " . $contact['name'] . "\n";
            print  "Teléfono: " . $contact['phone'] . "\n";
        }
    }


    function updContact($agenda) {
        $contact = getContactInfo();
        if ($contact) {
            print  "Contacto actualizado: \n";
            print  "Nombre: " . $contact['name'] . "\n";
            print  "Teléfono: " . $contact['phone'] . "\n";
        }
        print  " ❌ Contacto no actualizado\n";
    }

    function deleteContact($agenda) {
        $contact = getContactInfo();
        if ($contact) {
            foreach ($agenda as $key => $entry) {
                if ($entry['name'] == $contact['name']) {
                    unset($agenda[$key]);
                    print  "Contacto eliminado: \n";
                    print  "Nombre: " . $contact['name'] . "\n";
                    print  "Teléfono: " . $contact['phone'] . "\n";
                }
            }
            print " ❌ Contacto no eliminado\n";
        }
    }


// Llamamos a la función
contacts();

