package main

import "fmt"

func main() {
	var u User = User{"name", "last_name"}
	u.SetFirstName("name2")
	u.FirstName = "name3"
	u.SetLastName("last_name2")
	fmt.Println(u)
	fmt.Println(u.LastName)
	fmt.Println(u.GetFirstName())
}

type User struct {
	FirstName string
	LastName  string
}

func (u *User) SetFirstName(firstName string) {
	u.FirstName = firstName
}

func (u *User) SetLastName(lastName string) {
	u.LastName = lastName
}

func (u *User) GetFirstName() string {
	return u.FirstName
}
