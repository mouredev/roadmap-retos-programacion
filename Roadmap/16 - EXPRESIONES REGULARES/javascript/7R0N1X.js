const regex = /\-?\d+/;
const str = 'precio: 888'
console.log(str.match(regex))


// DIFICULTAD EXTRA
const emailRegex = /\S+@\S+\.\S+/;
const email = 'admin@mail.com'
emailRegex.test(email) ? console.log(`El correo ${email} es válido.`) : console.log(`El correo ${email} es inválido.`)

const phoneRegex = /^\+?(\d{1,3})?[-.\s]?(\d{2,4})[-.\s]?(\d{3})[-.\s]?(\d{4})$/;
const phoneNumber = '+593 97 999 1222'
phoneRegex.test(phoneNumber) ? console.log(`El número de teléfono ${phoneNumber} es válido.`) : console.log(`El número de teléfono ${phoneNumber} es inválido.`)

const urlRegex = /^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(\/[^\s]*)?$/;
const url = 'https://tronix-portfolio.vercel.app'
urlRegex.test(url) ? console.log(`La url ${url} es válida.`) : console.log(`La url ${url} no es válida.`)