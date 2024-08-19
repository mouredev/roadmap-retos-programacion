// todo. FUNCIONES ================================================================================
// FUNCIÓN SIMPLE 
void HelloFunction() {
    Print("Hola usuario :D"); 
}

// FUNCIÓN CON PARÁMETROS 
void HelloFunction(string user) {
    Print("Hola ", user, " ten un excelente día ^-^"); 
}

// FUNCIÓN CON RETORNO 
string Hello() {
    return "¿Qué tal?, usuario :0"; 
}

// CREAR FUNCIONES DENTRO DE UNA FUNCIÓN
//! Error -  No es posible hacer esto 

// FUNCIÓN PREDEFINIDA 
// Devuelve el valor más grande entre 2 números 
double biggestNumber = MathMax(10, 5); // Función pre-definida
double CustomMathMax(double a, double b) {
    return (a >= b) ? a : b; 
}



// todo. VARIABLES ================================================================================
// VARIABLES (GLOBAL Y LOCAL)
string variable = "GLOBAL"; 
void LocalAndGlobal() {
    string variable = "LOCAL"; 
    Print("Dentro del método tiene priodidad la variable ", variable); 
    Print("Pero también podemos acceder a la variable ", ::variable, " usando -> ::variable"); 
}



//todo. EXTRA =====================================================================================
int Bonus(string oneStr, string twoStr) {
    int coutn = 0; 
    
    for(int i=1; i <= 100; i++) {
        
        bool multipleOf3 = (i%3 == 0), multipleOf5 = (i%5 == 0); 
        
        if(multipleOf3 && multipleOf5) 
            Print(oneStr, twoStr); 
        else if(multipleOf3) 
            Print(oneStr); 
        else if(multipleOf5) 
            Print(twoStr); 
        else {
            coutn++; 
            Print(i); 
        }
    }
    
    return coutn; 
}



// todo. EJECUCIÓN ================================================================================
void OnStart() {
    HelloFunction();                // Función simple 
    HelloFunction("Confley");       // Función con parámetro
    Print(Hello());                 // Función de retorno 
    Print(biggestNumber);           // Función pre-definida 
    Print(CustomMathMax(3, 5));     // Función personalizada 
    LocalAndGlobal();               // Variables global y local
    int x = Bonus("Pit", "Zaahot ");// Díficultad extra 
    Print("Los números se imprimeron ", x, " veces"); 
}


// todo. OBSERVACIONES ============================================================================
// - Las funciones solo se pueden declarar a nivel global o dentro de una clase. 
// - Acepta polimorfismo -> Varias funciones con mismo nombre, pero distintos parametros. 
// - Los :: para acceder a la variable global solo se ponen porque tenemos el mismo nombre en ambas; 
//   el tener el mismo nombre y declarar ambas variables nos genera un warning en el compilador.