<?php
    $now = date("d/m/Y H:i:s");

    $birth = date("09/03/1975 09:40:25");

    $now = strtotime($now);
    $birth = strtotime($birth);

    $diff = $now - $birth;
    echo "Hoy es el ".date("d/m/Y H:i:s", $now)."\n";
    echo "Naci el ".date("d/m/Y H:i:s", $birth)."\n";

    $diff = $now - $birth;
    $years = floor($diff / (60 * 60 * 24 * 365));
    $months = floor(($diff - $years * 60 * 60 * 24 * 365) / (60 * 60 * 24 * 30));
    $days = floor(($diff - $years * 60 * 60 * 24 * 365 - $months * 60 * 60 * 24 * 30) / (60 * 60 * 24));
    $hours = floor(($diff - $years * 60 * 60 * 24 * 365 - $months * 60 * 60 * 24 * 30 - $days * 60 * 60 * 24) / (60 * 60));
    $minutes = floor(($diff - $years * 60 * 60 * 24 * 365 - $months * 60 * 60 * 24 * 30 - $days * 60 * 60 * 24 - $hours * 60 * 60) / 60);
    $seconds = floor($diff - $years * 60 * 60 * 24 * 365 - $months * 60 * 60 * 24 * 30 - $days * 60 * 60 * 24 - $hours * 60 * 60 - $minutes * 60);

    echo "\n\nHan pasado ".$years." años, ".$months." meses, ".$days." días, ".$hours." horas, ".$minutes." minutos y ".$seconds." segundos desde que nací\n";

    // Extra

    // Muestra la fecha de naciemnteo por patntalla en formato dd/mm/yyyy
    echo date("d/m/Y", $birth)."\n";

    // Muestra la fecha de naciemnteo por patntalla en formato dd/mm/yy

    echo date("d/m/y", $birth)."\n";

    // Muestra la fecha de naciemnteo por patntalla en formato dd de mm de yyyy con el mes en letra (foramto español)
    echo date("d \\d\\e F \\d\\e Y", $birth)."\n";

    // Muestra el dia de la fema que fue el dia de la fecha de nacimeinto

    echo "Naci un ".date("l", $birth)."\n";

    // Muestra que dia del año fue la fecha de nacimiento

    echo "El día de mi nacimiento era el ".date("z", $birth)." dia del año\n";

    // Muestra que semana del año fue la fecha de nacimiento
    echo "La fecha de mi nacimiento estaba en la semana ".date("W", $birth)."\n";

    // Muestra si el año de la fecha de nacimiento es bisiesto
    echo "Mi año de nacimiento ".(date("L", $birth) ? "es" : "no es")." bisiesto\n";

    // Muestra el nombre del mes de la fecha de nacimiento
    echo "Nací en ".date("F", $birth)."\n";

    // Muestra el nombre del mes de la fecha de nacimiento en 3 letras
    echo "Nací en ".date("M", $birth)."\n";

    // Muestra en que decada naci
    echo "Nací en la decada de los ".substr(date("Y", $birth), 2, 1)."0\n";

    // Muestra en que siglo naci
    $century = intval(substr(date("Y", $birth), 0, 2)) +1;
    echo "Nací en el siglo ".$century."\n";

    // Hora de nacimiento en formato 24 horas
    echo "Nací a las ".date("H:i:s", $birth)."\n";

    // Hora de nacimiento en formato 12 horas
    echo "Nací a las ".date("h:i:s a", $birth)."\n";

    

