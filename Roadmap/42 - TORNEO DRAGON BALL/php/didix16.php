<?php

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

namespace didix16\DragonBallTourament;

function msleep(int $milliseconds)
{
    usleep($milliseconds * 1000);
}

function randomValueFrom(array $list)
{
    return $list[array_rand($list)];
}

enum AttackType
{
    case PHYSICAL_ATK;
    case KI_WEAK_ATK;
    case KI_STRONG_ATK;
    case KI_ULTIMATE_ATK;

    public static function isPhysicalAtk(AttackType $type): bool
    {
        return $type === self::PHYSICAL_ATK;
    }

    public static function isKiWeakAtk(AttackType $type): bool
    {
        return $type === self::KI_WEAK_ATK;
    }

    public static function isKiStrongAtk(AttackType $type): bool
    {
        return $type === self::KI_STRONG_ATK;
    }

    public static function isKiUltimateAtk(AttackType $type): bool
    {
        return $type === self::KI_ULTIMATE_ATK;
    }
}

function printAtack(Fighter $fighter1, Fighter $fighter2, int $damage, bool $evaded, bool $isCritical = false, bool $defenseIgnored): void
{
    $fighter1Name = $fighter1->getName();
    $fighter2Name = $fighter2->getName();

    if (!$evaded) {
        printf(
            "%s ataca 🤜 a %s y le hace %d de daño 💔⬇️.%s%s\n",
            $fighter1Name,
            $fighter2Name,
            $damage,
            $isCritical ? ' 💥💥 ¡UUH ESO HA SIDO UN CRÍTICO! 💥💥' : '',
            $defenseIgnored ? ' 💥🛡️ ¡UUH LE HA PUESTO TODA SU ENERGÍA Y HA ATRAVESADO LA DEFENSA! 🛡️💥' : ''
        );
    } else {
        printf(
            "%s ataca 🤜 a %s pero %s esquiva el ataque! 🤸‍♂️💨\n",
            $fighter1Name,
            $fighter2Name,
            $fighter2Name
        );
    }
}

function kiAtackTypeMsg(AttackType $atk): string
{
    return match ($atk) {
        AttackType::KI_WEAK_ATK => 'un ataque de ki débil',
        AttackType::KI_STRONG_ATK => 'un ataque de ki fuerte',
        AttackType::KI_ULTIMATE_ATK => 'el ataque de ki definitivo',
    };
};

function printKiAtack(Fighter $fighter1, Fighter $fighter2, int $damage, bool $evaded, bool $defenseIgnored, AttackType $atkType): void
{
    $fighter1Name = $fighter1->getName();
    $fighter2Name = $fighter2->getName();
    $kiAtkIcon = '🫸〰️' . (AttackType::isKiUltimateAtk($atkType) ? '🧿' : '');

    if (!$evaded) {
        printf(
            "%s ataca %s a %s con %s y le hace %d de daño 💔⬇️.%s\n",
            $fighter1Name,
            $kiAtkIcon,
            $fighter2Name,
            kiAtackTypeMsg($atkType),
            $damage,
            $defenseIgnored ? ' 💥💥 ¡UUH ESA ATAQUE HA HECHO MELLA! 💥💥' : ''
        );
    } else {
        printf(
            "%s ataca %s a %s con %s pero %s esquiva el ataque! 🤸‍♂️💨\n",
            $fighter1Name,
            $kiAtkIcon,
            $fighter2Name,
            kiAtackTypeMsg($atkType),
            $fighter2Name
        );
    }
}

function printHealthAndKiOf(Fighter $fighter): void
{
    printf(
        "%s tiene %d de vida ❤️ y %s.\n",
        $fighter->getName(),
        $fighter->getHealth(),
        !$fighter->isInSparkingMode() ? $fighter->getKi() . ' de ki ⚡' : $fighter->getSparkingGauge() . ' de SPARKING! MODE 🌟⚡'
    );
}

// ki/sparking gauge amount to discharge by atk type
function dischargeKiAmountByType(AttackType $atk)
{

    return match ($atk) {
        AttackType::PHYSICAL_ATK => 5,
        AttackType::KI_WEAK_ATK => 20,
        AttackType::KI_STRONG_ATK => 40,
        AttackType::KI_ULTIMATE_ATK => 50,
    };
};

