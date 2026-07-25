/**
 * Async function to simulate a timed execution.
 * @param name Name of the function.
 * @param timeInSeconds Time until the function ends in seconds.
 * @returns Promise<void>
 */
function asyncFunction(name: string, timeInSeconds: number): Promise<void> {
  return new Promise((resolve) => {
    console.log(`${name}: Inicia la ejecución (⌚ ${timeInSeconds}s)`);
    setTimeout(() => {
      console.log(`${name}: Finaliza la ejecución`);
      resolve();
    }, timeInSeconds * 1000);
  });
}

(() => {
  // Run functions C, B and A in parallel
  Promise.all([
    asyncFunction("C", 3),
    asyncFunction("B", 2),
    asyncFunction("A", 1),
  ])
    // Run function D after the previous functions have been executed successfully
    .then(() => asyncFunction("D", 1))
    // Handle errors if something goes wrong
    .catch((err) => console.log(err));
})();
