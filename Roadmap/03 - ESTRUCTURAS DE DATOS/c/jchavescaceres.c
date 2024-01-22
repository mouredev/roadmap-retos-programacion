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
#include <string.h>

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

#define MAX_SIZE_OF_TELEPHONE_NUMBER 11

#define MAX_BUFFER 250

/*
Define a phone directory record
*/
typedef struct {
	char* name;
	char* telephone;
} t_phone_directory_record;

/*
Return 1 if inLeft == inRecord
*/
int isLeftEqualToRight (
	t_phone_directory_record inLeft,
	t_phone_directory_record inRight);

/*
Return 1 if inLeft > inRecord
*/
int isLeftGreaterThanRight (
	t_phone_directory_record inLeft,
	t_phone_directory_record inRight);

/*
Return 1 if inLeft >= inRecord
*/
int isLeftGreaterOrEqualThanRight (
	t_phone_directory_record inLeft,
	t_phone_directory_record inRight);

/*
Return 1 if inLeft >= inRecord
*/
void freeResources (t_phone_directory_record inPhoneDirectoryRecord);

/*
Define a phone directory list
User MUSTN'T malloc or free memory related with the list (next)
*/
typedef struct t_struct_phone_directory {
	t_phone_directory_record phoneDirectoryRecord;
	struct t_struct_phone_directory* next;
} t_phone_directory;

/*
Insert a new record, inOutPhoneDirectory will be updated with pointer to first element
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
void insertPhoneDirectoryRecord (
	t_phone_directory** inOutPhoneDirectory, 
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
Update record (if found), inOutPhoneDirectory will be updated with pointer to first element
callbackOldRecord is a function that will be invoked before updating the record, 
user for example can use it to free resources from that record, 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
void updatePhoneDirectoryRecord (
	t_phone_directory** inOutPhoneDirectory,
	t_phone_directory_record OldPhoneDirectoryRecord,
	t_phone_directory_record NewPhoneDirectoryRecord,
	t_callback_record callbackOldRecord);

/*
Delete record (if found), inOutPhoneDirectory will be updated with pointer to first element
callbackRecord is a function that will be invoked before removing the record, 
can use it to for example to free resources from that record, 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
void deletePhoneDirectoryRecord (
	t_phone_directory** inOutPhoneDirectory,
	t_phone_directory_record inPhoneDirectoryRecord,
	t_callback_record callbackRecord);

/*
Delete all records, inOutPhoneDirectory will be set to NULL
callbackRecord is a function that will be invoked before removing the record, 
can use it to for example to free resources from that record, 
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
void deleteAllPhoneDirectory (
	t_phone_directory** inOutPhoneDirectory,
	t_callback_record callbackRecord);

/*
Sort all record, inOutPhoneDirectory will be updated with pointer to first element
This function is never needed as all insert, update or delete mantains the phone directory sorted
Do not malloc or free memory related with t_phone_directory* or "next field", use delete functions
*/
void sortPhoneDirectory (t_phone_directory** inPhoneDirectory);

/*
Menu options
*/
typedef enum {E_SEARCH=1, E_SEARCH_ALL=2, E_INSERT=3, E_UPDATE=4, E_DELETE=5, E_EXIT=6, E_WRONG_ACTION} t_action;

/*
Display wrong action 
*/
void displayWrongAction();

/*
Display main menu
*/
t_action displayMainMenu();

/*
Display search menu
*/
void displaySearchMenu(t_phone_directory **phoneDirectory);

/*
Display search all menu
*/
void displaySearchAllMenu(t_phone_directory **phoneDirectory);

/*
Display insert menu
*/
void displayInsertMenu(t_phone_directory **phoneDirectory);

/*
Display update menu
*/
void displayUpadteMenu(t_phone_directory **phoneDirectory);

/*
Display delete menu
*/
void displayDeleteMenu(t_phone_directory **phoneDirectory);


