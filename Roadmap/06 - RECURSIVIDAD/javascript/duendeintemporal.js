/*   #06 Recursividad  */
//I use Eloquent Javascript A Modern Introduction to Programming by Marijn Haverbeke for concepts reference.
//I also use Professional JavaScript for web developers by Matt Frisbie.
//and GPT

// short for console.log()
let log = console.log.bind(console);

//A recursive function typically is formed when a function calls itself by name

const countBack = (n)=>{
    log(n);
    if(n == 0) return;
    return countBack(n - 1);
}

log(countBack(100))


// without recursion

const power_v1 = (base, exponent)=> {
   let result; 
    (exponent == 0)? result = 1 : result = base;
    for(let i = 2; i <= exponent; i++){
        result *=  base; 
    }
    return result;
} 

log(power_v1(4,3)); // 64

// with recursion

const power = (base, exponent)=> {
    if (exponent == 0) {
        return 1;
    } else {
        return base * power(base, exponent - 1);
    }
}

log(power(4, 3)); // 64

/*This is rather close to the way mathematicians define exponentiation and
arguably describes the concept more clearly than the looping variant. The
function calls itself multiple times with ever smaller exponents to achieve the
repeated multiplication.

But this implementation has one problem: in typical JavaScript implementa-
tions, it’s about three times slower than the looping version. Running through
a simple loop is generally cheaper than calling a function multiple times. 

In the case of the power function, the inelegant (looping) version is still fairly
simple and easy to read. It doesn’t make much sense to replace it with the
recursive version
*/

//Extra dificulty exercises

const factorial = (n)=>{
    if(n <= 1) return 1;
    return n * factorial(n - 1);
}

log(factorial(5))// 120

//this function return the serie fibonacci until the number passed as parameter
const fibonacciSerie = (n, a = 0, b = 1)=> {
    if (a > n) {
        return [];
    } else {
        return [a].concat(fibonacciSerie(n, b, a + b));
    }
}


log(fibonacciSerie(17)); // Array(8) [ 0, 1, 1, 2, 3, 5, 8, 13 ]

//this function return the number equivalent to the possition in the fibonacci serie

const fibonacciNum = (n)=> {
    if (n === 0) {
        return 0;
    }
    if (n === 1) {
        return 1;
    }
    return fibonacciNum(n - 1) + fibonacciNum(n - 2);
  }

  log(fibonacciNum(17))// 1597

/*Note: The recursive version with memoization is more efficient than the simple recursive one, as it avoids redundant calculations. However, it still uses the call stack, which can be a problem for very large values of a.*/

const fibonacciNumMemo = (n, memo = {})=> {
    if (n in memo) {
        return memo[n];
    }
    if (n === 0) {
        return 0;
    }
    if (n === 1) {
        return 1;
    }
    memo[n] = fibonacciNumMemo(n - 1, memo) + fibonacciNumMemo(n - 2, memo);
    return memo[n];
}

log(fibonacciNumMemo(17)); // 1597



/* The iterative approach is generally more efficient in terms of time and space, as it does not use the call stack of recursion. */

const iterativeFibonacci = (n)=> {
    if (n === 0) return 0;
    if (n === 1) return 1;

    let a = 0;
    let b = 1;
    let resultado;

    for (let i = 2; i <= n; i++) {
        resultado = a + b;
        a = b;
        b = resultado;
    }
    return resultado;
}

log(iterativeFibonacci(4222)); // infinity
log(iterativeFibonacci(453))// 2.0985341020594266e+94  



window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #6.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #6. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #6'); 
});