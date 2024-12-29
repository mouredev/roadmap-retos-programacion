/*
 * EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita 
 * interactuar con Git y GitHub de manera real desde terminal.
 * 
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
 *
 * Puedes intentar controlar los diferentes errores.
 */

const fs = require("fs");
const { chdir, cwd } = require("process");
const { exec } = require('child_process');
const readLine = require("readline");
const { stdin: input, stdout: output } = require("process");
const rl = readLine.createInterface({ input, output });
let menuText = "\n1. Establecer el directorio de trabajo.\n2. Crear un nuevo repositorio.\n3. Crear una nueva rama.\n4. Cambiar de rama.\n5. Mostrar ficheros pendientes de hacer commit.\n6. Hacer commit (junto con un add de todos los ficheros).\n7. Mostrar el historial de commits.\n8. Eliminar rama.\n9. Establecer repositorio remoto.\n10. Hacer pull.\n11. Hacer push.\n12. Salir.\n";

function runCommand(command) {
  exec(command, (error, stdout) => {
    if (error) {
      console.log(`\nOcurrió un error: ${error}`);
    } else {
      console.log(`\n${stdout}`);
    }
  });
}

function menuCLI() {
  console.log(`\nDirectorio actual: ${cwd()}`);

  rl.question(menuText, (answer) => {
    let option = parseInt(answer, 10);

    if (option === 1) {
      rl.question("\nIngresa el directorio: ", (path) => {
        try {
          chdir(path);
        } catch (error) {
          console.log(`\nEl directorio no existe: ${error}`);
        }

        menuCLI();
      });
    } else if (option === 2) {
      if (fs.existsSync(`${cwd()}/.git`)) {
        console.log("\nYa se ha inicializado un repositorio.");
      } else {
        runCommand("git init && git branch -M main");
      }

      menuCLI();
    } else if (option  === 3) {
      rl.question("\nIngresa el nombre de la rama que quieres crear: ", (branch) => {
        runCommand(`git branch ${branch}`);
        menuCLI();
      });
    } else if (option === 4) {
      rl.question("\nIngresa el nombre de la rama a la cual quieres cambiar: ", (branch) => {
        runCommand(`git checkout ${branch}`);
        menuCLI();
      });
    } else if (option === 5) {
      runCommand("git status");
      menuCLI();
    } else if (option === 6) {
      runCommand("git add .");

      rl.question("\nIngresa el mensaje del commit: ", (message) => {
        runCommand(`git commit -m "${message}"`);
        menuCLI();
      });
    } else if (option === 7) {
      runCommand("git log");
      menuCLI();
    } else if (option === 8) {
      rl.question("\nIngresa el nombre de la rama que quieres eliminar: ", (branch) => {
        runCommand(`git branch -D ${branch}`);
        menuCLI();
      });
    } else if (option === 9) {
      rl.question("\nIngresa la URL del repositorio: ", (url) => {
        runCommand(`git remote add origin ${url}`);
        menuCLI();
      });
    } else if (option === 10) {
      rl.question("\nIngresa el nombre de la rama que quieres fusionar: ", (branch) => {
        runCommand(`git pull origin ${branch}`);
        menuCLI();
      });
    } else if (option === 11) {
      rl.question("\nIngresa el nombre de la rama: ", (branch) => {
        runCommand(`git push -u origin ${branch}`);
        menuCLI();
      });
    } else if (option === 12) {
      console.log("Cerrando CLI...");

      return rl.close();
    }
    else {
      console.log("\nSelecciona una de las opciones del menú.");

      menuCLI();
    }
  });
}

menuCLI();
