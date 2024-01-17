/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

#include <stdio.h>
#include <stdlib.h>

/*
Example of structure
*/
typedef struct {
	int firstField;
	long secondField; 
} t_structSample;


/*
Another example of structure is union, only one field can be used 
*/
typedef union {
	unsigned int firstField;
	long secondField;
} t_union;

#define SIZE_OF_TELEPHONE_NUMBER 11


typedef struct t_struct_phone_directory {
	const char* name;
	char telephone[SIZE_OF_TELEPHONE_NUMBER];
	struct t_struct_phone_directory* next;
} t_phone_directory;

/*
Define a generic list, it will emulate a template although (as far as I know templates don't exist in C)
It's a little bit ugly anyway
User MUSTN'T malloc or free memory related with the list, user is responsable of record memory
*/
typedef struct t_generic_list {
	void* record;
	struct t_generic_list* next;
} t_generic_list;

/*
*Pointer to function which should return 0 if inLeft >= inRight 
*/
typedef int (*isLeftRecordGreaterOrEqualThanRight)(void *inLeft, void *inRight);

/*
Insert a new record, user must alway store return t_generic_list*, eg 
	list = insertPhoneDirectoryRecord (list, new_record);
First time inList will be NULL and a new t_generic_list will be created.
User is only responsible of memory allocated to inNewRecord, do not malloc or free inList
*/
t_generic_list* insertPhoneDirectoryRecord (t_generic_list* inList, void* inNewRecord, isLeftRecordGreaterOrEqualThanRight);


void main() {

	/* Create a struct */
	t_structSample myStruct;

	/* Create a union  */
	t_union myUnion;

	/* Initialize struct */
	myStruct.firstField = 1;
	myStruct.secondField = 2;

	/* Initialize union */
	myUnion.firstField = 1;
	myUnion.secondField = -2;

	printf ("Struct: First field %d, second field %ld\n", myStruct.firstField, myStruct.secondField);

	printf ("Union: First field %u, second field %ld, remains only second field\n", myUnion.firstField, myUnion.secondField);

};
