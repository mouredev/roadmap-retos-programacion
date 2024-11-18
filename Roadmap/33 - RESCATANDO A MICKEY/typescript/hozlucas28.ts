import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                UTILITY TYPES                               */
/* -------------------------------------------------------------------------- */

type ArrayOfN<
    T extends any,
    N extends number,
    Acc extends T[] = []
> = Acc['length'] extends N ? Acc : ArrayOfN<T, N, [T, ...Acc]>

type NumberBetween<
    Min extends number,
    Max extends number,
    Counter extends 0[] = ArrayOfN<0, Min>,
    Acc extends number[] = []
> = Counter['length'] extends Max
    ? Acc[number]
    : NumberBetween<Min, Max, [0, ...Counter], [Counter['length'], ...Acc]>

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

type Cell = '⬜️' | '⬛️' | '🐭' | '🚪'

type Dashboard = ArrayOfN<ArrayOfN<Cell, 6>, 6>

interface Position {
    x: NumberBetween<0, 6> | (number & {})
    y: NumberBetween<0, 6> | (number & {})
}

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

class ExitNotFoundError extends Error {
    public constructor() {
        super('Exit not found')
        this.name = 'ExitNotFoundError'
    }
}

class GameOverError extends Error {
    public constructor() {
        super('Game over')
        this.name = 'GameOverError'
    }
}

class InvalidPlayerPositionError extends Error {
    public constructor(invalidPos: Position) {
        super(
            `Position (${invalidPos.x}, ${invalidPos.y}) is invalid for a player`
        )
        this.name = 'InvalidPlayerPositionError'
    }
}

class PlayerNotFoundError extends Error {
    public constructor() {
        super('Player not found')
        this.name = 'PlayerNotFoundError'
    }
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ---------------------------------- Maze ---------------------------------- */

interface InitialPositions {
    exitPos: Position
    playerPos: Position
}

interface IMaze {
    getDashboard: () => Dashboard
    getExitPos: () => Position
    getPlayerPos: () => Position
    setPlayerPos: (newPos: Position) => this | never
}

interface MazeConstructor {
    dashboard: Dashboard
}

class Maze implements IMaze {
    private dashboard: Dashboard
    private exitPos: Position
    private playerPos: Position
    private originalCellAtPlayerPos: Cell

    public constructor({dashboard}: MazeConstructor) {
        const {exitPos, playerPos} = this.getInitialPositions(dashboard)
        this.dashboard = dashboard
        this.exitPos = exitPos
        this.playerPos = playerPos
        this.originalCellAtPlayerPos = '⬜️'
    }

    private getInitialPositions(
        dashboard: Dashboard
    ): InitialPositions | never {
        let exitPos: Position = {x: -1, y: -1}
        let playerPos: Position = {x: -1, y: -1}

        for (let y = 0; y < dashboard.length; y++) {
            const row = dashboard[y]
            for (let x = 0; x < row.length; x++) {
                const col = row[x]
                if (col === '🚪') exitPos = {x, y}
                else if (col === '🐭') playerPos = {x, y}
            }
        }

        if (exitPos.x < 0) throw new ExitNotFoundError()
        if (playerPos.x < 0) throw new PlayerNotFoundError()

        return {exitPos, playerPos}
    }

    public getDashboard(): Dashboard {
        return this.dashboard
    }

    public getExitPos(): Position {
        return this.exitPos
    }

    public getPlayerPos(): Position {
        return this.playerPos
    }

    public setPlayerPos(pos: Position): this | never {
        if (!this.isValidPosForPlayer(pos))
            throw new InvalidPlayerPositionError(pos)

        const prevPlayerPos = this.playerPos
        const prevOriginalCellAtPlayerPos = this.originalCellAtPlayerPos

        this.originalCellAtPlayerPos = this.dashboard[pos.y][pos.x]
        this.dashboard[pos.y][pos.x] = '🐭'
        this.dashboard[prevPlayerPos.y][prevPlayerPos.x] =
            prevOriginalCellAtPlayerPos
        this.playerPos = pos
        return this
    }

