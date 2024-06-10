package main

import "fmt"

type Animal interface {
	MakeSound() string
}

type Dog struct {
	Name string
}

func (d Dog) MakeSound() string {
	return "Woof!"
}

type Cat struct {
	Name string
}

func (c Cat) MakeSound() string {
	return "Meow!"
}

func PrintSound(a Animal) {
	fmt.Printf("%s\n", a.MakeSound())
}

/* extra */
type Employee struct {
	ID   int
	Name string
}

type Manager struct {
	Employee
	Employees []Employee
}

type ProjectManager struct {
	Manager
	Projects []string
}

type Programmer struct {
	Employee
	Languages []string
}

func PrintDetails(e Employee) {
	fmt.Printf("ID: %d, Name: %s\n", e.ID, e.Name)
}

func PrintManagerDetails(m Manager) {
	PrintDetails(m.Employee)
	fmt.Println("Employees under management:")
	for _, emp := range m.Employees {
		PrintDetails(emp)
	}
}

func PrintProjectManagerDetails(pm ProjectManager) {
	PrintManagerDetails(pm.Manager)
	fmt.Println("Projects managed:")
	for _, project := range pm.Projects {
		fmt.Println(project)
	}
}

func PrintProgrammerDetails(p Programmer) {
	PrintDetails(p.Employee)
	fmt.Println("Programming languages known:")
	for _, lang := range p.Languages {
		fmt.Println(lang)
	}
}

func main() {
	dog := Dog{Name: "Buddy"}
	cat := Cat{Name: "Whiskers"}

	PrintSound(dog)
	PrintSound(cat)

	/* extra */
	manager := Manager{
		Employee: Employee{ID: 1, Name: "Alice"},
		Employees: []Employee{
			{ID: 2, Name: "Bob"},
			{ID: 3, Name: "Charlie"},
		},
	}

	projectManager := ProjectManager{
		Manager: Manager{
			Employee: Employee{ID: 4, Name: "Diana"},
			Employees: []Employee{
				{ID: 5, Name: "Eve"},
				{ID: 6, Name: "Frank"},
			},
		},
		Projects: []string{"Project X", "Project Y"},
	}

	programmer := Programmer{
		Employee:  Employee{ID: 7, Name: "Grace"},
		Languages: []string{"Go", "Python", "Java"},
	}

	PrintManagerDetails(manager)
	fmt.Println()
	PrintProjectManagerDetails(projectManager)
	fmt.Println()
	PrintProgrammerDetails(programmer)
}
