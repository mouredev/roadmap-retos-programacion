/*
 * Autor: didix16
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 *  --------------
 *  NOTAS: Algunos retoques añadidos
 *  1. Asumo que cada vez que un luchado pasa de ronda, se le cura la vida
 *  2. Mecánica de crítico: Si el atacante tiene 70 o más de ataque, tiene un 20% de probabilidad de hacer un crítico, sino solo un 10%
 *  3. Los críticos hacen el doble de daño y si el defensor tiene más defensa que el ataque del atacante o son iguales, el crítico ignora la defensa
 *  4. Si el personaje tiene una velocidad de 70 o más, tendrá más probabilidad de esquivar el ataque (+10%) pero menos probabilidad de hacer un crítico (-5%)
 *  5. En caso de que el daño sea 0 o negativo, el daño será el 10% del ataque del atacante.
 *  6. Si un personaje tiene 0 de velocidad, no podrá esquivar los ataques pero tendrá superarmadura, haciendo que los golpes con daño positivo solo le quiten el 10% (min 1)
 *  7. Si un personaje tiene 100 de velocidad, será supersónico y tendrá un 50% de probabilidad de esquivar los ataques!!!
 *  8. Mecánica de ki y SPARKING! MODE. Los personajes tienen 50 de ki máximo (y pueden empezar con 20 o 30) y disponen de 3 ataques especiales que comsumen ki, el débil consume 20, el fuerte 40 y la definitiva 50.
 *  Los turnos deberán usarse para atacar o recuperar ki. Si un personaje se queda sin ki, no podrá usar ataques especiales y está obligado a recuperar ki.
 *  Cada personaje dipondrá de una velocidad de recuperación de ki (cantidad a recuperar entre 10 o 20 por turno) y una probabilidad de recuperar ki que dependerá de la cantidad de ki restante
 *  en su turno. La probabilidad de recuperar ki dependerá de la cantidad de recuperación de ki del personaje, a cuanta más cantidad menos probabilidad.
 *  La probabilidad de escoger recuperación en vez de ataque dependerá de la cantidad de ki restante. Para ello generaremos 2 tipos de curvas cúbicas a trozos (natural cubic spline) que aproximen la probabilidad:
 *      - una para los que recuperan 10 de ki por turno (Ki Recharge = 10)
 *      - otra para los que recuperan 20 de ki por turno (Ki Recharge = 20)
 *  Si un personaje tiene menos de 20 de ataque se considerará débil pero como bonificación para balancear un poco la cosa, sus ataques de ki débil tendrán un 20% más de daño y los fuertes un 50% más de daño además de tener 10% más de probabilidad de ignorar la defensa del defensor.
 *  Los ataques de ki no se calculan como los ataques normales, sino que tienen un daño base (atk+%) y una probabilidad de ignorar la defensa del defensor además de no tener críticos:
 *  Los ataques de ki débiles producen un daño equivalente al atk + 25% (+50% si personaje debil; min 2 daño) y tienen una probabilidad del 20% (30% si personaje debil) de ignorar el 80% de la defensa del defensor.
 *  Los ataques de ki fuertes producen un daño equivalente al atk + 50% (+100% si personaje debil; min 5 daño) y tienen una probabilidad del 40% (50% si personaje debil) de ignorar el 80% de la defensa del defensor.
 *  Los ataques de ki definitivos producen un daño equivalente al atk + 200% (+300% si personaje debil; min 10 daño) y tienen un 70% de probabilidad de ignorar el 100% de la defensa del defensor.
 *  Además, para realizar un ataque de ki definitivo, el personaje debe entrar en modo SPARKING!. Para ello, el personaje debe tener 50 de ki y la probabilidad de entrar en modo SPARKING! se calcula como:
 *     - 50% si el personaje no es considerado débil
 *     - 60% si el personaje es considerado débil
 *     - 65% + ((atk-70)/30)*20% si el personaje es considerado fuerte (70atk => 65%, 100atk => 85%)
 *  Entrar en modo SPARKING! consumirá un turno. En este modo, el personaje obtendrá:
 *     - +5% de probabilidad de crítico adicional
 *     - +10% de probabilidad de esquivar adicional
 *     - +10% de atk adicional
 *     - -20% de reducción defensa
 *     - posibilidad de realizar el ataque definitivo de ki
 *  Este modo consta de un contador especial de 50 unidades las cuales cuando llegue a 0, el personaje saldrá del modo SPARKING!
 *  Durante el modo SPARKING! el personaje consumirá contador SPARKING! según el ataque que realice:
 *     - 5 unidades por ataque físico
 *     - 20 unidades por ataque de ki débil
 *     - 40 unidades por ataque de ki fuerte
 *     - 50 unidades por ataque de ki definitivo (consume 50 de ki y sale del modo SPARKING!)
 *  Mientras el contador sea positivo, se podrá realizar cualquier combinación de ataque posible. Cuando el contador llegue a 0, el personaje saldrá del modo SPARKING!. Realizar un ataque definitivo de ki consumirá el contador y el ki del personaje.
 *  Para elegir entre ataque físico o de ki, dependerá de si tiene ki disponible (o contador SPARKING!) y si lo tiene entonces la probabilidad se calcula como:
 *     - Si modo SPARKING! activo
 *          - 10% para el ataque de ki débil
 *          - 20% para el ataque de ki fuerte
 *          - 10% para ataques físicos
 *          - 60% para ataque definitivo de ki
 *     - Si ki disponible >= 40
 *          - 15% para el ataque de ki débil
 *          - 25% para el ataque de ki fuerte
 *          - 60% para ataques físicos
 *     - Si ki disponible >= 20 y < 40
 *         - 25% para el ataque de ki débil
 *         - 75% para ataques físicos
 *    - Si ki disponible < 20
 *      -  100% para ataques físicos
 */

