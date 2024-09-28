'''
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
 *
'''

from dataclasses import dataclass, field
from typing import Callable, Optional, Union

VALID_OPERATIONS = ("1", "2", "3", "4", "5", "exit")


@dataclass()
class Contact:
    """Representa un contacto con nombre y número de teléfono.

    Attributes:
        name (str): El nombre del contacto.
        number (int): El número telefónico del contacto.

    Raises:
        ValueError: Si el número telefónico tiene más de 11 dígitos.
    """

    name: str
    number: int

    def __post_init__(self):
        """Verifica la validez del número telefónico al inicializar el contacto."""
        if len(str(self.number)) > 11:
            raise ValueError("El número telefónico no puede tener más de 11 dígitos.")


@dataclass()
class Directory:
    """Representa una agenda de contactos.

    Attributes:
        contacts (list[Contact]): Una lista de Contact que representa la agenda.
    """

    contacts: list[Contact] = field(default_factory=list)

    def search_contact(self, name: str, return_index: bool = False) -> Optional[Union[Contact, int]]:
        """Busca un contacto por nombre.

        Args:
            name (str): El nombre del contacto a buscar.
            return_index (bool): Si es True, devuelve el índice del contacto en lugar del contacto mismo.

        Returns:
            Optional[Union[Contact, int]]: El contacto o su índice si se encuentra, None en caso contrario.
        """
        if self.contact_exists(name):
            for index, contact in enumerate(self.contacts):
                if contact.name.lower() == name.lower():
                    return contact if not return_index else index
        else:
            return None

    def insert_contact(self, new_contact: Contact) -> None:
        """Inserta un nuevo contacto en la agenda.

        Args:
            new_contact (Contact): El contacto a agregar.

        Prints:
            Mensaje de éxito o error.
        """
        if self.contact_exists(new_contact.name):
            print(f"Contacto con el nombre {new_contact.name} ya existe.")
        else:
            try:
                self.contacts.append(new_contact)
                print(f"{new_contact.name} fue agregado con éxito en la agenda.")
            except Exception as e:
                print(e)

    def update_contact(self, modified_contact: Contact) -> None:
        """Actualiza un contacto existente.

        Args:
            modified_contact (Contact): El contacto con la información actualizada.

        Prints:
            Mensaje de éxito, error o solicitud de confirmación para agregar el contacto si no existe.
        """
        contact_index = self.search_contact(modified_contact.name, return_index=True)
        if contact_index:
            self.contacts[contact_index] = modified_contact
            print(f"El contacto {modified_contact.name} fue actualizado con éxito.")
        else:
            print(
                f"El contacto {modified_contact.name} no existe en la agenda.",
                "\n",
                "Desea agregarlo? (Si/No)",
            )
            response = input()
            if response.lower() == "si":
                self.insert_contact(modified_contact)

    def delete_contact(self, name: str) -> None:
        """Elimina un contacto de la agenda por nombre.

        Args:
            name (str): El nombre del contacto a eliminar.

        Prints:
            Mensaje de éxito o error.
        """
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"El contacto {name} fue eliminado con éxito")
        else:
            print(f"El contacto {name} no existe en la agenda.")

    def display_contacts(self):
        """Muestra todos los contactos de la agenda."""
        if self.contacts:
            for contact in self.contacts:
                print(f"Nombre: {contact.name}, Número: {contact.number}")
        else:
            print("No hay contactos en la agenda.")

    def contact_exists(self, name: str) -> bool:
        """Verifica si existe un contacto con un determinado nombre.

        Args:
            name (str): El nombre del contacto a verificar.

        Returns:
            bool: True si el contacto existe, False en caso contrario.
        """
        return any(contact.name.lower() == name.lower() for contact in self.contacts)


# Funciones para solicitar entrada del usuario
def request_input(prompt: str, validation: Optional[Callable[[str], bool]] = None) -> str:
    """Solicita entrada al usuario hasta que cumpla con la validación.

    Args:
        prompt (str): El mensaje a mostrar al usuario.
        validation (Optional[Callable[[str], bool]]): La función de validación que debe pasar la entrada.

    Returns:
        str: La entrada del usuario que pasó la validación.
    """
    while True:
        user_input = input(prompt)
        if not validation or validation(user_input):
            return user_input


def validate_operation(operation: str) -> bool:
    """Valida si la operación ingresada es válida.

    Args:
        operation (str): La operación a validar.

    Returns:
        bool: True si la operación es válida, False en caso contrario.

    Prints:
        Mensaje pidiendo una operación válida si la entrada es inválida.
    """
    if operation.lower() in VALID_OPERATIONS:
        return True
    print("Por favor ingrese una operación válida.")
    return False


def validate_number(number: str) -> bool:
    """Valida si el número ingresado es válido (numérico y no más de 11 dígitos).

    Args:
        number (str): El número a validar.

    Returns:
        bool: True si el número es válido, False en caso contrario.

    Prints:
        Mensaje pidiendo un número válido si la entrada es inválida.
    """
    try:
        number = int(number)
        return True
    except ValueError:
        print("Por favor ingrese un número válido.")
        return False


def main():
    directory = Directory()
    while True:
        print("---------------------------------------------------------------------")
        print("Operaciones posibles:")
        print(
            "1. Buscar contacto",
            "2. Agregar contacto",
            "3. Actualizar contacto",
            "4. Eliminar contacto",
            "5. Mostrar todos los contactos",
            sep="\n",
        )
        print("Si desea salir de la aplicación escriba la palabra 'Exit'")
        operation = request_input("Digite la opción: ", validate_operation)
        print("************************************************")

        if operation.lower() == "exit":
            break

        if operation == "1":
            name = request_input("Ingrese el nombre que desea buscar: ")
            contact = directory.search_contact(name)
            contact_print = contact if contact else f"El contacto con número {name} no existe en la agenda."
            print(contact_print)
        elif operation == "2":
            name = request_input("Ingrese el nombre del contacto: ")
            number = request_input("Ingrese el número del contacto: ", validate_number)
            try:
                contact = Contact(name=name, number=int(number))
                directory.insert_contact(contact)
            except Exception as e:
                print(e)
        elif operation == "3":
            name = request_input("Ingrese el nombre del contacto que va a actualizar: ")
            number = request_input("Ingrese el nuevo número del contacto: ", validate_number)
            try:
                contact = Contact(name=name, number=int(number))
                directory.update_contact(contact)
            except Exception as e:
                print(e)
        elif operation == "4":
            try:
                name = request_input("Ingrese el nombre del contacto que desea eliminar: ")
                directory.delete_contact(name=name)
            except Exception as e:
                print(e)
        elif operation == "5":
            directory.display_contacts()

        print("************************************************")
        next_iter = request_input("Desea continuar? (si, no): ", lambda choice: choice.lower() in ("si", "no", "exit"))
        if next_iter in ("no", "exit"):
            break


if __name__ == "__main__":
    main()
