package main

import (
	"fmt"
	"sync"
)

type Singleton struct {
	value string
}

var (
	instanceA *Singleton
	onceA     sync.Once
)

func GetInstanceA() *Singleton {
	onceA.Do(func() {
		instanceA = &Singleton{value: "initializing..."}
	})
	return instanceA
}

func (s *Singleton) SetValue(value string) {
	s.value = value
}

func (s *Singleton) GetValue() string {
	return s.value
}

/* extra challenge */

type User struct {
	ID       int
	Username string
	Name     string
	Email    string
}

type Session struct {
	user *User
	mu   sync.Mutex
}

var (
	instance *Session
	once     sync.Once
)

func GetInstance() *Session {
	once.Do(func() {
		instance = &Session{}
	})
	return instance
}

func (s *Session) SetUser(user *User) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.user = user
}

func (s *Session) GetUser() *User {
	s.mu.Lock()
	defer s.mu.Unlock()
	return s.user
}

func (s *Session) ClearUser() {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.user = nil
}

func main() {
	s1 := GetInstanceA()
	fmt.Println(s1.GetValue())

	s1.SetValue("new value")

	s2 := GetInstanceA()
	fmt.Println(s2.GetValue())

	fmt.Printf("s1 and s2 are equals: %v\n", s1 == s2)

	/* extra challenge */
	session := GetInstance()

	user := &User{
		ID:       1,
		Username: "qwik-zgheib",
		Name:     "Qwik Zgheib",
		Email:    "qwikzgheib@gmail.com",
	}

	session.SetUser(user)

	retrievedUser := session.GetUser()
	fmt.Printf("User: %v\n", retrievedUser)

	session.ClearUser()

	retrievedUser = session.GetUser()
	fmt.Printf("User after clear: %v\n", retrievedUser)
}
