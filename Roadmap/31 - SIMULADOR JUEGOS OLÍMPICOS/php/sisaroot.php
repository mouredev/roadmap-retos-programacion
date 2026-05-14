<?php
// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

$events = [];
$medalTable = [];

function inp(string $p): string
{
    echo $p;
    return trim(fgets(STDIN));
}

function addMedal(string $c, string $t): void
{
    global $medalTable;
    if (!isset($medalTable[$c]))
        $medalTable[$c] = ['gold' => 0, 'silver' => 0, 'bronze' => 0];
    $medalTable[$c][$t]++;
}

function registerEvent(): void
{
    global $events;
    $name = inp("Nombre del evento: ");
    if (!$name) {
        echo "Invalido.\n";
        return;
    }
    foreach ($events as $ev)
        if (strtolower($ev['name']) === strtolower($name)) {
            echo "Ya existe.\n";
            return;
        }
    $events[] = ['name' => $name, 'participants' => []];
    echo "Evento '$name' registrado.\n";
}

function registerParticipant(): void
{
    global $events;
    if (!$events) {
        echo "No hay eventos.\n";
        return;
    }
    foreach ($events as $i => $ev)
        echo "  " . ($i + 1) . ". {$ev['name']}\n";
    $idx = (int)inp("Selecciona número: ");
    if ($idx < 1 || $idx > count($events)) {
        echo "Invalido.\n";
        return;
    }
    $n = inp("Nombre: ");
    $c = inp("País: ");
    $events[$idx - 1]['participants'][] = ['name' => $n, 'country' => $c];
    echo "'$n ($c)' añadido a '{$events[$idx - 1]['name']}'.\n";
}

function simulateEvents(): void
{
    global $events;
    if (!$events) {
        echo "No hay eventos.\n";
        return;
    }
    foreach ($events as &$ev) {
        echo "\n=== Simulando: {$ev['name']} ===\n";
        $p = $ev['participants'];
        if (count($p) < 3) {
            echo "  Necesita >=3. Saltando.\n";
            continue;
        }
        shuffle($p);
        echo "  Oro:    {$p[0]['name']} ({$p[0]['country']})\n";
        echo "  Plata:  {$p[1]['name']} ({$p[1]['country']})\n";
        echo "  Bronce: {$p[2]['name']} ({$p[2]['country']})\n";
        addMedal($p[0]['country'], 'gold');
        addMedal($p[1]['country'], 'silver');
        addMedal($p[2]['country'], 'bronze');
    }
}

function showReport(): void
{
    global $medalTable;
    echo "\n== INFORME FINAL ==\n";
    if (!$medalTable) {
        echo "Sin resultados.\n";
        return;
    }
    $r = array_map(fn($c, $m) => ['c' => $c, ...$m, 't' => $m['gold'] + $m['silver'] + $m['bronze']], array_keys($medalTable), $medalTable);
    usort($r, fn($a, $b) => $b['gold'] - $a['gold'] ?: $b['silver'] - $a['silver'] ?: $b['bronze'] - $a['bronze']);
    foreach ($r as $i => $x)
        printf("%d. %-20s Oro:%d Plata:%d Bronce:%d Total:%d\n", $i + 1, $x['c'], $x['gold'], $x['silver'], $x['bronze'], $x['t']);
}

while (true) {
    echo "\n====== SIMULADOR JJOO ======\n1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir\n";
    match (inp("Opción: ")) {
            "1" => registerEvent(), "2" => registerParticipant(),
            "3" => simulateEvents(), "4" => showReport(),
            "5" => (function () {
            echo "Hasta luego!\n";
            exit(0); })(),
            default => print("Invalido.\n"),
        };
}
