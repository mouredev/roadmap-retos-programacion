package main

// La interfaz Vehicle define el comportamiento de un vehículo
// "Clase" Vehicle
type Vehicle interface {
	Accelerate()
	Brake()
}

// Car implementa la interfaz Vehicle
type Car struct{}

func (c Car) Accelerate() {
	println("Acelerando carro")
}

func (c Car) Brake() {
	println("Frenando carro")
}

// Boat implementa la interfaz Vehicle
type Boat struct{}

func (b Boat) Accelerate() {
	println("Acelerando bote")
}

func (b Boat) Brake() {
	println("Frenando bote")
}

// Boat implementa una funcion para Unmoor, por lo tanto estamos agregando un objeto S sin afectar al comportamiento
func (b Boat) Unmoor() {
	println("Desamarrando bote")
}

// DriveVehicle acelera y frena un vehículo
func DriveVehicle(v Vehicle) {
	v.Accelerate()
	v.Brake()
}

func main() {
	car := Car{}
	boat := Boat{}

	DriveVehicle(car)
	DriveVehicle(boat)

	// Llamados particulares
	boat.Unmoor()
}
