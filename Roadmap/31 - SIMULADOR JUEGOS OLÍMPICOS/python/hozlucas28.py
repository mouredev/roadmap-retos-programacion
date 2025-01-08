# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods,broad-exception-raised

from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Literal, Self, LiteralString, TypedDict
from random import sample

# ---------------------------------------------------------------------------- #
#                                SHARED_TYPES.PY                               #
# ---------------------------------------------------------------------------- #

type TName = str


# ---------------------------------------------------------------------------- #
#                                   UTILS.PY                                   #
# ---------------------------------------------------------------------------- #

TCountryWithNumberOfMedals = TypedDict(
    "TCountryWithNumberOfMedals", {"name": str, "number_of_medals": int}
)


def countries_ranking_by_number_of_medals(
    *sport_events: "TSportEvent",
) -> list[TCountryWithNumberOfMedals]:
    ranking_per_country: list[TCountryWithNumberOfMedals] = []

    winners: list[TCompetitor] = []
    for sport_event in sport_events:
        for winner_ in sport_event.winners:
            winners.append(winner_)

    indexes_to_ignore: list[int] = []

    for i, anchor_winner in enumerate(winners):
        if i in indexes_to_ignore:
            continue

        country_stats: TCountryWithNumberOfMedals = {
            "name": anchor_winner.country,
            "number_of_medals": len(anchor_winner.medals),
        }

        for j in range(i + 1, len(winners)):
            if j in indexes_to_ignore:
                continue

            next_winner = winners[j]

            if anchor_winner.country.upper() == next_winner.country.upper():
                country_stats["number_of_medals"] += len(next_winner.medals)
                indexes_to_ignore.append(j)

        ranking_per_country.append(country_stats)

    ranking_per_country.sort(
        key=lambda stats: stats["name"],
        reverse=False,
    )

    ranking_per_country.sort(
        key=lambda stats: stats["number_of_medals"],
        reverse=True,
    )

    return ranking_per_country


# ---------------------------------------------------------------------------- #
#                                   MEDAL.PY                                   #
# ---------------------------------------------------------------------------- #

type TCategory = "MedalCategory"
type TDate = datetime
type TSportEvent = "AbcSportEvent"

MedalCategory = Literal["silver", "gold", "bronze"]


class AbcMedal(metaclass=ABCMeta):
    @property
    @abstractmethod
    def category(self) -> TCategory:
        pass

    @property
    @abstractmethod
    def date(self) -> TDate:
        pass

    @property
    @abstractmethod
    def sport_event(self) -> TSportEvent:
        pass


class Medal(AbcMedal):
    __category: TCategory
    __date: TDate
    __sport_event: TSportEvent

    def __init__(
        self, *, category_: TCategory, date_: TDate, sport_event_: TSportEvent
    ) -> None:
        self.__category = category_
        self.__date = date_
        self.__sport_event = sport_event_

    @property
    def category(self) -> str:
        return self.__category

    @property
    def date(self) -> TDate:
        return self.__date

    @property
    def sport_event(self) -> TSportEvent:
        return self.__sport_event


# ---------------------------------------------------------------------------- #
#                                 COMPETITOR.PY                                #
# ---------------------------------------------------------------------------- #


TCountry = (
    Literal[
        "argentina",
        "españa",
        "estados unidos",
        "méxico",
        "canada",
        "chile",
        "brazil",
        "germany",
        "france",
        "italy",
        "australia",
        "japan",
    ]
    | LiteralString
)


class AbcCompetitor(metaclass=ABCMeta):
    @property
    @abstractmethod
    def country(self) -> TCountry:
        pass

    @property
    @abstractmethod
    def medals(self) -> list["AbcMedal"]:
        pass

    @property
    @abstractmethod
    def name(self) -> TName:
        pass

    @abstractmethod
    def add_medals(self, *new_medals: AbcMedal) -> Self:
        pass


