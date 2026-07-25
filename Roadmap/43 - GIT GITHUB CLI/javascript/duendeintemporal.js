//43 - GIT GITHUB CLI 
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

let log = console.log;

const { exec } = require('child_process');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let currentDirectory = process.cwd();
let currentBranch = 'main';
let remoteRepository = '';

function runGitCommand(command) {
  return new Promise((resolve, reject) => {
    exec(`git ${command}`, { cwd: currentDirectory }, (error, stdout, stderr) => {
      if (error) {
        reject(stderr);
      } else {
        resolve(stdout.trim());
      }
    });
  });
}

async function main() {
  log('Welcome to the GitHub Universe 2024 CLI!');

  while (true) {
    const options = [
      '1. Set working directory',
      '2. Create new repository',
      '3. Create new branch',
      '4. Switch branch',
      '5. Show pending files',
      '6. Commit changes',
      '7. Show commit history',
      '8. Delete branch',
      '9. Set remote repository',
      '10. Pull from remote',
      '11. Push to remote',
      '12. Exit'
    ];

    log('\nPlease select an option:');
    log(options.join('\n'));

    const choice = await new Promise(resolve => rl.question('Enter your choice: ', resolve));

    switch (choice) {
      case '1':
        currentDirectory = await new Promise(resolve => rl.question('Enter the new working directory: ', resolve));
        log(`Working directory set to: ${currentDirectory}`);
        break;
      case '2':
        const newRepoName = await new Promise(resolve => rl.question('Enter the name of the new repository: ', resolve));
        await runGitCommand(`init ${newRepoName}`);
        log(`New repository created: ${newRepoName}`);
        break;
      case '3':
        const newBranchName = await new Promise(resolve => rl.question('Enter the name of the new branch: ', resolve));
        await runGitCommand(`checkout -b ${newBranchName}`);
        currentBranch = newBranchName;
        log(`New branch created: ${newBranchName}`);
        break;
      case '4':
        const branchToSwitch = await new Promise(resolve => rl.question('Enter the name of the branch to switch to: ', resolve));
        await runGitCommand(`checkout ${branchToSwitch}`);
        currentBranch = branchToSwitch;
        log(`Switched to branch: ${branchToSwitch}`);
        break;
      case '5':
        const pendingFiles = await runGitCommand('status --porcelain');
        log('Pending files:');
        log(pendingFiles);
        break;
      case '6':
        await runGitCommand('add .');
        const commitMessage = await new Promise(resolve => rl.question('Enter the commit message: ', resolve));
        await runGitCommand(`commit -m "${commitMessage}"`);
        log('Changes committed successfully');
        break;
      case '7':
        const commitHistory = await runGitCommand('log --oneline');
        log('Commit history:');
        log(commitHistory);
        break;
      case '8':
        const branchToDelete = await new Promise(resolve => rl.question('Enter the name of the branch to delete: ', resolve));
        await runGitCommand(`branch -d ${branchToDelete}`);
        log(`Branch ${branchToDelete} deleted`);
        break;
      case '9':
        remoteRepository = await new Promise(resolve => rl.question('Enter the URL of the remote repository: ', resolve));
        await runGitCommand(`remote add origin ${remoteRepository}`);
        log(`Remote repository set to: ${remoteRepository}`);
        break;
        case '10':
            await runGitCommand(`pull origin ${currentBranch}`);
            log('Pulled changes from remote repository');
            break;
          case '11':
            await runGitCommand(`push -u origin ${currentBranch}`);
            log('Pushed changes to remote repository');
            break;
          case '12':
            log('Exiting the GitHub Universe 2024 CLI...');
            rl.close();
            return;
          default:
            log('Invalid choice. Please try again.');
            break;
    }
  }
}  
          main();