void main() {

	/* Create a struct */
	t_structSample myStruct;

	/* Create a union  */
	t_union myUnion;

	t_phone_directory *phone_directory = NULL;

	/* Initialize struct */
	myStruct.firstField = 1;
	myStruct.secondField = 2;

	/* Initialize union */
	myUnion.firstField = 1;
	myUnion.secondField = -2;

	printf ("Struct: First field %d, second field %ld\n", myStruct.firstField, myStruct.secondField);

	printf ("Union: First field %u, second field %ld, remains only second field\n", myUnion.firstField, myUnion.secondField);

	do {
	} while (displayMainMenu (&phone_directory) != E_EXIT);

	deleteAllPhoneDirectory (&phone_directory, freeResources);


	/*Tests*/
//	t_phone_directory_record a, b, c, d;
//
//	a.name = "aaaa";
//	a.telephone = "34669587172";
//
//	b.name = "bbbb";
//	b.telephone = "33669587172";
//
//	c.name = "cccc";
//	c.telephone = "34669587173";
//
//	d.name = "dddd";
//	d.telephone = "34669587173";
//
//	printf ("isLeftGreaterThanRight %d, isLeftEqualToRight: %d\n", isLeftGreaterThanRight (a, b), isLeftEqualToRight (a,b));
//	printf ("isLeftGreaterOrEqualThanRight %d\n", isLeftGreaterOrEqualThanRight (a,b));
//
//	void printRecord (t_phone_directory_record inRecord) {
//
//		printf ("name : %s, telephone : %s\n", inRecord.name, inRecord.telephone);
//	};
//
//	insertPhoneDirectoryRecord ( &phone_directory, d);
//	insertPhoneDirectoryRecord ( &phone_directory, c);
//	insertPhoneDirectoryRecord ( &phone_directory, b);
//	insertPhoneDirectoryRecord ( &phone_directory, a);
//
//	iteratePhoneDirectory (phone_directory, printRecord);
//
//	printf ("Update :\n");
//	t_phone_directory_record new = c;
//	new.telephone [0]= '9';
//	updatePhoneDirectoryRecord (&phone_directory, c, new, NULL);
//	iteratePhoneDirectory (phone_directory, printRecord);
//
//	printf ("Ordenar todos :\n");
//	/* unsort manually 
//	bbbb -> aaaa -> cccc
//	*/
//	t_phone_directory *aaaa = phone_directory;
//	t_phone_directory *bbbb = aaaa->next;
//	t_phone_directory *cccc = bbbb->next;
//	phone_directory = bbbb;
//	bbbb->next = aaaa;
//	aaaa->next = cccc;
//	printf ("Antes de ordenar todos :\n");
//	iteratePhoneDirectory (phone_directory, printRecord);
//
//	sortPhoneDirectory (&phone_directory);
//	printf ("Despues de ordenar todos :\n");
//	iteratePhoneDirectory (phone_directory, printRecord);
//
//	printf ("Borrar uno :\n");
//	deletePhoneDirectoryRecord (&phone_directory, a, NULL);
//	printf ("Nueva :\n");
//	iteratePhoneDirectory (phone_directory, printRecord);
//
//	printf ("Borrar todos :\n");
//	deleteAllPhoneDirectory (&phone_directory, NULL);
//	iteratePhoneDirectory (phone_directory, printRecord);


};

int isLeftEqualToRight (
	t_phone_directory_record inLeft,
	t_phone_directory_record inRight) {
	
	int res = 0;

	if (strcasecmp (inLeft.name, inRight.name) == 0) {

		res = (strcmp (inLeft.telephone, inRight.telephone) == 0 ? 1 : 0);
	}

	return res;
};

int isLeftGreaterThanRight (
	t_phone_directory_record inLeft,
	t_phone_directory_record inRight) {
	
	const int compareName = strcasecmp (inLeft.name, inRight.name);
	int res = 0;


	if (compareName < 0) {
		res = 1;
	}
	else if (compareName == 0) {
		res = strcmp (inLeft.telephone, inRight.telephone) < 0 ? 1 : 0;
	}

	return res;
};

int isLeftGreaterOrEqualThanRight (
	t_phone_directory_record inLeft,
	t_phone_directory_record inRight) {

	return isLeftGreaterThanRight (inLeft, inRight) || isLeftEqualToRight (inLeft, inRight);
};

void freeResources (t_phone_directory_record inPhoneDirectoryRecord) {
	free (inPhoneDirectoryRecord.name);
	free (inPhoneDirectoryRecord.telephone);
};

