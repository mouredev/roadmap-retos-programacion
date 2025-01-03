package main

import (
	"fmt"
	"strings"
)

type TextStorage struct {
	content string
}

func (ts *TextStorage) AddText(text string) {
	ts.content += text + "\n"
}

func (ts *TextStorage) GetText() string {
	return ts.content
}

type TextFormatter struct{}

func (tf *TextFormatter) UpperCase(text string) string {
	return strings.ToUpper(text)
}

func (tf *TextFormatter) LowerCase(text string) string {
	return strings.ToLower(text)
}

func main() {
	storage := &TextStorage{}
	formatter := &TextFormatter{}

	storage.AddText("Hello, Go")
	storage.AddText("This is a example")

	fmt.Println("Text:")
	fmt.Println(storage.GetText())

	fmt.Println("Text on uppercase:")
	fmt.Println(formatter.UpperCase(storage.GetText()))

	fmt.Println("Text on lowercase:")
	fmt.Println(formatter.LowerCase(storage.GetText()))
}