    private isValidPos(pos: Position): boolean {
        const {x, y}: Position = pos
        const dashboard: Dashboard = this.dashboard

        const dashboardMaxY: number = dashboard.length - 1
        const outOfYRange: boolean = y < 0 || y > dashboardMaxY
        if (outOfYRange) return false

        const dashboardMaxX: number = dashboard[0].length - 1
        const outOfXRange: boolean = x < 0 || x > dashboardMaxX
        if (outOfXRange) return false

        return true
    }

    private isValidPosForPlayer(pos: Position): boolean {
        if (!this.isValidPos(pos)) return false

        const {x, y}: Position = pos
        const posAtDashboard: Cell = this.dashboard[y][x]

        const obstacleAtPos: boolean = posAtDashboard === '⬛️'
        if (obstacleAtPos) return false

        return true
    }
}

/* ---------------------------------- Game ---------------------------------- */

type Move = 'down' | 'left' | 'right' | 'up'

interface IGame {
    getMaze: () => IMaze
    movePlayer: (move: Move) => this | never
    isGameOver: () => boolean
}

interface GameConstructor {
    maze: IMaze
}

class Game implements IGame {
    private maze: IMaze

    public constructor({maze}: GameConstructor) {
        this.maze = maze
    }

    public getMaze(): IMaze {
        return this.maze
    }

    public movePlayer(move: Move): this | never {
        if (this.isGameOver()) throw new GameOverError()

        const maze: IMaze = this.getMaze()
        const {x, y}: Position = maze.getPlayerPos()

        const moveActions: Record<Move, () => void> = {
            down: () => maze.setPlayerPos({x, y: y + 1}),
            left: () => maze.setPlayerPos({x: x - 1, y}),
            right: () => maze.setPlayerPos({x: x + 1, y}),
            up: () => maze.setPlayerPos({x, y: y - 1}),
        }

        moveActions[move]()

        return this
    }

    public isGameOver(): boolean {
        const maze: IMaze = this.getMaze()
        const exitPos = maze.getExitPos()
        const playerPos = maze.getPlayerPos()

        const playerAtExitPos: boolean =
            playerPos.x === exitPos.x && playerPos.y === exitPos.y

        return playerAtExitPos
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const maze: Maze = new Maze({
        dashboard: [
            ['🚪', '⬛️', '⬛️', '⬛️', '⬛️', '⬛️'],
            ['⬜️', '⬛️', '⬜️', '⬜️', '⬜️', '⬛️'],
            ['⬜️', '⬛️', '⬜️', '⬛️', '⬜️', '⬜️'],
            ['⬜️', '⬜️', '⬜️', '⬛️', '⬜️', '🐭'],
            ['⬛️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️'],
            ['⬛️', '⬛️', '⬜️', '⬜️', '⬜️', '⬛️'],
        ],
    })

    const game: Game = new Game({maze})
    console.dir(game.getMaze().getDashboard())

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    while (!game.isGameOver()) {
        const move = await rl.question(
            "\n> Enter a move ('up', 'right', 'left', or 'down'): "
        )

        try {
            console.log()

            switch (move.trim().toUpperCase() as Uppercase<Move>) {
                case 'DOWN':
                    game.movePlayer('down')
                    console.dir(game.getMaze().getDashboard())
                    break

                case 'LEFT':
                    game.movePlayer('left')
                    console.dir(game.getMaze().getDashboard())
                    break

                case 'RIGHT':
                    game.movePlayer('right')
                    console.dir(game.getMaze().getDashboard())
                    break

                case 'UP':
                    game.movePlayer('up')
                    console.dir(game.getMaze().getDashboard())
                    break

                default:
                    console.log('> Invalid move! Try again...')
            }
        } catch (error) {
            if (error instanceof InvalidPlayerPositionError)
                console.log('> Player can not move down!')
        }
    }
    rl.close()

    console.log('\n> Game over!')
})()
