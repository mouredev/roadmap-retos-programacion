// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function drawTree(tree) {
  console.clear();
  tree.forEach(line => console.log(line));
  console.log();
}

function initializeTree(height, hasStar) {
  const tree = [];

  if (hasStar) {
    tree.push(' '.repeat(height) + '@');
  }

  for (let i = 0; i < height; i++) {
    const width = 2 * i + 1;
    const row = ' '.repeat(height - i - 1) + '*'.repeat(width);
    tree.push(row);
  }

  const trunk = ' '.repeat(height - 1) + '|||';
  tree.push(trunk);
  tree.push(trunk);

  return tree;
}

function toggleStar(tree, height, hasStar) {
  hasStar = !hasStar;
  const newTree = initializeTree(height, hasStar);
  console.log(`Estrella ${hasStar ? 'añadida' : 'eliminada'}.`);
  return { tree: newTree, hasStar };
}

function addOrRemove(tree, height, symbol, count, add) {
  let modifications = 0;

  for (let i = 1; i <= height; i++) {
    const row = tree[i].split('');

    for (let j = 0; j < row.length; j++) {
      if ((add && row[j] === '*' && Math.random() < 0.5) || (!add && row[j] === symbol)) {
        row[j] = add ? symbol : '*';
        modifications++;
      }
      if (modifications === count) break;
    }

    tree[i] = row.join('');
    if (modifications === count) break;
  }

  console.log(`${add ? 'Añadido' : 'Eliminado'} ${modifications} de ${symbol}.`);
  return tree;
}

function toggleLights(tree, height, lightsOn) {
  lightsOn = !lightsOn;

  for (let i = 1; i <= height; i++) {
    const row = tree[i].split('');
    for (let j = 0; j < row.length; j++) {
      if (row[j] === '*' || row[j] === '+') {
        row[j] = lightsOn ? '+' : '*';
      }
    }
    tree[i] = row.join('');
  }

  console.log(`Luces ${lightsOn ? 'encendidas' : 'apagadas'}.`);
  return { tree, lightsOn };
}

function main() {
  rl.question('Ingresa la altura del árbol: ', input => {
    const height = parseInt(input, 10);
    if (isNaN(height) || height <= 0) {
      console.log('Altura inválida.');
      rl.close();
      return;
    }

    let hasStar = true;
    let lightsOn = false;
    let tree = initializeTree(height, hasStar);

    function menu() {
      drawTree(tree);
      rl.question('Opciones: [estrella, bolas, luces, apagar, salir]: ', option => {
        switch (option.trim().toLowerCase()) {
          case 'estrella':
            ({ tree, hasStar } = toggleStar(tree, height, hasStar));
            break;
          case 'bolas':
            tree = addOrRemove(tree, height, 'o', 2, true);
            break;
          case 'luces':
            tree = addOrRemove(tree, height, '+', 3, true);
            break;
          case 'apagar':
            ({ tree, lightsOn } = toggleLights(tree, height, lightsOn));
            break;
          case 'salir':
            console.log('Gracias por decorar el árbol!');
            rl.close();
            return;
          default:
            console.log('Opción no válida.');
        }
        menu();
      });
    }

    menu();
  });
}

main();