// utils
const rand = Math.random;
const randInt = (min: number, max: number) => Math.floor(rand() * (max - min + 1) + min);
const randValuesFrom = <T>(list: Array<T>) => list[randInt(0, list.length - 1)];
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

enum AttackType {
    PHYSICAL_ATK,
    KI_WEAK_ATK,
    KI_STRONG_ATK,
    KI_ULTIMATE_ATK,
}

namespace AttackType {
    export function isPhysicalAtk(atkType: AttackType): boolean {
        return atkType === AttackType.PHYSICAL_ATK;
    }

    export function isKiWeakAtk(atkType: AttackType): boolean {
        return atkType === AttackType.KI_WEAK_ATK;
    }

    export function isKiStrongAtk(atkType: AttackType): boolean {
        return atkType === AttackType.KI_STRONG_ATK;
    }

    export function isKiUltimateAtk(atkType: AttackType): boolean {
        return atkType === AttackType.KI_ULTIMATE_ATK;
    }
}

const printAtack = (
    fighter1: Fighter,
    fighter2: Fighter,
    damage: number,
    evaded: boolean,
    isCrit: boolean,
    defenseIgnored: boolean
) => {
    if (!evaded)
        console.log(
            `${fighter1.getName()} ataca 🤜 a ${fighter2.getName()} y le hace ${damage} de daño 💔⬇️. ${
                isCrit ? ' 💥💥 ¡UUH ESO HA SIDO UN CRÍTICO! 💥💥' : ''
            }${defenseIgnored ? ' 💥🛡️ ¡UUH LE HA PUESTO TODA SU ENERGÍA Y HA ATRAVESADO LA DEFENSA! 🛡️💥' : ''}`
        );
    else
        console.log(
            `${fighter1.getName()} ataca 🤜 a ${fighter2.getName()} pero ${fighter2.getName()} esquiva el ataque! 🤸‍♂️💨`
        );
};

const kiAtackTypeMsg: Record<AttackType | number, string> = {
    [AttackType.KI_WEAK_ATK]: 'un ataque de ki débil',
    [AttackType.KI_STRONG_ATK]: 'un ataque de ki fuerte',
    [AttackType.KI_ULTIMATE_ATK]: 'el ataque definitivo de ki',
};

