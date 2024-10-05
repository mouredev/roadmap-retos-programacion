// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>
#include <algorithm>

using namespace std;

// Casas
vector<string> houses = {"Frontend", "Backend", "Mobile", "Data"};

// Preguntas y asignación de puntos
struct Question {
    string question;
    vector<int> scores;
};

vector<Question> questions = {
    {"¿Prefieres trabajar en interfaces visuales?", {3, 1, 2, 0}},
    {"¿Te gusta optimizar el rendimiento del servidor?", {0, 3, 1, 1}},
    {"¿Te interesa crear aplicaciones móviles?", {1, 0, 3, 1}},
    {"¿Te apasiona analizar grandes conjuntos de datos?", {0, 1, 0, 3}},
    // 6 preguntas más...
};

vector<int> askQuestions() {
    vector<int> scores(4, 0);
    for (const auto& q : questions) {
        cout << q.question << endl;
        int answer;
        cout << "Responde 1, 2, 3 o 4: ";
        cin >> answer;
        answer -= 1;
        for (int i = 0; i < 4; ++i) {
            scores[i] += q.scores[answer];
        }
    }
    return scores;
}

void sortingHat() {
    string name;
    cout << "¿Cuál es tu nombre? ";
    cin >> name;
    
    vector<int> scores = askQuestions();
    int max_score = *max_element(scores.begin(), scores.end());
    
    vector<string> candidates;
    for (int i = 0; i < 4; ++i) {
        if (scores[i] == max_score) {
            candidates.push_back(houses[i]);
        }
    }

    srand(time(0));
    
    // Si hay empate, selecciona aleatoriamente
    if (candidates.size() > 1) {
        cout << name << ", la decisión ha sido complicada..." << endl;
        cout << name << ", has sido asignado a " << candidates[rand() % candidates.size()] << "." << endl;
    } else {
        cout << name << ", has sido asignado a " << candidates[0] << "." << endl;
    }
}

int main() {
    sortingHat();
    return 0;
}
