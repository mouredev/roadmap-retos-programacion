use Modern::Perl '2015';
use autodie;

#  Comentario en perl
#  Sitio oficial: https://www.perl.org/
#  En Perl las variables tienen un símbolo que indica el tipo del valor de la variable

#  Variables Escalares (Usan el signo de dólar $)
my $escalares;

#  Variables de Matriz - Arreglos (usan el signo at @)
my @arreglo;

#  Variables Hash (usan el signo de porcentaje %)
my %hash;

#  Strings 
my $perl_language = "Perl";

#  Números
my $integer   = 42;
my $float     = 0.007;
my $sci_float = 1.02e14;
my $binary    = 0b101010;
my $octal     = 052;
my $hex       = 0x20;

print "¡Hola, ", $perl_language, "!\n";
