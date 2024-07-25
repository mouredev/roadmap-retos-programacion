const esPalindromo = (t) => {
  return t.split('').reverse().join('') === t
    ? `${t} es un palindromo`
    : `${t} no es un palindromo`;
};

const esAnagrama = (t1, t2) => {
  let esAnagrama;
  const letrasDeT1 = t1.lenght;
  const letrasDeT2 = t2.lenght;

  if (letrasDeT1 === letrasDeT2) {
    esAnagrama = t1.split('').sort().join('') == t2.split('').sort().join('');
  }

  return esAnagrama
    ? `${t1} es un anagrama de ${t2}`
    : `${t1} no es un anagrama de ${t2}`;
};

const esIsograma = (t) => {
  const letras = t.split('').sort();
  const contador = [];
  let esIsograma = true;
  let cap;

  letras.forEach((letra) => {
    if (contador[letra]) {
      contador[letra].count++;
    } else {
      contador[letra] = {
        value: letra,
        count: 1,
      };
    }
  });

  Object.values(contador).forEach((letra, i) => {
    if (i === 0) {
      cap = letra.count;
    }

    if (letra.count != cap) {
      esIsograma = false;
    }
  });

  return esIsograma ? `${t} es un Isograma` : `${t} no es un Isograma`;
};

const analisisPalabras = (t1, t2) => {
  const t1Palindromo = esPalindromo(t1);
  const t2Palindromo = esPalindromo(t2);

  console.log(t1Palindromo, t2Palindromo);

  const anagrama = esAnagrama(t1, t2);

  console.log(anagrama);

  console.log(esIsograma(t1));
  console.log(esIsograma(t2));
};

analisisPalabras('Holaa', 'Halo');
