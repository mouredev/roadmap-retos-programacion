const WeekDays = {
  Monday: 1,
  Tuesday: 2,
  Wednesday: 3,
  Thursday: 4,
  Friday: 5,
  Saturday: 6,
  Sunday: 7
}

const obtainDay = numberOfDay => {
  const days = Object.keys(WeekDays)
  console.log(`Number of the day ${numberOfDay} of the week is ${days[numberOfDay - 1]}`);
};

obtainDay(3);
obtainDay(7);