const printKiAtack = (
    fighter1: Fighter,
    fighter2: Fighter,
    damage: number,
    evaded: boolean,
    ignoreDefense: boolean,
    atkType: AttackType
) => {
    const fighter1Name = fighter1.getName();
    const fighter2Name = fighter2.getName();
    const kiAtkIcon = `🫸〰️${AttackType.isKiUltimateAtk(atkType) ? '🧿' : ''}`;
    if (!evaded)
        console.log(
            `${fighter1Name} ataca ${kiAtkIcon} a ${fighter2Name} con ${
                kiAtackTypeMsg[atkType]
            } y le hace ${damage} de daño 💔⬇️. ${ignoreDefense ? ' 💥💥 ¡UUH ESA ATAQUE HA HECHO MELLA! 💥💥' : ''}`
        );
    else
        console.log(
            `${fighter1Name} ataca ${kiAtkIcon} a ${fighter2Name} con ${kiAtackTypeMsg[atkType]} pero ${fighter2Name} esquiva el ataque! 🤸‍♂️💨`
        );
};

const printHealthAndKiOf = (fighter: Fighter) => {
    console.log(
        `${fighter.getName()} tiene ${fighter.getHealth()} de vida ❤️ y ${
            !fighter.isInSparkingMode()
                ? fighter.getKi() + ' de ki ⚡'
                : fighter.getSparkingGauge() + ' de SPARKING! MODE 🌟⚡'
        }`
    );
};

// some ki natural cubic spline functions
const rechargeProbabilities: Record<10 | 20, (ki: number) => number> = {
    10: (ki) =>
        ki >= 0 && ki <= 10
            ? -2.9508e-5 * ki ** 3 - 1.7049e-2 * ki + 1
            : ki > 10 && ki <= 20
            ? 4.7541e-5 * ki ** 3 - 2.3115e-3 * ki ** 2 + 6.0656e-3 * ki + 0.92295
            : ki > 20 && ki <= 40
            ? -3.6885e-6 * ki ** 3 + 7.623e-4 * ki ** 2 - 5.541e-2 * ki + 1.3328
            : ki > 40 && ki <= 50
            ? -1.0656e-5 * ki ** 3 + 1.5984e-3 * ki ** 2 - 8.8852e-2 * ki + 1.7787
            : 0,
    20: (ki) =>
        ki >= 0 && ki <= 10
            ? 1.1639e-4 * ki ** 3 - 7.163e-2 * ki + 1
            : ki > 10 && ki <= 20
            ? -1.3197e-4 * ki ** 3 + 7.4508e-3 * ki ** 2 - 1.4615e-1 * ki + 1.2484
            : ki > 20 && ki <= 40
            ? 1.4549e-5 * ki ** 3 - 1.3402e-3 * ki ** 2 + 2.9672e-2 * ki + 7.623e-2
            : ki > 40 && ki <= 50
            ? -1.3525e-5 * ki ** 3 + 2.0287e-3 * ki ** 2 - 1.0508e-1 * ki + 1.873
            : 0,
};

// ki/sparking gauge amount to discharge by atk type
const dischargeKiAmountByType: Record<AttackType | number, number> = {
    [AttackType.PHYSICAL_ATK]: 5,
    [AttackType.KI_WEAK_ATK]: 20,
    [AttackType.KI_STRONG_ATK]: 40,
    [AttackType.KI_ULTIMATE_ATK]: 50,
};

// class Fighter
class Fighter {
    protected static MAX_KI = 50;
    protected health = 100;
    protected ki: number;
    protected initialKi: number;
    protected kiRechargeAmount = 10;
    protected name: string;
    protected atk: number;
    protected def: number;
    protected speed: number;
    protected evasionProbability: number;
    protected kiRechargeProbability = (ki: number) => 0;
    protected sparkingGauge = 0;

    constructor(name: string, atk: number, def: number, speed: number, ki = 20, kiRecharge: 10 | 20 = 10) {
        this.name = name;
        this.atk = atk;
        this.def = def;
        this.speed = speed;
        this.ki = Math.max(0, Math.min(Fighter.MAX_KI, ki));
        this.initialKi = ki;
        this.evasionProbability = this.isSuperSonic() ? 0.5 : this.isFast() ? 0.3 : !this.hasSuperArmor() ? 0.2 : 0.0;
        this.kiRechargeAmount = kiRecharge;
        this.kiRechargeProbability = rechargeProbabilities[kiRecharge];
    }

