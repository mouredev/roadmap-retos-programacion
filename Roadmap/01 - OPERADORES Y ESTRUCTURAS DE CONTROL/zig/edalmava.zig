const std = @import("std");
const print = std.debug.print;

pub fn main() void {
    // Sentencia if
    var x: i32 = 0;
    if (true) { // La condición debe ser una expresión que se evalue como true o false si no genera un error en compilación
        x = 1;
    } else {
        x = 2;
    }
    print("{}\n", .{x});

    // Sentencia if como expresión
    const a = true;
    x = 0;
    x += if (a) 1 else 2;
    print("{}\n", .{x});

    // Bucle while: una condición, un bloque y una expresión de continuación
    // Sin una expresión de continuación
    var i: u8 = 2;
    while (i < 100) { // La condición se debe evaluar como true o false
        i *= 2;
    }
    print("{}\n", .{i}); // Se espera 128
    // Con una expresión continua
    var sum: u8 = 0;
    i = 1;
    while (i <= 10) : (i += 1) {
        sum += i;
    }
    print("{}\n", .{sum}); // Se espera 55
    // while con continue
    sum = 0;
    i = 0;
    while (i <= 3) : (i += 1) {
        if (i == 2) continue;
        sum += i;
    }
    print("{}\n", .{sum}); // Se espera 4
    // while con break
    sum = 0;
    i = 0;
    while (i <= 3) : (i += 1) {
        if (i == 2) break;
        sum += i;
    }
    print("{}\n", .{sum}); // Se espera 1

    // Bucle for
    // Para iterar matrices y otros tipos
    // Se puede usar continue y break como en while
    // Los literales caracter son equivalentes a literales enteros
    const string = [_]u8{ 'a', 'b', 'c' };

    for (string, 0..) |character, index| {
        //_ = character;  // Como Zig no deja tener valores sin utilizar se usa el _
        //_ = index;      // Como Zig no deja tener valores sin utilizar se usa el _

        print("Índice: {} - Caracter: {c}\n", .{ index, character });
    }

    // RETO EXTRA
    print("\n\n***RETO EXTRA***\n\n", .{});
    i = 10;
    while (i <= 55) : (i += 1) {
        if (i % 2 == 0 and i != 16 and i % 3 != 0) {
            print("{}\n", .{i});
        }
    }
}
