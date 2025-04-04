function ejercicio() {
  let val = "hola";
  console.log(`texto original: ${val}`);
  f_valor(val);
  console.log(`texto en variable original: ${val}`);
  console.log(`\n asignacion de  valores por referencia`);
  f_referencia();
}

function f_valor(val) {
  /**
   ** cuando se pasa una variable por valor, se pasa una copia de esta, si se modifica,
   ** esto solo afectaria a la copia, mas a la variable original no
   */
  console.log(`\ntexto pasado: ${val}`);
  val = "adios";
  console.log(`texto modificado: ${val}`);
}

function f_referencia() {
  /**
   ** cuando se pasa un valor por referencia, se pasa la ubicacion de donde está guardado esa
   ** variable en la memoria, si se modifica algo, si afectaria a la variable
   ** en javascript , los objetos y arreglos se manejan por referencias
   **Cuando asignas un objeto o un arreglo a una variable, en realidad
   ** estás asignando una referencia a la ubicación en memoria donde se almacena ese objeto o arreglo.
   * *Modificar el objeto o arreglo a través de una variable
   ** también afectará a otras variables que hagan referencia al mismo objeto o arreglo.
   */
  let obj1 = {
    nombre: "juan",
    edad: 15,
  };
  console.log(`obj1 :`);
  console.log(obj1);
  //* como le estoy pasando la direccion de memoria de obj1 a obj2, estan compartiendo o mejor dicho
  //* tinene el mismo espacio en la memoria, asi que si modificamos obj2, tambian se modificará obj1
  let obj2 = obj1;
  obj2.nombre = "andres";
  console.log(`obj1 modificado:`);
  console.log(obj2);
  //* lo mismo se puede hacer en un array
  let arr = [1, 2, 3, 4, 5];
  console.log("arr: ");
  console.log(arr);
  let arr_2 = arr;
  arr_2.pop();
  console.log("arr modificado: ");
  console.log(arr);

  //* pasando valores por referencia

  function modificarObjeto(obj) {
    obj.propiedad = "nuevo valor";
  }

  let obj = {
    propiedad: "valor original",
  };
  console.log("obj original: ");
  console.log(obj);
  modificarObjeto(obj);
  console.log("obj modificado: ");
  console.log(obj);
}

// ejercicio();

function extra() {
  let v1 = 1;
  let v2 = 2;
  console.log(`valor original 1: ${v1}`);
  console.log(`valor original 2: ${v2}`);
  let [c1, c2] = cambio_valor(v1, v2);
  console.log("\n");
  console.log(`copia valor 1: ${c1}`);
  console.log(`copia valor 2: ${c2}`);
  console.log("\n");
  let r1 = [1];
  let r2 = [2];
  console.log(`valor original de r1: ${r1[0]}`);
  console.log(`valor original de r2: ${r2[0]}`);
  console.log("\n");
  let [cr1, cr2] = cambio_referencia(r1, r2);
  console.log(`el valor de cr1 es: ${cr1[0]}`);
  console.log(`el valor de cr2 es: ${cr2[0]}`);
  console.log("\n");
  console.log(`el valor de r1: ${r1[0]}`);
  console.log(`el valor de r2: ${r2[0]}`);
}

function cambio_valor(v1, v2) {
  let aux = v1;
  v1 = v2;
  v2 = aux;
  return [v1, v2];
}

function cambio_referencia(r1, r2) {
  let aux = r1[0];
  r1[0] = r2[0];
  r2[0] = aux;
  return [r1, r2];
}

extra();
