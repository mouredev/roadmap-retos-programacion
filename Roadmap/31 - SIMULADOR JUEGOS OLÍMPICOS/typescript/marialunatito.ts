enum MedalEnum {
  gold = "gold",
  silver = "silver",
  bronze = "bronze",
}

interface IPlayer {
  id: number | undefined;
  name: string | undefined;
  country: string | undefined;
  event: IOlympics | undefined;
  medal: MedalEnum | undefined;
}

interface IOlympics {
  id: number | undefined;
  name: string | undefined;
}

class Olympics implements IOlympics {
  id: number | undefined;
  name: string | undefined;

  private listEventsWithPlayers: IOlympics[] = [];

  addEvents(data: IOlympics) {
    this.id = data.id;
    this.name = data.name;

    this.listEventsWithPlayers.push({
      id: this.id,
      name: this.name,
    });
  }
}
