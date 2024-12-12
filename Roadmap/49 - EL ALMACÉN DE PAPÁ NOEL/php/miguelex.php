<?php
function generateCode() {
    $characters = array_merge(range('A', 'C'), range(1, 3));
    shuffle($characters);
    return implode('', array_slice($characters, 0, 4));
}

$code = generateCode();
$attempts = 10;

echo "¡Bienvenido! Tienes 10 intentos para descifrar el código.\n";

while ($attempts > 0) {
    echo "Intento #{$attempts}. Ingresa un código de 4 caracteres: ";
    $input = trim(fgets(STDIN));
    
    if (strlen($input) != 4 || !preg_match('/^[A-C1-3]{4}$/', $input)) {
        echo "Código inválido. Debe tener 4 caracteres (letras A-C, números 1-3).\n";
        continue;
    }

    $result = [];
    $used = array_fill(0, 4, false);

    for ($i = 0; $i < 4; $i++) {
        if ($input[$i] === $code[$i]) {
            $result[] = "Correcto";
            $used[$i] = true;
        } elseif (strpos($code, $input[$i]) !== false && !$used[array_search($input[$i], str_split($code))]) {
            $result[] = "Presente";
        } else {
            $result[] = "Incorrecto";
        }
    }

    echo implode(", ", $result) . "\n";

    if ($input === $code) {
        echo "¡Felicidades! Descifraste el código: {$code}\n";
        exit;
    }

    $attempts--;
}

echo "Lo siento, no lograste descifrar el código: {$code}\n";