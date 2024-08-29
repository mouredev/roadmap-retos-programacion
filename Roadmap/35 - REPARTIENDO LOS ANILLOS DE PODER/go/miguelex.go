package main

import (
	"fmt"
	"math"
)

func esPrimo(num int) bool {
	if num <= 1 {
		return false
	}
	if num == 2 {
		return true
	}
	if num%2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Sqrt(float64(num))); i += 2 {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func repartirAnillos(totalAnillos int) string {
	if totalAnillos < 4 {
		return "Error: No hay suficientes anillos para cumplir con los requisitos."
	}

	anillosSauron := 1
	totalAnillos -= 1

	mejorDiferencia := int(^uint(0) >> 1) // Máximo entero
	var mejorReparto []int

	for anillosElfos := 1; anillosElfos <= totalAnillos; anillosElfos += 2 {
		for anillosEnanos := 2; anillosEnanos <= totalAnillos; anillosEnanos++ {
			if esPrimo(anillosEnanos) {
				anillosHombres := totalAnillos - anillosElfos - anillosEnanos
				if anillosHombres > 0 && anillosHombres%2 == 0 {
					diferencia := max(anillosElfos, anillosEnanos, anillosHombres) - min(anillosElfos, anillosEnanos, anillosHombres)
					if diferencia < mejorDiferencia {
						mejorDiferencia = diferencia
						mejorReparto = []int{anillosElfos, anillosEnanos, anillosHombres, anillosSauron}
					}
				}
			}
		}
	}

	if mejorReparto != nil {
		return fmt.Sprintf("Reparto exitoso: Elfos = %d, Enanos = %d, Hombres = %d, Sauron = %d", mejorReparto[0], mejorReparto[1], mejorReparto[2], mejorReparto[3])
	} else {
		return "Error: No se encontró una combinación válida para repartir los anillos."
	}
}

func max(nums ...int) int {
	maxNum := nums[0]
	for _, num := range nums {
		if num > maxNum {
			maxNum = num
		}
	}
	return maxNum
}

func min(nums ...int) int {
	minNum := nums[0]
	for _, num := range nums {
		if num < minNum {
			minNum = num
		}
	}
	return minNum
}

func main() {
	var totalAnillos int
	fmt.Print("Ingresa el número total de anillos: ")
	fmt.Scanf("%d", &totalAnillos)

	resultado := repartirAnillos(totalAnillos)
	fmt.Println(resultado)
}
