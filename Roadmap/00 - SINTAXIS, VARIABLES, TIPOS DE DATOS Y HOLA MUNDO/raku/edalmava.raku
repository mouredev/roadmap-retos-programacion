# Sitio oficial: https://raku.org/

# Comentario de una sola línea

#`(
 Comentario de varias líneas comienzan con los caracteres #` seguidos de un par de estos caracteres
 (), {}, []
)

# Variables escalares comienzan con el signo dólar $
my $escalares;

# Strings
my $raku_language = "Raku";

# Números 
my $entero = 42;
my $racional = 3/4;
my $ieee = 5.424E40;

# Booleanos
my $true = True;
my $false = False;

# Rangos
my $mi_rango = 1 .. 5;

say "¡Hola, " ~ $raku_language ~ "!\n";     # Para concatenar cadenas se usa el signo ~
print "¡Hola, $raku_language!";             # Usando interpolación de variables