// some ki natural cubic spline functions
interface KiRechargeInterface
{

    public function kiRechargeProbability(int $ki): float;
}

class KiRecharge10 implements KiRechargeInterface
{

    public function kiRechargeProbability(int $ki): float
    {
        return ($ki >= 0 && $ki <= 10)
            ? (-2.9508e-5 * $ki ** 3 - 1.7049e-2 * $ki + 1)
            : (($ki > 10 && $ki <= 20)
                ? (4.7541e-5 * $ki ** 3 - 2.3115e-3 * $ki ** 2 + 6.0656e-3 * $ki + 0.92295)
                : (($ki > 20 && $ki <= 40)
                    ? (-3.6885e-6 * $ki ** 3 + 7.623e-4 * $ki ** 2 - 5.541e-2 * $ki + 1.3328)
                    : (($ki > 40 && $ki <= 50)
                        ? (-1.0656e-5 * $ki ** 3 + 1.5984e-3 * $ki ** 2 - 8.8852e-2 * $ki + 1.7787)
                        : 0
                    )
                )
            );
    }
}

class KiRecharge20 implements KiRechargeInterface
{

    public function kiRechargeProbability(int $ki): float
    {
        return ($ki >= 0 && $ki <= 10)
            ? (1.1639e-4 * $ki ** 3 - 7.163e-2 * $ki + 1)
            : (($ki > 10 && $ki <= 20)
                ? (-1.3197e-4 * $ki ** 3 + 7.4508e-3 * $ki ** 2 - 1.4615e-1 * $ki + 1.2484)
                : (($ki > 20 && $ki <= 40)
                    ? (1.4549e-5 * $ki ** 3 - 1.3402e-3 * $ki ** 2 + 2.9672e-2 * $ki + 7.623e-2)
                    : (($ki > 40 && $ki <= 50)
                        ? (-1.3525e-5 * $ki ** 3 + 2.0287e-3 * $ki ** 2 - 1.0508e-1 * $ki + 1.873)
                        : 0
                    )
                )
            );
    }
}

// class Fighter
class Fighter implements KiRechargeInterface
{
    protected const MAX_KI = 50;
    protected int $health = 100;
    protected int $evasionProbability = 0;
    protected int $sparkingGauge = 0;
    protected int $initialKi = 0;
    protected KiRechargeInterface $kiRecharger;

