package main

import (
	"fmt"
)

/* -------------------------------------------------------------------------- */
/*                               ANIMAL (CLASS)                               */
/* -------------------------------------------------------------------------- */

type Animal struct {
	_averageSpeed  float32
	_averageWeight float32
	_name          string
	_sound         string
}

func (animal *Animal) setAverageSpeed(averageSpeed float32) *Animal {
	animal._averageSpeed = averageSpeed
	return animal
}

func (animal *Animal) setAverageWeight(averageWeight float32) *Animal {
	animal._averageWeight = averageWeight
	return animal
}

func (animal *Animal) setName(name string) *Animal {
	animal._name = name
	return animal
}

func (animal *Animal) setSound(sound string) *Animal {
	animal._sound = sound
	return animal
}

func (animal *Animal) getAverageSpeed() float32 {
	return animal._averageSpeed
}

func (animal *Animal) getAverageWeight() float32 {
	return animal._averageWeight
}

func (animal *Animal) getName() string {
	return animal._name
}

func (animal *Animal) getSound() string {
	return animal._sound
}

func (animal *Animal) getAttributes() string {
	return fmt.Sprintf("Average speed --> %.2f", animal.getAverageSpeed()) +
		fmt.Sprintf("\nAverage weight --> %.2f", animal.getAverageWeight()) +
		fmt.Sprintf("\nName --> %s", animal.getName()) +
		fmt.Sprintf("\nSound --> %s", animal.getSound())
}

func (animal *Animal) printSound() *Animal {
	fmt.Printf("%s!", animal.getSound())
	return animal
}

/* -------------------------------------------------------------------------- */
/*                                 DOG (CLASS)                                */
/* -------------------------------------------------------------------------- */

type Dog struct {
	_ownerName   string
	_ownerPhone  string
	_parentClass Animal
}

func (dog *Dog) setOwnerName(ownerName string) *Dog {
	dog._ownerName = ownerName
	return dog
}

func (dog *Dog) setOwnerPhone(ownerPhone string) *Dog {
	dog._ownerPhone = ownerPhone
	return dog
}

func (dog *Dog) getOwnerName() string {
	return dog._ownerName
}

func (dog *Dog) getOwnerPhone() string {
	return dog._ownerPhone
}

func (dog *Dog) getAttributes() string {
	return dog._parentClass.getAttributes() +
		fmt.Sprintf("\nOwner name --> %s", dog.getOwnerName()) +
		fmt.Sprintf("\nOwner phone --> %s", dog.getOwnerPhone())
}

func (dog *Dog) printSound() *Dog {
	dog._parentClass.printSound()
	return dog
}

/* -------------------------------------------------------------------------- */
/*                                 CAT (CLASS)                                */
/* -------------------------------------------------------------------------- */

type Cat struct {
	_ownerName   string
	_ownerPhone  string
	_parentClass Animal
}

func (cat *Cat) setOwnerName(ownerName string) *Cat {
	cat._ownerName = ownerName
	return cat
}

func (cat *Cat) setOwnerPhone(ownerPhone string) *Cat {
	cat._ownerPhone = ownerPhone
	return cat
}

func (cat *Cat) getOwnerName() string {
	return cat._ownerName
}

func (cat *Cat) getOwnerPhone() string {
	return cat._ownerPhone
}

func (cat *Cat) getAttributes() string {
	return cat._parentClass.getAttributes() +
		fmt.Sprintf("\nOwner name --> %s", cat.getOwnerName()) +
		fmt.Sprintf("\nOwner phone --> %s", cat.getOwnerPhone())
}

func (cat *Cat) printSound() *Cat {
	cat._parentClass.printSound()
	return cat
}

/* -------------------------------------------------------------------------- */
/*                              EMPLOYEE (CLASS)                              */
/* -------------------------------------------------------------------------- */

type Employee struct {
	_id     int
	_name   string
	_salary float32
}

func (employee *Employee) setName(name string) *Employee {
	employee._name = name
	return employee
}

func (employee *Employee) setSalary(salary float32) *Employee {
	employee._salary = salary
	return employee
}

func (employee *Employee) getId() int {
	return employee._id
}

func (employee *Employee) getName() string {
	return employee._name
}

func (employee *Employee) getSalary() float32 {
	return employee._salary
}

func (employee *Employee) getAttributes() string {
	return fmt.Sprintf("Id --> %d", employee.getId()) +
		fmt.Sprintf("\nName --> %s", employee.getName()) +
		fmt.Sprintf("\nSalary --> %.2f", employee.getSalary())
}

/* -------------------------------------------------------------------------- */
/*                             PROGRAMMER (CLASS)                             */
/* -------------------------------------------------------------------------- */

type Programmer struct {
	_languages   []string
	_side        string
	_parentClass Employee
}

func (programmer *Programmer) setLanguages(languages []string) *Programmer {
	programmer._languages = languages
	return programmer
}

func (programmer *Programmer) setSide(side string) *Programmer {
	programmer._side = side
	return programmer
}

func (programmer *Programmer) getLanguages() []string {
	return programmer._languages
}

func (programmer *Programmer) getSide() string {
	return programmer._side
}

