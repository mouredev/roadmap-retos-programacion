/* No encuentro una web oficial de SQL, 
por lo menos uno que me de confianza, asi que pongo éste
que sí es de confianza. https://www.w3schools.com/sql/ */

-- Para los comentarios en una sola línea se usa "--...."

/* Para los comentarios en varias líneas
se utiliza /*....*/ */ 

/*La variable se forma de dos instrucciones: "DECLARE" y "SET" 
(Sintaxis DECLARE: "Instrucción", "NombreVariable", "Tipo de Datos")
(Sintaxis SET: "Instrucción", "Nombre de la variable DECLARE 
a la que hace referencia", "=", "Valor")*/

DECLARE @NombreVariable INT ;/*en una instrucción se puede añadir 
                            más de una variable.*/
        @NombreVariable2 VARCHAR(50) ;

SET     @NombreVariable = 25 ;/*en una instrucción se puede añadir 
                            más de un valor.*/
        @NombreVariable2 = María de la O ;

/*SQL no soporta constantes de forma nativa pero puedes usar una 
variable para simular una constante*/
 DECLARE @NombreConstante INT ;

 SET    @NombreConstante = 50 ;/*Sólo hay que evitar cambiar este 
                                valor y declararlo en un comentario.*/


--Variables y sus tipos de datos nativos (algunos)

DECLARE @char CHAR(50) ;
        @binary BINARY ;
        @bool BOOLEAN ;
        @int INT ;
        @float FLOAT ;
        @date DATE ;
        
SET     @char = Pepe ;
        @binary = 1 ;
        @bool = true ;
        @int = 2 ; 
        @float = 2.5 ; 
        @date = 2025/12/13 ;


PRINT ("Hola,SQL") ;








