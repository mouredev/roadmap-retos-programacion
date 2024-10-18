<?php
class Luchador
{
    public $nombre = "";
    public $velocidad = 0;
    public $ataque = 0;
    public $defensa = 0;
    public $salud = 100;
    public $color = "#000000";

    public function __construct($i, $v)
    {
        if (isset($v)) {
            $this->nombre = "<span class='badge text-bg-info'>" . $i . "</span> " . $v[0];
            $this->velocidad = $this->checkAtributo($v[1]);
            $this->ataque = $this->checkAtributo($v[2]);
            $this->defensa = $this->checkAtributo($v[3]);
        } else {
            $this->nombre = "<span class='badge text-bg-info'>" . $i . "</span> " . $this->nombre();
            $this->velocidad = mt_rand(1, 100);
            $this->ataque =  mt_rand(1, 100);
            $this->defensa = mt_rand(1, 100);
        }
        $this->color = "#" . $this->colorAleatorio();
    }
    private function nombre()
    {
        return ucfirst(strtolower(substr(str_shuffle("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), 0, 6)));
    }
    private function checkAtributo($a)
    {
        if ($a >= 0 && $a <= 100) {
            return $a;
        } else {
            throw new Error("El valor debe estar entre 0 y 100");
        }
    }
    private function colorAleatorio()
    {
        return ucfirst(strtolower(substr(str_shuffle("0123456789ABCDEF"), 0, 6)));
    }
    public function getLuchador()
    {
        $html = "<div class='card mb-4 rounded-3 shadow-sm'><div class='card-header'><h4>";
        $html .= '<svg xmlns="http://www.w3.org/2000/svg" style="color:' . $this->color . '" width="1em" height="1em" fill="currentColor" class="bi bi-person-arms-up flex-shrink-0 me-3" viewBox="0 0 16 16">
<path d="M8 3a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
<path d="m5.93 6.704-.846 8.451a.768.768 0 0 0 1.523.203l.81-4.865a.59.59 0 0 1 1.165 0l.81 4.865a.768.768 0 0 0 1.523-.203l-.845-8.451A1.5 1.5 0 0 1 10.5 5.5L13 2.284a.796.796 0 0 0-1.239-.998L9.634 3.84a.7.7 0 0 1-.33.235c-.23.074-.665.176-1.304.176-.64 0-1.074-.102-1.305-.176a.7.7 0 0 1-.329-.235L4.239 1.286a.796.796 0 0 0-1.24.998l2.5 3.216c.317.316.475.758.43 1.204Z"/>
</svg>';
        $html .= $this->nombre;
        $html .= "</h4></div><div class='card-body'>";
        $html .= "<div class='col d-flex align-items-start mb-0'>";
        $html .= '<svg xmlns="http://www.w3.org/2000/svg" width="1.75em" height="1.75em" fill="currentColor" class="bi bi-crosshair flex-shrink-0 me-3" viewBox="0 0 16 16">
<path d="M8.5.5a.5.5 0 0 0-1 0v.518A7 7 0 0 0 1.018 7.5H.5a.5.5 0 0 0 0 1h.518A7 7 0 0 0 7.5 14.982v.518a.5.5 0 0 0 1 0v-.518A7 7 0 0 0 14.982 8.5h.518a.5.5 0 0 0 0-1h-.518A7 7 0 0 0 8.5 1.018zm-6.48 7A6 6 0 0 1 7.5 2.02v.48a.5.5 0 0 0 1 0v-.48a6 6 0 0 1 5.48 5.48h-.48a.5.5 0 0 0 0 1h.48a6 6 0 0 1-5.48 5.48v-.48a.5.5 0 0 0-1 0v.48A6 6 0 0 1 2.02 8.5h.48a.5.5 0 0 0 0-1zM8 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4"/>
</svg>';
        $html .= "<div><h5 class='fw-bold mb-2 fs-5 text-body-emphasis'>Ataque</h5>";
        $html .= "</div></div>";
        $html .= '<div class="progress" role="progressbar" aria-label="Ataque" aria-valuenow="' . $this->ataque . '" aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar bg-danger" style="width: ' . $this->ataque . '%">' . $this->ataque . '</div></div>';

        $html .= "<div class='col d-flex align-items-start mb-0 mt-3'>";
        $html .= '<svg xmlns="http://www.w3.org/2000/svg" width="1.75em" height="1.75em" fill="currentColor" class="bi bi-bricks flex-shrink-0 me-3" viewBox="0 0 16 16">
        <path d="M0 .5A.5.5 0 0 1 .5 0h15a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5H14v2h1.5a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5H14v2h1.5a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5H.5a.5.5 0 0 1-.5-.5v-3a.5.5 0 0 1 .5-.5H2v-2H.5a.5.5 0 0 1-.5-.5v-3A.5.5 0 0 1 .5 6H2V4H.5a.5.5 0 0 1-.5-.5zM3 4v2h4.5V4zm5.5 0v2H13V4zM3 10v2h4.5v-2zm5.5 0v2H13v-2zM1 1v2h3.5V1zm4.5 0v2h5V1zm6 0v2H15V1zM1 7v2h3.5V7zm4.5 0v2h5V7zm6 0v2H15V7zM1 13v2h3.5v-2zm4.5 0v2h5v-2zm6 0v2H15v-2z"/>
      </svg>';
        $html .= "<div><h5 class='fw-bold mb-2 fs-5 text-body-emphasis'>Defensa</h5>";
        $html .= "</div></div>";
        $html .= '<div class="progress" role="progressbar" aria-label="Defensa" aria-valuenow="' . $this->defensa . '" aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar bg-warning" style="width: ' . $this->defensa . '%">' . $this->defensa . '</div></div>';

        $html .= "<div class='col d-flex align-items-start mb-0 mt-3'>";
        $html .= '<svg xmlns="http://www.w3.org/2000/svg" width="1.75em" height="1.75em" fill="currentColor" class="bi bi-hurricane flex-shrink-0 me-3" viewBox="0 0 16 16">
<path d="M6.999 2.6A5.5 5.5 0 0 1 15 7.5a.5.5 0 0 0 1 0 6.5 6.5 0 1 0-13 0 5 5 0 0 0 6.001 4.9A5.5 5.5 0 0 1 1 7.5a.5.5 0 0 0-1 0 6.5 6.5 0 1 0 13 0 5 5 0 0 0-6.001-4.9M10 7.5a2 2 0 1 1-4 0 2 2 0 0 1 4 0"/>
</svg>';
        $html .= "<div><h5 class='fw-bold mb-2 fs-5 text-body-emphasis'>Velocidad</h5>";
        $html .= "</div></div>";
        $html .= '<div class="progress" role="progressbar" aria-label="Velocidad" aria-valuenow="' . $this->velocidad . '" aria-valuemin="0" aria-valuemax="100">
<div class="progress-bar bg-info" style="width: ' . $this->velocidad . '%">' . $this->velocidad . '</div></div>';
        $html .= "</div><div class='card-footer'><div class='col d-flex align-items-start mb-0'>";
        $html .= '<svg xmlns="http://www.w3.org/2000/svg" idth="1.75em" height="1.75em" fill="currentColor" class="bi bi-battery-half flex-shrink-0 me-3" viewBox="0 0 16 16">
        <path d="M2 6h5v4H2z"/>
        <path d="M2 4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm10 1a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm4 3a1.5 1.5 0 0 1-1.5 1.5v-3A1.5 1.5 0 0 1 16 8"/>
      </svg>';
        $html .= "<div><h5 class='fw-bold mb-0 fs-5 text-body-emphasis'>Salud</h5></div></div>";
        $html .= '<div class="progress" role="progressbar" aria-label="Salud" aria-valuenow="' . $this->salud . '" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-bar bg-success" style="width: ' . $this->salud . '%">' . $this->salud . '</div></div>';
        $html .= "</div></div>";
        return $html;
    }
    public function getNombre()
    {
        $html = "<span>";
        $html .= '<svg xmlns="http://www.w3.org/2000/svg" style="color:' . $this->color . '" width="1em" height="1em" fill="currentColor" class="bi bi-person-arms-up flex-shrink-0 me-3" viewBox="0 0 16 16">
<path d="M8 3a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
<path d="m5.93 6.704-.846 8.451a.768.768 0 0 0 1.523.203l.81-4.865a.59.59 0 0 1 1.165 0l.81 4.865a.768.768 0 0 0 1.523-.203l-.845-8.451A1.5 1.5 0 0 1 10.5 5.5L13 2.284a.796.796 0 0 0-1.239-.998L9.634 3.84a.7.7 0 0 1-.33.235c-.23.074-.665.176-1.304.176-.64 0-1.074-.102-1.305-.176a.7.7 0 0 1-.329-.235L4.239 1.286a.796.796 0 0 0-1.24.998l2.5 3.216c.317.316.475.758.43 1.204Z"/>
</svg>';
        $html .= $this->nombre;
        $html .= '<div class="progress" role="progressbar" aria-label="Salud" aria-valuenow="' . $this->salud . '" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-bar bg-success" style="width: ' . $this->salud . '%">' . $this->salud . '</div></div></span>';
        return $html;
    }
}


function veintePorCiento()
{
    return mt_rand(1, 100) >= 20;
}

function turnoAtaque($i, $j)
{
    $html = '<br>' . $i->salud . ' <svg xmlns="http://www.w3.org/2000/svg" style="color:' . $i->color . '" width="1em" height="1em" fill="currentColor" class="bi bi-person-arms-up flex-shrink-0 me-1" viewBox="0 0 16 16">
    <path d="M8 3a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
    <path d="m5.93 6.704-.846 8.451a.768.768 0 0 0 1.523.203l.81-4.865a.59.59 0 0 1 1.165 0l.81 4.865a.768.768 0 0 0 1.523-.203l-.845-8.451A1.5 1.5 0 0 1 10.5 5.5L13 2.284a.796.796 0 0 0-1.239-.998L9.634 3.84a.7.7 0 0 1-.33.235c-.23.074-.665.176-1.304.176-.64 0-1.074-.102-1.305-.176a.7.7 0 0 1-.329-.235L4.239 1.286a.796.796 0 0 0-1.24.998l2.5 3.216c.317.316.475.758.43 1.204Z"/>
    </svg>';
    $html .= $i->nombre . " ataca - ";
    $html .= $j->salud . ' <svg xmlns="http://www.w3.org/2000/svg" style="color:' . $j->color . '" width="1em" height="1em" fill="currentColor" class="bi bi-person-arms-up flex-shrink-0 me-1" viewBox="0 0 16 16">
            <path d="M8 3a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
            <path d="m5.93 6.704-.846 8.451a.768.768 0 0 0 1.523.203l.81-4.865a.59.59 0 0 1 1.165 0l.81 4.865a.768.768 0 0 0 1.523-.203l-.845-8.451A1.5 1.5 0 0 1 10.5 5.5L13 2.284a.796.796 0 0 0-1.239-.998L9.634 3.84a.7.7 0 0 1-.33.235c-.23.074-.665.176-1.304.176-.64 0-1.074-.102-1.305-.176a.7.7 0 0 1-.329-.235L4.239 1.286a.796.796 0 0 0-1.24.998l2.5 3.216c.317.316.475.758.43 1.204Z"/>
            </svg>';
    $html .= $j->nombre . " defiende ";
    echo $html;
    $t = mt_rand(1, 100);
    if ($t >= 20) {
        $dano = $i->ataque - $j->defensa;
        if ($dano <= 0) {
            $dano = $i->ataque * 0.1;
            $dano = round($dano);
        }
        echo "El ataque ha causado " . $dano . " de daño";
        return $dano;
    } else {
        echo "<span class='badge text-bg-warning'>Esquiva el ataque</span>";
        return  0;
    }
}
function combate($i, $j)
{
    while ($i->salud > 0 && $j->salud > 0) {
        $j->salud -= turnoAtaque($i, $j);
        if ($j->salud > 0) {
            $i->salud -= turnoAtaque($j, $i);
        }
    }

    return ($i->salud > 0) ? $i : $j;
}
function combates($luchadores, $numerodeluchadores)
{
    $html = "<div class='row'>";
    for ($i = 0; $i < $numerodeluchadores; $i++) {
        if ($i == 0) {
            $html .= "<div class='col-sm-3'>";
        }
        if ($i == $numerodeluchadores / 2) {
            $html .= "</div><div class='col-sm-3 offset-sm-6'>";
        }
        if ($i % 2 == 0) {
            $html .= "<div class='card mb-4 rounded-3 shadow-sm'><ul class='list-group'><li class='list-group-item'><h4>" . $luchadores[$i]->getNombre() . "</h4></li>";
        } else if ($i % 2 != 0 && $numerodeluchadores == 2) {
            $html .= "</ul></div></div><div class='col-sm-3 offset-sm-6'><div class='card mb-4 rounded-3 shadow-sm'><ul class='list-group'><li class='list-group-item'><h4>" . $luchadores[$i]->getNombre() . "</h4></li></ul></div>";
        } else {
            $html .= "<li class='list-group-item text-center'>VS</li><li class='list-group-item'><h4>" . $luchadores[$i]->getNombre() . "</h4></li></ul></div>";
        }
    }
    $html.= "</div></div>";
    return $html;
}
?>
<!doctype html>
<html>

<head>
    <meta charset="utf-8" />
    <title>Torneo Dragon Ball</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>

    <main class="container">
        <h1>Comienza el torneo</h1>
        <?php
        $numerodeluchadores = pow(2, 4);
        //Si lo queremos hacer en aleatorio
        // for ($i = 1; $i <= $numerodeluchadores; $i++) {
        //     $luchadores[$i] = new Luchador($i, null);
        // }
        $contendientes = array(
            array("Goku", 89, 85, 90),
            array("Vegeta", 92, 92, 80),
            array("Trunks", 80, 69, 81),
            array("Gohan", 75, 79, 90),
            array("Krillin", 76, 60, 65),
            array("Picollo", 75, 80, 99),
            array("A17", 92, 80, 99),
            array("A18", 79, 70, 99),
            array("Ten", 79, 60, 50),
            array("Chaoz", 30, 30, 30),
            array("Yamcha", 35, 10, 40),
            array("Cabba", 75, 86, 80),
            array("Hit", 89, 30, 99),
            array("Kafla ", 99, 90, 60),
            array("Satan", 1, 1, 1),
            array("Arale", 99, 99, 20),
            

        );
        for ($i = 1; $i <= $numerodeluchadores; $i++) {
            $luchadores[$i] = new Luchador($i, $contendientes[$i - 1]);
        }
        echo "<div class='row row-cols-sm-4 row-cols-xs-2'>";
        for ($i = 1; $i <= $numerodeluchadores; $i++) {
            echo "<div class='luchador col'>" . $luchadores[$i]->getLuchador() . "</div>";
        }
        echo "</div><hr>";
        echo "<h2>Primera Ronda</h2>";

        do {
            shuffle($luchadores);
            echo combates($luchadores, $numerodeluchadores);
            $clasificados = array();
            for ($i = 0; $i < $numerodeluchadores; $i += 2) {
                if ($i % 2 == 0) {
                    if ($luchadores[$i]->velocidad >= $luchadores[$i + 1]->velocidad) {
                        $vencedor = combate($luchadores[$i], $luchadores[$i + 1]);
                    } else {
                        $vencedor = combate($luchadores[$i + 1], $luchadores[$i]);
                    }
                }
                echo "<br><div class='alert alert-success'>El combate entre " . $luchadores[$i]->nombre . " y " . $luchadores[$i + 1]->nombre . " ha concluido con la victoria de <b>" . $vencedor->nombre . "</b></div>";
                $clasificados[] = $vencedor;
            }
            if (count($clasificados) > 1) {
                $numerodeluchadores = count($clasificados);
                if ($numerodeluchadores > 4) {
                    echo "<hr><h3>Siguiente Ronda</h3>";
                } else if ($numerodeluchadores == 4) {
                    echo "<hr><div class='alert alert-warning'><h3 class='text-center'>SEMIFINALES</h3></div>";
                } else {
                    echo "<hr><div class='alert alert-info'><h3 class='text-center'>RONDA FINAL</h3></div>";
                }
                $luchadores = $clasificados;               
            } else {
                echo "<hr><h3>Ganador del torneo</h3><div class='row'>";
                echo '<div class="col-sm-12 iz">' . $clasificados[0]->getLuchador() . '</div></div>';
            }
        } while (count($clasificados) > 1)
        ?>

    </main>
</body>


</html>