class Competitor(AbcCompetitor):
    __country: TCountry
    __medals: list[AbcMedal]
    __name: TName

    def __init__(
        self, *, country_: TCountry, medals_: list[AbcMedal] | None = None, name_: TName
    ) -> None:
        if medals_ is None:
            medals_ = []

        self.__country = country_
        self.__medals = medals_
        self.__name = name_

    @property
    def country(self) -> TCountry:
        return self.__country

    @property
    def medals(self) -> list[AbcMedal]:
        return self.__medals

    @property
    def name(self) -> TName:
        return self.__name

    def add_medals(self, *new_medals: AbcMedal) -> Self:
        current_medals: list[AbcMedal] = self.__medals
        joined_medals: list[AbcMedal] = [*current_medals, *new_medals]
        self.__medals = joined_medals
        return self


# ---------------------------------------------------------------------------- #
#                                 SPORTEVENT.PY                                #
# ---------------------------------------------------------------------------- #

type TCompetitor = AbcCompetitor
type TWinner = TCompetitor


class AbcSportEvent(metaclass=ABCMeta):
    @property
    @abstractmethod
    def competitors(self) -> list[TCompetitor]:
        pass

    @property
    @abstractmethod
    def name(self) -> TName:
        pass

    @property
    @abstractmethod
    def winners(self) -> list[TCompetitor]:
        pass

    @abstractmethod
    def add_competitors(self, *new_competitors: TCompetitor) -> Self:
        pass

    @abstractmethod
    def start(self) -> Self:
        pass


class SportEvent(AbcSportEvent):
    __competitors: list[TCompetitor]
    __name: str
    __winners: list[TCompetitor]

    def __init__(
        self,
        *,
        competitors_: list[TCompetitor] | None = None,
        name_: str,
    ) -> None:
        if competitors_ is None:
            competitors_ = []

        self.__competitors = competitors_
        self.__name = name_

    @property
    def competitors(self) -> list[TCompetitor]:
        return self.__competitors

    @property
    def name(self) -> str:
        return self.__name

    @property
    def winners(self) -> list[TCompetitor]:
        return self.__winners

    @staticmethod
    def minimum_number_of_competitors() -> int:
        return 3

    def __has_enough_competitors(self) -> bool:
        return len(self.__competitors) >= SportEvent.minimum_number_of_competitors()

    def add_competitors(self, *new_competitors: AbcCompetitor) -> Self:
        current_competitors: list[TCompetitor] = self.__competitors
        joined_competitors: list[TCompetitor] = [*current_competitors, *new_competitors]
        self.__competitors = joined_competitors
        return self

    def start(self) -> Self:
        if not self.__has_enough_competitors():
            raise Exception(
                f"`Sport event '${self.__name}' needs more competitors. It currently has {len(self.__competitors)} competitor(s), but requires a minimum of {SportEvent.minimum_number_of_competitors()}."
            )

        [first_place_index, second_place_index, third_place_index] = sample(
            population=range(0, len(self.__competitors)), k=3
        )

        first_place_medal: AbcMedal = Medal(
            category_="gold", date_=datetime.today(), sport_event_=self
        )

        second_place_medal: AbcMedal = Medal(
            category_="silver", date_=datetime.today(), sport_event_=self
        )

        third_place_medal: AbcMedal = Medal(
            category_="bronze", date_=datetime.today(), sport_event_=self
        )

        self.__competitors[first_place_index].add_medals(first_place_medal)
        self.__competitors[second_place_index].add_medals(second_place_medal)
        self.__competitors[third_place_index].add_medals(third_place_medal)

        self.__winners = [
            self.competitors[first_place_index],
            self.competitors[second_place_index],
            self.competitors[third_place_index],
        ]
        return self


medal = Medal(
    category_="bronze", date_=datetime.today(), sport_event_=SportEvent(name_="Juan")
)


# ---------------------------------------------------------------------------- #
#                                   EXERCISE                                   #
# ---------------------------------------------------------------------------- #

print("> Paris 2024 olympic games...")

