package main

import "fmt"

// En go no existen las clases, pero se pueden simular con estructuras y métodos
type Animal struct {
	name string
} 

func (a *Animal) makeSound() {
	fmt.Printf("Soy un %s y hago ruido\n", a.name)
}

type Dog struct {
	Animal // "Herencia" (composición)
}

func (d *Dog) makeSound() {
	// imprimir la frase 'El <nombre> hace guau!' y agregar un salto de línea
	fmt.Printf("El %s hace guau!\n", d.name)
}

type Cat struct {
	Animal
}

func (c *Cat) makeSound() {
	fmt.Printf("El %s hace miau!\n", c.name)
}

func main() {
	d := Dog{Animal{"Perro"}}
	c := Cat{Animal{"Gato"}}

	d.makeSound()
	c.makeSound()

	// Extra:
	mgr := Manager{Employee{1, "Gerardo"}, []Employee{{2, "Pedro"}, {3, "María"}, {4, "Juan"}}}
	pm := ProjectManager{Employee{5, "Luis"}, []string{"Proyecto 1", "Proyecto 2"}}
	p := Programmer{Employee{6, "Ana"}, "Go"}


	mgr.work()
	mgr.evaluate()
	pm.work()
	pm.manageProject()
	p.work()
	p.code()
}

// Solución extra:
type Employee struct {
	id   int
	name string

}

func (e *Employee) work() {
	fmt.Printf("El empleado %s está trabajando\n", e.name)
}


type Manager struct {
	Employee
	employees []Employee
}

func (m *Manager) evaluate(){
	fmt.Printf("El gerente %s está evaluando a sus empleados %v\n", m.name, m.employees)
}

type ProjectManager struct {
	Employee
	projects []string
}

func (pm *ProjectManager) manageProject(){
	fmt.Printf("El gerente de proyecto %s está manejando los proyectos %v\n", pm.name, pm.projects)
}

type Programmer struct {
	Employee
	language string
}

func (p *Programmer) code(){
	fmt.Printf("El programador %s está programando en %s\n", p.name, p.language)
}