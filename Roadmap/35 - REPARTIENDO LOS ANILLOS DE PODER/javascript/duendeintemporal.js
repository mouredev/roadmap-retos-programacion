
//#35 - REPARTIENDO LOS ANILLOS DEL PODER
/*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */

const log = console.log;

// Function to check if a number is prime
const isPrime = (num) => {
    if (num <= 1) return false; // Numbers less than or equal to 1 are not prime
    if (num <= 3) return true; // 2 and 3 are prime numbers
    if (num % 2 === 0 || num % 3 === 0) return false; // Eliminate even numbers and multiples of 3

    // Check for factors from 5 to the square root of num
    for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false; // Check i and i + 2
    }
    return true; // If no factors were found, num is prime
};

// Function to find the largest prime number less than a given number
const firstPrime = (num) => {
    for (let i = num - 1; i >= 2; i--) {
        if (isPrime(i)) return i; // Return the first prime found
    }
    return 2; // Return 2 if no prime found (should not happen for valid input)
};

const isOdd = (num) => {
    return num % 2 !== 0; // Return true if the number is odd
};

// Function to assign rings based on the rules
function assignRings(num) {
    // Check if the number of rings is odd and greater than or equal to 7
    if (!isOdd(num) || num < 7) {
        log('The number of rings must be an odd number and greater than or equal to 7');
        start(); // Prompt for input again
        return;
    }

    let arr_of_rings = [0, 0, 0, 1]; // Sauron always gets 1 ring
    let fPrime = firstPrime(num); // Find the largest prime less than num
    let r = num - fPrime; // Remaining rings after giving to Dwarves

    // Adjust remaining rings if less than 4
    if (r < 4) {
        fPrime = firstPrime(num - 3)
        r = num - fPrime; 
    }

    // Distribute rings based on the remaining count
    if (r === 4) {
        arr_of_rings[0] = (r / 2) - 1; // Elves
        arr_of_rings[1] = fPrime;      // Dwarves
        arr_of_rings[2] = r / 2;        // Men
    } else if (r === 6) {
        arr_of_rings[0] = Math.round(((r - 1) / 2)); // Elves
        arr_of_rings[1] = fPrime;      // Dwarves
        arr_of_rings[2] = Math.floor((r - 1) / 2); // Men
    } else if (r === 8) {
        arr_of_rings[0] = Math.floor((r - 1) / 2); // Elves
        arr_of_rings[1] = fPrime;      // Dwarves
        arr_of_rings[2] = Math.round(((r - 1) / 2)); // Men
    } else {
        // Alternative distribution logic for other values of r
        alternativeDistribution(arr_of_rings, fPrime, r);
    }

    // Output the distribution of rings
    log('\n');
    log(`${arr_of_rings[0]} rings to: Elves, ${arr_of_rings[1]} rings to: Dwarves, ${arr_of_rings[2]} rings to: Men, and ${arr_of_rings[3]} ring to: Sauron`);
    rl.close(); // Close the readline interface after showing the result
}

function alternativeDistribution(arr_of_rings, fPrime, r) {
    // Dwarves get the prime
    arr_of_rings[1] = fPrime; // Dwarves
    arr_of_rings[3] = 1; // Sauron gets 1 ring

    // Calculate remaining rings after assigning to Dwarves and Sauron
    let remainingForElvesAndMen = r - arr_of_rings[3]; // Only subtract Sauron's ring

    // Ensure Elves get an odd number and Men get an even number
    
    if(isOdd(remainingForElvesAndMen)){
        arr_of_rings[0] = Math.max(1, Math.round(remainingForElvesAndMen / 2)); // Ensure Elves get an odd number
        arr_of_rings[2] = remainingForElvesAndMen - arr_of_rings[0]; // Calculate remaining rings for Men
    }else{
        log("It's not possible to do the distribution accordly with the getRandomValues.");
    }
        

}

// Set up readline interface for user input
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// Function to start the input process
const start = () => {
    rl.question('Indicate the number of rings to distribute: ', (answer) => {
        let totalRings = parseInt(answer); 
        if (!isNaN(totalRings)) {
            assignRings(totalRings); 
        } else {
            log('Please enter a valid number.'); // Prompt for valid input
            start(); // Prompt again for valid input
        }
    });
};

console.clear(); 
start(); 
