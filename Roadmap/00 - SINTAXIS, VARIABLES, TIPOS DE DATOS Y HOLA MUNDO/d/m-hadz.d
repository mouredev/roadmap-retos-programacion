module mhadz;

/*
    Aqui se define el nombre del modulo
    ya que el compilador dmd tira error
    si el nombre del archivo tiene un -
*/

import std.stdio;

// https://dlang.org/

// Se usa para comentarios de una linea

/*
  Se utiliza para comentarios
  de multiples lineas
*/


int variable = 3;

const double constante = 3.14;

// Estos son los tipos de datos primitivos de D

byte valorByte = 10;

ubyte valorUByte = 100; // byte sin signo

short valorShort = -200;

ushort valorUShort = 5000; // short sin signo

int entero = 3;

uint valorUInt = 3U; // entero sin signo

long valorLong = -123456789000000L;

ulong valorULong = 12345678990000000L; // long sin signo

float valorFloat = 3.1F;

double valorDouble = 3.14;

real valorReal = 1.925;

bool booleano = true;

char valorChar = 'a'; // UTF8

wchar valorWChar = 'ñ'; // UTF16

dchar valorDCchar = '⚙'; // UTF32

void main() {
    writeln("¡Hola, D!");
}
