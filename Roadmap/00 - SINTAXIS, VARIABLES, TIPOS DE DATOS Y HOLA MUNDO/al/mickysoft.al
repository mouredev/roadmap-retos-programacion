// https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-programming-in-al

// Comentario de una linea

/*
Comentario de 
varias 
lineas
*/

var
    //- Crea una variable (y una constante si el lenguaje lo soporta).
    MyIntegerVal : Integer;        
    MyConstText : Label 'My constant'; //Esto es una constante de texto, admite traducciones y se añade en el fichero .xliff que se genera al compilar
    
    //- Crea variables representando todos los tipos de datos primitivos
    MyInteger : Integer;    
    MyDecimal : Decimal;
    MyBigInteger : BigInteger;
    MyBoolean : Boolean;    
    MyDate : Date;
    MyTime : Time;
    MyDateTime : DateTime;
    MyDuration : Duration;
    MyBigText : BigText;
    MyByte : Byte;
    MyText : Text[50];
    MyChar : Char;
    MyCode : Code[20];
    MyGuid : Guid;
    MyTextBuilder : TextBuilder;


procedure HelloWorld()
begin    
    Message('¡Hola, AL!');
end;

    