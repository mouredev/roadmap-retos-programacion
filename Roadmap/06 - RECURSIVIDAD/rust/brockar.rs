fn main(){
    println!("Contando desde 100 hasta 0");
    cien_cero(100);

    println!("EXTRA EXTRAA!");
    println!("Factorial de un número concreto (5)");
    let num = 5;
    println!("{}",factorial(num));

    println!("Fibonacci de un número concreto (5)");
    println!("{}",fibo(num));
}

fn cien_cero(num:u8){
    if num == 0{
        println!("0");
    } else {
        println!("{}", num);
        cien_cero(num - 1);
    }
}

// Los enteros podrían ser unsigned (u16) ya que para esto no se utilizan negativos.
fn factorial(num:i16) -> i16{
    if num == 0{
        return 1;
    }
    else{
        return num * factorial(num - 1);
    }
}

fn fibo(num:i16)-> i16{
    if num<0{
        println!("El numero debe ser mayor a 0.");
        return 0;
    }
    else if num==0{
        return 0;
    }
    else if num==1{
        return 1;
    }
    return fibo(num-1) + fibo(num-2);
}