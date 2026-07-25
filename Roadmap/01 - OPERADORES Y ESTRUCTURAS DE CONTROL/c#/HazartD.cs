using System; //Primero que nada, pense que a lo mejor este seria mas facil,
using System.Collections.Generic; // porque el anterior me llevo como 6 horas en hacer.
using System.Linq; //Pero cuando busque en el doc los operadores que hay en C#,
using System.Text; //la parte de operadores tiene 12 entradas.
class Ejercicio1 {
    public enum TEST{YUCAFRITA, ATOLCHUCO, QUESADILLA, PANCONPOLLO, PUPUSA} // Los enum al ser constantes no pueden ir dentro de metodos, si lo pusieras ahi empezaria a tirar errores por cada linea de la funcion.
    static void Main(){
        //descubri que esto es porque los projectos ejecutan de inicio una unica funcion estatica llamada Main
        //como al crear con consola un proyecto sale un nuevo archivo con ese Main, estube peleando con el vscode por como 2 horas para descubrilo xddd
    
    //creare 3 variables de estos 2 para probarlos.
        byte a = 1;
        byte b = 2; //los iba a poner como variables publicas arriba
        byte c = 3; //pero marca errores 
        sbyte d = -1;
        float fa = 1.1f; //«Se requiere una referencia de objeto para el campo, método o propiedad 'Ejercicio1.a' no estáticos»
        float fb = 2.2f; //creo que solo es que no puede usar nada no estatico dentro de funciones estaticas
        float fc = 3.3f; //igual se podrian poner ambas, poner las goblales arriba y luego las locales igualadas

        Console.WriteLine("\nAritmeticos Y Asignacion\n\n");
        Console.WriteLine($"\nIncremento\nAl poner «a++», se le sumara 1 a «a», pero usarlo dara el valor de antes de la operacion. Valor de a: {a++}");
        Console.WriteLine($"Valor actual de a: {a}");
        Console.WriteLine($"Pero, al poner «++a», se le sumara 1 a «a» y quedara ya como con su valor sumado. Valor de a: {++a}");
        Console.WriteLine($"\nDecremento\nPasa lo mismo poniendo «--a» y «a--», solo que esto resta 1 a «a». Valor de a:{a--}");
        Console.WriteLine($"Valor actual de a: {a}");
        Console.WriteLine($"Valor de a con --a:{--a}");
        Console.WriteLine("\nEstos 2 son los unicos operadores que cambian el valor almacenado en la variable. Los siguientes no.");

        Console.WriteLine("\nUnarios\nEstos son como los signos + y - normales de algebra.");
        Console.WriteLine("Poner + antes de una variable te dara la variable sin cambios, y ponerle - te dara su opuesto.");
        Console.WriteLine("Si la variable es positiva te dara negativo y viceversa.");
        Console.WriteLine($"Teniendo el float «fa» con valor:{fa}. Al escribir «+fa» su valor no cambia: {+fa}. Pero poniendole «-fa»: {-fa}. Y a su vez si pongo «-(-fa)»:{-(-fa)}");
        /*
        La doc menciona (y comprobe) que el unico tipo con el que no es compatible el - es el ulong.
        Interpreto que esto se debe modo de prevenir errores graves si el valor sobrepasa el minimo
        que puede almacenar el long. De modo que la computadora no podria procesarlo. Yo me entiendo xd.
        */
        Console.WriteLine($"\nMultiplicacion\nPoner «*» entre 2 variables o numeros te los multiplica. Teniendo b={b} y fb={fb}. Este es el valor de «b*fb»{b*fb}.");
        Console.WriteLine($"\nDivicion\nPoner «/» entre 2 variables o numeros te los divide. Este es el valor de «b/fb»{b/fb}.");
        Console.WriteLine($"La divicion da la precicion mas alta que tengan los valores usados; ya sea float, double o decimal. Usando solo int, se omitiran los decimales. Valor de «b/a»: {b/a}");
        Console.WriteLine($"Valor de «a/b»: {a/b}");
        Console.WriteLine($"Valor de «678.997m/1»: {678.997m/1}.\nPor algun motivo, la doc quizo omitir que debes poner «d» a final de un double y «m» al final de un decimal.");

        Console.WriteLine($"\nModulo\nPoniendo «%» entre 2 variables o numeros. Teniendo c={c}, «a%c» da:{a%c} y «c%a» da:{c%a}");
        Console.WriteLine("Con los decimales float y double, si «x%y» teniendo «z=|x| / |y|» redondeando decimales hacia abajo y siendo del mismo signo que «x», se calculan como «|x| - n * |y|»");
        Console.WriteLine($"Por ejemplo, «fa%fc» da: {fa%fc} y «fc%fa» da:{fc%fa}");
        Console.WriteLine($"Los decimal tienen su propia formula interna para modulos, pero la doc no la especifica");
        Console.WriteLine("En caso de los double, se pueden calcular tambien con el metodo «Math.IEEERemainder». Ya que la formula mencionada es analoga a la del entero, pero omitiendo la «especificación IEEE 754»");
        Console.WriteLine("Si se tienen «x/y» el metodo mencionado calcula el modulo asi: «x - (y * Math.Round(x / y))»");
        Console.WriteLine($"Con «-16.3 % 4.1» da: {-16.3 % 4.1}. Y con «Math.IEEERemainder(-16.3, 4.1)» da: {Math.IEEERemainder(-16.3, 4.1)}");

        Console.WriteLine("\nSuma y Resta\nPues lo que dice, con + sumas 2 weas y con - las restas");
        Console.WriteLine($"1+1={1+1} y 1-1={1-1}");
        Console.WriteLine("Pero, el + tambien se puede usar para unir 2 string. La segunda se pone al final de la primera.");
        Console.WriteLine("Y aqui empieza un problema, que resumire como pueda. Hay variables de referencia llamadas lambda que pueden ser una onda llamada delegados.");
        Console.WriteLine("Estos delegados son una linea de instruncion de una funcion basicamente. Puede ponerse un «var» que sume las variables delegadas, volviendo esa var otro delegado que ejecuta las iniciales en el orden que lo pones.");
        Console.WriteLine("Y tambien se pueden restar, segun cierto modo en que lo escribas puede que en realidad no pase nada al cambiarlo, que facilmente me podria quedar a leer y ejemplificar.");
        Console.WriteLine("Pero ya son las 10 pm y me quiero dormir. No hay un «XD», tengo sueño y la laptop no aguanta VScode y 2 pestañas de google a la vez por mucho tiempo.");

        Console.WriteLine($"\nAsignadores compuestos\n Son solo poner los operadores mencionados antes del =");
        Console.WriteLine($"Escribir «a+=b» es lo mismo (o incluso mas eficiente) que «a=a+b». Valor de «a*=b»:{a*=b}");
        Console.WriteLine($"Valor de «a/=b»:{a/=b}");

        Console.WriteLine("\nOtras indicaciones\n");
        Console.WriteLine("Puedes poner (*un tipo*) antes de una operacion para que el resultado se convierta a ese tipo o asegurarte de que no cambie el tipo de la variable a la que se asigna.");
        Console.WriteLine("Ejemplo: «a=(byte)a*fa». Convierte el resultado tipo float a byte, ya que se le tiene que asignar a «a»");
        Console.WriteLine("Cuando una operacion sobrepasa el numero maximo de un tipo (Ejemplo: «x= int.MaxValue +1») se da una OverflowException, mas adelante se explicara que son las excepciones, que ni yo sé todavia xd");
        Console.WriteLine("Es importante mencionar que esa excepción y la DivideByZeroException (dividir entre 0) solo afectan a enteros y Decimal");
        Console.WriteLine("Los float y double no producen estas excepciónes, tienen las constantes .NegativeInfinity y .PositiveInfinity para cuando pasa del maximo, y la constante .NaN para dividir entre 0");
        Console.WriteLine("Tambien hay errores de redondeo para todos los decimales (limitaciones de representacion). Por ejemplo, «decimal a= 3 (1/3)» deberia ser 1, pero por el error de redondeo equivale a: 0.9999999999999999999999999999");
        

        Console.WriteLine("\n\nLogicos booleanos\n\n");
        Console.WriteLine($"Esta el «!», el NOT, un «prefijo unario» que invierte los true a false y asi. Valor de !true: {!true}. Valor de !false: {!false}.\nEl «!» como posfijo permite valores NULL (lo que sea que signifique).");
        Console.WriteLine($"El «&» es AND. Si los 2 valores son true el resultado es true, pero aunque el primero sea false procesa el segundo, poniendo «&&» se evita el segundo calculo.\nValor de «true & true»:{true & true}. Valor de «false && true»:{false&&true}.");
        Console.WriteLine($"El «^» es el «OR exclusivo lógica, conocido como operador XOR lógico». Da true si los que opera son distintos y false si son iguales. Valor de «true ^ true»:{true ^ true}. Valor de «false ^ true»:{false^true}.");
        Console.WriteLine($"El «|» es OR, es como el «&» pero dando true si algunos es true. Pasa lo mismo con el «&&» y «||». Valor de «false | false»:{false|false}. Valor de «true || false»:{true||false}.");
        Console.WriteLine("Los | y & tambien funcionan con los «bool?», pero no pueden operar «null *| o &* null». Puesto que el error que saldria dice que el operador «es ambiguo en operandos del tipo '<NULL>' y '<NULL>'»");//Para & y | daran null si ambos operandos son null. «null & null»: {null&null}.«null | null»: {null|null}.");
        Console.WriteLine($"Para &, si alguno es false, dara false, para dar null uno tiene que ser true. true & null= {true & null}. null & true= {null & true}.");
        Console.WriteLine($"Para |, si alguno es true, dara true, para dar null uno tiene que ser false. false | null= {false | null}. null | false= {null | false:S}.");
        
        Console.WriteLine("\nAhora, solo para complicarme la vida: el & solito tambien es un «operador relacionado al puntero»");
        Console.WriteLine("Es una verga llamada «address-of» que te da la direccion en la memoria de una variable.");

        Console.WriteLine("Se supone que si declaras una variable asi «unsafe{byte* pointer = &a;...}» y luego te escribo «(long)pointer:X» saldra esa direccion.");
        Console.WriteLine("La doc menciona que hay variables fijas (para las que sirve esto) y moviles (para las que no) como los array y objetos. Pero que esas tambien hay modo de fijarlas.");
        Console.WriteLine("Para ello, pones unas «{}» para hacer un bloque, pones tipo «fixed (byte* pointer = &a)» y te servira solo para ese bloque.");
        Console.WriteLine("Parece ser importante que la variable de la posicion, la del *, sea del mismo tipo que la que se opera o un void.");
        Console.WriteLine("Otro punto importante es que para que el compilador ejecute lo que hay en bloques unsafe debes habilitarle una opcion.");
        Console.WriteLine("De no ser porque no se donde cambiarlo, lo habria mostrado, ya habia terminado de escribirlo cuando vi que no se podia.");

        
        Console.WriteLine("\n\nComparadores e Identidad\n\n");
        Console.WriteLine("\nLos meti en lo mismo porque crei que eran lo mismo, despues vi que se clasificaban distinto xd.\n");
        Console.WriteLine("Es solo son los ya sabidos mayor que, menor que e iguales que ya enseñan en clases:");
        Console.WriteLine("«<», «<=», «>», «>=». Tambien esta el operador «==» que comprueva si los dos valores son iguales y «!=» que son distintos.");
        Console.WriteLine("Ejemplos:");
        Console.WriteLine($"a<=c: {a<=c}   a>=c: {a>=c}   a<fa: {a<fa}   a>fa: {a>fa}   a==a: {a==a}   a==b: {a==b}   a!=a: {a!=a}  a!=b: {a!=b}");
        Console.WriteLine("Operar «x!=y» es lo mismo que«!(x == y)=», ya que este da el boleano opuesto, false si son iguales y true a contrario.");
        Console.WriteLine($"Usar la constante .NaN de cualquier decimal con un comparador siempre dara false, aunque sea «double.NaN == double.NaN»: {double.NaN == double.NaN}");
        Console.WriteLine("\nDe ahi para arriba van las igualdades de tipos complejos que no hemos visto, mas o menos he buscado pero no se mucho todavia.");
        Console.WriteLine("Por ejemplo, como se menciono en el antrior, el == puede dar true a 2 strings con el mismo contenido, pero no el object.ReferenceEquals ya que no refieren al mismo objeto.");
        Console.WriteLine("Lo mismo pasa con los delegados que mencionamos. Con ambos tambien pasa que dan true en == si las 2 variables son null");
            
            {uint ba = 0b_1111_1111;
            uint bb =  ba;
            bb=~bb;
            Console.WriteLine("\n\nBit a bit y desplazamiento\n\n");
            Console.WriteLine("Creo, tengo entendido, que los bit a bit se referiere a que operan los propios bits y va mejor el procesador. Esos operadores son validos para los char y los numericos enteros.");
            Console.WriteLine("Estan hechos para los int, uint, long y ulong. Cualquier otro valor aplicable se convierte a int, el cual tambien es el tipo del resultado. Tambien funcionan con la asignacion compuesta y conversion que mencionamos antes.");
            Console.WriteLine("Por cierto, los operadores para los que aplica la asignacion compuesta son los «binarios», llamados asi porque los pones entre 2 operandos. Los otros son unarios. En este caso, los operadores de bits se parecen a los logicos.");
            Console.WriteLine("Para este ejemplo las variables «ba» y «bb» son uint.");
            Console.WriteLine($"\nComplemento (unario). El NOT. Con «~» inviertes los bits de otra onda. Si el valor de «ba» es: {ba} y en bits: {Convert.ToString(ba, toBase: 2)} y declaro el valor de «bb» es «~ba»: {bb} y en bits: {Convert.ToString(bb, toBase: 2)}. Como el resultado siempre es int, todos los 1 que bb tiene de mas son los 0 que ba no muestra.");//Complemento. Con «~» inviertes los bits de otra onda. Si el valor de «ba» es:252645132 y declaro el valor de «bb» como «~ba»: 4042322163
            Console.WriteLine($"\nAND &. Compara los bits en la misma posicion de cada operando, si ambos tienen un 1 en una posicion, el resultado tendra 1 en esa posicion, de lo contrario sera 0. Valor de «ba &= 0b_1010_1001»: {ba &= 0b_1010_1001} y en bits: {Convert.ToString(ba, toBase: 2)}.");
            Console.WriteLine($"\nOR |. Siguiendo el tema, si ambos son 0 el resultado tendra 0 en esa posicion, de lo contrario sea 1. Valor de «ba |= 0b_0101_0101»: {ba |= 0b_0101_0101} y en bits: {Convert.ToString(ba, toBase: 2)}.");
            Console.WriteLine($"\nXOR ^. Igualmente, si ambos son distintos dara 1 en esa posicion, de lo contrario es true. Valor de «ba ^= bb»: {ba ^= bb} y en bits: {Convert.ToString(ba, toBase: 2)}.");
            Console.WriteLine($"\n<<. Deplaza el bit de la izquierda la cantidad de pociones que indique el operando de la derecha, reemplazando por 0 las posiciones vacias. Valor de «ba =<< 5»: {ba <<= 5} y en bits: {Convert.ToString(ba, toBase: 2)}.");
            Console.WriteLine($"\n>>. Lo mismo a la izquierda. Si el numero izquierdo es int o long y es negativo, se rellenan con 1, si es positivo con 0. Si son uint o ulong siempre es 0. Valor de «ba >>= 3»: {ba >>= 3} y en bits: {Convert.ToString(ba, toBase: 2)}.");
            Console.WriteLine($"\n>>>. Desplazamiento a la izquierda, pero siempre rellena con 0. Valor de «ba >>>= 2»: {ba >>>= 2} y en bits: {Convert.ToString(ba, toBase: 2)}.");
            Console.WriteLine($"\nLa prioridad que tienen los operadores de bits de mayor(primero) a menor(ultimo): ~, <<, >>, >>>, &, ^ y |.");}



        {   Console.WriteLine("\n\n\nOtros que me salieron en la doc\n\n\n");
            byte[] numeros = new byte[8]{0,1,2,4,8,16,32,64};
            Console.WriteLine($"Teniendo el array numeros: {string.Join(", ",numeros)}");
            Console.WriteLine($"Ya se sabe que con «[]» accedes a un valor de una coleccion, ejemplo «numeros[1]»: {numeros[1]}. Pero con el «^», el valor se toma empezando a contar desde el final, ejemplo «numeros[^1]»: {numeros[^1]}.");
            Console.WriteLine($"Por otro lado, con «..» se accede al intervalo de la coleccion.\nnumeros[0..3] = {string.Join(", ",numeros[0..3])}\nnumeros[3..^1] = {string.Join(", ",numeros[3..^1])}\nnumeros[3..^3] = {string.Join(", ",numeros[3..^3])}\nnumeros[..3] = {string.Join(", ",numeros[..3])}\nnumeros[3..] = {string.Join(", ",numeros[3..])}");
            Console.WriteLine("\nComo se noto, si solo pones un lado se continua al otro hasta donde llega. Y dejando solo el «[..]» da todos los elementos y ya. Cuidando de no poner al revez los numeros del rango, cuanta como que exediste la cantidad que hay y produce una excepción.");
           
            Console.WriteLine($"Otra funcion que tiene es la de concatenar arreglos. Si declaras un array como «int[] array3= [array0,array1,array2]» dara un error, ya que estas haciedo un array de arrays, debes poner: «int[][]»");
            Console.WriteLine($"Para ponerlos en un solo array debes poner «int[] array3= array0.Concat(array1).Concat(array2).ToArray».\nO simplemente «int[] array3= [..array0,..array1,..array2]»");
            
            Console.WriteLine("\nEl «is» comprueba si una variable es de un tipo concreto, como se pone el tipo del mismo modo en que se declararia una variable, si es true se puede asignar el mismo valor a una variable.");
            Console.WriteLine($"«numeros[3] is byte»: {numeros[3] is byte}. «numeros[3] is byte numa»: {numeros[3] is byte numa}. «numa»: {numa}");
            Console.WriteLine("Puede usarse junto al [..] para saber si los valores escritos estan presentes en un array. Tambien da true al comparar una clase con una clase de la que herede.");
            
            Console.WriteLine($"\nPara convertir un tipo en otro esta el operador «as» y la exprecion cast, que es la usada en «Otras indicaciones». «Se debe usar con un tipo de referencia o un tipo que acepte valores NULL». Valor de «100.2424m as int?»{100.2424m as int?}");
            Console.WriteLine($"\nEl «typeof(*tipo*)» regresa como esta en el System el tipo puesto como argumento. No se debe poner una variable o exprecion como argumento, en ese caso se le pone «.GetType()». No se pueden poner «dynamic» y los que aceptan null, se pone «object» y el tipo normal.");
            Console.WriteLine($"typeof(Dictionary<,>): {typeof(Dictionary<,>)}\nnumeros.GetType(): {numeros.GetType()}\nnumeros.GetType() == typeof(byte[]): {numeros.GetType() == typeof(byte[])}");
            
            Console.WriteLine("\nAl poner «ref» cuando se asigna un valor en base a una variable, esa nueva variable tiene una referencia a la primera.");
            
            Console.WriteLine("\nSe usa «::» para acceder a los namespace, lo que se pone arriba como using, iria tipo «global::System.Console.WriteLine(\"Using global alias\")».");
            
            int porDefecto = default;
            Console.WriteLine($"\nCon «default» se saca el valor por defecto de un tipo. default(int): {default(int)}. int porDefecto = default: {porDefecto}.");
            
            Console.WriteLine($"Con «nameof(*casi lo que sea*)» te genera el nombre de algo en tiempo de compilacion. Los @ al inicios de variables no cuentan.\nnameof(System.Collections.Generic):{nameof(System.Collections.Generic)}\nnameof(numeros):{nameof(numeros)}");
            
            Console.WriteLine("\nEsta en la doc por algun motivo el «new» para crear instancias como un operador.");

            Console.WriteLine($"\nEsta para los contextos unsafe el «sizeof(*un tipo*)» que muestra los bytes que ocupa un tipo de dato, tambien se puede usar sin unsafe con los tipos nativos y un nombre de enum.\nsizeof(byte): {sizeof(byte)}\nsizeof(TEST):{sizeof(TEST)}.");
            Console.WriteLine($"En este caso, regresa el espacio del tipo que son cada elemento del enum, que por defecto es int. TEST:{TEST.YUCAFRITA}, {TEST.ATOLCHUCO}, {TEST.QUESADILLA}, {TEST.PANCONPOLLO}, {TEST.PUPUSA}.");

            Console.WriteLine("\nCon «whith» se crea un objeto en base a otro con cambios. «var object2 = object1 whith {propiedadCambiada= \"nuevo valor\"}»");

            Console.WriteLine("\nTambien se puede usar las palabras «operator», «implicit» y «explicit» para crear operadores, pero esa madre me va extender mucho mas esto xd.\n");}
        
        
        
        Console.WriteLine("\n\n\nEstructuras de Control\n\n\n"); //los if, else y elif o else if siempre se han hecho muy faciles de comprender
        
        
        
        Console.WriteLine("\nif, else y else if o elif\n"); //no los explicare, si a alguien le da problemas, «if» es tipo «si pasa tal cosa has esto» y «else» es «si no paso, has lo otro»
        if (a.GetType() == d.GetType()){Console.WriteLine("Tanto «a» como «d» son byte o sbyte");}//1
        else if (a.GetType() == typeof(sbyte) && d.GetType() == typeof(byte)){Console.WriteLine("«a» es un sbyte y «d» un byte");}//2
        else if (a is byte && d is sbyte){Console.WriteLine("«a» es un byte y «d» un sbyte");}//3
        else {Console.WriteLine("Ni «a» ni «d» son byte o byte");}//4
        Console.WriteLine("Cuando en un if usas «&&» para saber si se cumplen mas de una condicion, lo estas volviendo una operacion logica como la vista anteriormente. Esta probando si ambos valores son true.");
/*
ALGO (no) MUY IMPORTANTE:
2 y 3 hacen la misma comprobacion, pero 3 tira el error «warning CS0183: La expresión dada siempre es del tipo proporcionado»
Si 2 estuviera escrita del mismo modo que 3, tiraria «warning CS0184: La expresión dada nunca es del tipo proporcionado»
Ya que como son variables declaradas con su tipo, hacer esa comprobacion es estupido e innecesario.
Sin embargo, «GetType» se llama en tiempo de ejecucion, por tanto el compilador no sabe que regresara hasta que lo haga.
Pareceria util de saber, pero a menos que uses dynamic o var (que no se si funcionen como creo), es un dato muy inutil.

Por cierto, «typeof» solo acepta tipos, no puedes usarlo para sacar el tipo de una variable.
*/
        Console.WriteLine("\nTambien, dentro de los if y else estan los operadores ternarios. No deberian de tenerse muchos, pero cuando solo hay un if y su else, es util.");
        Console.WriteLine("Al asignar valor a una variable puedes poner entre «()» una condicion, signo «?» y las 2 vertientes separadas por «:». La primera es para true y la segunda para false");
        Console.WriteLine("Ejemplo «string mensaje = (edad >= 18)?\"Mayor de edad\":\"Menor de edad\"»");
        {   int edad =18;
            string mensaje = (edad >= 18)? "Mayor de edad":"Menor de edad";
            Console.WriteLine($"edad: {edad}. mensaje: {mensaje}.");
        Console.WriteLine( "Del mismo modo, puedes usar «?» para no necesitar usar if y else para comprobar que algo no sea null, ya que si el codigo siguiera en caso como ese generaria errores.");
           int? na=null,nb=1,nc=0;
            string?[]? nd=null;
            Console.WriteLine("Si quiero usar el valor de una variable que puede ser un null, en vez de poner «if *variable*!=null» puedes poner «*variable* ?? *valor por defecto*».");
            Console.WriteLine($"Teniendo los valores: «na=null», «nb=1» y «nc». Valor de «nc= na ?? nb»: {nc= na ?? nb}");
            Console.WriteLine("Igualmente, para usar metodos o propiedades de un objeto que puede ser null o tener un null se pone «?» despues de cada cosa, antes del punto. Segun la doc se le llama «operador elvis» xddd");
            Console.WriteLine($"Teniendo «string?[]? nd= null». Valor de «nd?.Length»: {nd?.Length}.");
            Console.WriteLine("Ahora, asignandole «nd= new string?[]{null,\"Digimon GOD\"}»");
            nd= new string?[2]{null,"Digimon GOD"};
            Console.WriteLine($"Valor de «nd?.Length»: {nd?.Length}.");
            Console.WriteLine($"Valor de «nd?[0]?.Length»: {nd?[0]?.Length}. Valor de «nd?[1]?.Length»: {nd?[1]?.Length}.");}

        Console.WriteLine("\nswitch\n");
            Console.WriteLine("Aqui pones una variable o algo que regrese un valor y vas poniendo «case *valor posible*:» y que se ejecute una linea. Tambien el «dafault» para cualquier valor que no coindida");
        switch (d.GetType()){ //
            case Type t when t == typeof(int):// he probado mil formas distintas de poner estos case
                Console.WriteLine("No, «d» no es sbyte, es un int");
                break; //al final me funciono esta que es de chat gpt
            case Type t when t == typeof(long): //y no la entiendo 
                Console.WriteLine("No, «d» no es sbyte, es un long");
                break;// si quitas el «when t =» y dejas como si fuera variable, el System.tipo correspondiente o solo el metodo no funciona
            case Type t when t == typeof(sbyte): //Bueno, el punto es que debesponer «case *posible valor constante de la exprecion*:»
                Console.WriteLine("¿Para que compruebas de nuevo, imbecil? «d» es un sbyte");
                break;//y de ahi pones el codigo y de ultimo un «break»
            default://este ultimo se ejecuta cuando no coincide con ninguna opcion de arriba
                Console.WriteLine("No se reconocio el tipo de «d»");
                break;}
            Console.WriteLine("Una alternativa a los que dependen de valores numericos, es poner un array de Accions y que acceda a la pociones correspondiente.");
            Console.WriteLine("¿Que es un accion? no se bien, pero creo que son esos delegados, que son funciones.");
            

        Console.WriteLine("\nwhile\n");
        Console.WriteLine("El while comprueba condicion, ejecuta codigo, comprueba condicion y repite Hasta que deje de cumplirce.");
        Console.WriteLine("Cuando la condicion sea false se detendra el bucle y continuara el codigo.");
        // este parentesis de llave hace que lo que este dentro exista solo dentro de ahi, no puedes usar las variables fuera. Creo que lo use mas veces arriba, pero lo primero que hize fue esto ultimo.
        {dynamic[] lista = new dynamic[4] {0.0f,1,false,"aa",};
            Console.WriteLine("Lista: {0}",lista);
            int n=0; 
        while (lista[n].GetType()!= typeof(string)){
            Console.WriteLine($"«n»({n}) no coincide con el indice de una string dentro de «lista»");
            n++;}
        Console.WriteLine($"«n»({n}) coincide con el indice de una string dentro de «lista»");

        Console.WriteLine("\ndo while\n");
        Console.WriteLine("Esto es lo mismo al revez, ejecuta, comprueba, ejecuta y repite.");
        Console.WriteLine("Me gusta relacionarlo con cuando te dicen «haz x cosa si pasa y cosa» y ya lo estabas haciendo.");
        do {
            Console.WriteLine($"«n»({n}) no coincide con el indice de un float dentro de «lista»");
            n--;
        }while(lista[n].GetType()!= typeof(float));
        Console.WriteLine($"«n»({n}) coincide con el indice de un float dentro de «lista»");}

               {Console.WriteLine("\nfor\n");
                Console.WriteLine("Los for son bucles mas seguros que los while, ya que estos incluyen en su declaracion la lo que lleva a que se cancele.");
                Console.WriteLine("Usualmente se declara como «for (int i=0;i<=*cantidad*;i++)». Esto refiere a que se declara una variable local, se pone la condicion que comprobaria un while y la asignacion a esa variable que se ejecuta al final de cada ciclo.");
                for (int i = 0; i < 11; i++){Console.WriteLine($"i:{i}");};

                Console.WriteLine("\nforeach\n");
                Console.WriteLine("Es similar al for, pero afecta a cada elemento de una coleccion.");
                Console.WriteLine("Teniendo declarado un array de strings con nombres, si quiero hacer un List<string> con los nombres que inicien con A Se puede hacer esto:");
                string[] letters = new string[10]{"Atsuko Kagari", "Masaru Daimon", "Chaosmon", "Aki Maita", "Akiyoshi Hongo", "Abe Yoshitoshi", "Chiaki Juan Konaka", "Lain Imakura", "Angela Anaconda", "Alejandro Jorge De las Mercedes Fernandez"};
                List<string> lettersList = new List<string>();
                foreach (string letter in letters){ if (letter.ToUpper()[0]=='A'){lettersList.Add(letter);};};
                Console.WriteLine("Resultado de «foreach (string letter in letters){ if (letter.ToUpper()=='A'){lettersList.Add(letter)}}»:");
                Console.WriteLine(string.Join(", ",lettersList));

                List<string> lettersList2 = letters.Where(n=>n.ToUpper()[0]!='A').ToList();
                Console.WriteLine("\nTambien, una alternativa a esto es usar la funcion «Where». Para mostrar los otros nombres:");
                Console.WriteLine($"Valor declarado como: «List<string> lettersList2 = letters.Where(n=>n.ToUpper()[0]!='A').ToList();»:\n{string.Join(", ",lettersList2)}");}

        Console.WriteLine("\nKeyword importantes para los bucles\n");
        Console.WriteLine("continue: termina una iteracion y continua la siguiente.");
        Console.WriteLine("break: termina un bucle y continua la funcion.");
        Console.WriteLine("return: aplica para toda funcion, la termina y regresa un valor a quien la llamo.");
        
        Console.WriteLine("\ntry catch\n");
        Console.WriteLine("Cuando es posible que se produzca un error/excepción puedes poner la operacion o exprecion que lo cause dentro de un «try{*exprecion*} catch{*excepción esperada*}»");
        Console.WriteLine("Puede haber varios catch seguidos y se pueden hacer mas precisos con la Keyword «when» seguida de una condicion.");
        Console.WriteLine("Hay mucha mas informacion sobre esto, pero creo que seria extenderme mucho");
        Console.WriteLine("Esto es el try catch usado por cualquier error posible al intentar mostrar por consola «1/0»");
        try{
            int cero = default;
            int result = 1/cero;
            Console.WriteLine($"Processing succeeded: {result}");}
        catch (Exception e) when (e is ArgumentException || e is DivideByZeroException){Console.WriteLine($"Processing failed: {e.Message}");}
        catch (OperationCanceledException) {Console.WriteLine("Processing is cancelled.");}
        Console.WriteLine("\nUn dato importante de esto es que los try catch son muy lentos, ya que crean objects para funcionar. Por eso son excepciónes, porque se usan en casos excepciónales que no se pueden predecir, como apagones y tal.");
        Console.WriteLine("Muchos try catch de situaciones previsibles se pueden reemplazar por un if, else que compruebe que no va vaya a producir la excepción y una List que guarde los «mensajes de error» generados.");
        /*DOC:
        Siempre puede usar las siguientes propiedades de solo lectura para examinar
        y obtener un valor de una variable de tipo de valor que admite valores NULL:
        Nullable<T>.HasValue indica si una instancia de un tipo que admite valores NULL tiene un
        valor de su tipo subyacente.
        Nullable<T>.Value obtiene el valor de un tipo subyacente si HasValue es true.
        Si HasValue es false, la propiedad Value inicia una excepción InvalidOperationException.
        */ // Iba a usar eso para el try catch, pero para acortar el tema lo deje.        
        Console.Write("\n\n\nLos numeros del ejercicio extra son: ");//llamar la funcion me dio MUCHISIMOS problemas, pero resulta que para llamar una funcion dentro de una estatica, tambien tiene que ser estatica
        Extra(10,55,2,3,16);}//creo que la terminal lo decia, pero pense «que se joda la maquina esta, nunca funciona»(cosas de venir de godot) y probe muchas cosas a lo estupido xdd
    static void Extra(int start, int end, int divisorRequerido, int divisorProibido,int numeroProhibido){for (int i=start;i<=end;i++) {if (i %divisorRequerido==0 && i %divisorProibido!=0 && i!=numeroProhibido){Console.Write(i+", ");}}}}//yo soy muy de preferir codigo eficiente antes que limpio, pero me gusto la idea de que sea una funcion aparte
