# OPERADORES ARITMETICOS
# toman los operadores que se le indican y realizan un cálculo matemático


suma=$((5+3))
echo $suma
resta=$((5-3))
echo $resta
multiplicacion=$((5*3)) 
echo $multiplicacion
division=$((5/2))
echo $division
modulo=$((10%3))  # Modulo es el resto que nos queda de la división en éste caso es 1
echo $modulo
potencia=$((10**3)) # Eleva a la potencia 3 el pirmer operando que le pasamos 
echo $potencia

echo -e "\n\n=======================================================================\n\n"

# OPERADORES RELACIONALES
# Son los que relacionan dos elementos entre sí

echo $((5>3))  # Devuelve 1 (True) si es verdadero
echo $((5>=3)) # Devuelve 1 (True) si es verdadero
echo $((5<3))  # Devuelve 1 (True) si es verdadero
echo $((5<=3)) # Devuelve 1 (True) si es verdadero
echo $((5==3)) # Devuelve 1 (True) solo si los dos operandos son iguales
echo $((5!=3)) # Devuelve 1 (True) solo si los dos operandos son diferentes

echo -e "\n\n=======================================================================\n\n"

# OPERADORES LOGICOS
# Se usan basandonos en condiciones

# El operando "AND" "&&" devuelve True (1) siempre que los dos operandos sean correctos
echo "$(( 3 + 2 == 5 && 7 * 2 == 14 ))"
# El operando "OR" "||" devuelve True (1) siempre que uno de los dos operandos sea correcto
echo "$((3 + 2 == 5 || 7 * 2 == 10 ))"
# El operando "NOT" "!" devuelve True (1) siempre que uno de los dos operandos sea falso
echo "$(( 10 + 3 != 14 ))"

echo -e "\n\n=======================================================================\n\n"

# OPERADORES DE ASIGNACION
# Son los que se usan para dar valor a una variable por ejemplo

my_variable=5         # Asignación    
echo $my_variable

let my_variable+=1
echo $my_variable      # Suma y Asignación

let my_variable-=1
echo $my_variable      # Resta y Asignación

let my_variable*=2
echo $my_variable      # Multiplicación y Asignación

let my_variable/=2
echo $my_variable      # División y Asignación

let my_variable%=3
echo $my_variable      # Mòdulo y aAsignación


echo -e "\n\n=======================================================================\n\n"


# Operadores de bit
# Realiza operaciones en los operandos bit a bit

a=10 # 1010 en binario
b=3  # 0011 en binario

echo $(( $a >> $b ))    # 0001 (1) Desplazamos a la derecha 3 bits y rellenamos con ceros por delante
echo $(( $a << $b ))    #1010000 (80) Cubrimos con ceros por detras las posiciones que nos pide el segundo operando

echo -e "\n\n=======================================================================\n\n"

# ESTRUCTURAS DE CONTROL 
# CONDICIONALES 

if [ $a -lt $b ]; then
    echo "$a es menor que $b"
elif [ $a -eq $b ];then
    echo "$a es igual a $b"
else [ $a -gt $b ];
    echo  "$a en mayor que $b"
fi
echo -e "\n\tla equivalencia de condicionales es:\n
        -gt     >       mayor\n
        -lt     <       menor\n
        -ge     >=      mayor o igual\n
        -le     <=      menor o igual\n
        -eq     ==      igual\n
        -ne     !=      distinto\n"

echo -e "\n\n=======================================================================\n\n"

# ESTRUCTURAS DE CONTROL 
# ITERATIVAS

for i in $(seq 1 10); do
    echo "$i"
done

echo -e "\n\n=======================================================================\n\n"

comienza=10
termina=20

while [ $termina -ge $comienza ] 
do
    echo $comienza
    let comienza=$comienza+1
done

echo -e "\n\n=======================================================================\n\n"


for number in $(seq 10 56);do
    if [ $((number % 2)) -eq 0 ] && [ $((number)) -ne 16 ] && [ $((number %3)) -ne 0 ]; then
        echo "$number"
    fi
done
