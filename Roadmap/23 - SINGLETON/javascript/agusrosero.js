/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 */
class Office {
  constructor(name, employees) {
    this.name = name;
    this.employees = employees;
    if (typeof Office.instance === "object") {
      return Office.instance;
    }
    Office.instance = this;
    return this;
  }
}

const office1 = new Office("Principal", 30);
console.log(office1)
/* DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */

