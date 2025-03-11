//Ejemplo de asignación por valor:
let a = 10;
let b = a;  // b obtiene una copia del valor de a
b = 20;     // Cambiamos el valor de b

console.log(a);  // 10 (a permanece sin cambios)
console.log(b);  // 20 (b cambió independientemente de a)
//Aquí, b tiene una copia independiente del valor de a, por lo que cambiar b no afecta a a.

//Ejemplo de asignación por referencia:
let obj1 = { name: 'John' };
let obj2 = obj1;  // obj2 apunta al mismo objeto que obj1

obj2.name = 'Jane';  // Cambiamos la propiedad "name" a través de obj2

console.log(obj1.name);  // 'Jane' (obj1 también refleja el cambio)
console.log(obj2.name);  // 'Jane' (obj2 muestra el mismo objeto)
//En este caso, obj1 y obj2 apuntan al mismo objeto en la memoria, por lo que un cambio en obj2 afecta también a obj1.

//Otro ejemplo con arrays:
let arr1 = [1, 2, 3];
let arr2 = arr1;  // arr2 apunta al mismo array que arr1

arr2.push(4);  // Modificamos el array a través de arr2

console.log(arr1);  // [1, 2, 3, 4] (arr1 también refleja el cambio)
console.log(arr2);  // [1, 2, 3, 4] (arr2 muestra el mismo array)
/* Diferencia clave:
Por valor: Los cambios en una copia no afectan a la variable original.
Por referencia: Los cambios en una copia (referencia) afectan a la variable original, ya que ambas apuntan al mismo lugar en la memoria. */
//ASIGNACION POR VALOR Y REFERENCIAS EN FUNCIONES
// Ejemplo de paso por valor:
function changeValue(x:number) {
  x = 20;   // Modificamos el valor de x dentro de la función
  console.log(x);  // 20
}

let aa = 10;
changeValue(aa);    // Pasamos el valor de a (10) a la función
console.log(aa);    // 10 (a no cambia porque se pasó por valor)
//En este caso, el valor de a permanece inalterado fuera de la función porque x es una copia del valor de a, no la variable en sí.

//Pasar parámetros por referencia en funciones
/* Cuando pasas un objeto (incluyendo arrays) como argumento a una función, lo que se pasa es una referencia al objeto original en la memoria. Esto significa que si la función modifica el objeto, el cambio se reflejará fuera de la función también. */

function modifyObject(obj:{name:string}) {
  obj.name = 'Jane';   // Modificamos una propiedad del objeto
}

let person = { name: 'John', age: 30 };
modifyObject(person);   // Pasamos el objeto a la función
console.log(person.name);  // 'Jane' (El objeto fue modificado)
/* En este caso, la función modifyObject cambia la propiedad name del objeto person. Como obj es una referencia a person, cualquier cambio dentro de la función afecta el objeto original. */

//Ejemplo con arrays (paso por referencia):
function addToArray(arr:number[]) {
  arr.push(4);   // Modificamos el array añadiendo un nuevo valor
}

let numbers = [1, 2, 3];
addToArray(numbers);  // Pasamos el array a la función
console.log(numbers);  // [1, 2, 3, 4] (El array fue modificado)
/* Aquí, el array numbers es modificado dentro de la función, porque el array se pasa por referencia. Cualquier cambio en el array dentro de la función afecta el array original. */
/* DIFICULTAD EXTRA (opcional):
  Crea dos programas que reciban dos parámetros (cada uno) definidos como
  variables anteriormente.
  - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
    se asigna a dos variables diferentes a las originales. A continuación, imprime
    el valor de las variables originales y las nuevas, comprobando que se ha invertido
    su valor en las segundas.
    Comprueba también que se ha conservado el valor original en las primeras. */
    let option:string
    do{
option = prompt(`
 1.- asignacion por valor
 2.- asignacion por referencia
 *- Salir
  `) || ''
switch (option) {
  case '1':
    const [first,second]= [prompt('dame el valor 1'),prompt('dame el valor 2')]
    assignByValue(first||'',second||'')
    break;
    case '2':
      const [x,y]= [prompt('dame la referencia x')?.split('')||' '.split(''),prompt('dame la referencia y')?.split('')||' '.split('')]
    assigByReference(x,y)
      break;

  default:
    break;
}
    }while(['1','2'].some(select=> select===option))

function assignByValue(firstVar:string,secondVar:string){
  const [firstValue,secondValue] = [secondVar,firstVar]
  console.log(` Los valores ahora son:
    ${firstValue}<=>${firstVar}
    ${secondValue}<=>${secondVar}
    `)
}
function assigByReference(originalx:string[],originaly:string[]) {
let referenceX= originalx;
let referenceY = originaly;
let temp = referenceX
referenceX = referenceY
referenceY = temp
referenceX.push('?')// ejemplo intentando alterar las referencias
referenceY.push('¿')
  console.log(` Los valores ahora son:
    ${referenceX.join('')}<=>${originalx.join('')}
    ${referenceY.join('')}<=>${originaly.join('')}
    `)
}