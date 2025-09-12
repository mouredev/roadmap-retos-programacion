# Operador de asignación =
my ($name, $age) = 'Edalmava', 30;

say("Mi nombre es $name y tengo $age");

# Operador defined-o // para obtener un valor alternativo si una variable aún no está establecida
my $a = 'alpha';
say $a // 'gamma';    # Imprime alpha 

my $b;
say $b // 'delta';    # Imprime delta

# if - El código se ejecuta solo si se cumple una condición, por ej., una expresión se evalúa como True
# Si la condición no se cumple, podemos especificar bloques alternativos de ejecución utilizando:
# - else
# - elsif
my $número-de-asientos = 9;

if $número-de-asientos <= 5 {
  say 'Soy un sedan'
} elsif $número-de-asientos <= 7 {
  say 'Tengo 6 o 7 asientos'
} else {
  say 'Soy un microbus'
}

#`(
   unless - La negación de if es unless.
   La negación en Raku se realiza con ! o con not.

   unless (condición) se utiliza en lugar de if not (condición).

   unless no puede utilizar la claúsula else.
)

my $limpiar-zapatos = False;

unless $limpiar-zapatos {
  say 'Limpia tus zapatos'
}

# for - for itera sobre una serie de valores.
my @array = 1,2,3;

for @array -> $array-item {
  say $array-item * 100
}

# Para iterar sobre rangos

for 1..5 -> $n {
    say $n;
}

# Para cuerpo de bucle cortos se puede usar la forma posfija de for
.say for 1..5;

# given - En Raku given viene a ser switch en otros lenguajes
my $var = 42;

given $var {
    when 0..50 { say 'Menos o igual a 50' }
    when Int { say "es un Entero" }
    when 42  { say 42 }
    default  { say "¿ejem?" }
}

# loop es otra forma de escribir un for.
# Actualmente loop viene a ser el for utilizado en la familia de lenguajes de C.
loop (my $i = 0; $i < 5; $i++) {
  say "El número actual es $i"
}

# while - se repite mientras la condición sea verdadera
my $x = 0;
while $x <= 10 {
    $x = prompt 'Introduce un número, que no sea mayor que 10: ';
    say "Has introducido $x.";
}
say "$x es mayor que 10.";

# until - se repite hasta que la condición se haga verdadera
$x = 0;
until $x > 10 {
    $x = prompt 'Introduce un número que no sea mayor que 10: ';
    say "Has introducido $x.";
}
say "$x es mayor que 10.";

# repeat - el bloque repeat siempre se ejecuta al menos una vez.
$x = 100;
repeat {
    $x = prompt 'Enter a number: ';
    say "You entered $x.";
} while $x <= 10;                    # Usando while para la condición
say "$x is bigger than 10.";

$x = 0;
repeat {
    $x = prompt 'Enter a number: ';
    say "You entered $x.";
} until $x > 10;                     # Usando until para la condición 
say "$x is bigger than 10.";         

#`(
  RETO EXTRA
)

say '';
say '**************';
say '*****RETO EXTRA*****';
say '**************';
say '';

say "Usando for con rangos";

for 10 .. 55 -> $i {
    if $i %% 2 && $i != 16 && !($i %% 3)  {
        say $i
    }
}

say "Usando loop";

loop ($i = 10; $i <= 55; $i++) {
    if $i %% 2 && $i != 16 && !($i %% 3)  {
        say $i
    }
}

say "Usando la forma posfija de for - en una sola línea";
.say if $_ %% 2 && $_ != 16 && !($_ %% 3) for 10 .. 55;
