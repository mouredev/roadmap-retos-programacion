package main

import (
	"fmt"
	"slices"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

/* ------------------------------ FamilyStatus ------------------------------ */

type TFamilyStatus string

const (
	father TFamilyStatus = "father"
	mother TFamilyStatus = "mother"
)

type familyStatus struct {
	Father TFamilyStatus
	Mother TFamilyStatus
}

var FamilyStatus familyStatus = familyStatus{
	Father: father,
	Mother: mother,
}

/* ---------------------------------- UUID ---------------------------------- */

type UUID string

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

/* --------------------------- PersonNotFoundError -------------------------- */

type PersonNotFoundError struct {
	uuid UUID
	_    struct{}
}

func (err *PersonNotFoundError) Error() string {
	return fmt.Sprintf("Person with %s UUID not found", err.uuid)
}

/* --------------------- PersonDoesNotHaveChildrenError --------------------- */

type PersonDoesNotHaveChildrenError struct {
	uuid UUID
	_    struct{}
}

func (err *PersonDoesNotHaveChildrenError) Error() string {
	return fmt.Sprintf("Person with %s UUID does not have a children", err.uuid)
}

/* ---------------------- PersonDoesNotHavePartnerError --------------------- */

type PersonDoesNotHavePartnerError struct {
	uuid UUID
	_    struct{}
}

func (err *PersonDoesNotHavePartnerError) Error() string {
	return fmt.Sprintf("Person with %s UUID does not have a partner", err.uuid)
}

/* ------------------- PersonDoesNotHaveFamilyStatusError ------------------- */

type PersonDoesNotHaveFamilyStatusError struct {
	uuid UUID
	_    struct{}
}

func (err *PersonDoesNotHaveFamilyStatusError) Error() string {
	return fmt.Sprintf("Person with %s UUID does not have a family status", err.uuid)
}

/* ---------------------- PersonDoesNotHaveAFatherError --------------------- */

type PersonDoesNotHaveAFatherError struct {
	uuid UUID
	_    struct{}
}

func (err *PersonDoesNotHaveAFatherError) Error() string {
	return fmt.Sprintf("Person with %s UUID does not have a father", err.uuid)
}

/* ---------------------- PersonDoesNotHaveAMotherError --------------------- */

type PersonDoesNotHaveAMotherError struct {
	uuid UUID
	_    struct{}
}

func (err *PersonDoesNotHaveAMotherError) Error() string {
	return fmt.Sprintf("Person with %s UUID does not have a mother", err.uuid)
}

/* -------------------- FamilyTreeDoesNotHavePeopleError -------------------- */

type FamilyTreeDoesNotHavePeopleError struct{}

func (err *FamilyTreeDoesNotHavePeopleError) Error() string {
	return fmt.Sprintf("Family tree does not have people")
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* --------------------------------- Person --------------------------------- */

type IPerson interface {
	GetName() string
	GetUUID() UUID
	GetChildren() ([]IPerson, error)
	GetPartner() (IPerson, error)
	GetFamilyStatus() (TFamilyStatus, error)
	GetFather() (IPerson, error)
	GetMother() (IPerson, error)
	SetFamilyStatus(familyStatus TFamilyStatus)
	SetFather(father IPerson)
	SetMother(mother IPerson)
	SetPartner(partner IPerson)
	AddChildren(children ...IPerson)
	RemoveChildren(children ...UUID)
}

type person struct {
	name         string
	uuid         UUID
	children     []IPerson
	partner      IPerson
	familyStatus TFamilyStatus
	father       IPerson
	mother       IPerson
	_            struct{}
}

func NewPerson(name string, uuid UUID) IPerson {
	var sanitizedName string = strings.TrimSpace(name)
	var sanitizedUUID UUID = UUID(strings.TrimSpace(string(uuid)))

	if sanitizedName == "" {
		panic(
			fmt.Sprintf(
				"`name` parameter of `NewPerson` function must not be empty, received '%s' as `name`",
				name,
			),
		)
	} else if sanitizedUUID == "" {
		panic(
			fmt.Sprintf(
				"`uuid` parameter of `NewPerson` function must not be empty, received '%s' as `uuid`",
				uuid,
			))
	}

	var person person = person{name: sanitizedName, uuid: sanitizedUUID}
	return &person
}

func (p *person) GetName() string {
	return p.name
}

func (p *person) GetUUID() UUID {
	return p.uuid
}

func (p *person) GetChildren() ([]IPerson, error) {
	var children []IPerson = p.children
	if len(children) < 1 {
		return children, &PersonDoesNotHaveChildrenError{uuid: p.uuid}
	}

	return children, nil
}

func (p *person) GetPartner() (IPerson, error) {
	var partner IPerson = p.partner
	if partner == nil {
		return partner, &PersonDoesNotHavePartnerError{uuid: p.uuid}
	}

	return p.partner, nil
}

func (p *person) GetFamilyStatus() (TFamilyStatus, error) {
	var familyStatus TFamilyStatus = p.familyStatus
	if familyStatus == "" {
		return familyStatus, &PersonDoesNotHaveFamilyStatusError{uuid: p.uuid}
	}

	return familyStatus, nil
}

func (p *person) GetFather() (IPerson, error) {
	var father IPerson = p.father
	if father == nil {
		return father, &PersonDoesNotHaveAFatherError{uuid: p.uuid}
	}

	return father, nil
}

func (p *person) GetMother() (IPerson, error) {
	var mother IPerson = p.mother
	if mother == nil {
		return mother, &PersonDoesNotHaveAMotherError{uuid: p.uuid}
	}

	return mother, nil
}

func (p *person) SetFamilyStatus(familyStatus TFamilyStatus) {
	p.familyStatus = familyStatus
}

func (p *person) SetFather(father IPerson) {
	p.father = father
	father.AddChildren(p)
}

func (p *person) SetMother(mother IPerson) {
	p.mother = mother
	mother.AddChildren(p)
}

func (p *person) SetPartner(partner IPerson) {
	if p.partner == partner {
		return
	}

	p.partner = partner
	partner.SetPartner(p)
}

func (p *person) AddChildren(children ...IPerson) {
	p.children = append(p.children, children...)
}

func (p *person) RemoveChildren(children ...UUID) {
	for _, uuid := range children {
		p.children = slices.DeleteFunc(p.children, func(c IPerson) bool {
			var cUUID UUID = c.GetUUID()
			return uuid == cUUID
		})
	}
}

/* ------------------------------- FamilyTree ------------------------------- */

type IFamilyTree interface {
	GetPerson(uuid UUID) (IPerson, error)
	GetPeople() ([]IPerson, error)
	AddPeople(people ...IPerson)
	RemovePeople(people ...UUID)
	PeopleToString() string
}

type familyTree struct {
	people []IPerson
	_      struct{}
}

func NewFamilyTree() IFamilyTree {
	var familyTree familyTree = familyTree{}
	return &familyTree
}

func (ft *familyTree) GetPerson(uuid UUID) (IPerson, error) {
	people, err := ft.GetPeople()
	if err != nil {
		return nil, err
	}

	for _, person := range people {
		var pUUID UUID = person.GetUUID()

		if pUUID == uuid {
			return person, nil
		}
	}

	return nil, &PersonNotFoundError{uuid: uuid}
}

func (ft *familyTree) GetPeople() ([]IPerson, error) {
	var people []IPerson = ft.people
	if len(people) < 1 {
		return people, &FamilyTreeDoesNotHavePeopleError{}
	}

	return people, nil
}

func (ft *familyTree) AddPeople(people ...IPerson) {
	ft.people = append(ft.people, people...)
}

func (ft *familyTree) RemovePeople(people ...UUID) {
	for _, uuid := range people {
		ft.people = slices.DeleteFunc(ft.people, func(p IPerson) bool {
			var pUUID UUID = p.GetUUID()
			return uuid == pUUID
		})
	}
}

func (ft *familyTree) PeopleToString() string {
	var peopleStr string

	peopleStr += fmt.Sprintf("+%s+\n", strings.Repeat("-", 177))

	peopleStr += fmt.Sprintf("| %-20s ", "name")
	peopleStr += fmt.Sprintf("| %-64s ", "children")
	peopleStr += fmt.Sprintf("| %-16s ", "familyStatus")
	peopleStr += fmt.Sprintf("| %-20s ", "father")
	peopleStr += fmt.Sprintf("| %-20s ", "mother")
	peopleStr += fmt.Sprintf("| %-20s |\n", "partner")

	for _, p := range ft.people {
		peopleStr += fmt.Sprintf("-%s-\n", strings.Repeat("-", 177))

		var name string = p.GetName()
		peopleStr += fmt.Sprintf("| %-20s ", name)

		children, err := p.GetChildren()
		if err == nil {
			if len(children) > 1 {
				var aux []string
				for _, child := range children {
					aux = append(aux, child.GetName())
				}

				var childrenStr string
				childrenStr = strings.Join(aux[:len(aux)-1], ", ")
				childrenStr += fmt.Sprintf(", and %s.", aux[len(aux)-1])
				peopleStr += fmt.Sprintf("| %-64s ", childrenStr)
			} else {
				peopleStr += fmt.Sprintf("| %-64s ", children[0].GetName() + ".")
			}
		} else {
			peopleStr += fmt.Sprintf("| %-64s ", "nil")
		}

		familyStatus, err := p.GetFamilyStatus()
		if err == nil {
			peopleStr += fmt.Sprintf("| %-16s ", familyStatus)
		} else {
			peopleStr += fmt.Sprintf("| %-16s ", "nil")
		}

		father, err := p.GetFather()
		if err == nil {
			peopleStr += fmt.Sprintf("| %-20s ", father.GetName())
		} else {
			peopleStr += fmt.Sprintf("| %-20s ", "nil")
		}

		mother, err := p.GetMother()
		if err == nil {
			peopleStr += fmt.Sprintf("| %-20s ", mother.GetName())
		} else {
			peopleStr += fmt.Sprintf("| %-20s ", "nil")
		}

		partner, err := p.GetPartner()
		if err == nil {
			peopleStr += fmt.Sprintf("| %-20s |\n", partner.GetName())
		} else {
			peopleStr += fmt.Sprintf("| %-20s |\n", "nil")
		}

	}

	peopleStr += fmt.Sprintf("+%s+\n", strings.Repeat("-", 177))

	return peopleStr
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var jaehaerysTargaryen IPerson = NewPerson("Jaehaerys Targaryen", "1")
	jaehaerysTargaryen.SetFamilyStatus(FamilyStatus.Father)

	var alysanneTargaryen IPerson = NewPerson("Alysanne Targaryen", "2")
	alysanneTargaryen.SetPartner(jaehaerysTargaryen)
	alysanneTargaryen.SetFamilyStatus(FamilyStatus.Mother)

	var jocelynBaratheon IPerson = NewPerson("Jocelyn Baratheon", "3")
	jocelynBaratheon.SetFamilyStatus(FamilyStatus.Mother)

	var aemonTargaryen IPerson = NewPerson("Aemon Targaryen", "4")
	aemonTargaryen.SetPartner(jocelynBaratheon)
	aemonTargaryen.SetFamilyStatus(FamilyStatus.Father)
	aemonTargaryen.SetFather(jaehaerysTargaryen)
	aemonTargaryen.SetMother(alysanneTargaryen)

	var baelonTargaryen IPerson = NewPerson("Baelon Targaryen", "5")
	baelonTargaryen.SetFamilyStatus(FamilyStatus.Mother)
	baelonTargaryen.SetFather(jaehaerysTargaryen)
	baelonTargaryen.SetMother(alysanneTargaryen)

	var alyssaTargaryen IPerson = NewPerson("Alyssa Targaryen", "6")
	alyssaTargaryen.SetPartner(baelonTargaryen)
	alyssaTargaryen.SetFamilyStatus(FamilyStatus.Mother)
	alyssaTargaryen.SetFather(jaehaerysTargaryen)
	alyssaTargaryen.SetMother(alysanneTargaryen)

	var lyonelStrong IPerson = NewPerson("Lyonel Strong", "7")
	lyonelStrong.SetFamilyStatus(FamilyStatus.Father)

	var vaemondValaryon IPerson = NewPerson("Vaemond Valaryon", "8")

	var corlysVelaryon IPerson = NewPerson("Corlys Velaryon", "9")
	corlysVelaryon.SetFamilyStatus(FamilyStatus.Father)

	var rhaenysTargaryen IPerson = NewPerson("Rhaenys Targaryen", "10")
	rhaenysTargaryen.SetFamilyStatus(FamilyStatus.Mother)
	rhaenysTargaryen.SetPartner(corlysVelaryon)
	rhaenysTargaryen.SetFather(aemonTargaryen)
	rhaenysTargaryen.SetMother(jocelynBaratheon)

	var rheaRoyce IPerson = NewPerson("Rhea Royce", "11")
	rheaRoyce.SetFamilyStatus(FamilyStatus.Mother)

	var daemonTargaryen IPerson = NewPerson("Daemon Targaryen", "12")
	daemonTargaryen.SetFamilyStatus(FamilyStatus.Father)
	daemonTargaryen.SetPartner(rheaRoyce)
	daemonTargaryen.SetFather(baelonTargaryen)
	daemonTargaryen.SetMother(alyssaTargaryen)

	var aemmaArryn IPerson = NewPerson("Aemma Arryn", "13")
	aemmaArryn.SetFamilyStatus(FamilyStatus.Mother)

	var viserysTargaryen IPerson = NewPerson("Viserys Targaryen", "14")
	viserysTargaryen.SetFamilyStatus(FamilyStatus.Father)
	viserysTargaryen.SetPartner(aemmaArryn)
	viserysTargaryen.SetFather(baelonTargaryen)
	viserysTargaryen.SetMother(alyssaTargaryen)

	var ottoHightower IPerson = NewPerson("Otto Hightower", "15")
	ottoHightower.SetFamilyStatus(FamilyStatus.Father)

	var hobertHightower IPerson = NewPerson("Hobert Hightower", "16")

	var familyTree IFamilyTree = NewFamilyTree()

	familyTree.AddPeople(
		jaehaerysTargaryen,
		alysanneTargaryen,
		jocelynBaratheon,
		aemonTargaryen,
		baelonTargaryen,
		alyssaTargaryen,
		lyonelStrong,
		vaemondValaryon,
		corlysVelaryon,
		rhaenysTargaryen,
		rheaRoyce,
		daemonTargaryen,
		aemmaArryn,
		viserysTargaryen,
		ottoHightower,
		hobertHightower,
	)

	fmt.Printf("House of Dragon family tree from the first row to the third one...\n\n")

	fmt.Print(familyTree.PeopleToString())

	fmt.Println("\n> House of Dragon official family tree: https://www.hbo.com/house-of-the-dragon/character-guide")
}
