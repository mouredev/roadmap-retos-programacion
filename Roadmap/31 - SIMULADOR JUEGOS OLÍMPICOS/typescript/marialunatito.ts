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
