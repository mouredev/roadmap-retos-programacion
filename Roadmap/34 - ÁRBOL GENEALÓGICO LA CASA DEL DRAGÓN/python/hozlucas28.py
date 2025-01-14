# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-many-arguments

from abc import ABCMeta, abstractmethod
from typing import Literal
from uuid import UUID, uuid4


# ---------------------------------------------------------------------------- #
#                                     TYPES                                    #
# ---------------------------------------------------------------------------- #

type FamilyStatus = Literal["father", "mother"]


# ---------------------------------------------------------------------------- #
#                                  EXCEPTIONS                                  #
# ---------------------------------------------------------------------------- #


class FamilyTreeHasNotPeopleException(Exception):
    def __init__(self) -> None:
        super().__init__("Family tree does not have people")


class PersonNotFoundException(Exception):
    def __init__(self, *, uuid: UUID) -> None:
        super().__init__(f"Person with {uuid} UUID not found")


# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #


class AbcPerson(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def uuid(self) -> UUID:
        pass

    @property
    @abstractmethod
    def children(self) -> "list[AbcPerson] | None":
        pass

    @property
    @abstractmethod
    def partner(self) -> "AbcPerson | None":
        pass

    @property
    @abstractmethod
    def family_status(self) -> FamilyStatus | None:
        pass

    @property
    @abstractmethod
    def father(self) -> "AbcPerson | None":
        pass

    @property
    @abstractmethod
    def mother(self) -> "AbcPerson | None":
        pass

    @partner.setter
    def partner(self, partner: "AbcPerson") -> None:
        pass

    @abstractmethod
    def add_children(self, *children: "AbcPerson") -> None:
        pass

    @abstractmethod
    def remove_children(self, *children: UUID) -> None:
        pass


class Person(AbcPerson):
    __name: str
    __uuid: UUID
    __children: list[AbcPerson] | None
    __partner: AbcPerson | None
    __family_status: FamilyStatus | None
    __father: AbcPerson | None
    __mother: AbcPerson | None

    def __init__(
        self,
        *,
        name: str,
        uuid: UUID,
        children: list[AbcPerson] | None = None,
        partner: AbcPerson | None = None,
        familyStatus: FamilyStatus | None = None,
        father: AbcPerson | None = None,
        mother: AbcPerson | None = None,
    ) -> None:
        if partner is not None:
            partner.partner = self

        if father is not None:
            father.add_children(self)

        if mother is not None:
            mother.add_children(self)

        self.__name = name
        self.__uuid = uuid
        self.__children = children
        self.__partner = partner
        self.__family_status = familyStatus
        self.__father = father
        self.__mother = mother

    @property
    def name(self) -> str:
        return self.__name

    @property
    def uuid(self) -> UUID:
        return self.__uuid

    @property
    def children(self) -> "list[AbcPerson] | None":
        return self.__children

    @property
    def partner(self) -> "AbcPerson | None":
        return self.__partner

    @property
    def family_status(self) -> FamilyStatus | None:
        return self.__family_status

    @property
    def father(self) -> "AbcPerson | None":
        return self.__father

    @property
    def mother(self) -> "AbcPerson | None":
        return self.__mother

    @partner.setter
    def partner(self, partner: "AbcPerson") -> None:
        self.__partner = partner

    def add_children(self, *children: "AbcPerson") -> None:
        if self.__children is None:
            self.__children = [*children]
        else:
            self.__children.append(*children)

    def remove_children(self, *children: UUID) -> None:
        if self.__children is None:
            return

        self.__children = list(
            filter(
                lambda person: person.uuid not in children,
                self.__children,
            )
        )


# -------------------------------- FamilyTree -------------------------------- #


class AbcFamilyTree(metaclass=ABCMeta):
    @property
    @abstractmethod
    def people(self) -> list[AbcPerson] | None:
        pass

    @abstractmethod
    def get_person(self, *, uuid: UUID) -> AbcPerson:
        pass

    @abstractmethod
    def add_people(self, *people: AbcPerson) -> None:
        pass

    @abstractmethod
    def remove_people(self, *people: UUID) -> None:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class FamilyTree(AbcFamilyTree):
    __people: list[AbcPerson] | None

    def __init__(self, *, people: list[AbcPerson] | None = None) -> None:
        self.__people = people

    @property
    def people(self) -> list[AbcPerson] | None:
        return self.__people

    def get_person(self, *, uuid: UUID) -> AbcPerson:
        if self.__people is None:
            raise FamilyTreeHasNotPeopleException()

        for _person in self.__people:
            if _person.uuid == uuid:
                return _person

        raise PersonNotFoundException(uuid=uuid)

    def add_people(self, *people: AbcPerson) -> None:
        if self.__people is None:
            self.__people = [*people]
        else:
            self.__people.append(*people)

    def remove_people(self, *people_uuids: UUID) -> None:
        if self.__people is None:
            raise FamilyTreeHasNotPeopleException()

        self.__people = list(
            filter(
                lambda person: person.uuid not in people_uuids,
                self.__people,
            )
        )

    def __repr__(self) -> str:
        if self.__people is None:
            raise FamilyTreeHasNotPeopleException()

        _repr: list[str] = [
            f"|-{''.center(20, '-')}-|-"
            f"{'-'.center(64, '-')}-|-"
            f"{'-'.center(16, '-')}-|-"
            f"{'-'.center(20, '-')}-|-"
            f"{'-'.center(20, '-')}-|-"
            f"{'-'.center(20, '-')}-|",
            f"| {'name'.center(20)} | "
            f"{'children'.center(64)} | "
            f"{'family_status'.center(16)} | "
            f"{'father'.center(20)} | "
            f"{'mother'.center(20)} | "
            f"{'partner'.center(20)} |",
            f"|-{''.center(20, '-')}-|-"
            f"{'-'.center(64, '-')}-|-"
            f"{'-'.center(16, '-')}-|-"
            f"{'-'.center(20, '-')}-|-"
            f"{'-'.center(20, '-')}-|-"
            f"{'-'.center(20, '-')}-|",
        ]

        for person in self.__people:
            name: str = person.name
            family_status: str = (
                person.family_status if person.family_status is not None else "None"
            )
            father: str = person.father.name if person.father is not None else "None"
            mother: str = person.mother.name if person.mother is not None else "None"
            partner: str = person.partner.name if person.partner is not None else "None"

            children: str = "None"
            if person.children is not None:
                children = ""
                for j, child in enumerate(iterable=person.children):
                    if j == 0:
                        children = (
                            f"{child.name}." if len(person.children) < 2 else child.name
                        )
                    elif j == len(person.children) - 1:
                        children += f", and {child.name}."
                    else:
                        children += f", {child.name}"

            _repr.append(
                f"| {name.ljust(20)} | "
                f"{children.ljust(64)} | "
                f"{family_status.ljust(16)} | "
                f"{father.ljust(20)} | "
                f"{mother.ljust(20)} | "
                f"{partner.ljust(20)} |"
                f"\n|-{''.center(20, '-')}-|-"
                f"{'-'.center(64, '-')}-|-"
                f"{'-'.center(16, '-')}-|-"
                f"{'-'.center(20, '-')}-|-"
                f"{'-'.center(20, '-')}-|-"
                f"{'-'.center(20, '-')}-|",
            )

        return "\n".join(_repr)


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


jaehaerysTargaryen: Person = Person(
    name="Jaehaerys Targaryen",
    uuid=uuid4(),
    familyStatus="father",
)

alysanneTargaryen: Person = Person(
    name="Alysanne Targaryen",
    uuid=uuid4(),
    partner=jaehaerysTargaryen,
    familyStatus="mother",
)

jocelynBaratheon: Person = Person(
    name="Jocelyn Baratheon",
    uuid=uuid4(),
    familyStatus="mother",
)

aemonTargaryen: Person = Person(
    name="Aemon Targaryen",
    uuid=uuid4(),
    partner=jocelynBaratheon,
    familyStatus="father",
    father=jaehaerysTargaryen,
    mother=alysanneTargaryen,
)

baelonTargaryen: Person = Person(
    name="Baelon Targaryen",
    uuid=uuid4(),
    familyStatus="mother",
    father=jaehaerysTargaryen,
    mother=alysanneTargaryen,
)

alyssaTargaryen: Person = Person(
    name="Alyssa Targaryen",
    uuid=uuid4(),
    partner=baelonTargaryen,
    familyStatus="mother",
    father=jaehaerysTargaryen,
    mother=alysanneTargaryen,
)

lyonelStrong: Person = Person(
    name="Lyonel Strong",
    uuid=uuid4(),
    familyStatus="father",
)

vaemondValaryon: Person = Person(
    name="Vaemond Valaryon",
    uuid=uuid4(),
)

corlysVelaryon: Person = Person(
    name="Corlys Velaryon",
    uuid=uuid4(),
    familyStatus="father",
)

rhaenysTargaryen: Person = Person(
    name="Rhaenys Targaryen",
    uuid=uuid4(),
    familyStatus="mother",
    partner=corlysVelaryon,
    father=aemonTargaryen,
    mother=jocelynBaratheon,
)

rheaRoyce: Person = Person(
    name="Rhea Royce",
    uuid=uuid4(),
    familyStatus="mother",
)

daemonTargaryen: Person = Person(
    name="Daemon Targaryen",
    uuid=uuid4(),
    familyStatus="father",
    partner=rheaRoyce,
    father=baelonTargaryen,
    mother=alyssaTargaryen,
)

aemmaArryn: Person = Person(
    name="Aemma Arryn",
    uuid=uuid4(),
    familyStatus="mother",
)

viserysTargaryen: Person = Person(
    name="Viserys Targaryen",
    uuid=uuid4(),
    familyStatus="father",
    partner=aemmaArryn,
    father=baelonTargaryen,
    mother=alyssaTargaryen,
)

ottoHightower: Person = Person(
    name="Otto Hightower",
    uuid=uuid4(),
    familyStatus="father",
)

hobertHightower: Person = Person(
    name="Hobert Hightower",
    uuid=uuid4(),
)

familyTree: FamilyTree = FamilyTree()

familyTree.add_people(
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

print("House of Dragon family tree from the first row to the third one...\n")

print(familyTree)

print(
    "\n> House of Dragon official family tree: "
    + "https://www.hbo.com/house-of-the-dragon/character-guide"
)
