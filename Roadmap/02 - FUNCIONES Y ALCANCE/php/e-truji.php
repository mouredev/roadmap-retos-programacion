<?php

// --------------------------------------------------
// FUNCIONES BÁSICAS DE PHP
// --------------------------------------------------

### SIN PARAMETROS NI RETORNO ### 

// No necesita datos para ejecutarse ni devuelve nada, solo realiza una tarea
function maullar(): void {
    echo "Miau, miau, miau...\n";
}
maullar(); // Llamada a la función


### CON UN PARAMETRO Y SIN RETORNO ### 

// Recibe informacion para personalizar la acción, pero sigue sin devolver nada
function acariciarGato(string $nombreGato): void {
    echo "Acaricias a {$nombreGato}... *ronroneo*\n";
}
acariciarGato("Naruto");
acariciarGato("Luna"); // Llamada a la función


### CON VARIOS PARAMETROS Y CON RETORNO ### 

// Recibe varios datos, calcula el total y lo devuelve al código para guardarlo en una variable
function calcularGramosComida(int $numeroLatas, int $gramosPorLata): int {
    $totalGramos = $numeroLatas * $gramosPorLata;
    return $totalGramos; 
}

$comidaDelDia = calcularGramosComida(2, 75);
echo "Hoy tocan {$comidaDelDia}g de comida húmeda en total\n"; 


### CON PARAMETROS POR DEFECTO ### 

// Si no se le pasa un valor, la función usará el valor por defecto
function darPremio(string $nombreGato, string $premio = "un Churu"): string{
    return "Premio para {$nombreGato}: {$premio}\n";
}

echo darPremio("Naruto"); // Usa el valor por defecto
echo darPremio("Valkiria", "un poco de hierba gatera"); //Sobreescribe el valor


// --------------------------------------------------
// FUNCIONES NATIVAS DE PHP
// --------------------------------------------------

### MANEJO DE CADENAS ###

$mensaje = " Mis gatos adoran los Churu ";

// trim() elimina  espacios al inicio y final
$limpio = trim($mensaje);

// strtoupper() convierte a mayúsculas
$mayus = strtoupper($limpio);

//strlen() cuenta los caracteres de la cadena
$numLetras = strlen($mayus);

echo "Resultado: '{$mayus}' (Numero de caracteres: {$numLetras})\n";


### MANEJO DE ARRAYS ###

$gatos = ["naruto", "auri", "melo", "luna", "valkiria"];

// count() cuenta los elementos de un array
$totalGatos = count($gatos);

// in_array() verifica si un valor existe en el array (devuelve true o false)
$estaMelo = in_array("melo", $gatos);

//ucfirst() convierte la primera letra de una cadena a mayúsculas
$nombreGato = ucfirst($gatos[4]);

echo "Tengo {$totalGatos} gatos y uno de ellos es {$nombreGato}\n";
echo "¿Está Melo entre ellos? " . ($estaMelo ? "Sí" : "No") . "\n";


### MANEJO DE FECHAS ###

// time() devuelve la fecha y hora actual en formato timestamp
$fechaActual = time();

// date() formatea la fecha y hora según el formato que especifiquemos
$registroEntrada = date("d/m/Y H:i:s");
echo "Gatito registrado en la clínica el {$registroEntrada}\n";

// strtotime() Ejemplo1: calcula fechas futuras o pasadas a partir de una fecha en formato texto
$timestampProximaDosis = strtotime('+3 months');
$fechaProximaDosis = date("d/m/Y", $timestampProximaDosis);
echo "Próxima pastilla antiparasitaria: {$fechaProximaDosis}\n";

//strtotime() Ejemplo2: calcula la diferencia en segundos entre dos fechas, que podemos convertir a días
$fechaAdopcion = "03-12-2013";
$segundosDesdeAdopcion = $fechaActual - strtotime($fechaAdopcion);
$diasEnCasa = floor($segundosDesdeAdopcion  / (60 * 60 * 24));

echo "Han pasado {$diasEnCasa} días desde que adopté a mi primer gato el día {$fechaAdopcion}\n";


// --------------------------------------------------
// FUNCIONES DENTRO DE FUNCIONES (CLOSURES)
// --------------------------------------------------
/*
* En PHP, las funciones pueden definirse dentro de otras funciones. 
* Esto se conoce como "closures" o funciones anónimas.
*/

function revisarPesoGato(string $nombreGato, float $peso): void {

    // Función anónima auxiliar para evaluar el peso del gato
    $evaluarPeso = function (float $kg): string {
        if ($kg < 3.5) {
            return "necesita ganar peso. Más Churu y pollito.";
        } elseif ($kg > 5.5) {
            return "necesita perder peso. Nada de Churu por un tiempo";
        } else {
            return "está en su peso ideal";
        }
    };

    $diagnostico = $evaluarPeso($peso);
    echo "{$nombreGato} pesa {$peso}kg y {$diagnostico}\n";
        
}

revisarPesoGato("Naruto", 8.0);
revisarPesoGato("Luna", 3.6);
revisarPesoGato("Melo", 2.8);
revisarPesoGato("Valkiria", 5.4);
revisarPesoGato("Auri", 3.7);

// --------------------------------------------------
// VARIABLES LOCALES Y GLOBALES (SCOPE)
// --------------------------------------------------

// Variable GLOBAL: Existe en todo el script principal
$veterinarioDeUrgencias = "Dra. Trujillo";

function consultaVeterinaria(): void {
    // Variable LOCAL: solo vive mientras dura esta función
    $paciente = "Gatito recién nacido";

    // Para leer $veterinarioDeUrgencias aquí, necesitamos usar la palabra 'global'
    global $veterinarioDeUrgencias;

    echo "En consulta: {$paciente}, atendido por {$veterinarioDeUrgencias}\n";
}

consultaVeterinaria();
echo "En recepción sabemos que está de guardia: {$veterinarioDeUrgencias}\n";

//echo $paciente; // ERROR: $paciente no existe fuera de la función


/* --------------------------------------------------

    DIFICULTAD EXTRA:

    Crea una funcioón que reciba dos parámetros de tipo cadena de texto y retorne un número.

    - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        - Si el número es múltiplo de 3, muestra la adena de texto del primer parámetro.
        - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
        - Si el número es múltiplo de 3 y 5, muestra las dos cadenas de texto concatenadas.

    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

----------------------------------------------------- */

function numerosConSorpresa(string $sorpresa3, string $sorpresa5): int {
    $contador = 0;

    for ($i = 1; $i <= 100; $i++) {
        // Comprobamos si es múltiplo de 3 y 5
        if ($i % 3 === 0 && $i % 5 === 0) {
            echo $sorpresa3 . $sorpresa5 . "\n";

        } elseif ($i % 3 === 0) {
            echo $sorpresa3 . "\n";

        } elseif ($i % 5 === 0) {
            echo $sorpresa5 . "\n";
        } else {
            echo $i . "\n";
            $contador++;
        }
    }
    return $contador;
}

$vecesNumeros = numerosConSorpresa("Ronroneo", "Zarpazo");
echo "Los números han sido impresos por pantalla {$vecesNumeros} veces en lugar de las sorpresas.\n";
?>