void OnStart() {
    // TODO. OPERADORES DE MQL4
    // Aritméticos 
    Print("Suma:            10 + 5 = ", 10 + 5); // 15
    Print("Resta:           10 - 5 = ", 10 - 5); // 5
    Print("Multiplicación:  10 * 5 = ", 10 * 5); // 50
    Print("División:        10 / 5 = ", 10 / 5); // 2
    Print("Módulo:          10 % 5 = ", 10 % 5); // 0
    
    // Asignación  
    int a; 
    Print("Valor de 'a':                          ", a);      // a = 0 
    Print("Asignación:                  a = 3  es ", a = 3);  // a = 3
    Print("Suma y asignación:           a += 3 es ", a += 3); // a = 6
    Print("Resta y asignación:          a -= 3 es ", a -= 3); // a = 3
    Print("Multiplicación y asignación: a *= 3 es ", a *= 3); // a = 9
    Print("División y asignación:       a /= 3 es ", a /= 3); // a = 3 
    Print("Módulo y asignación:         a %= 3 es ", a %= 3); // a = 0
    
    // Comparasión 
    Print("Igualdad:        a == 10 es ", a == 10); // false
    Print("Desigualdad:     a != 10 es ", a != 10); // true
    Print("Mayor que:       a > 10  es ", a > 10);  // false 
    Print("Menor que:       a < 10  es ", a < 10);  // true
    Print("Mayor o igual:   a >= 10 es ", a >= 10); // false 
    Print("Menor o igual:   a <= 10 es ", a <= 0);  // true
    
    // Lógicos 
    Print("AND &&: false && false  es ", false && false); // true
    Print("OR  ||: true || flase   es ", true || false);  // true
    Print("NOT  !: !true           es ", !true);          // false
    
    // Bit a Bit
    // 5 -> 0101
    // 3 -> 0011
    Print("AND &: 5 & 3 es ", 5 & 3); // 0001 -> 1 
    Print("OR  |: 5 | 3 es ", 5 | 3); // 0111 -> 7 
    Print("XOR ^: 5 ^ 3 es ", 5 ^ 3); // 0110 -> 6
    Print("NOT ~: ~ 5 es", ~5);       // 1010 -> -6
    Print("Desplazamiento izquierda <<: 5 << 1 es ", 5 << 1); // 1010 -> 10 
    Print("Desplazamiento derecha >>: 5 >> 1 es ", 5 >> 1);   // 0010 -> 2 
    
    // Incremento y decremento 
    int i = 3; 
    i++; Print("Incremento: i++ es ", i); // 4
    i--; Print("Decremento: i-- es ", i); // 3
    
    // Ternarios -> Forma abreviada de if 
    // '(condicional) ? [val_verdadero] : [val_falso]' 
    Print("Ternario: (i == 3) ? true : false -> ", i == 3 ? true : false);
    
    
    
    // TODO. ESTRUCTURAS DE CONTROL ===============================================================
    // Condicionales 
    string var = "mql4"; 
    if (var == "mql4") { 
        Print("Variable es 'mql4'. "); 
    } else if (var == "texto") { 
        Print("Variable no es 'mql4', pero es 'texto'. "); 
    } else { 
        Print("Variable no es ningún caso. "); 
    }
    
    int A = 6; 
    switch(A) {
        case 0:
            Print("La variable 'A' entra en el caso 1, donde vale 0. "); 
            break; 
        case 3: 
            Print("La variable 'A' entra en el caso 2, donde vale 3. "); 
            break; 
        case 6: 
            Print("La variable 'A' entra en el caso 2, donde vale 6. "); 
            break; 
        default: 
            Print("La variable 'A' entra en el caso por defecto, donde no encontramos su valor. "); 
            break; 
    }    
    
    
    
    // Bucles 
    int start = 0, stop = 10; 
    for (int j=start; j<=stop; j++) {
        // Usamos j para saber el número de la iteración en la que vamos 
        Print("j vale ", j); 
    } 
    
    // j = 11
    while (j > start) {
        j--; 
        Print("j vale ", j); 
    }
    
    // j = 0
    do {
        j++; 
        Print("j vale ", j); 
    } while (j == 1); 
    
    
    // En mql4 no hay manejo de excepciones :(
    
    Print("======================================");
    // TODO. EJERCICIO EXTRA 
    for(int c=10; c<=55; c+=2) {
        if(c == 54) { Print(c+1); continue; } // ¿El 55 también se incluye o no? .-.  
        if(c%3 == 0 || c == 16) continue;   // Se salta la iteración actual 
        Print(c); 
    }
}

//* OBSERVACIONES 
// - Para concatenar en print es con ' + ' o con ' , '. 
// - No se puede imprimir directamente el operador incremental ' c++ '. 
// - '' las comillas simples no se pueden poner en una impresión (print). 
// - En consola true / false se representa con 0 y 1. 
// - el switch solo funciona con datos enteros (int). 