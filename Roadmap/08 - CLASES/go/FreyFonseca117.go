// # #08 CLASES
// > #### Dificultad: Fácil | Publicación: 19/02/24 | Corrección: 26/02/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
//  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
//  * de tu lenguaje).
//  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
//  * utilizando su función.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
//  * en el ejercicio número 7 de la ruta de estudio)
//  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
//  *   retornar el número de elementos e imprimir todo su contenido.
//  * 
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import (
	"errors"
	"fmt"
)

// En GO las clases son diferentes a los demás lenguajes, se usan structs
type Student struct {
	id   int
	name string
}

// Constructor
func NewStudent() Student {
	return Student{}
}

// También es posible simular los métodos setter y getter
func (s *Student) SetId(id int) {
	s.id = id
}
func (s *Student) SetName(name string) {
	s.name = name
}

func (s *Student) GetId() int {
	return s.id
}

func (s *Student) GetName() string {
	return s.name
}

func (s *Student) ToString() string {
	return fmt.Sprintf("{Id: %d, Name: %s}", s.id, s.name)
}

// Pila LIFO último en entrar, primero en salir
type Stack[T any] struct {
	elements []T
}

func NewStack[T any]() Stack[T] {
	return Stack[T]{}
}

func (s *Stack[T]) Empty() bool {
	return len(s.elements) == 0
}

func (s *Stack[T]) Push(item T) T {
	s.elements = append(s.elements, item)
	return item
}

func (s *Stack[T]) Pop() (T, error) {
	var zero T
	if s.Empty() {
		return zero, errors.New("stack is empty")
	}
	item := s.elements[len(s.elements)-1]
	s.elements = s.elements[:len(s.elements)-1]
	return item, nil
}

func (s *Stack[T]) Peek() (T, error) {
	var zero T
	if s.Empty() {
		return zero, errors.New("stack is empty")
	}
	return s.elements[len(s.elements)-1], nil
}

func (s *Stack[T]) Size() int {
	return len(s.elements)
}

func (s *Stack[T]) Print() {
	fmt.Println(s.elements)
}

// Colas FIFO primero en entrar, primero en salir
type Queue[T any] struct {
	elements []T
}

func (q *Queue[T]) Empty() bool {
	return len(q.elements) == 0
}
func NewQueue[T any]() Queue[T] {
	return Queue[T]{}
}

func (q *Queue[T]) Add(item T) T {
	q.elements = append(q.elements, item)
	return item
}

func (q *Queue[T]) Poll() (T, error) {
	var item T
	if q.Empty() {
		return item, errors.New("queue is empty")
	}
	item = q.elements[0]
	q.elements = q.elements[1:]
	return item, nil
}

func (q *Queue[T]) Size() int {
	return len(q.elements)
}

func (q *Queue[T]) Print() {
	fmt.Println(q.elements)
}

func main() {
	//CLASES
	student := Student{}
	student.SetId(100)
	student.SetName("Amador")
	fmt.Println(student.ToString())
	//PILAS
	stack := NewStack[int]()
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)
	stack.Push(4)
	stack.Push(5)
	fmt.Println(stack.Size())
	stack.Print()
	stack.Pop()
	stack.Pop()
	fmt.Println(stack.Size())
	stack.Print()

	//COLAS
	queue := NewQueue[string]()
	queue.Add("Amador")
	queue.Add("Alex")
	queue.Add("Pedro")
	fmt.Println(queue.Size())
	queue.Print()
	queue.Poll()
	fmt.Println(queue.Size())
	queue.Print()

}
