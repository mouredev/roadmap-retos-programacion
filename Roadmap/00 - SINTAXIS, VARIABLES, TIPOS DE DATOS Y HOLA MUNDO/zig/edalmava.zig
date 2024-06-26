//! Comentario Doc de nivel superior: comienzan con dos barras y un signo de exclamación
//! Documenta el módulo actual
//! Es un error de compilación si no se coloca un comentario doc de nivel superior al principio,
//! antes de cualquier expresión.

// Los comentarios en Zig inician con // y va hasta el final de la línea
// No existen comentarios de varias líneas

/// Comentarios Doc: comienzan con tres barras ///

// Sitio oficial: https://ziglang.org/
// En este archivo se uso Zig 0.13.0
// Documentación Oficial: https://ziglang.org/documentation/0.13.0/

const std = @import("std");
const print = std.debug.print;

pub fn main() void {
    // Para declarar una variable es preferible utilizar la palabra const en lugar de var
    // Usar la palabra clave const para asignar un valor a un identificador
    // El valor no se puede modificar
    // Si se desea modificar el valor usar la palabra clave var

    // Valores enteros
    const entero: i32 = 1 + 1;
    print("1 + 1 = {}\n", .{entero});
    // entero = 2;   // Esta línea sin comentar genera un error debido a que no se puede asignar un nuevo valor a const

    var entero2: i32 = 1;
    entero2 = 2;

    // Valores flotantes
    const flotante: f32 = 7.0 / 3.0;
    print("7.0 / 3.0 = {}\n", .{flotante});

    // Valores Booleanos
    print("true and false = {}\ntrue or false = {}\n!true = {}\n", .{ true and false, true or false, !true });

    // Valores caracter o Unicode
    const letra = 'A';
    const rayo = '⚡';
    print("{u} - {u}\n", .{ letra, rayo });

    // Cadenas literales de varias líneas se usan dos barras invertidas \\ por cada línea
    const plantilla_html =
        \\ <html>
        \\   <head></head>
        \\   <body></body>
        \\ </html>
    ;
    print("{s}\n", .{plantilla_html});

    // Cadenas literales
    const lenguaje = "Zig";
    print("¡Hola, {s}!\n", .{lenguaje});
}
