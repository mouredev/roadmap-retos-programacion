// Creado por: EdiedRamos

type Pet = {
  name: string;
};

function fooValue(a: number, b: number) {
  [a, b] = [b, a];
  return {
    a,
    b,
  };
}

function fooReference(a: Pet, b: Pet) {
  [a.name, b.name] = [b.name, a.name];
  return {
    a,
    b,
  };
}

(() => {
  const aValue = 5,
    bValue = 10;

  const aReference: Pet = {
      name: "Snoopy",
    },
    bReference: Pet = {
      name: "Pluto",
    };

  const { a: aValueFoo, b: bValueFoo } = fooValue(aValue, bValue);
  const { a: aReferenceFoo, b: bReferenceFoo } = fooReference(
    aReference,
    bReference
  );

  console.log("*".repeat(50));
  console.log("CASO: POR VALOR");
  console.log("Originales:", { aValue, bValue });
  console.log("Retorno de la función:", { aValueFoo, bValueFoo });
  console.log("*".repeat(50));

  console.log("*".repeat(50));
  console.log("CASO: POR REFERENCIA");
  console.log("Originales:", { aReference, bReference });
  console.log("Retorno de la función:", { aReferenceFoo, bReferenceFoo });
  console.log("*".repeat(50));

  // Se verifica que las variables pasadas por valor no sean alteradas.
  /*
    No debería fallar porque el tipo "number" es un tipo primitivo,
    y los primitivos siempre son argumentos pasados por valor.
  */
  console.assert(
    aValue === 5,
    'El valor original de "aValue" ha sido alterado.'
  );
  console.assert(
    bValue === 10,
    'El valor original de "bValue" ha sido alterado.'
  );

  // Se verifica que las variables pasadas por referencia no sean alteradas.
  /*
    Debería fallar porque el tipo "object" es un tipo NO primitivo,
    y los NO primitivos siempre son argumentos pasador por referencia.
   */
  console.assert(
    aReference.name === "Snoopy",
    'El valor original de "aReference" ha sido alterado.'
  );
  console.assert(
    bReference.name === "Pluto",
    'El valor original de "bReference" ha sido alterado.'
  );
})();
