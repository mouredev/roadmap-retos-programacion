package main

import (
	"fmt"
	"sync"
)

type User struct {
	Name  string
	Id    int
	Email string
}

var einMal sync.Once
var UserUser *User

func GetI() *User {
	einMal.Do(func() {
		UserUser = &User{"", 0, ""}
	})
	return UserUser
}

func (u *User) SetUser(name string, id int, email string) {
	u.Name = name
	u.Id = id
	u.Email = email

}

func (u *User) GetUser() string {
	if u != nil {
		return fmt.Sprintf(" Name %v, Id %v, Email %v", u.Name, u.Id, u.Email)
	}
	return "User is Nil"

}

func (u *User) DeleteUser() {
	u.Name = ""
	u.Id = 0
	u.Email = ""
}

func main() {
	fmt.Println(("Singleton"))

	user1 := GetI()
	user2 := GetI()
	user1.SetUser("Periko", 10001, "e@gmail.com")

	fmt.Println(user1.GetUser())
	fmt.Println(user2.GetUser())
	user3 := GetI()
	user3.DeleteUser()
	fmt.Println(user1.GetUser())
	fmt.Println(user2.GetUser())
	fmt.Println(user3.GetUser())
}