    public function __construct(
        protected string $name,
        protected int $attack,
        protected int $defense,
        protected int $speed,
        protected int $ki = 0,
        protected int $kiRechargeAmount = 10,
    ) {
        $this->kiRecharger = match ($kiRechargeAmount) {
            10 => new KiRecharge10(),
            20 => new KiRecharge20(),
            default => new KiRecharge10(),
        };
        $this->ki = max(0, min($this->ki, self::MAX_KI));
        $this->initialKi = $this->ki;
        $this->evasionProbability = $this->isSuperSonic() ? 50 : ($this->isFast() ? 30 : (!$this->hasSuperArmor() ? 20 : 0));
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function getAtk(): int
    {
        return ! $this->isInSparkingMode() ? $this->attack : intval($this->attack * 1.1);
    }

    public function getDef(): int
    {
        return ! $this->isInSparkingMode() ? $this->defense : intval($this->defense * 0.8);
    }

    public function getSpeed(): int
    {
        return $this->speed;
    }

    public function getKiRechargeAmount(): int
    {
        return $this->kiRechargeAmount;
    }

    public function getHealth(): int
    {
        return $this->health;
    }

    public function getKi(): int
    {
        return $this->ki;
    }

    public function getSparkingGauge(): int
    {
        return $this->sparkingGauge;
    }

    public function kiRechargeProbability(int $ki): float
    {
        return $this->kiRecharger->kiRechargeProbability($ki) * 100;
    }

    public function isInSparkingMode(): bool
    {
        return $this->sparkingGauge > 0;
    }

    public function enterInSparkingMode(): bool
    {
        if ($this->ki === self::MAX_KI) {
            $sparkingProbability = match (true) {
                $this->isStrong() => 65 + (($this->attack - 70) / 30) * 20,
                $this->isWeak() => 60,
                default => 50,
            };

            if (rand(1, 100) <= $sparkingProbability) {
                $this->sparkingGauge = self::MAX_KI;
                return true;
            } else {
                return false;
            }
        }
        return false;
    }

    public function exitSparkingMode(): self
    {
        $this->sparkingGauge = 0;
        return $this;
    }

    public function dischargeSparkingGauge(int $amount): self
    {
        $this->sparkingGauge = max(0, $this->sparkingGauge - $amount);
        return $this;
    }

    // if true, the fighter will recharge ki, if false, the fighter will attack
    public function hasToRechageKi(): bool
    {
        return rand(1, 100) <= $this->kiRechargeProbability($this->ki);
    }

    public function evade(): bool
    {
        return rand(1, 100) <= (!$this->isInSparkingMode() ? $this->evasionProbability : $this->evasionProbability + 10);
    }

    public function useKiOrPhysicalAttack(): AttackType
    {

        $r = rand(1, 100);

        // check if the fighter is in sparking mode
        if ($this->isInSparkingMode()) {
            // 10% for weak ki atk, 20% for strong ki atk, 10% for physical atk and 60% for ultimate ki atk
            return match (true) {
                $r <= 10 => AttackType::KI_WEAK_ATK,
                $r <= 30 => AttackType::KI_STRONG_ATK,
                $r <= 40 => AttackType::PHYSICAL_ATK,
                default => AttackType::KI_ULTIMATE_ATK,
            };
        }

        if ($this->ki >= 40) {
            // 15% for weak ki atk, 25% for strong ki atk, 60% for physical atk
            return match (true) {
                $r <= 15 => AttackType::KI_WEAK_ATK,
                $r <= 40 => AttackType::KI_STRONG_ATK,
                default => AttackType::PHYSICAL_ATK,
            };
        } else if ($this->ki >= 20) {
            // 25% for weak ki atk, 75% for physical atk
            return $r <= 25 ? AttackType::KI_WEAK_ATK : AttackType::PHYSICAL_ATK;
        } else {
            return AttackType::PHYSICAL_ATK;
        }
    }

    // return the damage and if the defense was ignored partially or totally
    public function takeKiDamageFrom(Fighter $fighter, AttackType $kiType): array
    {

        $damage = 0;
        $ignoreDefense = false;
        $minDamage = 0;
        $tempDef = $this->getDef();

        switch ($kiType) {
            case AttackType::KI_WEAK_ATK:
                $damage = intval($fighter->getAtk() * ($fighter->isWeak() ? 1.25 : 1.2));
                $tempDef = rand(1, 100) <= ($fighter->isWeak() ? 30 : 20) ? intval($tempDef * 0.8) : $tempDef;
                $minDamage = 2;
                break;
            case AttackType::KI_STRONG_ATK:
                $damage = intval($fighter->getAtk() * ($fighter->isWeak() ? 2 : 1.5));
                $tempDef = rand(1, 100) <= ($fighter->isWeak() ? 50 : 40) ? intval($tempDef * 0.8) : $tempDef;
                $minDamage = 5;
                break;
            case AttackType::KI_ULTIMATE_ATK:
                $damage = intval($fighter->getAtk() * ($fighter->isWeak() ? 4 : 3));
                $ignoreDefense = rand(1, 100) <= 70;
                $minDamage = 10;
                break;
            default:
                throw new \Exception('Invalid ki type');
        }

        if (!$ignoreDefense) {
            $damage = $damage - $tempDef;
        }

        $this->health -= $damage = max($minDamage, $damage);
        return [$damage, $ignoreDefense || $this->getDef() !== $tempDef];
    }

    public function takePhysicalDamageFrom(Fighter $fighter): array
    {

        $damage = $fighter->getAtk() - $this->getDef();
        $critProbability = ($fighter->isStrong() ? 20 : 10) - ($fighter->isFast() ? 5 : 0);
        $critProbability += $fighter->isInSparkingMode() ? 5 : 0;
        $defenseIgnored = false;

        $isCritical = rand(1, 100) <= $critProbability;
        if ($isCritical) {
            // if the defender has more defense than the atk of the atacker or they are the same, the crit ignores the defense
            if ($damage <= 0) {
                $damage = $fighter->getAtk() << 1; // double the damage (fighter atk) ignoring the defense
                $defenseIgnored = true;
            } else {
                $damage = $damage << 1; // double the damage (fighter atk)
            }
        }
        // if the defender has more defense than the atk of the atacker or they are the same, the damage  is the 10% of the atk of the atacker
        else if ($damage <= 0) $damage = intval($fighter->getAtk() * 0.1); // get the integer part;

        // if the defender has super armor, the damage is reduced by 90% (min 1)
        if ($this->hasSuperArmor()) {
            $damage = max(1, intval($damage * 0.1));
        }

        $this->health -= $damage;
        return [$damage, $isCritical, $defenseIgnored];
    }

    public function hasSuperArmor(): bool
    {
        return $this->speed === 0;
    }

    public function isSuperSonic(): bool
    {
        return $this->speed === 100;
    }

    public function isFast(): bool
    {
        return $this->speed >= 70;
    }

    public function isStrong(): bool
    {
        return $this->attack >= 70;
    }

    public function isWeak(): bool
    {
        return $this->attack < 20;
    }

    public function isDead(): bool
    {
        return $this->health <= 0;
    }

    public function heal(): self
    {
        $this->health = 100;
        return $this;
    }

    public function healKi(): self
    {
        $this->ki = $this->initialKi;
        return $this;
    }

    public function dischargeKiAmount(int $amount): self
    {
        $this->ki = max(0, $this->ki - $amount);
        return $this;
    }

    public function rechargeKi(): self
    {
        $this->ki = min(self::MAX_KI, $this->ki + $this->kiRechargeAmount);
        return $this;
    }
}

// Singleton Tournament
/**
 * Usage:
 * $tournament = Tournament::getInstance();
 * reset(); reset the tournament after it ends. return the torunament object
 * init($numOfFighters, timeInMsBetweenAttacks); start the tournament with numOfFighters and simulate the time between attacks and rounds if timeInMsBetweenAttacks is set
 * returns the winner of the tournament
 * 
 * Example 1 (first time) with 8 fighters and no time between attacks:
 * $tournament->init(8);
 * Example 2 (first time) with 8 fighters and 1.1s between attacks and rounds:
 * $tournament->init(8, 1100);
 * Example 3 (reset the tournament) with 16 fighters and no time between attacks:
 * $tournament->reset()->init(16);
 */
class Tournament
{
    protected static ?Tournament $instance = null;
    protected array $fighters = [];
    protected int $rounds = 0;
    protected int $timmer = 0; // use this to simulate the time between attacks and rounds
    protected ?Fighter $winner = null;

