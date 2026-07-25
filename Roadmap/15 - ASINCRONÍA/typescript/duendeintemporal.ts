//#15 { retosparaprogramadores } ASINCRONÍA 

// Short for console.log()
const log = console.log;

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #15.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #15. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #15');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #15');
}

/**
 * Simulates an asynchronous function that runs for a specified number of seconds.
 * @param name - The name of the function.
 * @param seconds - The duration in seconds that the function should run.
 * @returns A promise that resolves when the function completes.
 */
function runFunc(name: string, seconds: number): Promise<void> {
    return new Promise((resolve) => {
        log(`${name} - Start at: ${new Date().toLocaleTimeString()}`);
        log(`${name} - Last: ${seconds} seconds`);

        setTimeout(() => {
            log(`${name} - Ends at: ${new Date().toLocaleTimeString()}`);
            resolve();
        }, seconds * 1000);
    });
}

/**
 * Runs multiple asynchronous functions in parallel and then runs a final function sequentially.
 */
async function runFunces(): Promise<void> {
    // Run functions C, B, and A in parallel
    const functionC = runFunc('Function C', 3);
    const functionB = runFunc('Function B', 2);
    const functionA = runFunc('Function A', 1);

    // Wait for all functions to complete
    await Promise.all([functionC, functionB, functionA]);

    // Run function D sequentially after the others complete
    await runFunc('Function D', 1);
}

// Execute the main function
runFunces();

/* Logs: 
         Function C - Start at: 13:01:18
         Function C - Last: 3 seconds
         Function B - Start at: 13:01:18
         Function B - Last: 2 seconds
         Function A - Start at: 13:01:18
         Function A - Last: 1 seconds
         Function A - Ends at: 13:01:19
         Function B - Ends at: 13:01:20
         Function C - Ends at: 13:01:21
         Function D - Start at: 13:01:21
         Function D - Last: 1 seconds
         Function D - Ends at: 13:01:22
*/