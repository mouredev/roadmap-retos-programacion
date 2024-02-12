
// Funciones

// básica
function saludar() {
  console.log('Hola');
}
saludar()

// de flecha
const bienvenida = () => {
  console.log('Bienvenidos!')
}

bienvenida()

// retorna
function obtenerSaludo() {
  return "Hola, Bienvenido!"
}

console.log(obtenerSaludo())

//con parametros
function saludarPersona(nombre) {
  console.log(`Hola, ${nombre} bienvenido!`)
}

saludarPersona('Typescript')

// parametros opcionales
function saludarOpcional(nombre=''){
  console.log(`Hola, ${nombre} bienvenido!`)
}

saludarOpcional('mxtrar23')
saludarOpcional('')

// parametros y retorno
function obtenerSaludarPersona(nombre) {
  return `Hola, ${nombre} bienvenidos!`
}

console.log(obtenerSaludarPersona('Devs'))

// retorno con dispercion 
function obtenerSaludoMultipleArray() {
  return ['Hola','Bienvenidos']
}

const [saludoText,bienvenidaText] = obtenerSaludoMultipleArray()

console.log(saludoText,bienvenidaText);

function obtenerSaludoMultipleObject() {
  return {
    saludoObj:'Hola',
    bienvenidaObj:'Bienvenidos'
  }
}

const {saludoObj,bienvenidaObj} = obtenerSaludoMultipleObject()

console.log(saludoObj,bienvenidaObj);

// multiples parametros
function SaludoMultiple (...rest){
  rest.forEach(el => {
    console.log(`Hola, ${el}`);
  });
}

SaludoMultiple('Mundo','Typescript','Devs','Mxtrar23')


// parametros con palabra clave de Objeto
function saludoClave (data){
  Object.keys(data).forEach(e=>{
    console.log(`{${e}} =  {${data[e]}}`);
  })
}

saludoClave({
  language:'TypeScript',
  name:'Arb',
  alias:'Mxtrar23',
  edad:29
});


// funcion anónima
(()=>{
  console.log('Ejecución de Funcion anónima')
})();

//function intera
function funcionExterna(){
  function functionInterna(){
    console.log('Saludos desde dentro');
  }
  functionInterna()
}

funcionExterna()

//calback
function funcionretornoEnParametro(n1,n2,callback){
  callback(n1+n2)
}

funcionretornoEnParametro(5,2,(n)=>console.log('La suma es ',n))

const variabelGlobal = 'Typescript'

function misVariables() {
  const varibaleLocal = 'Bienvenido'
  console.log(varibaleLocal,variabelGlobal);
}

console.log(variabelGlobal);
misVariables()

//Dificultad Extra

function remplaza(str1,str2){
  let count =0
  for (let num = 1; num <=100; num++) {
    if(num%3==0 && num%5==0){
      console.log(`${str1}${str2}`);
    } else if (num%3==0){
      console.log(`${str1}`);
    } else if (num%5==0){
      console.log(`${str2}`);
    } else{
      count++
      console.log(`${num}`);
    }
  }
  return count
}

console.log(remplaza('Mde3','Mde5'))