func (programmer *Programmer) getAttributes() string {
	return programmer._parentClass.getAttributes() +
		fmt.Sprintf("\nLanguages --> %s", programmer.getLanguages()) +
		fmt.Sprintf("\nSide --> %s", programmer.getSide())
}

func (programmer *Programmer) writeCode(language string) *Programmer {
	fmt.Printf("\nWriting code in %s", language)
	return programmer
}

/* -------------------------------------------------------------------------- */
/*                           PROJECT MANAGER (CLASS)                          */
/* -------------------------------------------------------------------------- */

type ProjectManager struct {
	_functions   []string
	_programmers []Programmer
	_parentClass Employee
}

func (projectManager *ProjectManager) setFunctions(functions []string) *ProjectManager {
	projectManager._functions = functions
	return projectManager
}

func (projectManager *ProjectManager) setProgrammers(programmers []Programmer) *ProjectManager {
	projectManager._programmers = programmers
	return projectManager
}

func (projectManager *ProjectManager) getFunctions() []string {
	return projectManager._functions
}

func (projectManager *ProjectManager) getProgrammers() []Programmer {
	return projectManager._programmers
}

func (projectManager *ProjectManager) getAttributes() string {
	return projectManager._parentClass.getAttributes() +
		fmt.Sprintf("\nFunctions --> %s", projectManager.getFunctions()) +
		fmt.Sprintf("\nProgrammers --> %v", projectManager.getProgrammers())
}

func (projectManager *ProjectManager) makeManagement() *ProjectManager {
	fmt.Printf("\nJust a project manager doing everything expect programming.")
	return projectManager
}

/* -------------------------------------------------------------------------- */
/*                               MANAGER (CLASS)                              */
/* -------------------------------------------------------------------------- */

type Manager struct {
	_department      string
	_functions       []string
	_projectManagers []ProjectManager
	_parentClass     Employee
}

func (manager *Manager) setDepartment(department string) *Manager {
	manager._department = department
	return manager
}

func (manager *Manager) setFunctions(functions []string) *Manager {
	manager._functions = functions
	return manager
}

func (manager *Manager) setProjectManagers(projectManagers []ProjectManager) *Manager {
	manager._projectManagers = projectManagers
	return manager
}

func (manager *Manager) getDepartment() string {
	return manager._department
}

func (manager *Manager) getFunctions() []string {
	return manager._functions
}

func (manager *Manager) getProjectManagers() []ProjectManager {
	return manager._projectManagers
}

func (manager *Manager) getAttributes() string {
	return manager._parentClass.getAttributes() +
		fmt.Sprintf("\nDepartment --> %s", manager.getDepartment()) +
		fmt.Sprintf("\nFunctions --> %s", manager.getFunctions()) +
		fmt.Sprintf("\nProject managers --> %v", manager.getProjectManagers())

}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var dog Dog = Dog{
		_ownerName:  "Juan Nuñez",
		_ownerPhone: "1148574862",
		_parentClass: Animal{
			_averageSpeed:  28.60,
			_averageWeight: 21.78,
			_name:          "Cunca",
			_sound:         "Woof",
		},
	}

	fmt.Println("Dog attributes...")
	fmt.Printf("\n%s", dog.getAttributes())

	fmt.Println("\n\nDog sound...")
	fmt.Printf("\ndog.printSound() --> ")
	dog.printSound()

	var cat Cat = Cat{
		_ownerName:  "Lucas Hoz",
		_ownerPhone: "1124565887",
		_parentClass: Animal{
			_averageSpeed:  18.56,
			_averageWeight: 10.86,
			_name:          "Mini",
			_sound:         "Meow",
		},
	}

	fmt.Println("\n\nCat attributes...")
	fmt.Printf("\n%s", cat.getAttributes())

	fmt.Println("\n\nCat sound...")
	fmt.Printf("\ncat.printSound() --> ")
	cat.printSound()

	fmt.Println("\n\n# ---------------------------------------------------------------------------------- #\n")

	/*
		Additional challenge...
	*/

	fmt.Println("Additional challenge...")

	var programmer Programmer = Programmer{
		_languages: []string{"TypeScript", "Python", "Golang"},
		_side:      "Backend",
		_parentClass: Employee{
			_id:     0,
			_name:   "Lucas Hoz",
			_salary: 125000,
		},
	}

	fmt.Println("\nProgrammer attributes...")
	fmt.Printf("\n%s", programmer.getAttributes())

	var projectManager ProjectManager = ProjectManager{
		_functions:   []string{"Time management", "Management"},
		_programmers: []Programmer{programmer},
		_parentClass: Employee{
			_id:     1,
			_name:   "Juan Nuñez",
			_salary: 175000,
		},
	}

	fmt.Println("\n\nProject manager attributes...")
	fmt.Printf("\n%s", projectManager.getAttributes())

	var manager Manager = Manager{
		_department:      "Development",
		_functions:       []string{"Time management", "Financial planning", "Communication"},
		_projectManagers: []ProjectManager{projectManager},
		_parentClass: Employee{
			_id:     2,
			_name:   "Martin Gomez",
			_salary: 225000,
		},
	}

	fmt.Println("\n\nManager attributes...")
	fmt.Printf("\n%s", manager.getAttributes())
}
