function showError(){
    throw new Error("Error en la aplicación");
}

function iniciarApp(){
    try{
        showError();
    } catch(error){
        console.error(`${error}`);
    } finally {
        console.log("Aplicación finalizada\n")
    }
}

iniciarApp();

//EXTRA
interface errorSuma{
    errorCode:number,
    body:string
}
console.log("**************MANEJO DE ERRORES*************")
export abstract class CustomError extends Error{
    abstract errorCode: number;

    constructor(message: string){
        super(message);
        Object.setPrototypeOf(this, new.target.prototype);
    }
}

export class ValidationError extends CustomError{
    errorCode = 0;
    constructor(message:string){
        super(message);
        this.name="ValidationError"
    }
}
export class OutOfRange extends CustomError{
    errorCode = -1;
    constructor(message:string){
        super(message);
        this.name="OutOfRange"
    }
}

export default function handleError(error: unknown): errorSuma {
    if (error instanceof CustomError) {
      return {
        errorCode: error.errorCode,
        body: JSON.stringify({ message: error.message }),
      };
    } else {
      return {
        errorCode: 500,
        body: JSON.stringify({ error }),
      };
    }
  }

  function app(numero:number){
    try{
        switch(numero){
            case 1:
                throw new ValidationError("Validación incorrecta, inténtalo de nuevo");
            case 2:
                throw new OutOfRange("El número esta fuera del rango permitido");
            case 3:
                let list:string[]=["hola"];
                let data:number=list[2].length
                console.log(data);
                break;
            default:
                console.dir("No se ha producido ningún error")
                break;
        }
    } catch(error){
        const response = handleError(error);
        console.warn("Código de error: "+response.errorCode)
        if(response.errorCode<=0){
            console.error(`ERROR: ${response.errorCode}, ${response.body}`);
        } else {
            console.error(`ERROR: ${error}`);
        }
    } finally {
      console.log("Aplicación finalizada\n");
    }
  }
  
  app(1);
  app(2);
  app(3);
  app(4);