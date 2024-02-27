<?php

function actualizarFork($nombreRama = "main") {
    // Obtener los cambios del repositorio original
    shell_exec("git fetch upstream");

    // Hacer merge de los cambios en la rama local
    shell_exec("git merge upstream/$nombreRama");

    // Enviar los cambios actualizados al fork en GitHub
    shell_exec("git push");
}

// Llamada a la función para actualizar el fork
actualizarFork();
