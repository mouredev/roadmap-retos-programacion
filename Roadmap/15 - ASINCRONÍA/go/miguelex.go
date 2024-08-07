package main

import (
	"fmt"
	"time"
)

func asyncTask(name string, seconds int) <-chan struct{} {
	done := make(chan struct{})
	go func() {
		fmt.Printf("Comienza la función %s. Duración de %d segundos. Hora de comienzo %s\n", name, seconds, time.Now().Format("15:04:05"))
		time.Sleep(time.Duration(seconds) * time.Second)
		fmt.Printf("Finaliza la función %s. Hora de finalización %s\n", name, time.Now().Format("15:04:05"))
		close(done)
	}()
	return done
}

func main() {

	done := asyncTask("Test 1", 5)
	<-done

	// Extra
	doneC := asyncTask("C", 3)
	doneB := asyncTask("B", 2)
	doneA := asyncTask("A", 1)
	<-doneC
	<-doneB
	<-doneA
	doneD := asyncTask("D", 1)
	<-doneD
}
