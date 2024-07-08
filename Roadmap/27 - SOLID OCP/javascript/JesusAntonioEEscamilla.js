/** #27 - JavaScript -> Jesus Antonio Escamilla */

/**
 * El principio abierto-cerrado dice que el código debe estar abierto a la ampliación,
   pero cerrado a la modificación.
 * Lo que esto significa es que si queremos añadir funcionalidad adicional, deberíamos
   poder hacerlo simplemente ampliando la funcionalidad original, sin necesidad de modificarla.
 * El Principio de Abierto/Cerrado (Open/Closed Principle, OCP) establece que las entidades de software
   (como clases, módulos, funciones, etc.) deben estar abiertas para extensión, pero cerradas para modificación.
 * Esto significa que debemos ser capaces de agregar nuevo comportamiento al código existente sin modificarlo.
 */

//---EJERCIÓ---
//  INCORRECTO
class Employee__{
   constructor(nombre, tipo){
      this.nombre = nombre;
      this.tipo = tipo;
   }

   calculatePay(){
      if (this.tipo === 'fulltime') {
         return 4000;
      } else if(this.tipo === 'parttime'){
         return 2000;
      } else if (this.tipo === 'intern') {
         return 1000;
      }
      // Si agregamos un nuevo tipo, tenemos que modificar este método
   }
}

// Ejemplo de uso de forma Incorrecta
const fulltimeEmployee__ = new Employee__('Lizette', 'fulltime');
console.log(fulltimeEmployee__.calculatePay());

const partTimeEmployee__ = new Employee__('Antonio', 'parttime');
console.log(partTimeEmployee__.calculatePay());


//  CORRECTO
class Employee{
   constructor(nombre){
      this.nombre = nombre;
   }

   calculatePay(){
      throw new Error('You have implement the method calculatePay');
   }
}

class FullTimeEmployee extends Employee{
   calculatePay(){
      return 4000;
   }
}

class PartTimeEmployee extends Employee{
   calculatePay(){
      return 2000;
   }
}

class InternEmployee extends Employee{
   calculatePay(){
      return 1000;
   }
}

// Ejemplo de uso de forma Correcta
const fulltimeEmployee = new FullTimeEmployee('Jesus');
console.log(fulltimeEmployee.calculatePay());

const partTimeEmployee = new PartTimeEmployee('Fatima');
console.log(partTimeEmployee.calculatePay());

const internEmployee = new InternEmployee('Enrique');
console.log(internEmployee.calculatePay());

// Si necesitamos agregar un nuevo tipo de empleado, simplemente creamos una nueva clase que herede de Employee.
class ContractorEmployee extends Employee{
   calculatePay(){
      return 3000;
   }
}

const contractorEmployee = new ContractorEmployee('Mari');
console.log(contractorEmployee.calculatePay());


/**-----DIFICULTAD EXTRA-----*/

// Pendiente

/**-----DIFICULTAD EXTRA-----*/