#include <iostream>

using namespace std;

void num_mayorAMenor(int num) {
    cout << num << ' ';

    if (num != 0) num_mayorAMenor(num - 1);
};

int factorial(int num) {
    if (num == 1) return 1;

    return num * factorial(num - 1);
}


int fibonacci(int num) {
    if (num <= 1) return 0;

    else if (num == 2) return 1;

    else return fibonacci(num - 1) + fibonacci(num - 2);
}


int main() {
    cout << "\n [+] Numeros del 100-0: ";
    num_mayorAMenor(100);

    cout << '\n';

    // ************ DIFICULTAD EXTRA ************ //n
    
    cout << "\n [+] Factorial de 5: " << factorial(5);
    cout << '\n';

    cout << "\n [+] Fibonacci Pos 5: " << fibonacci(5);
    cout << '\n';

    return 0;
}