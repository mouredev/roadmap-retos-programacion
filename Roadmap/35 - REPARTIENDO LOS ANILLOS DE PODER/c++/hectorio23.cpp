// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void distributeRings(int totalRings) {
    int sauronRings = 1;
    int remainingRings = totalRings - sauronRings;
    
    // Try different combinations for elves and dwarves
    for (int elvesRings = 1; elvesRings < remainingRings; elvesRings += 2) {  // Elves get odd numbers
        for (int dwarvesRings = 2; dwarvesRings < remainingRings; dwarvesRings++) {
            if (isPrime(dwarvesRings)) {  // Dwarves get prime numbers
                int humansRings = remainingRings - elvesRings - dwarvesRings;
                if (humansRings > 0 && humansRings % 2 == 0) {  // Humans get even numbers
                    cout << "Elves: " << elvesRings << ", Dwarves: " << dwarvesRings 
                         << ", Humans: " << humansRings << ", Sauron: " << sauronRings << endl;
                    return;
                }
            }
        }
    }
    cout << "Error: No valid distribution found." << endl;
}

int main() {
    int totalRings = 20;
    distributeRings(totalRings);
    return 0;
}