void insertPhoneDirectoryRecord (
	t_phone_directory** inOutPhoneDirectory, 
	t_phone_directory_record inPhoneDirectoryRecord) {
	
	t_phone_directory *first = *inOutPhoneDirectory;
	t_phone_directory *current, *new = NULL;

	current = first;

	new = malloc (sizeof (t_phone_directory));
	new-> phoneDirectoryRecord = inPhoneDirectoryRecord;
	new-> next = NULL;


	if (first == NULL) {
		/* First element in the list*/
		first = new;
	}
	else if (isLeftGreaterOrEqualThanRight (
			new->phoneDirectoryRecord,
			first->phoneDirectoryRecord)) {
		/*new item is the first in an existing list, we add it */
		new->next = first;
		first = new;
	}
	else {
		/*
		Iterate to find the proper position in the list
		first -> A -> B -> NEW -> NULL
		*/
		current = first;

		while (current  != NULL) {

			if (current-> next == NULL) {
				/* Last one, add new at the end */
				current-> next = new;
				break;
			}
			else {
				if (isLeftGreaterOrEqualThanRight (
					current->phoneDirectoryRecord,
					new->phoneDirectoryRecord) &&
				    isLeftGreaterOrEqualThanRight (
					new->phoneDirectoryRecord,
					current->next->phoneDirectoryRecord)) {
						/*
						Found position, add it and exit loop
						*/
						new->next = current->next;
						current->next = new;
						break;
					}
			};
			current = current->next;
		};
	};

	*inOutPhoneDirectory = first;
};

void iteratePhoneDirectory(
	t_phone_directory* inPhoneDirectory,
	t_callback_record callbackRecord) {

	t_phone_directory *current = inPhoneDirectory;

	if (callbackRecord != NULL) {
		while (current != NULL) {

			callbackRecord (current->phoneDirectoryRecord);
			current = current->next;

		};
	};
};


void updatePhoneDirectoryRecord (
	t_phone_directory** inOutPhoneDirectory,
	t_phone_directory_record OldPhoneDirectoryRecord,
	t_phone_directory_record NewPhoneDirectoryRecord,
	t_callback_record callbackOldRecord) {
	

	int found = 0;
	void callback_record (t_phone_directory_record inRecord) {

		found = 1;

		if (callbackOldRecord != NULL) {
			callbackOldRecord (inRecord);
		};
	};

	deletePhoneDirectoryRecord (inOutPhoneDirectory, OldPhoneDirectoryRecord, callback_record);

	if (found) {

		insertPhoneDirectoryRecord (inOutPhoneDirectory, NewPhoneDirectoryRecord);

	};

};

void deletePhoneDirectoryRecord (
	t_phone_directory** inOutPhoneDirectory,
	t_phone_directory_record inPhoneDirectoryRecord,
	t_callback_record callbackRecord) {

	t_phone_directory *first = *inOutPhoneDirectory;
	t_phone_directory *current = NULL;
	t_phone_directory *previous = NULL;

	if (first != NULL) {
		if (isLeftEqualToRight (first->phoneDirectoryRecord, inPhoneDirectoryRecord)) {
			/* First one is to be removed */
			
			if (callbackRecord != NULL) {
				callbackRecord (first->phoneDirectoryRecord);
			};
	
			current = first;
			first = first->next;
			free (current);
		}
		else {
			current = first->next;
			previous = first;
	
			while (current != NULL) {
				/* first -> A -> OLD -> C -> NULL*/
				if (isLeftEqualToRight (current->phoneDirectoryRecord, inPhoneDirectoryRecord)) {
		
					/* Found */
					if (callbackRecord != NULL) {
						callbackRecord (current->phoneDirectoryRecord);
					};
	
					previous->next = current->next;
					free (current);
					break;
				}
				previous = current;
				current = current->next;
			};
		};

	};
	*inOutPhoneDirectory = first;
};

