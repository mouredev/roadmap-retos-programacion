enum WeekDays {
  Monday = 1,
  Tuesday = 2,
  Wednesday = 3,
  Thursday = 4,
  Friday = 5,
  Saturday = 6,
  Sunday = 7
}

const obtainDay = (numberOfDay: number) => {
  console.log(`Number of the day ${numberOfDay} of the week is ${WeekDays[numberOfDay]}`) 
}

obtainDay(3)
obtainDay(7)