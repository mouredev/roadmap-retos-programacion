// https://www.typescriptlang.org/

// Array
const fruits: string[] = ["apple", "banana", "cherry"];
fruits.push("date");
fruits.splice(1, 1);
fruits[0] = "avocado";
fruits.sort();
console.log(fruits);

// Tuple
let person: [string, number] = ["Alice", 30];
console.log(person);

// Object
const user: { name: string; age: number } = { name: "Bob", age: 25 };
user.age = 26;
console.log(user);

// Map
const scores: Map<string, number> = new Map();
scores.set("Alice", 100);
scores.set("Bob", 90);
scores.delete("Bob");
console.log(scores);

// Set
const ids: Set<number> = new Set([1, 2, 3, 2, 1]);
ids.add(4);
ids.delete(1);
console.log(ids);

// Dificultad extra: agenda de contactos
type Contact = { name: string; phone: string };
const contacts: Contact[] = [];

function addContact(name: string, phone: string): void {
  if (!/^\d{1,11}$/.test(phone)) {
    console.log("Teléfono inválido");
    return;
  }
  contacts.push({ name, phone });
  console.log(`Contacto "${name}" añadido`);
}

function findContact(name: string): void {
  const found = contacts.find((c) => c.name === name);
  console.log(found ? found : "Contacto no encontrado");
}

function updateContact(name: string, phone: string): void {
  const contact = contacts.find((c) => c.name === name);
  if (!contact) {
    console.log("Contacto no encontrado");
    return;
  }
  if (!/^\d{1,11}$/.test(phone)) {
    console.log("Teléfono inválido");
    return;
  }
  contact.phone = phone;
  console.log(`Contacto "${name}" actualizado`);
}

function deleteContact(name: string): void {
  const index = contacts.findIndex((c) => c.name === name);
  if (index === -1) {
    console.log("Contacto no encontrado");
    return;
  }
  contacts.splice(index, 1);
  console.log(`Contacto "${name}" eliminado`);
}

addContact("Carlos", "1234567890");
addContact("Laura", "12");
findContact("Carlos");
updateContact("Carlos", "0987654321");
deleteContact("Carlos");
findContact("Carlos");
