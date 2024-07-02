// Ejercicio

/* Patrón de diseño singleton */

class Person {
  constructor(name, age) {
    if (typeof Person.instance === 'object') { /* Si la clase Person existe se devuelve la instancia creada */
      return Person.instance;
    } 
    /* En caso contrario se establecen las propiedades */
    this.name = name;
    this.age = age;

    Person.instance = this;
    return this;
  }
}

let person1 = new Person('José', 44);/* El objeto creado solo tendrá una instancia */
let person2 = new Person('María', 30);
console.log(person1);
console.log(person2);