/* 
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

// Posibles casillas para el tablero de juego 6x6

const board = [
  ["🐭", "⬜", "⬛", "⬜", "⬜", "⬜"],
  ["⬛", "⬜", "⬜", "⬜", "⬛", "⬜"],
  ["⬛", "⬛", "⬛", "⬛", "⬛", "⬜"],
  ["⬜", "⬜", "🚪", "⬛", "⬛", "⬜"],
  ["⬜", "⬛", "⬛", "⬛", "⬜", "⬜"],
  ["⬜", "⬜", "⬜", "⬜", "⬜", "⬛"],
]

let position = { x: 0, y: 0 } // posicion del jugador

function showLabyrinth() {
  console.clear()

  for (let y = 0; y < board.length; y++) {
    let row = ""
    for (let x = 0; x < board[y].length; x++) {
      if (x === position.x && y === position.y) {
        row += "🐭" // representa al jugador
      } else {
        row += board[y][x]
      }
    }
    console.log(row)
  }
}

showLabyrinth()
