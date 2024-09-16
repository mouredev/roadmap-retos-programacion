package main

import "fmt"

//Go no cuenta con una palabra para declarar herencia en los structs, sin embargo sí tiene algo parecido.
//Para que un struct en go posea todos los campos que declara otro struct, le pasamos este último como un campo anónimo

type Animal struct {
	code string
	name string
}

type Cat struct {
	Animal
}

type Dog struct {
	Animal
}

type Sound interface {
	MakeSound()
}

func (c *Cat) MakeSound() {
	fmt.Printf("El gato %s hace miau miau \n", c.name)
}

func (d *Dog) MakeSound() {
	fmt.Printf("El perro %s hace wau wau \n", d.name)
}

//Está función puede recibir cualquier struct que implemente la interfaz Sound
func PrintAnimal(sound Sound) {
	sound.MakeSound()
}

//=============================================================
//======================= EXTRA ===============================
//=============================================================
type EmployeeManager interface {
	AddEmployee(employee Employee)
	PrintEmployees()
}

type Employee struct {
	id        int
	name      string
	employees []Employee
}

func (e *Employee) AddEmployee(employee Employee) {
	e.employees = append(e.employees, employee)
}

func (e *Employee) PrintEmployees() {
	for _, employee := range e.employees {
		fmt.Printf("id : %d, name:%s\n", employee.id, employee.name)
	}
}

type Manager struct {
	Employee
}

func (m *Manager) CoordinateProjects() {
	fmt.Printf("%s está coordinando todos los proyectos de la empresa.\n", m.name)
}

type ProjectManager struct {
	Employee
	project string
}

func (pm *ProjectManager) CoordinateProject() {
	fmt.Printf("%s está coordinando su proyecto %s \n", pm.name, pm.project)
}

type Programmer struct {
	Employee
	languages []string
}

func (e *Programmer) AddEmployee(employee Employee) {
	fmt.Println("Un programador no puede tener empleados, no se ha agregado")
}

func (e *Programmer) Code() {
	fmt.Printf("%s está programando en %v", e.name, e.languages)
}

func main() {
	cat1 := Cat{Animal{code: "0001", name: "Thor"}}
	PrintAnimal(&cat1)
	dog1 := Dog{Animal{code: "0002", name: "Run Run"}}
	PrintAnimal(&dog1)
	//EXTRA
	m := Manager{Employee{id: 100, name: "Amador"}}
	m.AddEmployee(Employee{id: 200, name: "Alex"})
	p := Programmer{languages: []string{"Java", "Go"}, Employee: Employee{id: 100, name: "Mia"}}
	p.AddEmployee(Employee{id: 300, name: "Pedro"})

	var employeeManagers []EmployeeManager
	employeeManagers = append(employeeManagers, &m, &p)

	for _, manager := range employeeManagers {
		manager.AddEmployee(Employee{id: 500, name: "New Employee"})
	}
	m.CoordinateProjects()
	m.PrintEmployees()
}
