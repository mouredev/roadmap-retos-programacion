package main

import (
	"fmt"
	"sync"
)

// El patrón Singleton garantiza que solo haya una única instancia de una clase en toda la aplicación.

// En GO no hay clases, por lo que se utiliza una estructura para representar la clase Singleton.
type Singleton struct {
	// Atributos de la estructura.
}
// instance representa la instancia única de la estructura Singleton.
var instance *Singleton
// once representa una estructura que permite ejecutar una función una sola vez.
var once sync.Once
// GetInstance devuelve la instancia única de la estructura Singleton.
func GetInstance() *Singleton {
	once.Do(func() {
		instance = &Singleton{}
	})
	return instance
}

func main() {
	instance1 := GetInstance()
	instance2 := GetInstance()
	fmt.Println(instance1 == instance2) // con esto se comprueba que la instancia es única

	//Extra:
	extra()
}

// Extra: User representa la sesión de usuario de la aplicación.
type User struct {
	ID       int
	Username string
	Name     string
	Email    string
}
// Extra: instanceUser representa la instancia única de la estructura User.
var instanceUser *User
// Extra: onceUser representa una estructura que permite ejecutar una función una sola vez.
var onceUser sync.Once

// Extra: GetUserInstance devuelve la instancia única de la estructura User.
func GetUserInstance() *User {
	onceUser.Do(func() {
		instanceUser = &User{}
	})
	return instanceUser
}

// Extra: SetUser asigna los datos del usuario a la instancia Singleton.
func (user *User) SetUser(id int, username, name, email string) {
	fmt.Println("Datos del usuario asignados:")
	fmt.Println("ID:", id)
	fmt.Println("Username:", username)
	fmt.Println("Nombre:", name)
	fmt.Println("Email:", email)
}

// Extra: GetUser devuelve los datos del usuario asignados a la instancia Singleton.
func (user *User) GetUser() {
	fmt.Println("Datos obtenidos del usuario:")
	fmt.Println("ID:", user.ID)
	fmt.Println("Username:", user.Username)
	fmt.Println("Nombre:", user.Name)
	fmt.Println("Email:", user.Email)
}

// Extra: DeleteUser borra los datos del usuario asignados a la instancia Singleton.
func (user *User) DeleteUser() {
	fmt.Println("Borrando datos del usuario ahora...")
	user.ID = 0
	user.Username = ""
	user.Name = ""
	user.Email = ""
}

func extra() {
	userInstance := GetUserInstance()
	userInstance.SetUser(1, "thegera", "Gerardo Medellin", "thegera4@hotmail.com")
	userInstance.GetUser()
	userInstance.DeleteUser()
	userInstance.GetUser()
}