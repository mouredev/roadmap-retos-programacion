const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class RescatandoMickey {
    constructor(){
        this.matrix = [
            ["🚪", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
            ["⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️"],
            ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️"],
            ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
            ["⬜️", "⬛️", "⬜️", "⬛️", "⬜️", "⬜️"],
            ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🐭"]
        ];
        this.positions = {
            actual: {x: 5, y: 5},
            new: {x: 0, y: 0}
        }
        this.move = '';
    }

    showMaze(){
        let matrix = this.matrix;
        for(let i = 0; i < matrix.length; i++){
            for(let j = 0; j < matrix.length; j++){
                process.stdout.write(matrix[i][j]);
            }
            console.log("");
        }
    }

    changePositions() {
        let actualPositionX      = this.positions.actual.x;
        let actualPositionY      = this.positions.actual.y;
        let newPositionX         = this.positions.new.x;
        let newPositionY         = this.positions.new.y;
        let matrix               = this.matrix;
        let temporalActual       = matrix[actualPositionX][actualPositionY];//🐭
        matrix[actualPositionX][actualPositionY] = matrix[newPositionX][newPositionY];//🐭 = ⬜️  
        matrix[newPositionX][newPositionY] = temporalActual;//⬜️ = 🐭 
        this.matrix = matrix;
        this.positions.actual.x = newPositionX;
        this.positions.actual.y = newPositionY;
        this.start();
    }

    validationMove() {
        let mickeyX = this.positions.new.x;
        let mickeyY = this.positions.new.y;
        let move    = this.move;
        let matrix  = this.matrix;

        if(mickeyX == 6 && move == 's'){
            console.log("===== No puedes ir abajo =====");
            this.start();
        } else if(mickeyY == 6 && move == 'd'){
            console.log("===== No puedes ir a la derecha =====");
            this.start();
        } else if(mickeyY < 0  && move == 'a') {
            console.log("===== No puedes ir a la izquierda =====");
            this.start();
        } else if(mickeyX < 0 && move == 'w') {
            console.log("===== No puedes ir arriba =====");
            this.start();
        } else if(matrix[mickeyX][mickeyY] == "⬛️"){
            console.log("===== No puedes moverte a esa dirección porque hay un obstaculo =====");
            this.start();
        } else if(matrix[mickeyX][mickeyY] == "🚪"){
            console.log("====== Felicidades has rescatado a Mickey :D =====");
            rl.close();
        } else if (matrix[mickeyX][mickeyY] == "⬜️"){
            this.changePositions();
        }
    }

    start(){
        console.log("----------------------------------------");
        console.log("¡Ayuda a Mickey a salir del laberinto!");
        this.showMaze();
        rl.question("Selecciona una de las siguientes opciones: [w] Arriba, [s] Abajo, [a] Izquierda, [d] Derecha, [f] Salir: ", (resp) =>{
            this.move = resp;
            switch(resp){
                case 'w':
                    this.positions.new.x = this.positions.actual.x-1;
                    this.positions.new.y = this.positions.actual.y;
                    this.validationMove();
                    break;
                case 's':
                    this.positions.new.x = this.positions.actual.x+1;
                    this.positions.new.y = this.positions.actual.y;
                    this.validationMove();
                    break;
                case 'a':
                    this.positions.new.x = this.positions.actual.x;
                    this.positions.new.y = this.positions.actual.y-1;
                    this.validationMove();
                    break;
                case 'd':
                    this.positions.new.x = this.positions.actual.x;
                    this.positions.new.y = this.positions.actual.y+1;
                    this.validationMove();
                    break;
                case 'f':
                    rl.close();
                    break;
                default:
                    process.stdout.write("Opción no valida, intenta de nuevo");
                    this.start();
            }
        });
    }
}

let rescatandoMickey = new RescatandoMickey();
rescatandoMickey.start();
