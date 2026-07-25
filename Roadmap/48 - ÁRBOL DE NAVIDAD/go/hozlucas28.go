package main

import (
	"fmt"
	"os"
	"os/exec"
	"slices"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

type ChristmasTree interface {
	GetHeight() uint8
	GetTree() string

	AddBalls(ball rune) ChristmasTree
	AddLights(light rune) ChristmasTree
	AddStar(star rune) ChristmasTree
	RemoveBalls(ball rune) ChristmasTree
	RemoveLights(light rune) ChristmasTree
	RemoveStar(star rune) ChristmasTree
	TurnOffLights(lightOff rune) ChristmasTree
	TurnOnLights(lightOn rune) ChristmasTree
}

type christmasTree struct {
	height        uint8
	tree          []string
	lightsIndexes [][2]uint8
	_             struct{}
}

func NewChristmasTree(height uint8) ChristmasTree {
	var tree []string = []string{}

	for i := 0; i < int(height); i++ {
		var branchBlankSpaces string = " "
		if height >= 2 {
			branchBlankSpaces = strings.Repeat(" ", int(height)-i-1)
		}

		tree = append(tree, branchBlankSpaces+strings.Repeat("*", i*2+1))

	}

	var trunkBlankSpaces string
	if height >= 2 {
		trunkBlankSpaces = strings.Repeat(" ", int(height)-2)
	}

	tree = append(tree, trunkBlankSpaces+"|||")
	tree = append(tree, trunkBlankSpaces+"|||")

	var christmasTree christmasTree = christmasTree{height: height, tree: tree, lightsIndexes: [][2]uint8{}}

	return &christmasTree
}

func (christmasTree *christmasTree) GetHeight() uint8 {
	return christmasTree.height
}

func (christmasTree *christmasTree) GetTree() string {
	return strings.Join(christmasTree.tree, "\n")

}

func (christmasTree *christmasTree) AddBalls(ball rune) ChristmasTree {
	for i := 1; i < len(christmasTree.tree)-2; i++ {
		var branch string = christmasTree.tree[i]
		var counter int = 0

		var newBranch string

		for _, char := range branch {
			if counter%2 == 0 && char == '*' {
				newBranch += string(ball)
			} else {
				newBranch += string(char)
			}

			counter++
		}

		christmasTree.tree[i] = newBranch
	}

	return christmasTree
}

func (christmasTree *christmasTree) AddLights(light rune) ChristmasTree {
	for i := 1; i < len(christmasTree.tree)-2; i++ {
		var branch string = christmasTree.tree[i]
		var counter int = 0

		var newBranch string

		for j := 0; j < len(branch); j++ {
			var char byte = branch[j]

			if counter%2 != 0 && char == '*' {
				var lightIndex [2]uint8 = [2]uint8{uint8(i), uint8(j)}

				newBranch += string(light)
				christmasTree.lightsIndexes = append(christmasTree.lightsIndexes, lightIndex)
			} else {
				newBranch += string(char)
			}

			counter++
		}

		christmasTree.tree[i] = newBranch
	}

	return christmasTree
}

func (christmasTree *christmasTree) AddStar(star rune) ChristmasTree {
	christmasTree.tree[0] = strings.Replace(christmasTree.tree[0], "*", string(star), 1)
	return christmasTree
}

func (christmasTree *christmasTree) RemoveBalls(ball rune) ChristmasTree {
	for i := 1; i < len(christmasTree.tree)-2; i++ {
		christmasTree.tree[i] = strings.ReplaceAll(christmasTree.tree[i], string(ball), "*")

	}

	return christmasTree
}

func (christmasTree *christmasTree) RemoveLights(light rune) ChristmasTree {

	for len(christmasTree.lightsIndexes) != 0 {
		var lightIndex [2]uint8 = christmasTree.lightsIndexes[0]
		var branch uint8 = lightIndex[0]
		var index uint8 = lightIndex[1]

		var newBranch string

		for j := 0; j < len(christmasTree.tree[branch]); j++ {
			if j == int(index) {
				newBranch += "*"
				christmasTree.lightsIndexes = slices.Delete(christmasTree.lightsIndexes, 0, 1)
				continue
			}

			newBranch += string(christmasTree.tree[branch][j])
		}

		christmasTree.tree[branch] = newBranch
	}

	return christmasTree
}

func (christmasTree *christmasTree) RemoveStar(star rune) ChristmasTree {
	christmasTree.tree[0] = strings.Replace(christmasTree.tree[0], string(star), "*", 1)
	return christmasTree
}

func (christmasTree *christmasTree) TurnOffLights(lightOff rune) ChristmasTree {
	for i := 0; i < len(christmasTree.lightsIndexes); i++ {
		var lightIndex [2]uint8 = christmasTree.lightsIndexes[i]
		var branch uint8 = lightIndex[0]
		var index uint8 = lightIndex[1]

		var newBranch string

		for j := 0; j < len(christmasTree.tree[branch]); j++ {
			if j == int(index) {
				newBranch += string(lightOff)
				continue
			}

			newBranch += string(christmasTree.tree[branch][j])
		}

		christmasTree.tree[branch] = newBranch
	}

	return christmasTree
}

func (christmasTree *christmasTree) TurnOnLights(lightOn rune) ChristmasTree {
	for i := 0; i < len(christmasTree.lightsIndexes); i++ {
		var lightIndex [2]uint8 = christmasTree.lightsIndexes[i]
		var branch uint8 = lightIndex[0]
		var index uint8 = lightIndex[1]

		var newBranch string = ""

		for j := 0; j < len(christmasTree.tree[branch]); j++ {
			if j == int(index) {
				newBranch += string(lightOn)
				continue

			}

			newBranch += string(christmasTree.tree[branch][j])
		}

		christmasTree.tree[branch] = newBranch
	}

	return christmasTree
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var christmasTree ChristmasTree

	var input uint8
	var cmd *exec.Cmd

	fmt.Printf("> Enter the height of the christmas tree: ")
	fmt.Scanf("%d\n", &input)

	christmasTree = NewChristmasTree(input)

	cmd = exec.Command("clear")
	cmd.Stdout = os.Stdout
	cmd.Run()

	fmt.Println(christmasTree.GetTree())

	fmt.Println(
		"\n> Available operations...\n\n",
		" 1 - Add star.\n",
		" 2 - Remove star.\n",
		" 3 - Add balls.\n",
		" 4 - Remove balls.\n",
		" 5 - Add lights.\n",
		" 6 - Remove lights.\n",
		" 7 - Turn on lights.\n",
		" 8 - Turn off lights.\n",
		" 0 - Exit.",
	)

	fmt.Printf("\n> Enter an operation: ")
	fmt.Scanf("%d\n", &input)

	for input != 0 {
		switch input {
		case 1:
			christmasTree.AddStar('@')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 2:
			christmasTree.RemoveStar('@')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 3:
			christmasTree.AddBalls('o')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 4:
			christmasTree.RemoveBalls('o')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 5:
			christmasTree.AddLights('+')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 6:
			christmasTree.RemoveLights('*')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 7:
			christmasTree.TurnOnLights('+')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		case 8:
			christmasTree.TurnOffLights('*')

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println(christmasTree.GetTree())

		default:
			fmt.Println("\n> Invalid operation! Try again...")
		}

		fmt.Println(
			"\n> Available operations...\n\n",
			" 1 - Add star.\n",
			" 2 - Remove star.\n",
			" 3 - Add balls.\n",
			" 4 - Remove balls.\n",
			" 5 - Add lights.\n",
			" 6 - Remove lights.\n",
			" 7 - Turn on lights.\n",
			" 8 - Turn off lights.\n",
			" 0 - Exit.",
		)

		fmt.Printf("\n> Enter an operation: ")
		fmt.Scanf("%d\n", &input)
	}
}
