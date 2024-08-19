function dividir(num1,num2){

  if(num2 === 0){
    throw new Error("No se puede dividir entre cero");
  }
  else{
    return num1/num2;
  }
 
}
function Probar(n1,n2){
    try {
        dividir(n1,n2);
        
    } catch (error) {
        console.log("Erro:",error);
    }
    finally{
        console.log("Intente ingrsar un divisor distinto a 0");
    }
}
Probar(10,0);
//Difucultad Extra

function exepciones(us,pas){
    if(pas.length<7){
        throw new Error ("La contraseña debe de tener más de 7 caracteres");
    }
    else if(typeof us !== 'string'){
        throw new Error("Solo se permiten caracteres");
    }
    else if(us === "" || pas === ""){
        throw new Error ("Campos vacios");
    }

}
function Comprobar(user, password){
 try {
    exepciones(user,password);
    console.log("No ocurrienron exepciones",user,password);
    
 } catch (error) {
    confirm.log ("Error", error);
 }
 finally{

    console.log("Ingrese  los datos nuevamente");
 }


}
