// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// Estructura para representar el árbol
typedef vector<string> Tree;

void drawTree(const Tree& tree) {
    for (const string& line : tree) {
        cout << line << endl;
    }
    cout << endl;
}

void initializeTree(Tree& tree, int height, bool hasStar) {
    tree.clear();

    if (hasStar) {
        tree.push_back(string(height, ' ') + "@");
    }

    for (int i = 0; i < height; i++) {
        int width = 2 * i + 1;
        string row = string(height - i - 1, ' ') + string(width, '*');
        tree.push_back(row);
    }

    string trunk = string(height - 1, ' ') + "|||";
    tree.push_back(trunk);
    tree.push_back(trunk);
}

void toggleStar(Tree& tree, int height, bool& hasStar) {
    hasStar = !hasStar;
    initializeTree(tree, height, hasStar);
    cout << "Estrella " << (hasStar ? "añadida." : "eliminada.") << endl;
}

void addOrRemove(Tree& tree, int height, char symbol, int count, bool add) {
    srand(time(0));
    int modifications = 0;

    for (int i = 1; i <= height; i++) {
        for (int j = 0; j < tree[i].size(); j++) {
            if (tree[i][j] == (add ? '*' : symbol)) {
                if (add && rand() % 2 == 0 && (j == 0 || tree[i][j - 1] != symbol)) {
                    tree[i][j] = symbol;
                    modifications++;
                } else if (!add && tree[i][j] == symbol) {
                    tree[i][j] = '*';
                    modifications++;
                }
                if (modifications == count) break;
            }
        }
        if (modifications == count) break;
    }

    cout << (add ? "Añadido" : "Eliminado") << " " << modifications << " de " << symbol << ".\n";
}

void toggleLights(Tree& tree, int height, bool& lightsOn) {
    lightsOn = !lightsOn;

    for (int i = 1; i <= height; i++) {
        for (int j = 0; j < tree[i].size(); j++) {
            if (tree[i][j] == (lightsOn ? '*' : '+')) {
                tree[i][j] = lightsOn ? '+' : '*';
            }
        }
    }

    cout << "Luces " << (lightsOn ? "encendidas." : "apagadas.") << endl;
}

int main() {
    int height;
    cout << "Ingresa la altura del árbol: ";
    cin >> height;

    Tree tree;
    bool hasStar = true;
    bool lightsOn = false;

    initializeTree(tree, height, hasStar);

    string option;
    while (true) {
        drawTree(tree);
        cout << "Opciones: [estrella, bolas, luces, apagar, salir]: ";
        cin >> option;

        if (option == "estrella") {
            toggleStar(tree, height, hasStar);
        } else if (option == "bolas") {
            addOrRemove(tree, height, 'o', 2, true);
        } else if (option == "luces") {
            addOrRemove(tree, height, '+', 3, true);
        } else if (option == "apagar") {
            toggleLights(tree, height, lightsOn);
        } else if (option == "salir") {
            cout << "Gracias por decorar el árbol!\n";
            break;
        } else {
            cout << "Opción no válida.\n";
        }
    }

    return 0;
}
