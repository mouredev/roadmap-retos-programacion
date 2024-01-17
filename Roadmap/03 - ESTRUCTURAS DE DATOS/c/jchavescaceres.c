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

/*
Define a phone directory record
*/
typedef struct {
	const char* name;
	char telephone [SIZE_OF_TELEPHONE_NUMBER];
} t_phone_directory_record;

/*
Define a phone directory list
User MUSTN'T malloc or free memory related with the list (next)
*/
typedef struct t_struct_phone_directory {
	t_phone_directory_record phoneDirectoryRecord;
	struct t_struct_phone_directory* next;
} t_phone_directory;

/*
Insert a new record, user must alway store return t_phone_directory*, eg:
	list = insertPhoneDirectoryRecord (list, new_record);
First time inList will be NULL and a new t_phone_directory will be created.
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
t_phone_directory* insertPhoneDirectoryRecord (
	t_phone_directory* inPhoneDirectory, 
	t_phone_directory_record inPhoneDirectoryRecord);

typedef void (t_callback_record)(t_phone_directory_record inRecord);

/*
Iterate the list, invoke callbackRecord for each record 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
void iteratePhoneDirectory(
	t_phone_directory* inPhoneDirectory,
	t_callback_record callbackRecord);

/*
Update record (if found), user must alway store return t_phone_directory*, eg:
	list = updatePhoneDirectoryRecord (list, inOldRecord, inNewRecord, freeResourcesOldRecord);
callbackOldRecord is a function that will be invoked before updating the record, 
user for example can use it to free resources from that record, 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
t_phone_directory* updatePhoneDirectoryRecord (
	t_phone_directory* inPhoneDirectory,
	t_phone_directory_record OldPhoneDirectoryRecord,
	t_phone_directory_record NewPhoneDirectoryRecord,
	t_callback_record callbackOldRecord);

/*
Delete record (if found), user must alway store return t_phone_directory*, eg:
	list = deletePhoneDirectoryRecord (list, inRecord, freeResourcesRecord);
callbackRecord is a function that will be invoked before removing the record, 
can use it to for example to free resources from that record, 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
t_phone_directory* deletePhoneDirectoryRecord (
	t_phone_directory* inPhoneDirectory,
	t_phone_directory_record inPhoneDirectoryRecord,
	t_callback_record callbackRecord);

/*
Delete all records, user must alway store return t_phone_directory*, eg:
	list = deletePhoneDirectoryRecord (list, inRecord, freeResourcesRecord);
callbackRecord is a function that will be invoked before removing the record, 
can use it to for example to free resources from that record, 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
t_phone_directory* deleteAllPhoneDirectory (
	t_phone_directory* inPhoneDirectory,
	t_callback_record callbackRecord);


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
