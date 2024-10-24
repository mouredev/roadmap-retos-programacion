//#15 ASINCRONÍA 

// short for console.log()
let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #15.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #15. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #15'); 
});


function runFunc(name, seconds) {
    return new Promise((resolve) => {
        log(`${name} - Start at: ${new Date().toLocaleTimeString()}`);
        log(`${name} - Last: ${seconds} seconds`);

        setTimeout(() => {
            log(`${name} - Ends at: ${new Date().toLocaleTimeString()}`);
            resolve();
        }, seconds * 1000);
    });
}

async function runFunces() {
    const functionC = runFunc('Function C', 3);
    const functionB = runFunc('Function B', 2);
    const functionA = runFunc('Function A', 1);

    await Promise.all([functionC, functionB, functionA]);

    await runFunc('Function D', 1);
}

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