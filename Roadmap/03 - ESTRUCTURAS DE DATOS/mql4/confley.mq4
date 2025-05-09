/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa una agenda de contactos por terminal. - (luego lo implementó xd)
 */

//+------------------------------------------------------------------+
//| Métodos de apoyo                                                 |
//+------------------------------------------------------------------+
// Imprimir un array unidimensional
void PrintArray(int &arr[]) {
    string output = "";
    int size = ArraySize(arr);
    for (int i = 0; i < size; i++) {
        output += "[" + i + "] " + arr[i] + ", ";
    }
    Print(output);
    Print("");
}

// Imprimir una matriz (array multidimensional)
void PrintMatrix(double &matrix[][]) {
    for (int i = 0; i < ArrayRange(matrix, 0); i++) {
        Print("Fila ", i, ": ", matrix[i][0], ", ", matrix[i][1]);
    }
    Print("");
}

//+------------------------------------------------------------------+
//| Declaración de estructuras y enumeraciones                      |
//+------------------------------------------------------------------+
enum OrderType {
    BUY = 10,
    SELL,       // Incrementa automáticamente el valor anterior (11)
    PENDING = 30
};

struct TradeInfo {
    string symbol;       // Símbolo del instrumento
    double lotSize;      // Tamaño del lote
    OrderType type;      // Tipo de orden
};

//+------------------------------------------------------------------+
//| Función principal                                                |
//+------------------------------------------------------------------+
void OnStart() {
    // ** ARRAYS **
    int array[4];
    // ArrayResize(array, 4);  // Redimensionar a 3 elementos
    array[0] = 50;
    array[1] = 10;
    array[2] = 30;
    array[3] = 300;
    Print("Array inicial:");
    PrintArray(array);

    // Actualización
    array[1] = 200;
    Print("Array después de actualización:");
    PrintArray(array);

    // Borrado (reduciendo tamaño)
    ArrayResize(array, 3);
    Print("Array después de borrado:");
    PrintArray(array);

    // Ordenación
    ArraySort(array);
    Print("Array después de ordenación:");
    PrintArray(array);

    // SERIES (Acceso inverso a datos históricos)
    ArraySetAsSeries(array, true);  // Convertir en serie
    Print("Array después de convertir a serie:");
    PrintArray(array);

    // ** MATRICES **
    double matrix[2][2] = {
        {2.1, 2.2},
        {1.1, 1.2},
    };
    Print("Matriz inicial:");
    PrintMatrix(matrix);

    // Agregar una fila
    ArrayResize(matrix, 3);  // Ahora tiene 3 filas
    matrix[2][0] = 3.1;
    matrix[2][1] = 3.2;
    Print("Matriz después de agregar una fila:");
    PrintMatrix(matrix);

    // Actualización
    matrix[1][1] = 2.5;
    Print("Matriz después de actualización:");
    PrintMatrix(matrix);

    // Ordenamiento 
    ArraySort(matrix); 
    Print("Matriz después de ordenación: ");
    PrintMatrix(matrix); 

    // ** STRUCTURES **
    TradeInfo myTrade;
    myTrade.symbol = "EURUSD";
    myTrade.lotSize = 0.1;
    myTrade.type = BUY;
    Print("Información de Trade:");
    Print("Símbolo: ", myTrade.symbol, ", Lote: ", myTrade.lotSize, ", Tipo: ", EnumToString(myTrade.type));

    // Actualización
    myTrade.lotSize = 0.2;
    Print("Información de Trade actualizada:");
    Print("Símbolo: ", myTrade.symbol, ", Lote: ", myTrade.lotSize);

    // ** ENUMERATIONS **
    OrderType orderType = SELL;
    if (orderType == SELL) {
        Print("Orden de tipo: ", EnumToString(orderType));
    }
}

//+------------------------------------------------------------------+
//| Observaciones finales                                            |
//+------------------------------------------------------------------+
/*
1. Arrays (unidimensionales):
    - No es dinámico, por lo que tienes que definir un tamaño al instanciar o cambiar su tamaño en ejecución. 
    - Se pueden redimensionar con `ArrayResize`.
    - Los elementos que queden fuera del rango de redimensión serán eliminados.
    - Se pueden ordenar con `ArraySort`.
    - `ArraySort` solo funciona con elementos númericos. 
    - Convertir un array a "serie" cambia el acceso (índices invertidos).

2. Matrices (multidimensionales):
    - Solo la primera dimensión puede redimensionarse dinámicamente.
    - La primera dimensión puede ser ordenada. 

3. Structures:
    - Son útiles para agrupar datos heterogéneos.
    - Las operaciones de actualización se hacen accediendo a los atributos.

4. Enumerations:
    - Útiles para definir listas de constantes con valores predefinidos y secuenciales.
    - No se puede usar con strings 

5. Limitaciones del lenguaje:
    - No se puede recibir entrada directamente del usuario a través del terminal.
    - Faltan estructuras avanzadas como diccionarios y listas dinámicas.
*/