package main

import (
	"errors"
	"fmt"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

/* ---------------------------------- Cell ---------------------------------- */

type TCell string

const (
	obstacle TCell = "⬛️"
	free     TCell = "⬜️"
	player   TCell = "🐭"
	exit     TCell = "🚪"
)

type cells struct {
	Obstacle TCell
	Free     TCell
	Player   TCell
	Exit     TCell
}

var Cell cells = cells{
	Obstacle: obstacle,
	Free:     free,
	Player:   player,
	Exit:     exit,
}

/* -------------------------------- Dashboard ------------------------------- */

type Dashboard [6][6]TCell

/* -------------------------------- Position -------------------------------- */

type Position struct {
	x int
	y int
	_ struct{}
}

/* ---------------------------------- Move ---------------------------------- */

type TMove string

const (
	down  TMove = "down"
	left  TMove = "left"
	right TMove = "right"
	up    TMove = "up"
)

type moves struct {
	Down  TMove
	Left  TMove
	Right TMove
	Up    TMove
}

var Move moves = moves{
	Down:  down,
	Left:  left,
	Right: right,
	Up:    up,
}

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

/* ---------------------------- ExitNotFoundError --------------------------- */

type ExitNotFoundError struct{}

func (err *ExitNotFoundError) Error() string {
	return "Exit not found"
}

/* -------------------------------- GameOver -------------------------------- */

type GameOverError struct{}

func (err *GameOverError) Error() string {
	return "Game over"
}

/* ----------------------- InvalidPlayerPositionError ----------------------- */

type InvalidPlayerPositionError struct {
	position *Position
	_        struct{}
}

func (err *InvalidPlayerPositionError) Error() string {
	return fmt.Sprintf("Position (%d, %d) is invalid for a player", err.position.x+1, err.position.y+1)
}

/* --------------------------- PlayerNotFoundError -------------------------- */

type PlayerNotFoundError struct{}

func (err *PlayerNotFoundError) Error() string {
	return "Player not found"
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

type initialPositions struct {
	exit   Position
	player Position
	_      struct{}
}

/* ---------------------------------- Maze ---------------------------------- */

type Maze interface {
	GetDashboard() *Dashboard
	GetExitPos() *Position
	GetPlayerPos() *Position
	SetPlayerPos(newPos *Position) error
}

type maze struct {
	dashboard               *Dashboard
	exitPos                 *Position
	playerPos               *Position
	originalCellAtPlayerPos TCell
	_                       struct{}
}

func NewMaze(dashboard *Dashboard) (Maze, error) {
	var maze maze

	var initialPositions initialPositions = initialPositions{
		exit:   Position{x: -1, y: -1},
		player: Position{x: -1, y: -1},
	}

	for y, row := range dashboard {
		for x, col := range row {
			if col == Cell.Exit {
				initialPositions.exit.x = x
				initialPositions.exit.y = y
			} else if col == Cell.Player {
				initialPositions.player.x = x
				initialPositions.player.y = y
			}
		}
	}

	if initialPositions.exit.x < 0 {
		return &maze, &ExitNotFoundError{}
	}

	if initialPositions.player.x < 0 {
		return &maze, &PlayerNotFoundError{}
	}

	maze.dashboard = dashboard
	maze.originalCellAtPlayerPos = Cell.Free
	maze.exitPos = &initialPositions.exit
	maze.playerPos = &initialPositions.player

	return &maze, nil
}

func (maze *maze) GetDashboard() *Dashboard {
	return maze.dashboard
}

func (maze *maze) GetExitPos() *Position {
	return maze.exitPos
}

func (maze *maze) GetPlayerPos() *Position {
	return maze.playerPos
}

func (maze *maze) SetPlayerPos(pos *Position) error {
	if !maze.isValidPlayerPos(pos) {
		return &InvalidPlayerPositionError{position: pos}
	}

	x, y := pos.x, pos.y

	var prevPlayerPos *Position = maze.playerPos
	var prevOriginalCellAtPlayerPos TCell = maze.originalCellAtPlayerPos

	maze.originalCellAtPlayerPos = maze.dashboard[y][x]
	maze.dashboard[y][x] = Cell.Player
	maze.dashboard[prevPlayerPos.y][prevPlayerPos.x] = prevOriginalCellAtPlayerPos
	maze.playerPos = pos

	return nil
}

func (maze *maze) isValidPos(pos *Position) bool {
	x, y := pos.x, pos.y

	var dashboard *Dashboard = maze.dashboard

	var dashboardMaxY int = len(dashboard) - 1
	var outOfYRange bool = y < 0 || y > dashboardMaxY
	if outOfYRange {
		return false
	}

	var dashboardMaxX int = len(dashboard[0]) - 1
	var outOfXRange bool = x < 0 || x > dashboardMaxX
	if outOfXRange {
		return false
	}

	return true
}

func (maze *maze) isValidPlayerPos(pos *Position) bool {
	if !maze.isValidPos(pos) {
		return false
	}

	var cellAtPos TCell = maze.dashboard[pos.y][pos.x]

	var obstacleAtPos bool = cellAtPos == Cell.Obstacle
	return !obstacleAtPos
}

/* ---------------------------------- Game ---------------------------------- */

type Game interface {
	GetMaze() *Maze
	MovePlayer(move TMove) error
	IsGameOver() bool
}

type game struct {
	maze *Maze
	_    struct{}
}

func NewGame(maze *Maze) Game {
	var game game = game{maze: maze}
	return &game
}

func (game *game) GetMaze() *Maze {
	return game.maze
}

func (game *game) MovePlayer(move TMove) error {
	if game.IsGameOver() {
		return &GameOverError{}
	}

	var maze *Maze = game.maze
	var playerPos *Position = (*maze).GetPlayerPos()

	x, y := playerPos.x, playerPos.y

	var err error

	switch move {
	case Move.Down:
		err = (*maze).SetPlayerPos(&Position{
			x: x,
			y: y + 1,
		})

	case Move.Left:
		err = (*maze).SetPlayerPos(&Position{
			x: x - 1,
			y: y,
		})

	case Move.Right:
		err = (*maze).SetPlayerPos(&Position{
			x: x + 1,
			y: y,
		})

	case Move.Up:
		err = (*maze).SetPlayerPos(&Position{
			x: x,
			y: y - 1,
		})
	}

	return err
}

func (game *game) IsGameOver() bool {
	var maze *Maze = game.maze
	var exitPos *Position = (*maze).GetExitPos()
	var playerPos *Position = (*maze).GetPlayerPos()

	var playerAtExitPos bool = playerPos.x == exitPos.x && playerPos.y == exitPos.y

	return playerAtExitPos
}

/* -------------------------------------------------------------------------- */
/*                                    UTILS                                   */
/* -------------------------------------------------------------------------- */

func printDashboard(dashboard *Dashboard) {
	fmt.Println("[")

	for _, row := range dashboard {
		fmt.Printf(" %v\n", row)
	}

	fmt.Println("]")
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var dashboard Dashboard = Dashboard{
		[6]TCell{Cell.Exit, Cell.Obstacle, Cell.Obstacle, Cell.Obstacle, Cell.Obstacle, Cell.Obstacle},
		[6]TCell{Cell.Free, Cell.Obstacle, Cell.Free, Cell.Free, Cell.Free, Cell.Obstacle},
		[6]TCell{Cell.Free, Cell.Obstacle, Cell.Free, Cell.Obstacle, Cell.Free, Cell.Free},
		[6]TCell{Cell.Free, Cell.Free, Cell.Free, Cell.Obstacle, Cell.Free, Cell.Player},
		[6]TCell{Cell.Obstacle, Cell.Obstacle, Cell.Free, Cell.Obstacle, Cell.Free, Cell.Obstacle},
		[6]TCell{Cell.Obstacle, Cell.Obstacle, Cell.Free, Cell.Free, Cell.Free, Cell.Obstacle},
	}

	maze, err := NewMaze(&dashboard)
	if err != nil {
		panic(err.Error())
	}

	var game Game = NewGame(&maze)
	printDashboard((*game.GetMaze()).GetDashboard())

	for !game.IsGameOver() {
		var move string
		fmt.Print("\n> Enter a move ('up', 'right', 'left', or 'down'): ")
		fmt.Scanf("%s\n", &move)

		fmt.Println()

		switch strings.TrimSpace(move) {
		case string(Move.Down):
			err = game.MovePlayer(Move.Down)

		case string(Move.Left):
			err = game.MovePlayer(Move.Left)

		case string(Move.Right):
			err = game.MovePlayer(Move.Right)

		case string(Move.Up):
			err = game.MovePlayer(Move.Up)

		default:
			fmt.Printf("> Invalid move! Try again...\n\n")
		}

		if err == nil {
			printDashboard((*game.GetMaze()).GetDashboard())
		} else {
			var invalidPlayerPositionError *InvalidPlayerPositionError

			if errors.As(err, &invalidPlayerPositionError) {
				fmt.Printf("> %s.\n", err.Error())
				err = nil
			} else {
				panic(err)
			}
		}
	}

	fmt.Print("\n> Game over!")
}
