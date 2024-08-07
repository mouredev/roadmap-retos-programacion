package main

import (
	"fmt"
	"sync"
)

type Singleton struct {
	name string
}

var single *Singleton
var onceExample sync.Once

func getInstanceSingleton() *Singleton {
	onceExample.Do(func() {
		single = &Singleton{name: "Jhon"}
	})
	return single
}

func (single *Singleton) GetName() string {
	return single.name
}

func (single *Singleton) SetName(name string) {
	single.name = name
}

// ************************************ RETO ************************************************* //

type User struct {
	ID       int
	Name     string
	Username string
	Email    string
}

type session struct {
	user *User
	sync.Mutex
}

var (
	instance *session
	once     sync.Once
)

func getSessionInstance() *session {
	once.Do(func() {
		instance = &session{}
	})
	return instance
}

func (s *session) SetUser(u *User) {
	s.Lock()
	defer s.Unlock()
	s.user = u
}

func (s *session) GetUser() *User {
	s.Lock()
	defer s.Unlock()
	return s.user
}

func (s *session) ClearSession() {
	s.Lock()
	defer s.Unlock()
	s.user = nil
}

func main() {

	session := getSessionInstance()

	user := &User{
		ID:       1,
		Name:     "John Doe",
		Username: "johndoe",
		Email:    "john.doe@example.com",
	}
	session.SetUser(user)

	currentUser := session.GetUser()
	fmt.Println("User ID:", currentUser.ID)
	fmt.Println("Name:", currentUser.Name)
	fmt.Println("Username:", currentUser.Username)
	fmt.Println("Email:", currentUser.Email)

	// Borrar los datos de la sesión
	session.ClearSession()

	currentUser = session.GetUser()
	if currentUser == nil {
		fmt.Println("La sesión ha sido borrada.")
	}
}
