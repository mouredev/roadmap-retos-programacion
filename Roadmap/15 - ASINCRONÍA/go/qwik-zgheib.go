package main

import (
	"fmt"
	"sync"
	"time"
)

type Task interface {
	Run()
	GetName() string
}

type NamedTask struct {
	Name     string
	Duration time.Duration
}

func NewNamedTask(name string, duration time.Duration) *NamedTask {
	return &NamedTask{Name: name, Duration: duration}
}

func (t *NamedTask) Run() {
	startTime := time.Now()
	fmt.Printf("Task %s started at %s and will run for %d seconds\n", t.Name, startTime.Format("15:04:05"), t.Duration)
	time.Sleep(t.Duration * time.Second)
	endTime := time.Now()
	fmt.Printf("Task %s ended at %s\n", t.Name, endTime.Format("15:04:05"))
}

func (t *NamedTask) GetName() string {
	return t.Name
}

type AsyncExecutor struct {
	tasks []Task
	wg    *sync.WaitGroup
}

func NewAsyncExecutor() *AsyncExecutor {
	return &AsyncExecutor{wg: &sync.WaitGroup{}}
}

func (ae *AsyncExecutor) AddTask(task Task) {
	ae.tasks = append(ae.tasks, task)
}

func (ae *AsyncExecutor) RunAllTasks() {
	for _, task := range ae.tasks {
		ae.wg.Add(1)
		go func(t Task) {
			defer ae.wg.Done()
			t.Run()
		}(task)
	}
}

func (ae *AsyncExecutor) Wait() {
	ae.wg.Wait()
}

func main() {
	taskC := NewNamedTask("C", 3)
	taskB := NewNamedTask("B", 2)
	taskA := NewNamedTask("A", 1)
	taskD := NewNamedTask("D", 1)

	executor := NewAsyncExecutor()

	executor.AddTask(taskC)
	executor.AddTask(taskB)
	executor.AddTask(taskA)

	executor.RunAllTasks()

	executor.Wait()

	taskD.Run()
}