    getName(): string {
        return this.name;
    }

    getAtk(): number {
        return !this.isInSparkingMode() ? this.atk : Math.trunc(this.atk * 1.1);
    }

    getDef(): number {
        return !this.isInSparkingMode() ? this.def : Math.trunc(this.def * 0.8);
    }

    getSpeed(): number {
        return this.speed;
    }

    getKiRechargeAmount(): number {
        return this.kiRechargeAmount;
    }

    getHealth(): number {
        return this.health;
    }

    getKi(): number {
        return this.ki;
    }

    getSparkingGauge(): number {
        return this.sparkingGauge;
    }

    isInSparkingMode(): boolean {
        return this.sparkingGauge > 0;
    }

    enterInSparkingMode(): boolean {
        if (this.ki === Fighter.MAX_KI) {
            const sparkingProbability = this.isStrong()
                ? 0.65 + ((this.atk - 70) / 30) * 0.2
                : this.isWeak()
                ? 0.6
                : 0.5;
            if (rand() < sparkingProbability) {
                this.sparkingGauge = Fighter.MAX_KI;
                return true;
            } else {
                return false;
            }
        }
        return false;
    }

    exitSparkingMode(): this {
        this.sparkingGauge = 0;
        return this;
    }

    dischargeSparkingGauge(amount: number): this {
        this.sparkingGauge = Math.max(0, this.sparkingGauge - amount);
        return this;
    }

    // if true, the fighter will recharge ki, if false, the fighter will attack
    hasToRechargeKi(): boolean {
        return rand() < this.kiRechargeProbability(this.ki);
    }

    evade(): boolean {
        return rand() < (!this.isInSparkingMode() ? this.evasionProbability : this.evasionProbability + 0.1);
    }

    useKiOrPhysicalAttack(): AttackType {
        const r = rand();

        // check if the fighter is in sparking mode
        if (this.isInSparkingMode()) {
            // 10% for weak ki atk, 20% for strong ki atk, 10% for physical atk and 60% for ultimate ki atk
            return r < 0.1
                ? AttackType.KI_WEAK_ATK
                : r < 0.3
                ? AttackType.KI_STRONG_ATK
                : r < 0.4
                ? AttackType.PHYSICAL_ATK
                : AttackType.KI_ULTIMATE_ATK;
        }

        if (this.ki >= 40) {
            // 15% for weak ki atk, 25% for strong ki atk and 60% for physical atk
            return r < 0.15 ? AttackType.KI_WEAK_ATK : r < 0.4 ? AttackType.KI_STRONG_ATK : AttackType.PHYSICAL_ATK;
        } else if (this.ki >= 20) {
            // 25% for weak ki atk and 75% for physical at
            return r < 0.25 ? AttackType.KI_WEAK_ATK : AttackType.PHYSICAL_ATK;
        } else {
            return AttackType.PHYSICAL_ATK;
        }
    }

    // return the damage and if the defense was ignored partially or totally
    takeKiDamageFrom(fighter: Fighter, kiType: AttackType): [number, boolean] {
        let damage = 0;
        let ignoreDefense = false;
        let minDamage = 0;
        let tempDef = this.getDef();
        switch (kiType) {
            case AttackType.KI_WEAK_ATK:
                damage = Math.trunc(fighter.getAtk() * (fighter.isWeak() ? 1.5 : 1.25));
                minDamage = 2;
                tempDef = rand() < (fighter.isWeak() ? 0.3 : 0.2) ? Math.trunc(tempDef * 0.8) : tempDef;
                break;
            case AttackType.KI_STRONG_ATK:
                damage = Math.trunc(fighter.getAtk() * (fighter.isWeak() ? 2 : 1.5));
                minDamage = 5;
                tempDef = rand() < (fighter.isWeak() ? 0.5 : 0.4) ? Math.trunc(tempDef * 0.8) : tempDef;
                break;
            case AttackType.KI_ULTIMATE_ATK:
                damage = Math.trunc(fighter.getAtk() * (fighter.isWeak() ? 4 : 3));
                minDamage = 10;
                ignoreDefense = rand() < 0.7;
                break;
            default:
                throw new Error('Invalid ki type');
        }

        if (!ignoreDefense) {
            damage = damage - tempDef;
        }

        this.health -= damage = Math.max(minDamage, damage);
        return [damage, ignoreDefense || this.getDef() !== tempDef];
    }

