const text: string = "There are 3 cats, 7 dogs and 15 birds in the park.";
const numbers: string[] = text.match(/\d+/g) || [];
console.log(numbers);

// ** Extra Exercise ** //

const emailPattern: RegExp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const email: string = "isaac@gmail.com";
console.log(emailPattern.test(email)); 

const telPattern: RegExp = /^\d{3}-\d{3}-\d{4}$/;
const number: string = "899-112-5641";
console.log(telPattern.test(number));

const urlPattern: RegExp = /^(https?:\/\/)?([\da-z.-]+\.[a-z.]{2,6}|[\d.]+)(:[0-9]{1,5})?(\/[\w.-]*)*\/?(\?[\w=&]*)?(#[\w-]*)?$/i;
const url: string = "https://retosdeprogramacion.com/roadmap/";
console.log(urlPattern.test(url));
