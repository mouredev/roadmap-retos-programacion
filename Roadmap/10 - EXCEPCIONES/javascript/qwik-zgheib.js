/* -- exercise */
try {
  let result = 10 / 0;
  console.log("Result:", result);
} catch (error) {
  console.error("Error:", error.message);
} finally {
  console.log("Finished");
}

try {
  let list = [1, 2, 3];
  console.log(list[5]);
} catch (error) {
  console.error("Error:", error.message);
} finally {
  console.log("Finished");
}

/* -- extra challenge */
function processParameters(parameter) {
  try {
    if (typeof parameter !== "number") throw new TypeError("Parameter must be a number");

    if (parameter === 0) throw new RangeError("Parameter cannot be zero");

    throw new Error("This is a custom error");
  } catch (error) {
    console.error("Error:", error.message);
  } finally {
    console.log("Finished");
  }
}

console.log("\nProcessing parameters:");
processParameters(5);
processParameters(0);
processParameters("text");
