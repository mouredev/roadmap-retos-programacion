//#27 - { retosparaprogramadores } Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)

/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */

// https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
/* In object-oriented programming, the open–closed principle (OCP) states "software entities (classes,
 modules, functions, etc.) should be open for extension, but closed for modification"; that is, such 
 an entity can allow its behaviour to be extended without modifying its source code.

The name open–closed principle has been used in two ways. Both ways use generalizations (for instance,
 inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and
  results are different. */

let log = console.log;

// Check if running in a browser environment
const isBrowser = typeof window !== 'undefined';

// Conditional check for browser environment
if (isBrowser) {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #27.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #27. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #27');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #27');
}


// Base Operation class
abstract class Operation {
    abstract execute(a: number, b: number): number;
}

// Concrete operations
class Addition extends Operation {
    execute(a: number, b: number): number {
        return a + b;
    }
}

class Subtraction extends Operation {
    execute(a: number, b: number): number {
        return a - b;
    }
}

class Multiplication extends Operation {
    execute(a: number, b: number): number {
        return a * b;
    }
}

class Division extends Operation {
    execute(a: number, b: number): number {
        if (b === 0) throw new Error('Division by zero');
        return a / b;
    }
}

// Custom operation for dynamically added operations
class CustomOperation extends Operation {
    private action: (a: number, b: number) => number;

    constructor(action: string) {
        super();
        // Use a safe function constructor to evaluate the action
        this.action = new Function('a', 'b', `return ${action};`) as (a: number, b: number) => number;
    }

    execute(a: number, b: number): number {
        return this.action(a, b);
    }
}

// Calculator class
class Calculator {
    private operations: { [key: string]: Operation } = {};

    addOperation(name: string, operation: Operation) {
        this.operations[name] = operation;
    }

    calculate(operationName: string, a: number, b: number): number {
        const operation = this.operations[operationName];
        if (!operation) {
            throw new Error('Operation not supported');
        }
        return operation.execute(a, b);
    }

    // Browser-specific method to add a button for the operation
    addButton(name: string, sign: string) {
        if (!isBrowser) return; // Only run in the browser

        const buttonBox = document.getElementById('button_box');
        if (!buttonBox) return;

        const button = document.createElement('button');
        button.innerText = sign;
        button.className = 'button';
        button.onclick = () => this.handleButtonClick(name);
        button.title = name;
        buttonBox.appendChild(button);
    }

    // Browser-specific method to handle button clicks
    handleButtonClick(operationName: string) {
        const a = parseFloat(prompt("Enter first number:") || "0");
        const b = parseFloat(prompt("Enter second number:") || "0");
        const result = this.calculate(operationName, a, b);
        const display = document.getElementById('display') as HTMLInputElement;
        if (display) {
            display.value = result.toString();
        }
    }
}

// Browser-specific UI logic
if (isBrowser) {
    const calculator = new Calculator();
    calculator.addOperation('add', new Addition());
    calculator.addOperation('subtract', new Subtraction());
    calculator.addOperation('multiply', new Multiplication());
    calculator.addOperation('divide', new Division());

    // Create the calculator UI
    const { display, buttonBox, addOperationButton, operationNameInput, operationActionInput, operationSignInput } = createCalculator();

    // Add buttons for the default operations
    calculator.addButton('add', '+');
    calculator.addButton('subtract', '-');
    calculator.addButton('multiply', '*');
    calculator.addButton('divide', '/');

    // Handle adding new operations
    addOperationButton.onclick = function () {
        const name = operationNameInput.value;
        const action = operationActionInput.value;
        const sign = operationSignInput.value;

        if (!name || !action || !sign) {
            alert('You have to fill all the fields: name, operation, and sign!');
            return;
        }

        // Add the new operation
        calculator.addOperation(name, new CustomOperation(action));
        calculator.addButton(name, sign);

        // Clear input fields
        operationNameInput.value = '';
        operationActionInput.value = '';
        operationSignInput.value = '';
    };
}

