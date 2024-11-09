// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function distributeRings(totalRings) {
    const sauronRings = 1;
    let remainingRings = totalRings - sauronRings;

    // Try different combinations for elves and dwarves
    for (let elvesRings = 1; elvesRings < remainingRings; elvesRings += 2) {  // Elves get odd numbers
        for (let dwarvesRings = 2; dwarvesRings < remainingRings; dwarvesRings++) {
            if (isPrime(dwarvesRings)) {  // Dwarves get prime numbers
                const humansRings = remainingRings - elvesRings - dwarvesRings;
                if (humansRings > 0 && humansRings % 2 === 0) {  // Humans get even numbers
                    return {
                        Elves: elvesRings,
                        Dwarves: dwarvesRings,
                        Humans: humansRings,
                        Sauron: sauronRings
                    };
                }
            }
        }
    }
    return "Error: No valid distribution found.";
}

// Example usage
const totalRings = 20;
console.log(distributeRings(totalRings));