    // some names and its usage
    protected static array $names = [
        'Goku' => 0,
        'Vegeta' => 0,
        'Piccolo' => 0,
        'Gohan' => 0,
        'Krillin' => 0,
        'Yamcha' => 0,
        'Tien' => 0,
        'Chiaotzu' => 0,
        'Master Roshi' => 0,
        'Trunks' => 0,
        'Goten' => 0,
        'Pan' => 0,
        'Frieza' => 0,
        'Cell' => 0,
        'Majin Buu' => 0,
        'Beerus' => 0,
        'Whis' => 0,
        'Jiren' => 0,
        'Hit' => 0,
        'Kale' => 0,
        'Caulifla' => 0,
        'Cabba' => 0,
        'Broly' => 0,
        'Zamasu' => 0,
        'Black Goku' => 0,
        'Vegito' => 0,
        'Gogeta' => 0,
        'Kefla' => 0,
        'Toppo' => 0,
        'Dyspo' => 0,
        'Android 17' => 0,
        'Android 18' => 0,
        'Android 16' => 0,
        'Android 19' => 0,
        'Android 20' => 0,
        'Android 21' => 0,
    ];


    private function __construct() {}

    public static function getInstance(): Tournament
    {
        if (self::$instance === null) {
            self::$instance = new Tournament();
        }
        return self::$instance;
    }

