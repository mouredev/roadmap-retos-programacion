//EJERCICIO
let myText = '4,iS?SbRj*E.g.URXcB5{iST23]-!i';
let regEx = /\d+/g;

console.log('\nTexto de ejemplo:', myText);
console.log(`\nNumeros encontrados: ${myText.match(regEx)}`);

//EXTRA
function validateEmail(email) {
	let emailRegEx = /\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b/gi;
	console.log(
		`\n${email} es un correo electrónico válido?:`,
		emailRegEx.test(email)
	);
}
validateEmail('ricFakeEmail@gmail.com');

function validatePhone(phone) {
	//Formato +58(000)-0000000
	let phoneRegEx = /\+58+(\(\d{3}\))\-(\d{7})/g;
	console.log(
		`\n${phone} es un número telefónico válido?:`,
		phoneRegEx.test(phone)
	);
}
validatePhone('+58(412)-3333333');

function validateUrl(url) {
	let urlRegEx = /[(http(s)?):\/\/(www\.)?\w\d]{2,}\.[a-z]{2,4}\b([-\w\d]*)/gi;
	console.log(`\n${url} es una url válida?`, urlRegEx.test(url));
}
validateUrl('https://github.com/');
