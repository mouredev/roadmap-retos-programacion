// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const readline = require("readline");
const { execSync } = require("child_process");

// Configurar readline para manejar entradas del usuario
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// Función para solicitar entrada al usuario de forma síncrona
const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));

// Opciones del CLI con nombres descriptivos
const actions = {
    1: { name: "Set working directory", action: async () => {
        const path = await prompt("Enter the working directory path: ");
        try {
            process.chdir(path);
            console.log(`Working directory set to ${process.cwd()}`);
        } catch (err) {
            console.error("Invalid directory path.");
        }
    }},
    2: { name: "Create a new repository", action: () => execSync("git init", { stdio: "inherit" }) },
    3: { name: "Create a new branch", action: async () => {
        const branch = await prompt("Enter branch name: ");
        execSync(`git branch ${branch}`, { stdio: "inherit" });
    }},
    4: { name: "Switch branch", action: async () => {
        const branch = await prompt("Enter branch name: ");
        execSync(`git checkout ${branch}`, { stdio: "inherit" });
    }},
    5: { name: "Show pending files", action: () => execSync("git status", { stdio: "inherit" }) },
    6: { name: "Commit changes", action: async () => {
        const message = await prompt("Enter commit message: ");
        execSync("git add .", { stdio: "inherit" });
        execSync(`git commit -m "${message}"`, { stdio: "inherit" });
    }},
    7: { name: "Show commit history", action: () => execSync("git log --oneline", { stdio: "inherit" }) },
    8: { name: "Delete branch", action: async () => {
        const branch = await prompt("Enter branch name to delete: ");
        execSync(`git branch -d ${branch}`, { stdio: "inherit" });
    }},
    9: { name: "Set remote repository", action: async () => {
        const remoteUrl = await prompt("Enter remote repository URL: ");
        execSync(`git remote add origin ${remoteUrl}`, { stdio: "inherit" });
    }},
    10: { name: "Pull changes", action: () => execSync("git pull origin", { stdio: "inherit" }) },
    11: { name: "Push changes", action: () => execSync("git push origin", { stdio: "inherit" }) },
    12: { name: "Exit", action: () => {
        console.log("Goodbye!");
        rl.close();
        process.exit(0);
    }},
};

// Loop principal para mostrar opciones y ejecutar comandos
(async function main() {
    while (true) {
        console.log("\nOptions:");
        Object.entries(actions).forEach(([key, { name }]) => {
            console.log(`${key}. ${name}`);
        });

        const choice = await prompt("\nSelect an option: ");
        const actionObj = actions[choice];
        if (actionObj) await actionObj.action();
        else console.log("Invalid option.");
    }
})();