    public function generateFighters(int $n, bool $timmerIsSet = false): self
    {
        // check if n is integer, is positive and max 2^10, its min 2 and is a power of 2
        if (!is_int($n) || ($n & ($n - 1)) !== 0 || $n < 2 || $n > 1024) {
            throw new \Exception('El torneo solo es válido con un número de luchadores potencia de 2,un mínimo de 2 luchadores y máximo de 1024');
        }

        while ($n--) {
            $name = array_rand(self::$names);
            // add #number to the name if it is repeated
            self::$names[$name]++ && ($name .= ' ' . self::$names[$name]);
            $atk = rand(10, 100); // min 10 atk to make some damage
            $def = rand(0, 100);
            $speed = rand(0, 100);
            $initialKi = randomValueFrom([20, 30]);
            $kiRechargeAmount = randomValueFrom([10, 20]);

            $this->fighters[] = new Fighter($name, $atk, $def, $speed, $initialKi, $kiRechargeAmount);
            printf(
                "%s se une al torneo con %d 💪 de ataque, %d de defensa 🛡️, %d de velocidad 🪽, %d de ki inicial ⚡ y %d de recarga de ki ⬆️⚡%s%s.\n",
                $name,
                $atk,
                $def,
                $speed,
                $initialKi,
                $kiRechargeAmount,
                $speed === 0 ? '¡¡¡INCLUSO TIENE SUPER ARMADURA!!! 🧱' : '[no tiene super armadura]',
                $speed === 100 ? '¡¡¡ES SUPERSÓNICO, ESQUIVARÁ CASI TODO!!! 🏃‍♂️💨' : '[no es supersónico]'
            );
            $timmerIsSet && msleep(250);
        }

        // sort the fighters by random order
        shuffle($this->fighters);


        return $this;
    }

    public function reset(): self
    {
        $this->fighters = [];
        $this->rounds = 0;
        $this->timmer = 0;
        $this->winner = null;
        self::$names = array_map(fn($v) => 0, self::$names);
        return $this;
    }

    public function init(int $numOfFighters, $timeInMsBetweenAttacks = 0): Fighter
    {
        $this->generateFighters($numOfFighters, $timeInMsBetweenAttacks > 0);
        $this->timmer = $timeInMsBetweenAttacks;
        $this->rounds = log($numOfFighters, 2);
        return $this->start();
    }

    protected function start(): Fighter
    {

        $winners = $this->fighters;
        for ($i = 0; $i < $this->rounds - 1; $i++) {
            printf("Ronda %d\n", $i + 1);
            msleep($this->timmer);
            $winners = $this->round($winners);
        }

        printf("Ronda final entre 🤜 %s y %s 🤛\n", $winners[0]->getName(), $winners[1]->getName());
        $winners = $this->round($winners, true);

        $this->winner = $winners[0];
        printf("¡¡¡%s ha ganado el torneo!!! 🏆🎉\n", $this->winner->getName());

        return $this->winner;
    }

    protected function round(array $fighters, bool $isFinal = false): array
    {

        $winners = [];
        $fightersLen = count($fighters);
        for ($i = 0; $i < $fightersLen; $i += 2) {
            $fighter1 = $fighters[$i];
            $fighter2 = $fighters[$i + 1];
            !$isFinal && printf("Empieza la batalla #%d entre 🤜 %s y %s 🤛!\n", ($i >> 1) + 1, $fighter1->getName(), $fighter2->getName());
            msleep($this->timmer);
            $winner = $this->battle($fighter1, $fighter2);
            !$isFinal && printf("%s avanza a la siguiente ronda 👏\n", $winner->getName());
            $winners[] = $winner;
        }

        return $winners;
    }

