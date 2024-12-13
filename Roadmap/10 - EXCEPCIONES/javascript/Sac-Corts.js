// Exercise // 
function divide(a, b) { 
    try {
        if (b === 0) {
            throw new Error("Cannot divide by 0.");
        } 
        return a / b;
    } catch (error) {
        console.error('Error:', error.message);
    } finally {
        console.log("Division operation completed.");
    }
}

divide(10, 0);

// Extra Exercise // 
class CustomError extends Error {
    constructor(message) {
        super(message);
        this.name = "CustomError";
    }
}

function processParameters(param) {
    try {
        if (param < 0) {
            throw new RangeError("The parameter must not be negative.");
        } 
        if (typeof param !== 'number') {
            throw new TypeError("The parameter must be a number");
        } 
        if (param === 0) {
            throw new CustomError("The parameter must no be zero");
        }
        return `The parameter ${param} was processed correctly.`
    } catch (error) {
        console.error(`Caught error: ${error.name} - ${error.message}`);
        throw error;
    }
}

try {
    let result = processParameters("Hi");
    console.log(result);
    console.log("No error occurred.");
} catch (error) {} finally {
    console.log("The execution ended.");
}