first_sport_event: TSportEvent = SportEvent(name_="football")
second_sport_event: TSportEvent = SportEvent(name_="handball")
third_sport_event: TSportEvent = SportEvent(name_="table tennis")
fourth_sport_event: TSportEvent = SportEvent(name_="swimming")

print("\n> First sport event...\n")
print(first_sport_event.__dict__)

print("\n> Second sport event...\n")
print(second_sport_event.__dict__)

print("\n> Third sport event...\n")
print(third_sport_event.__dict__)

print("\n> Fourth sport event...\n")
print(fourth_sport_event.__dict__)


competitors_of_first_sport_event: list[TCompetitor] = [
    Competitor(country_="argentina", name_="lionel messi"),
    Competitor(country_="españa", name_="sergio ramos"),
    Competitor(country_="estados unidos", name_="megan rapinoe"),
    Competitor(country_="méxico", name_="hirving lozano"),
    Competitor(country_="canada", name_="christine sinclair"),
]

competitors_of_second_sport_event: list[TCompetitor] = [
    Competitor(country_="brazil", name_="neymar"),
    Competitor(country_="germany", name_="manuel neuer"),
    Competitor(country_="france", name_="antoine griezmann"),
    Competitor(country_="italy", name_="giorgio chiellini"),
    Competitor(country_="australia", name_="sam kerr"),
]

competitors_of_third_sport_event: list[TCompetitor] = [
    Competitor(country_="japan", name_="naomi osaka"),
    Competitor(country_="china", name_="liu shiwen"),
    Competitor(country_="south korea", name_="choi hyojoo"),
    Competitor(country_="singapore", name_="feng tianwei"),
    Competitor(country_="germany", name_="han ying"),
]

competitors_of_fourth_sport_event: list[TCompetitor] = [
    Competitor(country_="sweden", name_="sarah sjöström"),
    Competitor(country_="united states", name_="caleb dressel"),
    Competitor(country_="australia", name_="emma mckeon"),
    Competitor(country_="canada", name_="penny oleksiak"),
    Competitor(country_="netherlands", name_="ranomi kromowidjojo"),
]

print("\n> Competitors of first sport event...\n")
for competitor in competitors_of_first_sport_event:
    print(competitor.__dict__)

print("\n> Competitors of second sport event...\n")
for competitor in competitors_of_second_sport_event:
    print(competitor.__dict__)

print("\n> Competitors of third sport event...\n")
for competitor in competitors_of_third_sport_event:
    print(competitor.__dict__)

print("\n> Competitors of fourth sport event...\n")
for competitor in competitors_of_fourth_sport_event:
    print(competitor.__dict__)

first_sport_event.add_competitors(*competitors_of_first_sport_event).start()
second_sport_event.add_competitors(*competitors_of_second_sport_event).start()
third_sport_event.add_competitors(*competitors_of_third_sport_event).start()
fourth_sport_event.add_competitors(*competitors_of_fourth_sport_event).start()

winners_of_first_sport_event: list[AbcCompetitor] = first_sport_event.winners
winners_of_second_sport_event: list[AbcCompetitor] = second_sport_event.winners
winners_of_third_sport_event: list[AbcCompetitor] = third_sport_event.winners
winners_of_fourth_sport_event: list[AbcCompetitor] = fourth_sport_event.winners

print("\n> Winners of first sport event...\n")
for winner in winners_of_first_sport_event:
    print(winner.__dict__)

print("\n> Winners of second sport event...\n")
for winner in winners_of_second_sport_event:
    print(winner.__dict__)

print("\n> Winners of third sport event...\n")
for winner in winners_of_third_sport_event:
    print(winner.__dict__)

print("\n> Winners of fourth sport event...\n")
for winner in winners_of_fourth_sport_event:
    print(winner.__dict__)

medal_ranking_per_country: list[TCountryWithNumberOfMedals] = (
    countries_ranking_by_number_of_medals(
        first_sport_event, second_sport_event, third_sport_event, fourth_sport_event
    )
)

print("\n> Medal ranking per country...\n")
for stats in medal_ranking_per_country:
    print(stats)