// Node.js specific logic
if (!isBrowser) {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const calculator = new Calculator();
    calculator.addOperation('add', new Addition());
    calculator.addOperation('subtract', new Subtraction());
    calculator.addOperation('multiply', new Multiplication());
    calculator.addOperation('divide', new Division());

    function promptUser() {
        rl.question('Enter operation (add, subtract, multiply, divide, or "add-operation" to add a new operation): ', (operation: string) => {
            if (operation === 'exit') {
                rl.close();
                return;
            }

            if (operation === 'add-operation') {
                rl.question('Enter operation name: ', (name: string) => {
                    rl.question('Enter operation action (e.g., a + b): ', (action: string) => {
                        rl.question('Enter operation sign: ', (sign: string) => {
                            calculator.addOperation(name, new CustomOperation(action));
                            console.log(`Operation "${name}" added successfully!`);
                            promptUser(); // Prompt again for the next operation
                        });
                    });
                });
            } else {
                rl.question('Enter first number: ', (firstNum: string) => {
                    rl.question('Enter second number: ', (secondNum: string) => {
                        const a = parseFloat(firstNum);
                        const b = parseFloat(secondNum);
                        try {
                            const result = calculator.calculate(operation, a, b);
                            console.log(`Result: ${result}`);
                        } catch (error) {
                            if (error instanceof Error) {
                                console.error(error.message);
                            } else {
                                console.error('An unknown error occurred');
                            }
                        }
                        promptUser(); // Prompt again for the next operation
                    });
                });
            }
        });
    }

    promptUser();
}

// Factory function to create calculator UI in the browser
function createCalculator() {
    if (!isBrowser) {
        throw new Error("This function can only be run in a browser environment.");
    }

    const calcWrapper = document.createElement('div');
    calcWrapper.id = 'calc_wrapper';
    document.body.appendChild(calcWrapper);

    const display = document.createElement('input');
    display.type = 'text';
    display.id = 'display';
    display.disabled = true;
    calcWrapper.appendChild(display);

    const buttonBox = document.createElement('div');
    buttonBox.id = 'button_box';
    calcWrapper.appendChild(buttonBox);

    const addOperationSection = document.createElement('div');
    const operationNameInput = document.createElement('input');
    operationNameInput.placeholder = 'Operation Name';
    const operationActionInput = document.createElement('input');
    operationActionInput.placeholder = 'Operation Action (e.g., a + b)';
    const operationSignInput = document.createElement('input');
    operationSignInput.placeholder = 'Operation Sign';
    const addOperationButton = document.createElement('button');
    addOperationButton.innerText = 'Add Operation';

    addOperationSection.appendChild(operationNameInput);
    addOperationSection.appendChild(operationActionInput);
    addOperationSection.appendChild(operationSignInput);
    addOperationSection.appendChild(addOperationButton);
    calcWrapper.appendChild(addOperationSection);

    const style = document.createElement('style');
    style.innerHTML = `
        body {
            text-align: center;
            background: #070707;
        }
        #calc_wrapper {
            position: relative;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -20%);
            background: rgba(0,0,0,0.2);
            width: 40vw;
            min-height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 10px;
            border: 1px solid yellow;
            border-radius: 15px;
        }
        #display {
            background: #c7c7c7;
            width: 38vw;
            height: 18px;
            border: 1px solid #fff;
            border-radius: 5px;
            padding-left: 10px;
            margin-bottom: 5px;
        }
        #button_box {
            width: 38vw;
            min-height: 180px;
            display: flex;
            flex-flow: row wrap;
            justify-content: flex-start;
            align-items: flex-start;
            padding: 2px 5px;
            border: 1px solid #fff;
            border-radius: 5px; 
            margin-bottom: 5px;       
        }
        .button {
            flex: 1 1 20%;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 5px;
            border: 1px solid #fff;
            border-radius: 2px;        
        }
    `;
    document.head.appendChild(style);

    return { display, buttonBox, addOperationButton, operationNameInput, operationActionInput, operationSignInput };
}