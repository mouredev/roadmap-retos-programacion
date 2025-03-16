// Iteraciones

// loop for
for (let i = 1; i <= 10; i++) 
    {
        console.log(i);
    }
    
    // loop for of
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for(const a of array) 
    {
        console.log(a);
    }
    
    // loop for in
    let objeto = {a:1, b:2, c:3, d:4, e:5, f:6, g:7, h:8, i:9, j:10}
    for (const o in objeto) 
    {
        console.log(objeto[o]);
    }
    
    // DIFICULTAD EXTRA
    
    // loop while
    
    let cont = 0
    
    while(cont < 10)
    {
        cont++
        console.log(cont);
    }
    
    // loop do while
    
    let cont2 = 0
    do
    {
        cont2++
        console.log(cont2);
    }while (cont2 < 10)
    
    // recursividad
    function recursivo(num)
    {
        if(num <= 10)
        {
            console.log(num);
            recursivo(num + 1)
        }
    }
    
    recursivo(1)
    
    // loop forEach()
    
    let array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    array2.forEach(num => console.log(num))
    
    // for of para un string
    
    for(const a of "0123456789") 
    {
        console.log(a);
    }