function safeDivision(a: number, b: number): number | null {
    try {
        if (b === 0) {
            throw new Error("Cannot divide by 0");
        }
        return a / b;
    } catch (error) {
        console.error("Error caught:", error.message);
        return null;
    } finally {
        console.log("Execution completed");
    }
}

const result = safeDivision(10, 0);
console.log("Result:", result);

// ** Extra Exercise ** //
class CustomeError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "CustomError";
    }
}

function processInput(input: any) {
    try {
        if (typeof input === "string") {
            throw new TypeError("Input cannot be a string");
        }

        if (input === null || input === undefined) {
            throw new ReferenceError("Input cannot be null or undefined");
        }

        if (input < 0) {
            throw new CustomeError("Input cannot be a negative number");
        }

        console.log("Processing input:", input);
    } catch (error) {
        throw error;
    }
}

function execute() {
    try {
        processInput(-10);
        console.log("No error has ocurred");
    } catch (error) {
        console.error(`Error caught: ${error.name} - ${error.message}`);
    } finally {
        console.log("Execution completed");
    }
}

execute();