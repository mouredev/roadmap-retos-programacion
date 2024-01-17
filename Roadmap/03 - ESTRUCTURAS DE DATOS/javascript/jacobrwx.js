class Contact {
    constructor(name, phoneNumber) {
        this._name = name;
        this._phoneNumber = phoneNumber;
    }

    set name(newName) {
        // Elimina espacios en blanco del inicio y el final del nombre
        newName = newName.trim();

        // Verificar si el nombre contiene solo letras y tiene mas de 2 acaracteres
        if (/^[a-zA-Z]+$/.test(newName) && newName.length > 2) {
            this._name = newName;
        } else {
            // Lanza una excepción si el nombre no cumple con los requisitos
            throw new Error("Nombre no válido");
        }
    }

    set phoneNumber(newPhoneNumber) {
        // Elimina los espacios en blanco y los guiones
        newPhoneNumber = newPhoneNumber.replace(/\s|-/g, '');

        // Verifica si el numero contiene solo dígitos y tiene longitud de 10
        if (/^\d+$/.test(newPhoneNumber) && newPhoneNumber.length === 10) {
            this._phoneNumber = newPhoneNumber;
        } else {
             // Lanza una excepción si el número de teléfono no cumple con los requisitos
            throw new Error("Número de teléfono no válido");
        }
    }

    get name() {
        return this._name.charAt(0).toUpperCase() + this._name.slice(1);
    }

    get phoneNumber() {
        return this._phoneNumber;
    }
}