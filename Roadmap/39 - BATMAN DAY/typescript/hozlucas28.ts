/* -------------------------------------------------------------------------- */
/*                               FIRST CHALLENGE                              */
/* -------------------------------------------------------------------------- */

function getBatmanDayAnniversary(anniversary: number): Date {
    const anniversaryDate: Date = new Date(1939, 8, 16)

    for (let i = 0; i < anniversary; i++) {
        const currentYear: number = anniversaryDate.getFullYear()

        anniversaryDate.setFullYear(currentYear + 1)
        anniversaryDate.setMonth(8, 1)

        let saturdayCounter: number = anniversaryDate.getDay() === 6 ? 1 : 0

        while (saturdayCounter < 3) {
            const currentDate: number = anniversaryDate.getDate()
            anniversaryDate.setDate(currentDate + 1)

            if (anniversaryDate.getDay() === 6) saturdayCounter++
        }
    }

    return anniversaryDate
}

const batmanDay85thAnniversary: Date = getBatmanDayAnniversary(85)
const batmanDay100thAnniversary: Date = getBatmanDayAnniversary(100)

console.log('> First challenge...')

console.log(
    `\n> The 85th anniversary of Batman day is on ${batmanDay85thAnniversary.toLocaleDateString()}.`
)

console.log(
    `\n> The 100th anniversary of Batman day is on ${batmanDay100thAnniversary.toLocaleDateString()}.`
)

/* -------------------------------------------------------------------------- */
/*                              SECOND CHALLENGE                              */
/* -------------------------------------------------------------------------- */

/* ---------------------------------- Types --------------------------------- */

type ArrayOfN<
    T extends any,
    N extends number,
    Acc extends T[] = []
> = Acc['length'] extends N ? Acc : ArrayOfN<T, N, [T, ...Acc]>

type ToRange<
    Stop extends number,
    Counter extends 0[] = [],
    Acc extends number[] = []
> = Counter['length'] extends Stop
    ? Acc[number]
    : ToRange<Stop, [0, ...Counter], [Counter['length'], ...Acc]>

type ThreatLevel = ToRange<21>

type Sensors = ArrayOfN<ArrayOfN<ThreatLevel, 20>, 20>

type SensorPosX = ToRange<20>
type SensorPosY = ToRange<20>

/* ---------------------------------- Main ---------------------------------- */

function getThreatLevels(
    sensors: Sensors
): [SensorPosX, SensorPosY, ThreatLevel][] {
    const threatLevels: [SensorPosX, SensorPosY, ThreatLevel][] = []

    for (let i = 1; i < sensors.length - 1; i++) {
        for (let j = 1; j < sensors[i].length - 1; j++) {
            let threatLevel: ThreatLevel = 0

            threatLevel += sensors[i - 1][j - 1]
            threatLevel += sensors[i - 1][j]
            threatLevel += sensors[i - 1][j + 1]

            threatLevel += sensors[i][j - 1]
            threatLevel += sensors[i][j]
            threatLevel += sensors[i][j + 1]

            threatLevel += sensors[i + 1][j - 1]
            threatLevel += sensors[i + 1][j]
            threatLevel += sensors[i + 1][j + 1]

            threatLevels.push([
                j as SensorPosX,
                i as SensorPosY,
                threatLevel as ThreatLevel,
            ])
        }
    }

    return threatLevels
}

const batmanCavePos = [0, 0]

const sensors: Sensors = [
    [1, 0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1],
    [2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0],
    [1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1],
    [0, 9, 8, 0, 2, 0, 9, 2, 8, 1, 0, 1, 3, 7, 8, 1, 0, 2, 7, 6],
    [1, 0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1],
    [3, 1, 8, 7, 9, 6, 1, 7, 9, 0, 1, 0, 1, 9, 2, 1, 3, 0, 8, 0],
    [1, 6, 9, 1, 2, 8, 0, 2, 1, 3, 2, 8, 7, 2, 8, 0, 1, 7, 9, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0],
    [2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2],
    [7, 8, 6, 1, 0, 9, 2, 8, 1, 3, 7, 1, 0, 2, 0, 9, 1, 6, 7, 8],
    [0, 1, 7, 9, 2, 8, 1, 6, 7, 8, 1, 2, 0, 3, 1, 8, 2, 7, 0, 1],
    [3, 0, 9, 1, 8, 6, 1, 0, 7, 9, 2, 0, 1, 2, 8, 0, 1, 9, 6, 1],
    [1, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0],
    [2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2],
    [9, 6, 1, 0, 9, 8, 7, 2, 8, 0, 1, 0, 3, 6, 2, 7, 9, 2, 8, 1],
    [0, 7, 8, 9, 6, 2, 1, 9, 6, 7, 8, 0, 9, 7, 6, 8, 1, 0, 2, 8],
    [2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2],
    [3, 2, 1, 9, 6, 7, 0, 3, 1, 8, 2, 7, 9, 2, 0, 9, 7, 6, 8, 0],
]

const threatLevels: [SensorPosX, SensorPosY, ThreatLevel][] =
    getThreatLevels(sensors)

const threatLevelsGreaterThanTwenty: [SensorPosX, SensorPosY, ThreatLevel][] =
    threatLevels.filter((sensor) => sensor[2] >= 20)

console.log('\n> Second challenge...')

console.log(
    '\n> Threat levels greater than 20 (security protocol activated)...'
)

for (let i = 0; i < threatLevelsGreaterThanTwenty.length; i++) {
    const [x, y, threatLevel] = threatLevelsGreaterThanTwenty[i]
    console.log(`\n> Coordinates (x, y): (${x}, ${y}).`)
    console.log(`> Threat level: ${threatLevel}.`)
}

console.log('\n> Position with the maximum threat level...')

let maxThreatLevel: [SensorPosX, SensorPosY, ThreatLevel] =
    threatLevelsGreaterThanTwenty[0]

for (const threatLevel of threatLevelsGreaterThanTwenty) {
    if (threatLevel[2] > maxThreatLevel[2]) maxThreatLevel = threatLevel
}

const distanceToBatmanCave: number =
    Math.abs(maxThreatLevel[0] - batmanCavePos[0]) +
    Math.abs(maxThreatLevel[1] - batmanCavePos[1])

console.log(
    `\n> Coordinates (x, y): (${maxThreatLevel[0]}, ${maxThreatLevel[1]}).`
)
console.log(`> Threat level: ${maxThreatLevel[2]}.`)
console.log(`> Distance to batman cave: ${distanceToBatmanCave} cells.`)
