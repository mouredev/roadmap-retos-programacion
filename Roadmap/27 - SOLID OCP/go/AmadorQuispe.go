package main

import (
	"errors"
	"fmt"
	"math"
)

type ReportServiceBad[T any] struct {
	data T
}

func (rs *ReportServiceBad[T]) ReportGenerator(typeReport string) {
	if typeReport == "PDF" {
		fmt.Println(rs.data)
		fmt.Println("Generando reporte PDF")
	} else if typeReport == "HTML" {
		fmt.Println(rs.data)
		fmt.Println("Generando reporte HTML")
	}
}

// Re factorización para cumplir el OCP
// ReportGenerator, interfaz que define el comportamiento de un generador de reportes
type ReportGenerator interface {
	GenerateReport(data interface{})
}

// PDFReportGenerator, implementación de ReportGenerator para reportes PDF
type PDFReportGenerator struct{}

func (p *PDFReportGenerator) GenerateReport(data interface{}) {
	fmt.Println(data)
	fmt.Println("Generando reporte PDF")
}

// HTMLReportGenerator, implementación de ReportGenerator para reportes HTML
type HTMLReportGenerator struct{}

func (h *HTMLReportGenerator) GenerateReport(data interface{}) {
	fmt.Println(data)
	fmt.Println("Generando reporte HTML")
}

// ReportService usa un generador de reportes para generar reportes
type ReportService struct {
	data      interface{}
	reportGen ReportGenerator
}

func (rs *ReportService) GenerateReport() {
	rs.reportGen.GenerateReport(rs.data)
}

// EXTRA
type Operation interface {
	Apply(num1, num2 float32) (float32, error)
}

// SUMA
type Addition struct{}

func (a *Addition) Apply(num1, num2 float32) (float32, error) {
	return num1 + num2, nil
}

// RESTA
type Subtraction struct{}

func (a *Subtraction) Apply(num1, num2 float32) (float32, error) {
	return num1 - num2, nil
}

// MULTIPLICACIÓN
type Multiplication struct{}

func (a *Multiplication) Apply(num1, num2 float32) (float32, error) {
	return num1 * num2, nil
}

// DIVISIÓN
type Division struct{}

func (a *Division) Apply(num1, num2 float32) (float32, error) {
	if num2 == 0 {
		return 0, errors.New("division by zero")
	}
	return num1 / num2, nil
}

// POTENCIA
type Pow struct{}

func (a *Pow) Apply(num1, num2 float32) (float32, error) {
	return float32(math.Pow(float64(num1), float64(num2))), nil
}

// Calculator usa una operación para calcular un resultado
type Calculator struct{}

func (c *Calculator) Calculate(operation Operation, num1, num2 float32) (float32, error) {
	return operation.Apply(num1, num2)
}

func main() {
	//VIOLA OCP
	reportServiceBad := ReportServiceBad[string]{data: "data de ejemplo bad"}
	reportServiceBad.ReportGenerator("PDF")

	//OCP
	data := "Datos de ejemplo"
	pdfGenerator := &PDFReportGenerator{}
	htmlGenerator := &HTMLReportGenerator{}

	pdfReportService := &ReportService{data: data, reportGen: pdfGenerator}
	htmlReportService := &ReportService{data: data, reportGen: htmlGenerator}

	pdfReportService.GenerateReport()
	htmlReportService.GenerateReport()

	//CALCULATOR
	num1 := float32(10)
	num2 := float32(5)

	calculator := &Calculator{}

	addition := &Addition{}
	subtraction := &Subtraction{}
	multiplication := &Multiplication{}
	division := &Division{}

	result, err := calculator.Calculate(addition, num1, num2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Suma:", result)
	}

	result, err = calculator.Calculate(subtraction, num1, num2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Resta:", result)
	}

	result, err = calculator.Calculate(multiplication, num1, num2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Multiplicación:", result)
	}

	result, err = calculator.Calculate(division, num1, num2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("División:", result)
	}

	//Potencia
	pow := &Pow{}
	result, err = calculator.Calculate(pow, num1, num2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Potencia:", result)
	}
}
