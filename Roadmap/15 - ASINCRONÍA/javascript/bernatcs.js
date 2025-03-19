// ** EJERCICIO

function funcionAsincrona(seg){
    console.log(`Esta función se llama ${funcionAsincrona.name} y acaba de empezar.\nLa función va a durar ${seg} segundos`)

    setTimeout(function() {
        console.log('La función ya ha terminado')
    }, seg*1000);
}

// funcionAsincrona(3)

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------------------

function funcA() {
    setTimeout(() => {
        console.log('Ha acabado la función A')
    }, 1000)
}

function funcB() {
    setTimeout(() => {
        console.log('Ha acabado la función B')
    }, 2000)
}

function funcC() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Ha acabado la función C')
            resolve()
        }, 3000)
    })
}

function funcD() {
    setTimeout(() => {
        console.log('Ha acabado la función D')
    }, 1000)
}

funcA()
funcB()
funcC()
    .then(() => funcD())


// -----------

function funcA2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Ha acabado la función A2');
            resolve();
        }, 1000);
    });
}

function funcB2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Ha acabado la función B2');
            resolve();
        }, 2000);
    });
}

function funcC2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Ha acabado la función C2');
            resolve();
        }, 3000);
    });
}

function funcD2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Ha acabado la función D2');
            resolve();
        }, 1000);
    });
}

async function ejecutarEnOrden() {
    await Promise.all([funcA2(), funcB2(), funcC2()]);
    await funcD2();
}

ejecutarEnOrden();