    protected function battle(Fighter $fighter1, Fighter $fighter2): Fighter
    {
        $turn = $fighter1->getSpeed() > $fighter2->getSpeed() ? [$fighter1, $fighter2] : [$fighter2, $fighter1];

        while (true) {
            $attacker = $turn[0];
            $defender = $turn[1];

            // check if the atacker attacks or recharges ki
            if ($attacker->hasToRechageKi()) {
                $attacker->rechargeKi();
                printf(
                    "%s recarga ki 🔄🧘 y recupera %d de ki⚡⬆️. Ahora tiene %d de ki ⚡\n",
                    $attacker->getName(),
                    $attacker->getKiRechargeAmount(),
                    $attacker->getKi()
                );
                msleep($this->timmer);
                $turn = [$defender, $attacker];
                continue;
            }

            // check if the attacker enters in sparking mode
            $attackerInSparkingMode = $attacker->isInSparkingMode();
            if (!$attackerInSparkingMode && $attacker->enterInSparkingMode()) {
                printf(
                    "%s entra en modo SPARKING! 🌟🔥 y aumenta sus habilidades 📈. La cosa se pone seria ⚠️\n",
                    $attacker->getName()
                );
                msleep($this->timmer);
                $turn = [$defender, $attacker];
                continue;
            }

            // attacker attacks
            // check if the attacker uses ki or physical attack
            $atkType = $attacker->useKiOrPhysicalAttack();

            // check if the defender evades the attack
            $evaded = $defender->evade();

            $damage = 0;

            // if the attacker uses ki attack, the defender takes ki damage
            if (!AttackType::isPhysicalAtk($atkType)) {

                [$damage, $defenseIgnored] = !$evaded ? $defender->takeKiDamageFrom($attacker, $atkType) : [0, false];

                $attackerInSparkingMode
                    ?   $attacker->dischargeSparkingGauge(dischargeKiAmountByType($atkType)) &&
                    AttackType::isKiUltimateAtk($atkType) &&
                    $attacker->dischargeKiAmount(dischargeKiAmountByType($atkType))
                    : $attacker->dischargeKiAmount(dischargeKiAmountByType($atkType));

                printKiAtack($attacker, $defender, $damage, $evaded, $defenseIgnored, $atkType);
                if ($defender->isDead()) {
                    printf("%s ha sido derrotado 💀😵\n", $defender->getName());
                    $attacker
                        ->heal()
                        ->healKi()
                        ->exitSparkingMode();
                    msleep($this->timmer);
                    return $attacker;
                } else {
                    // print if the attacker leaves the sparking mode
                    $attackerLeavesSparkingMode = $attackerInSparkingMode && !$attacker->isInSparkingMode();
                    $attackerLeavesSparkingMode && printf("%s sale del modo SPARKING! 🌟🔥\n", $attacker->getName());

                    printHealthAndKiOf($attacker);
                    printHealthAndKiOf($defender);

                    msleep($this->timmer);
                }

                $turn = [$defender, $attacker];
                continue;
            }

            [$damage, $isCritical, $defenseIgnored] = !$evaded ? $defender->takePhysicalDamageFrom($attacker) : [0, false, false];
            $attackerInSparkingMode && $attacker->dischargeSparkingGauge(dischargeKiAmountByType(AttackType::PHYSICAL_ATK));

            printAtack($attacker, $defender, $damage, $evaded, $isCritical, $defenseIgnored);

            if ($defender->isDead()) {
                printf("%s ha sido derrotado 💀😵\n", $defender->getName());

                $attacker
                    ->heal()
                    ->healKi()
                    ->exitSparkingMode();

                msleep($this->timmer);
                return $attacker;
            } else {
                // print if the attacker leaves the sparking mode
                $attackerLeavesSparkingMode = $attackerInSparkingMode && !$attacker->isInSparkingMode();
                $attackerLeavesSparkingMode && printf("%s sale del modo SPARKING! 🌟🔥\n", $attacker->getName());

                printHealthAndKiOf($attacker);
                printHealthAndKiOf($defender);

                msleep($this->timmer);
            }

            $turn = [$defender, $attacker];
        }
    }
}

if (php_sapi_name() === 'cli') {
    // start the tournament
    $numOfFighters = $argc > 1 ? intval($argv[1]) : 8;
    $timeInMsBetweenAttacks = $argc > 2 ? intval($argv[2]) : 0;
    Tournament::getInstance()->init($numOfFighters, $timeInMsBetweenAttacks);
} else {

    // start the tournament
    Tournament::getInstance()->init(8);
}