    takePhysicalDamageFrom(fighter: Fighter): [number, boolean, boolean] {
        let damage = fighter.getAtk() - this.getDef();
        let critProbability = (fighter.isStrong() ? 0.2 : 0.1) - (fighter.isFast() ? 0.05 : 0);
        let defenseIgnored = false;
        critProbability += fighter.isInSparkingMode() ? 0.05 : 0;

        const isCrit = rand() < critProbability;
        if (isCrit) {
            // if the defender has more defense than the atk of the atacker or they are the same, the crit ignores the defense
            if (damage <= 0) {
                damage = fighter.getAtk() << 1; // double the damage (fighter atk) ignoring the defense
                defenseIgnored = true;
            } else {
                damage <<= 1; // double the damage
            }
        }
        // if the defender has more defense than the atk of the atacker or they are the same, the damage  is the 10% of the atk of the atacker
        else if (damage <= 0) damage = Math.trunc(fighter.getAtk() * 0.1); // get the integer part;

        // if the defender has super armor, the damage is reduced by 90% (min 1)
        if (this.hasSuperArmor()) {
            damage = Math.max(1, Math.trunc(damage * 0.1));
        }

        this.health -= damage;
        return [damage, isCrit, defenseIgnored];
    }

    hasSuperArmor(): boolean {
        return this.speed === 0;
    }

    isSuperSonic(): boolean {
        return this.speed === 100;
    }

    isFast(): boolean {
        return this.speed >= 70;
    }

    isStrong(): boolean {
        return this.atk >= 70;
    }

    isWeak(): boolean {
        return this.atk < 20;
    }

    isDead(): boolean {
        return this.health <= 0;
    }

    heal(): this {
        this.health = 100;
        return this;
    }

    healKi(): this {
        this.ki = this.initialKi;
        return this;
    }

    dischargeKiAmount(amount: number): this {
        this.ki = Math.max(0, this.ki - amount);
        return this;
    }

    rechargeKi(): this {
        this.ki = Math.min(Fighter.MAX_KI, this.ki + this.kiRechargeAmount);
        return this;
    }
}

// Singleton Tournament
/**
 * Usage:
 *  reset() -> reset the tournament after it ends. return the torunament object
 *  init(numOfFighters, timeInMsBetweenAttacks) -> start the tournament with numOfFighters and simulate the time between attacks and rounds if timeInMsBetweenAttacks is set
 *  return the winner of the tournament
 *  Example 1 (first time) with 8 fighters and no time between attacks:
 *  await Tournament.getInstance().init(8);
 *  Example 2 (first time) with 8 fighters and 1.1s between attacks and rounds:
 *  await Tournament.getInstance().init(8, 1100);
 *  Example 3 (reset the tournament) with 16 fighters and no time between attacks:
 *  await Tournament.getInstance().reset().init(16);
 */
class Tournament {
    protected static instance: Tournament | null = null;
    protected fighters: Array<Fighter> = [];
    protected rounds: number = 0;
    protected winner: Fighter | null = null;
    protected timmer: number = 0; // If set, use this to simulate the time between attacks and rounds
    // some names and its usage
    protected static NAMES: Record<string, number> = {
        Goku: 0,
        Vegeta: 0,
        Piccolo: 0,
        Gohan: 0,
        Krillin: 0,
        Yamcha: 0,
        Tien: 0,
        Chiaotzu: 0,
        'Master Roshi': 0,
        Trunks: 0,
        Goten: 0,
        Pan: 0,
        Frieza: 0,
        Cell: 0,
        'Majin Buu': 0,
        Beerus: 0,
        Whis: 0,
        Jiren: 0,
        Hit: 0,
        Kale: 0,
        Caulifla: 0,
        Cabba: 0,
        Broly: 0,
        Zamasu: 0,
        'Black Goku': 0,
        Vegito: 0,
        Gogeta: 0,
        Kefla: 0,
        Toppo: 0,
        Dyspo: 0,
        'Android 17': 0,
        'Android 18': 0,
        'Android 16': 0,
        'Android 19': 0,
        'Android 20': 0,
        'Android 21': 0,
    };

