// ** EJERCICIO

// correcta

const basededatos = ['Pepe', 'Pepa']

class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getUserData() {
        return `Name: ${this.name}, Email: ${this.email}`;
    }
}

class UserRepository {
    save(user) {
        basededatos.push(user.name)
    }
}

const user = new User('Bernat', 'bernat@gmail.com');
console.log(user.getUserData());

const userRepository = new UserRepository();
userRepository.save(user);
console.log(basededatos)

// incorrecta

class User2 {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getUserData() {
        return `Name: ${this.name}, Email: ${this.email}`;
    }

    saveToDatabase() {
        basededatos.push(user2.name)
    }
}

// Uso
const user2 = new User2('Bernat', 'bernat@example.com');
console.log(user2.getUserData());
user2.saveToDatabase();