// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"sort"
	"strings"
	"time"
)

type Participant struct{ Name, Country string }
type Event struct {
	Name         string
	Participants []Participant
}
type CountryMedals struct {
	Country        string
	Gold, Silver, Bronze int
}

func (c CountryMedals) Total() int { return c.Gold + c.Silver + c.Bronze }

var events []Event
var medalTable = map[string]*CountryMedals{}
var reader = bufio.NewReader(os.Stdin)

func readLine(prompt string) string {
	fmt.Print(prompt)
	line, _ := reader.ReadString('\n')
	return strings.TrimSpace(line)
}

func registerEvent() {
	name := readLine("Nombre del evento: ")
	if name == "" { fmt.Println("Nombre invalido."); return }
	for _, ev := range events {
		if strings.EqualFold(ev.Name, name) { fmt.Printf("'%s' ya existe.\n", name); return }
	}
	events = append(events, Event{Name: name})
	fmt.Printf("Evento '%s' registrado.\n", name)
}

func registerParticipant() {
	if len(events) == 0 { fmt.Println("No hay eventos."); return }
	for i, ev := range events { fmt.Printf("  %d. %s\n", i+1, ev.Name) }
	var idx int
	fmt.Sscanf(readLine("Selecciona número: "), "%d", &idx)
	if idx < 1 || idx > len(events) { fmt.Println("Invalido."); return }
	ev := &events[idx-1]
	pname := readLine("Nombre: ")
	country := readLine("País: ")
	ev.Participants = append(ev.Participants, Participant{pname, country})
	fmt.Printf("'%s (%s)' añadido a '%s'.\n", pname, country, ev.Name)
}

func simulateEvents() {
	if len(events) == 0 { fmt.Println("No hay eventos."); return }
	rng := rand.New(rand.NewSource(time.Now().UnixNano()))
	for _, ev := range events {
		fmt.Printf("\n=== Simulando: %s ===\n", ev.Name)
		if len(ev.Participants) < 3 { fmt.Printf("  Necesita >=3 participantes. Saltando.\n"); continue }
		s := make([]Participant, len(ev.Participants))
		copy(s, ev.Participants)
		rng.Shuffle(len(s), func(i, j int) { s[i], s[j] = s[j], s[i] })
		fmt.Printf("  Oro:    %s (%s)\n", s[0].Name, s[0].Country)
		fmt.Printf("  Plata:  %s (%s)\n", s[1].Name, s[1].Country)
		fmt.Printf("  Bronce: %s (%s)\n", s[2].Name, s[2].Country)
		addMedal(s[0].Country, "gold"); addMedal(s[1].Country, "silver"); addMedal(s[2].Country, "bronze")
	}
}

func addMedal(country, t string) {
	if _, ok := medalTable[country]; !ok { medalTable[country] = &CountryMedals{Country: country} }
	switch t {
	case "gold": medalTable[country].Gold++
	case "silver": medalTable[country].Silver++
	case "bronze": medalTable[country].Bronze++
	}
}

func showReport() {
	fmt.Println("\n== INFORME FINAL ==")
	if len(medalTable) == 0 { fmt.Println("Sin resultados aun."); return }
	var r []*CountryMedals
	for _, cm := range medalTable { r = append(r, cm) }
	sort.Slice(r, func(i, j int) bool {
		if r[i].Gold != r[j].Gold { return r[i].Gold > r[j].Gold }
		if r[i].Silver != r[j].Silver { return r[i].Silver > r[j].Silver }
		return r[i].Bronze > r[j].Bronze
	})
	for i, c := range r {
		fmt.Printf("%d. %-20s Oro:%d Plata:%d Bronce:%d Total:%d\n", i+1, c.Country, c.Gold, c.Silver, c.Bronze, c.Total())
	}
}

func main() {
	for {
		fmt.Println("\n====== SIMULADOR JJOO ======")
		fmt.Println("1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir")
		switch readLine("Opción: ") {
		case "1": registerEvent()
		case "2": registerParticipant()
		case "3": simulateEvents()
		case "4": showReport()
		case "5": fmt.Println("Hasta luego!"); return
		default: fmt.Println("Invalido.")
		}
	}
}