    protected constructor() {}

    public static getInstance(): Tournament {
        if (!Tournament.instance) {
            Tournament.instance = new Tournament();
        }
        return Tournament.instance;
    }

    async generateFighters(n: number, timmerIsSet: boolean) {
        // check if n is integer, is positive and max 2^10, its min 2 and is a power of 2
        if (!Number.isInteger(n) || (n & (n - 1)) !== 0 || n < 2 || n > 1024) {
            throw new Error(
                'El torneo solo es válido con un número de luchadores potencia de 2,un mínimo de 2 luchadores y máximo de 1024'
            );
        }

        const nameList = Object.keys(Tournament.NAMES);
        const namesLength = nameList.length;

        for (let i = 0; i < n; i++) {
            const idx = randInt(0, namesLength - 1);
            let name = nameList[idx];
            // add #number to the name if it is repeated
            Tournament.NAMES[name]++ && (name += `#${Tournament.NAMES[name]}`);
            const atk = randInt(10, 100); // min 10 atk to make some damage
            const def = randInt(0, 100);
            const speed = randInt(0, 100);
            const initialKi = randValuesFrom([20, 30]);
            const rechargeAmount = randValuesFrom([10, 20]) satisfies 10 | 20;
            this.fighters.push(new Fighter(name, atk, def, speed, initialKi, rechargeAmount));
            console.log(
                `${name} se une al torneo con ataque: ${atk} 💪, defensa: ${def} 🛡️, velocidad: ${speed} 🪽, ki inicial: ${initialKi} ⚡ y ${rechargeAmount} de carga de ki ⬆️⚡ `,
                speed === 0 ? '¡¡¡INCLUSO TIENE SUPER ARMADURA!!! 🧱' : '[no tiene super armadura]',
                speed === 100 ? '¡¡¡ES SUPERSÓNICO, ESQUIVARÁ CASI TODO!!! 🏃‍♂️💨' : '[no es supersónico]'
            );
            timmerIsSet && (await sleep(250));
        }
        // sort the fighters by random
        this.fighters.sort(() => randInt(-1, 1));

        return this;
    }

    reset(): this {
        this.fighters = [];
        this.rounds = 0;
        this.winner = null;
        this.timmer = 0;
        // reset the names
        for (const name in Tournament.NAMES) {
            Tournament.NAMES[name] = 0;
        }

        return this;
    }

    async init(numOfFighters: number, timeInMsBetweenAttacks = 0) {
        await this.generateFighters(numOfFighters, timeInMsBetweenAttacks > 0);
        this.rounds = Math.log2(this.fighters.length);
        this.timmer = timeInMsBetweenAttacks;
        return await this.startAsync();
    }

    async startAsync(): Promise<Fighter> {
        let winners = this.fighters;
        for (let i = 0; i < this.rounds - 1; i++) {
            console.log(`Ronda ${i + 1}`);
            await sleep(this.timmer);
            winners = await this.roundAsync(winners);
        }

        console.log(`Ronda final entre 🤜 ${winners[0].getName()} y ${winners[1].getName()} 🤛`);
        winners = await this.roundAsync(winners, true);

        this.winner = winners[0];
        console.log(`El ganador es ${this.winner.getName()} 🎉`);
        return this.winner;
    }

    async roundAsync(fighters: Array<Fighter>, isFinal = false): Promise<Array<Fighter>> {
        let winners = [];
        for (let i = 0; i < fighters.length; i += 2) {
            const fighter1 = fighters[i];
            const fighter2 = fighters[i + 1];
            !isFinal &&
                console.log(
                    `Empieza la batalla #${(i >>> 1) + 1} 🤜 entre ${fighter1.getName()} y ${fighter2.getName()} 🤛!`
                ) &&
                (await sleep(this.timmer));
            const winner = await this.battleAsync(fighter1, fighter2);
            !isFinal && console.log(`${winner.getName()} avanza a la siguiente ronda 👏`) && (await sleep(this.timmer));
            winners.push(winner);
        }
        return winners;
    }

