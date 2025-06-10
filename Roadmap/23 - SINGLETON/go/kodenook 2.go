package main

import (
	"fmt"
	"sync"
)

type Singleton struct {
	data string
}

var instancia *Singleton

var once sync.Once

func GetInstance() *Singleton {
	once.Do(func() {
		instancia = &Singleton{data: "Data example"}
	})
	return instancia
}

func main() {

	singleton := GetInstance()
	fmt.Println(singleton.data)

	other := GetInstance()
	fmt.Println(other.data)

	singleton.data = "New data"

	fmt.Println(other.data)
}
