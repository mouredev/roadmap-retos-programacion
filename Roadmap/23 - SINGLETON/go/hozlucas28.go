package main

import (
	"fmt"
	"sync"
)

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* --------------------------------- Counter -------------------------------- */

type counter struct {
	__count int
}

var counterMutex *sync.Mutex = &sync.Mutex{}

var counterInstance *counter

func Counter() *counter {
	if counterInstance == nil {
		counterMutex.Lock()
		defer counterMutex.Unlock()

		if counterInstance == nil {
			counterInstance = &counter{}
		}
	}

	return counterInstance
}

func (counter *counter) getCount() int {
	return counter.__count
}

func (counter *counter) decrement() *counter {
	counter.__count -= 1
	return counter
}

func (counter *counter) increment() *counter {
	counter.__count += 1
	return counter
}

/* --------------------------------- Session -------------------------------- */

type session struct {
	__email    string
	__id       string
	__name     string
	__userName string
}

var sessionMutex *sync.Mutex = &sync.Mutex{}

var sessionInstance *session

type SessionParams struct {
	email    string
	id       string
	name     string
	userName string
}

func Session(params SessionParams) *session {

	if sessionInstance == nil {
		sessionMutex.Lock()
		defer sessionMutex.Unlock()

		if sessionInstance == nil {
			sessionInstance = &session{
				__email:    params.email,
				__id:       params.id,
				__name:     params.name,
				__userName: params.userName,
			}
		}
	}

	return sessionInstance
}

func (session *session) getEmail() string {
	return session.__email
}

func (session *session) getId() string {
	return session.__id
}

func (session *session) getName() string {
	return session.__name
}

func (session *session) getUserName() string {
	return session.__userName
}

func (session *session) setEmail(newEmail string) *session {
	session.__email = newEmail
	return session
}

func (session *session) setId(newId string) *session {
	session.__id = newId
	return session
}

func (session *session) setName(newName string) *session {
	session.__name = newName
	return session
}

func (session *session) setUserName(newUserName string) *session {
	session.__userName = newUserName
	return session
}

func (session *session) deleteData() *session {
	session.__email = ""
	session.__id = ""
	session.__name = ""
	session.__userName = ""

	return session
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Singleton pattern...
	*/

	fmt.Println("Singleton pattern...")

	var counter01 *counter = Counter()
	var counter02 *counter = Counter()

	fmt.Printf("\nAre `counter01` and `counter02` the same instance of `counter` class? %t\n", counter01 == counter02)

	fmt.Println("\nMethod call of `counter01` instance...")

	counter01.increment().increment().increment()
	fmt.Println("\ncounter01.increment().increment().increment()")

	fmt.Printf("\nCount attribute of `counter01` instance --> %d\n", counter01.getCount())

	fmt.Println("\nMethod call of `counter02` instance...")

	counter02.decrement()
	fmt.Println("\ncounter02.decrement()")

	fmt.Printf("\nCount attribute of `counter02` instance --> %d\n", counter02.getCount())

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var userSession *session = Session(SessionParams{
		email:    "marianogonzales@gmail.com",
		id:       "11U-287O-25ZK",
		name:     "Mariano",
		userName: "MarianoPro360",
	})

	fmt.Printf("\nUser session data: %s %s %s %s\n", userSession.getId(), userSession.getName(), userSession.getUserName(), userSession.getEmail())

	userSession.deleteData()
	fmt.Println("\nUser session data deleted!")

	fmt.Printf("\nUser session data: %s %s %s %s", userSession.getId(), userSession.getName(), userSession.getUserName(), userSession.getEmail())
}
