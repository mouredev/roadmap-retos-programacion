package main

import (
	"fmt"
	"slices"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                 SET (CLASS)                                */
/* -------------------------------------------------------------------------- */

type Set struct {
	elements []string
}

func NewSet(initialElements []string) *Set {
	var set Set = Set{}
	set.AddElements(initialElements...)

	return &set
}

func (set *Set) GetElements() []string {
	return slices.Clone(set.elements)
}

func (set *Set) AddElements(elements ...string) *Set {
	set.elements = append(set.elements, elements...)
	set.sanitizeElements()

	return set
}

func (set *Set) sanitizeElements() *Set {
	var sanitizedElements []string

	for i := 0; i < len(set.elements); i++ {
		var flag bool = true
		var anchorElement string = set.elements[i]

		for j := i + 1; j < len(set.elements); j++ {
			var nextElement string = set.elements[j]
			if strings.EqualFold(anchorElement, nextElement) {
				flag = false
				break
			}
		}

		if flag {
			sanitizedElements = append(sanitizedElements, anchorElement)
		}
	}

	set.elements = sanitizedElements

	return set
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func DifferenceSets(setA *Set, setB *Set) *Set {
	var set *Set = NewSet([]string{})

	var setAElements []string = setA.GetElements()
	var setBElements []string = setB.GetElements()

	for i := 0; i < len(setAElements); i++ {
		var flag bool = true
		var aElement string = setAElements[i]

		for j := 0; j < len(setBElements); j++ {
			var bElement string = setBElements[j]
			if strings.EqualFold(aElement, bElement) {
				flag = false
				break
			}
		}

		if flag {
			set.AddElements(aElement)
		}
	}

	return set
}

func IntersectionSets(setA *Set, setB *Set) *Set {
	var set *Set = NewSet([]string{})

	var setAElements []string = setA.GetElements()
	var setBElements []string = setB.GetElements()

	for i := 0; i < len(setAElements); i++ {
		var flag bool = false
		var aElement string = setAElements[i]

		for j := 0; j < len(setBElements); j++ {
			var bElement string = setBElements[j]
			if strings.EqualFold(aElement, bElement) {
				flag = true
				break
			}
		}

		if flag {
			set.AddElements(aElement)
		}
	}

	return set

}

func JoinSets(setA *Set, setB *Set) *Set {
	var set *Set = NewSet([]string{})

	var setAElements []string = setA.GetElements()
	var setBElements []string = setB.GetElements()

	set.AddElements(setAElements...)
	set.AddElements(setBElements...)

	return set
}

func SymmetricDifferenceSets(setA *Set, setB *Set) *Set {
	var set *Set = NewSet([]string{})

	var leftSide *Set = DifferenceSets(setA, setB)
	var rightSide *Set = DifferenceSets(setB, setA)

	set.AddElements(leftSide.GetElements()...)
	set.AddElements(rightSide.GetElements()...)

	return set
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Data methods...
	*/

	fmt.Println("Data methods...")

	var data []string = []string{
		"Buenos Aires",
		"Texas",
		"Madrid",
		"Houston",
		"California",
	}

	fmt.Printf("\ndata = %v\n", data)

	fmt.Println("\nAppend data at the end...")
	fmt.Println("\ndata = append(data, \"Berlin\")")

	data = append(data, "Berlin")
	fmt.Printf("data = %v\n", data)

	fmt.Println("\nAppend data at the start...")
	fmt.Println("\ndata = slices.Concat([]string{\"Chaco\"}, data)")

	data = slices.Concat([]string{"Chaco"}, data)
	fmt.Printf("data = %v\n", data)

	fmt.Println("\nAppend several data at the end...")
	fmt.Println("\ndata = append(data, \"Paris\", \"Montana\")")

	data = append(data, "Paris", "Montana")
	fmt.Printf("data = %v\n", data)

	fmt.Println("\nAppend several data at index 4...")
	fmt.Println("\ndata = slices.Concat(data[:4], []string{\"Jujuy\", \"Formosa\"}, data[4:])")

	data = slices.Concat(data[:4], []string{"Jujuy", "Formosa"}, data[4:])
	fmt.Printf("data = %v\n", data)

	fmt.Println("\nDelete data at index 3...")
	fmt.Println("\ndata = slices.Delete(data, 3, 3+1)")

	data = slices.Delete(data, 3, 3+1)
	fmt.Printf("data = %v\n", data)

	fmt.Println("\nUpdate data at index 6...")
	fmt.Println("\ndata[6] = \"Miami\"")

	data[6] = "Miami"
	fmt.Printf("data = %v\n", data)

	fmt.Println("\nCheck if a data is present...")
	fmt.Printf("\nslices.Contains(data, \"Buenos Aires\") => %t\n", slices.Contains(data, "Buenos Aires"))

	fmt.Printf("data = %v\n", data)

	fmt.Println("\nClear data...")
	fmt.Println("\ndata = nil")

	data = nil
	fmt.Printf("data = %v\n", data)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var firstSet *Set = NewSet([]string{"Hello", "Go (Golang)", "World!"})
	var secondSet *Set = NewSet([]string{"By", "Go (Golang)"})

	fmt.Printf("\nfirstSet = %v", firstSet.GetElements())
	fmt.Printf("\nsecondSet = %v\n", secondSet.GetElements())

	var intersectedSets *Set = IntersectionSets(firstSet, secondSet)
	fmt.Printf("\nIntersection (firstSet, and secondSet) => %v\n", intersectedSets.GetElements())

	var jointSets *Set = JoinSets(firstSet, secondSet)
	fmt.Printf("\nJoin (firstSet, and secondSet) => %v\n", jointSets.GetElements())

	var differencedSets *Set = DifferenceSets(firstSet, secondSet)
	fmt.Printf("\nDifferenced (firstSet, and secondSet) => %v\n", differencedSets.GetElements())

	var symmetricDifferencedSets *Set = SymmetricDifferenceSets(firstSet, secondSet)
	fmt.Printf("\nSymmetric difference (firstSet, and secondSet) => %v", symmetricDifferencedSets.GetElements())
}
