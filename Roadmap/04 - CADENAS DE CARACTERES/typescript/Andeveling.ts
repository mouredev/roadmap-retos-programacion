// Operaciones de Strings
// Consultas y acceso
const theString = "Andres Parra es un developer"
console.log("Length: ", theString.length)
console.log("at: ", theString.at(0))
console.log("chartAt: ", theString.charAt(theString.length - 2))
console.log("Charcode: ", theString.charCodeAt(theString.length - 2))
console.log("Code Point: ", theString.codePointAt(theString.length - 4))
console.log("👋".codePointAt(0))


const paragraph = `
Paragraph
This is a paragraph with multiple lines and many cats emojis, I love cats
    `
// Busqueda
console.log("Includes: ", theString.includes("developer"))
console.log("Start with: ", theString.startsWith("Andres"))
console.log("End with: ", theString.endsWith("developer"))
console.log("Index of: ", theString.indexOf("developer"))
console.log("Match: ", theString.match(/developer/));
console.log("Match All: ", [..."a1b2".matchAll(/\d/g)]);
console.log("Paragraph: ", paragraph.search(/cats/))

// Extraccion de subcadenas
console.log("Substring: ", theString.substring(0, 7))
console.log("Slice: ", theString.slice(0, 7))

// Remplazo y division
console.log("Replace: ", theString.replace("developer", "programador"))
console.log("Replace All: ", paragraph.replaceAll("cats", "programador"))
console.log("Split: ", theString.split(" "))

// Cambio de mayusculas y minusculas
console.log("To Upper: ", theString.toUpperCase())
console.log("To Locale Upper: ", theString.toLocaleUpperCase())
console.log("To Lower: ", theString.toLowerCase())
console.log("To Locale Lower: ", paragraph.toLocaleLowerCase())

// Espacios en blanco y relleno
console.log("Trim: ", theString.trim())
console.log("Trim Start: ", theString.trimStart())
console.log("Trim End: ", theString.trimEnd())
console.log("PadStart", "42".padStart(5, "0"))
console.log("PadEnd", "Hi".padEnd(4,"-").padStart(6,"-"))
console.log("-".repeat(19))
