package main

import (
	"testing"
)

func Addition(num1, num2 uint8) uint8 {
	return num1 + num2
}

func TestAddition(t *testing.T) {
	var expected uint8 = 5

	got := Addition(3, 2)
	if got != expected {
		t.Errorf("Expected: %v, got: %v", expected, got)
	}
}