    async battleAsync(fighter1: Fighter, fighter2: Fighter): Promise<Fighter> {
        let turn = fighter1.getSpeed() > fighter2.getSpeed() ? [fighter1, fighter2] : [fighter2, fighter1];
        while (true) {
            const atacker = turn[0];
            const defender = turn[1];

            // check if the atacker attacks or recharges ki
            if (atacker.hasToRechargeKi()) {
                atacker.rechargeKi();
                console.log(
                    `${atacker.getName()} recarga ki 🔄🧘 y recupera ${atacker.getKiRechargeAmount()} de ki ⚡⬆️. Ahora tiene ${atacker.getKi()} de ki ⚡`
                );
                await sleep(this.timmer);
                turn = [defender, atacker];
                continue;
            }

            // check if the atacker enters in sparking mode
            const atackerInSparkingMode = atacker.isInSparkingMode();
            if (!atackerInSparkingMode && atacker.enterInSparkingMode()) {
                console.log(`${atacker.getName()} entra en modo SPARKING! 🌟🔥. La cosa se pone seria ⚠️`);
                await sleep(this.timmer);
                turn = [defender, atacker];
                continue;
            }

            // atacker attacks
            // check if the atacker uses ki or physical attack
            const atkType = atacker.useKiOrPhysicalAttack();

            // check if the defender evades the attack
            const evaded = defender.evade();
            let damage = 0;

            // if the atacker uses ki, the defender takes ki damage
            if (!AttackType.isPhysicalAtk(atkType)) {
                let ignoreDefense = false;

                if (!evaded) [damage, ignoreDefense] = defender.takeKiDamageFrom(atacker, atkType);
                atackerInSparkingMode
                    ? atacker.dischargeSparkingGauge(dischargeKiAmountByType[atkType]) &&
                      AttackType.isKiUltimateAtk(atkType) &&
                      atacker.dischargeKiAmount(dischargeKiAmountByType[atkType])
                    : atacker.dischargeKiAmount(dischargeKiAmountByType[atkType]);

                printKiAtack(atacker, defender, damage, evaded, ignoreDefense, atkType);
                if (defender.isDead()) {
                    console.log(`${defender.getName()} ha muerto 💀`);
                    atacker.heal().healKi().exitSparkingMode();
                    await sleep(this.timmer);
                    return atacker;
                } else {
                    // print if the atacker leaves the sparking mode
                    const atackerLeavesSparkingMode = atackerInSparkingMode && !atacker.isInSparkingMode();
                    atackerLeavesSparkingMode && console.log(`${atacker.getName()} sale del modo SPARKING! 🌟🔥`);

                    printHealthAndKiOf(atacker);
                    printHealthAndKiOf(defender);

                    await sleep(this.timmer);
                }
                turn = [defender, atacker];
                continue;
            }

            let isCrit = false;
            let defenseIgnored = false;

            if (!evaded) [damage, isCrit, defenseIgnored] = defender.takePhysicalDamageFrom(atacker);
            atackerInSparkingMode && atacker.dischargeSparkingGauge(dischargeKiAmountByType[AttackType.PHYSICAL_ATK]);

            printAtack(atacker, defender, damage, evaded, isCrit, defenseIgnored);

            if (defender.isDead()) {
                console.log(`${defender.getName()} ha muerto 💀`);
                atacker.heal().healKi().exitSparkingMode();
                await sleep(this.timmer);
                return atacker;
            } else {
                // print if the atacker leaves the sparking mode
                const atackerLeavesSparkingMode = atackerInSparkingMode && !atacker.isInSparkingMode();
                atackerLeavesSparkingMode && console.log(`${atacker.getName()} sale del modo SPARKING! 🌟🔥`);

                printHealthAndKiOf(atacker);
                printHealthAndKiOf(defender);

                await sleep(this.timmer);
            }
            turn = [defender, atacker];
            await sleep(this.timmer);
        }
    }
}

// 8 fighters and 1s between attacks and rounds
(async () => await Tournament.getInstance().init(8, 1000))();