void deleteAllPhoneDirectory (
	t_phone_directory** inOutPhoneDirectory,
	t_callback_record callbackRecord) {

	t_phone_directory *current, *previous = NULL;

	current = *inOutPhoneDirectory;

	while (current != NULL) {

		if (callbackRecord != NULL) {
			callbackRecord (current->phoneDirectoryRecord);
		};
		previous = current;
		current = current->next;
		free (previous);
	};

	*inOutPhoneDirectory = current;
};

void sortPhoneDirectory (t_phone_directory** inPhoneDirectory) {

	/* Instead of sorting it will create a new phone diretory as all elements will be sorted */

	t_phone_directory *old = *inPhoneDirectory;
	t_phone_directory *new = NULL;

	void iterateCallback (t_phone_directory_record inPhoneDirectoryRecord) {

		insertPhoneDirectoryRecord (&new, inPhoneDirectoryRecord);

	};

	deleteAllPhoneDirectory (&old, iterateCallback);

	*inPhoneDirectory = new;
};

void displayWrongAction() {

	const char* WRONG_ACTION = "Opción incorrecta";
	printf ("%s\n\n", WRONG_ACTION);
};

t_action displayMainMenu(t_phone_directory **phoneDirectory) {

	char buffer [MAX_BUFFER];
	t_action action = E_EXIT;

	printf ("MENU PRINCIPAL:\n");
	printf ("1. Buscar:\n");
	printf ("2. Listar todos:\n");
	printf ("3. Insertar nuevo registro:\n");
	printf ("4. Actualizar registro:\n");
	printf ("5. Borrar registro:\n");
	printf ("6. Salir:\n");
	printf ("\nEscoja opcion: ");

	fgets (buffer, MAX_BUFFER, stdin);
	if (sscanf (buffer, "%d\n", (int*)&action) != 1) {
		displayWrongAction();
		action = E_WRONG_ACTION;
	}
	else {
		switch (action) {

			case E_SEARCH :
				displaySearchMenu(phoneDirectory);
				break;
			case E_SEARCH_ALL:
				displaySearchAllMenu(phoneDirectory);
				break;
			case E_INSERT:
				displayInsertMenu(phoneDirectory);
				break;
			case E_UPDATE:
				displayUpadteMenu(phoneDirectory);
				break;
			case E_DELETE: 
				displayDeleteMenu(phoneDirectory);
				break;
			case E_EXIT: 
				break;
			default:
				displayWrongAction();
				action = E_WRONG_ACTION;
				break;
		};
	};

	return action;
};

void displaySearchMenu(t_phone_directory **phoneDirectory) {
};

void displaySearchAllMenu(t_phone_directory **phoneDirectory) {

	void iterateCallback (t_phone_directory_record inPhoneDirectoryRecord) {

		printf("\nNombre: %s Teléfono : %s", inPhoneDirectoryRecord.name, inPhoneDirectoryRecord.telephone);
	};

	iteratePhoneDirectory(*phoneDirectory, iterateCallback);
	printf("\n");

};

void displayInsertMenu(t_phone_directory **phoneDirectory) {

	char buffer [MAX_BUFFER];
	t_phone_directory_record phoneRecord;
	phoneRecord.name = NULL;
	phoneRecord.telephone = NULL;
	int ok=0;

	printf("\nNombre : ");
	fgets (buffer, MAX_BUFFER, stdin);
	phoneRecord.name = malloc (strlen (buffer));
	strcpy (phoneRecord.name, buffer);

	printf("Telefono (máximo 11 dígitos) : ");
	fgets (buffer, MAX_BUFFER, stdin);
	if ( (strlen(buffer) -1) > MAX_SIZE_OF_TELEPHONE_NUMBER || strspn(buffer, "0123456789") != (strlen(buffer)-1) ) {
		printf ("Wrong number\n");
		ok=0;
	}
	else
	{
		ok=1;
		phoneRecord.telephone = malloc (strlen (buffer));
		strcpy (phoneRecord.telephone, buffer);
	}

	if (!ok) {
		free (phoneRecord.name);
		free (phoneRecord.telephone);
	}
	else {
		printf ("OK\n");
		insertPhoneDirectoryRecord (phoneDirectory, phoneRecord);
	}
};

void displayUpadteMenu(t_phone_directory **phoneDirectory) {
};

void displayDeleteMenu(t_phone_directory **phoneDirectory) {
};
