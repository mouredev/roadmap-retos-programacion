// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <cstdlib>
#include <map>
#include <functional>

// Para chdir en sistemas POSIX
#include <unistd.h> 

// Función para ejecutar comandos del sistema
void runCommand(const std::string& command) {
    system(command.c_str());
}

// Definir acciones con nombres descriptivos
std::map<int, std::pair<std::string, std::function<void()>>> actions = {
    {1, {"Set working directory", [] {
        std::string path;
        std::cout << "Enter the working directory path: ";
        std::cin >> path;
        // Cambiar el directorio de trabajo
        if (chdir(path.c_str()) == 0) 
            std::cout << "Working directory set to " << path << std::endl;
        else
            std::cerr << "Invalid directory path." << std::endl;
    }}},
    {2, {"Create a new repository", [] { runCommand("git init"); }}},
    {3, {"Create a new branch", [] {
        std::string branch;
        std::cout << "Enter branch name: ";
        std::cin >> branch;
        runCommand("git branch " + branch);
    }}},
    {4, {"Switch branch", [] {
        std::string branch;
        std::cout << "Enter branch name: ";
        std::cin >> branch;
        runCommand("git checkout " + branch);
    }}},
    {5, {"Show pending files", [] { runCommand("git status"); }}},
    {6, {"Commit changes", [] {
        std::string message;
        std::cout << "Enter commit message: ";
        std::cin.ignore();
        std::getline(std::cin, message);
        runCommand("git add . && git commit -m \"" + message + "\"");
    }}},
    {7, {"Show commit history", [] { runCommand("git log --oneline"); }}},
    {8, {"Delete branch", [] {
        std::string branch;
        std::cout << "Enter branch name to delete: ";
        std::cin >> branch;
        runCommand("git branch -d " + branch);
    }}},
    {9, {"Set remote repository", [] {
        std::string remoteUrl;
        std::cout << "Enter remote repository URL: ";
        std::cin >> remoteUrl;
        runCommand("git remote add origin " + remoteUrl);
    }}},
    {10, {"Pull changes", [] { runCommand("git pull origin"); }}},
    {11, {"Push changes", [] { runCommand("git push origin"); }}},
    {12, {"Exit", [] {
        std::cout << "Goodbye!" << std::endl;
        exit(0);
    }}},
};

int main() {
    while (true) {
        std::cout << "\nOptions:\n";
        for (const auto& [key, value] : actions)
            std::cout << key << ". " << value.first << std::endl;

        int choice;
        std::cout << "\nSelect an option: ";
        std::cin >> choice;

        if (actions.count(choice)) {
            actions[choice].second();
        } else {
            std::cout << "Invalid option." << std::endl;
        }
    }
    return 0;
}
