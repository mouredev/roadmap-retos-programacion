package main

import (
	"errors"
	"fmt"
)

type Set interface {
	Add(element int)
	AddToBeginning(element int)
	AddAll(elements ...int)
	AddAllAtPosition(position int, elements ...int)
	RemoveAt(position int) error
	UpdateAt(position int, element int) error
	Contains(element int) bool
	Clear()
	Union(other Set) Set
	Intersection(other Set) Set
	Difference(other Set) Set
	SymmetricDifference(other Set) Set
	Elements() []int
}

type IntSet struct {
	elements []int
}

func NewIntSet() *IntSet {
	return &IntSet{
		elements: []int{},
	}
}

func (s *IntSet) Add(element int) {
	s.elements = append(s.elements, element)
}

func (s *IntSet) AddToBeginning(element int) {
	s.elements = append([]int{element}, s.elements...)
}

func (s *IntSet) AddAll(elements ...int) {
	s.elements = append(s.elements, elements...)
}

func (s *IntSet) AddAllAtPosition(position int, elements ...int) {
	if position < 0 || position > len(s.elements) {
		return
	}
	s.elements = append(s.elements[:position], append(elements, s.elements[position:]...)...)
}

func (s *IntSet) RemoveAt(position int) error {
	if position < 0 || position >= len(s.elements) {
		return errors.New("position out of bounds")
	}
	s.elements = append(s.elements[:position], s.elements[position+1:]...)
	return nil
}

func (s *IntSet) UpdateAt(position int, element int) error {
	if position < 0 || position >= len(s.elements) {
		return errors.New("position out of bounds")
	}
	s.elements[position] = element
	return nil
}

func (s *IntSet) Contains(element int) bool {
	for _, el := range s.elements {
		if el == element {
			return true
		}
	}
	return false
}

func (s *IntSet) Clear() {
	s.elements = []int{}
}

func (s *IntSet) Elements() []int {
	return s.elements
}

func (s *IntSet) Union(other Set) Set {
	result := NewIntSet()
	existingElements := s.Elements()
	otherElements := other.Elements()
	result.AddAll(existingElements...)
	for _, el := range otherElements {
		if !result.Contains(el) {
			result.Add(el)
		}
	}
	return result
}

func (s *IntSet) Intersection(other Set) Set {
	result := NewIntSet()
	for _, el := range s.Elements() {
		if other.Contains(el) {
			result.Add(el)
		}
	}
	return result
}

func (s *IntSet) Difference(other Set) Set {
	result := NewIntSet()
	for _, el := range s.Elements() {
		if !other.Contains(el) {
			result.Add(el)
		}
	}
	return result
}

func (s *IntSet) SymmetricDifference(other Set) Set {
	result := NewIntSet()
	for _, el := range s.Elements() {
		if !other.Contains(el) {
			result.Add(el)
		}
	}
	for _, el := range other.Elements() {
		if !s.Contains(el) {
			result.Add(el)
		}
	}
	return result
}

func main() {
	set := NewIntSet()
	set.Add(5)
	set.AddToBeginning(1)
	set.AddAll(3, 4, 6)
	set.AddAllAtPosition(2, 2, 3)

	errUA := set.UpdateAt(2, 7)
	if errUA != nil {
		return
	}

	errRA := set.RemoveAt(3)
	if errRA != nil {
		return
	}

	fmt.Println("current set:", set.Elements())
	fmt.Println("contains 4:", set.Contains(4))
	fmt.Println("contains 8:", set.Contains(8))

	set.Clear()
	fmt.Println("set after cleaning:", set.Elements())

	set1 := NewIntSet()
	set1.AddAll(1, 2, 3, 4)
	set2 := NewIntSet()
	set2.AddAll(3, 4, 5, 6)

	fmt.Println("set1:", set1.Elements())
	fmt.Println("set2:", set2.Elements())

	unionSet := set1.Union(set2)
	intersectionSet := set1.Intersection(set2)
	differenceSet := set1.Difference(set2)
	symmetricDifferenceSet := set1.SymmetricDifference(set2)

	fmt.Println("union:", unionSet.Elements())
	fmt.Println("intersection:", intersectionSet.Elements())
	fmt.Println("difference:", differenceSet.Elements())
	fmt.Println("symmetric difference:", symmetricDifferenceSet.Elements())
}
