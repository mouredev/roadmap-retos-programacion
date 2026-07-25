//#27 - Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)

//https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
/*In object-oriented programming, the open–closed principle (OCP) states "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification";[1] that is, such an entity can allow its behaviour to be extended without modifying its source code.

The name open–closed principle has been used in two ways. Both ways use generalizations (for instance, inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and results are different.*/

let log = console.log;

//Not using Open-Close Principle (OCP)

class SimpleCalculator {
    calculate(operation, a, b) {
        switch (operation) {
            case 'add':
                return a + b;
            case 'subtract':
                return a - b;
            case 'multiply':
                return a * b;
            case 'divide':
                return a / b;
            default:
                throw new Error('Operation not supported');
        }
    }
}

const calculator1 = new SimpleCalculator();
console.log(calculator1.calculate('add', 856, 30)); // 886
console.log(calculator1.calculate('divide', 220, 4423)); // 0.04973999547818223

//Using Open-Close Principle (OCP)


    const title = document.createElement('h1');
    title.textContent = 'Retosparaprogramadores #20.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '20vh');
    title.style.setProperty('margin', '5vw 0');

    document.body.appendChild(title);    

    log('Retosparaprogramadores #27'); 

function createCalculator() {
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
        body{
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
            margin-botton: 5px;
        }

        #button_box{
            width: 38vw;
            min-height: 180px;
            display: flex;
            flex-flow: row wrap;
            justify-content: flex-start;
            align-items: flex-start;
            padding: 2px 5px;
            border: 1px solid #fff;
            border-radius: 5px; 
            margin-botton: 5px;       
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

class Operation {
    execute(a, b) {
        throw new Error('Method not implemented');
    }
}

class Addition extends Operation {
    execute(a, b) {
        return a + b;
    }
}

class Subtraction extends Operation {
    execute(a, b) {
        return a - b;
    }
}

class Multiplication extends Operation {
    execute(a, b) {
        return a * b;
    }
}

class Division extends Operation {
    execute(a, b) {
        return a / b;
    }
}

class Calculator {
    constructor() {
        this.operations = {};
    }

    addOperation(name, sign, operation) {
        this.operations[name] = operation;
        this.addButton(name, sign);
    }

    calculate(operationName, a, b) {
        const operation = this.operations[operationName];
        if (!operation) {
            throw new Error('Operation not supported');
        }
        return operation.execute(a, b);
    }

    addButton(name, sign) {
        const buttonBox = document.getElementById('button_box');
        const button = document.createElement('button');
        button.innerText = sign;
        button.className = 'button';
        button.onclick = () => this.handleButtonClick(name);
        button.title = name;
        buttonBox.appendChild(button);
    }

    handleButtonClick(operationName) {
        const a = parseFloat(prompt("Enter first number:"));
        const b = parseFloat(prompt("Enter second number:"));
        const result = this.calculate(operationName, a, b);
        document.getElementById('display').value = result;
    }
}

const { display, buttonBox, addOperationButton, operationNameInput, operationActionInput, operationSignInput } = createCalculator();

const calculator = new Calculator();
calculator.addOperation('add', '+', new Addition());
calculator.addOperation('sustract', '-', new Subtraction());
calculator.addOperation('multiply', '*', new Multiplication());
calculator.addOperation('divide', '/', new Division());

setTimeout(()=>{
    class CustomOperation extends Operation {
        execute(a, b) {
            return a ** b; 
        }
    }
    calculator.addOperation('powder', '**', new CustomOperation());
    alert('Class Powder added!')
}, 2000)

addOperationButton.onclick = function() {
    const name = operationNameInput.value;
    const action = operationActionInput.value;
    const sign = operationSignInput.value;

    if(!name || !action || !sign){
        alert('You have to fill all the fields name, operation and sign to add a new operation!');
        return;
    }

    // Create a new operation class dynamically
    class CustomOperation extends Operation {
        execute(a, b) {
            return eval(action); // Use eval to execute the action
        }
    }

    //Note: The use of eval(action) to execute the action is a flexible approach, but it comes with security risks, especially if the input can be influenced by users. If the action string contains malicious code, it could lead to vulnerabilities. Consider using a safer alternative if possible.

    // Add the new operation to the calculator
    calculator.addOperation(name, sign, new CustomOperation());

    // Clear input fields
   
    // Clear input fields
    operationNameInput.value = '';
    operationActionInput.value = '';
    operationSignInput.value = '';
};


