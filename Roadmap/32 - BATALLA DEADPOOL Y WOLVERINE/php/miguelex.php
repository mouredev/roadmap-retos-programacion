<?php

function simulateBattle($initialLifeDeadpool, $initialLifeWolverine) {
    $lifeDeadpool = $initialLifeDeadpool;
    $lifeWolverine = $initialLifeWolverine;
    
    $turn = 1;
    $skipTurnDeadpool = false;
    $skipTurnWolverine = false;

    echo "\n---------------\n";
    while ($lifeDeadpool > 0 && $lifeWolverine > 0) {
        echo "Turno: $turn\n";
        
        if (!$skipTurnDeadpool) {
            
            if (rand(1, 100) > 25) { 
                $damageDeadpool = rand(10, 100);
                $lifeWolverine -= $damageDeadpool;
                echo "Deadpool ataca y causa $damageDeadpool de daño a Wolverine.\n";
                if ($damageDeadpool == 100) {
                    echo "¡Deadpool causa daño máximo! Wolverine pierde su siguiente turno.\n";
                    $skipTurnWolverine = true;
                } else {
                    $skipTurnWolverine = false;
                }
            } else {
                echo "Deadpool intenta atacar, pero Wolverine esquiva el ataque.\n";
            }
        } else {
            echo "Deadpool pierde su turno para regenerarse.\n";
            $skipTurnDeadpool = false;
        }

        if ($lifeWolverine <= 0) {
            echo "Wolverine ha caído. ¡Deadpool gana!\n";
            break;
        }

        if (!$skipTurnWolverine) {
            
            if (rand(1, 100) > 20) { 
                $damageWolverine = rand(10, 120);
                $lifeDeadpool -= $damageWolverine;
                echo "Wolverine ataca y causa $damageWolverine de daño a Deadpool.\n";
                if ($damageWolverine == 120) {
                    echo "¡Wolverine causa daño máximo! Deadpool pierde su siguiente turno.\n";
                    $skipTurnDeadpool = true;
                } else {
                    $skipTurnDeadpool = false;
                }
            } else {
                echo "Wolverine intenta atacar, pero Deadpool esquiva el ataque.\n";
            }
        } else {
            echo "Wolverine pierde su turno para regenerarse.\n";
            $skipTurnWolverine = false;
        }

        if ($lifeDeadpool <= 0) {
            echo "Deadpool ha caído. ¡Wolverine gana!\n";
            break;
        }

        echo "Vida de Deadpool: $lifeDeadpool\n";
        echo "Vida de Wolverine: $lifeWolverine\n";
        echo "---------------\n";
        $turn++;
        sleep(1); 
    }

    echo "\nResultado final:\n";
    echo "Vida de Deadpool: $lifeDeadpool\n";
    echo "Vida de Wolverine: $lifeWolverine\n";
}

echo "\n¡Bienvenido a la batalla entre Deadpool y Wolverine!\n";

$initialLifeDeadpool = (int)readline("Introduce la vida inicial de Deadpool: ");
$initialLifeWolverine = (int)readline("Introduce la vida inicial de Wolverine: ");

simulateBattle($initialLifeDeadpool, $initialLifeWolverine);

