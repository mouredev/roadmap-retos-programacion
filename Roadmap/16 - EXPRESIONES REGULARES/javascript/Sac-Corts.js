const text = "There are 3 cats, 7 dogs and 15 birds in the park.";
const numbers = text.match(/\d+/g) || [];
console.log(numbers);

// Extra Exercise //
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const email = "isaac@gmail.com";
console.log(emailPattern.test(email)); 

const telPattern = /^\d{3}-\d{3}-\d{4}$/;
const number = "899-112-5641";
console.log(telPattern.test(number));

const urlPattern = /^(https?:\/\/)?([\da-z.-]+\.[a-z.]{2,6}|[\d.]+)(:[0-9]{1,5})?(\/[\w.-]*)*\/?(\?[\w=&]*)?(#[\w-]*)?$/i;
const url = "https://retosdeprogramacion.com/roadmap/"
console.log(urlPattern.test(url));