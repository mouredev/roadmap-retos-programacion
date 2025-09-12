const text: string = 'lor0em 9ip6sum 2 dolor 334, asit am3ed'
const getNumbersRegex: RegExp = /\d/g
console.log(text.match(getNumbersRegex)?.join(''))

// extra

const emailRegex: RegExp  = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
const phoneRegex: RegExp = /^\+?[1-9]\d{1,14}$/
const urlRegex: RegExp  = /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/