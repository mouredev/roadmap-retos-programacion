//OPERATORS
package main
import ("fmt")

func main(){
//ARITHMETIC OPERATORS
var one int = 1;
var two int = 2;
var three int = 3;
var result int = 0;
result = one + two;
fmt.Println(result);
result = one - three;
fmt.Println(result);
result = one * two;
fmt.Println(result);
result = two / three;
fmt.Println(result);
result = one % two;
fmt.Println(result);
result++;
fmt.Println(result);
result--;
fmt.Println(result);
//ASIGNMENT
var x = 4;
x +=3;
fmt.Println(x);
x -=3;
fmt.Println(x);
x*=3;
fmt.Println(x);
x/=3;
fmt.Println(x);
x%=3;
fmt.Println(x);
x&=3;
fmt.Println(x);
x|=3;
fmt.Println(x);
x^=3;
fmt.Println(x);

x = 10

    // AND a nivel de bits y asignación
    x &= 3 // x = x & 3
    fmt.Printf("AND: %d (binario: %b)\n", x, x);
    // OR a nivel de bits y asignación
    x = 10
    x |= 3 // x = x | 3
    fmt.Printf("OR: %d (binario: %b)\n", x, x)

    // XOR a nivel de bits y asignación
    x = 10
    x ^= 3 // x = x ^ 3
    fmt.Printf("XOR: %d (binario: %b)\n", x, x)

    // Desplazamiento a la derecha y asignación
    x = 10
    x >>= 2 // x = x >> 2
    fmt.Printf("Desplazamiento a la derecha: %d (binario: %b)\n", x, x)

    // Desplazamiento a la izquierda y asignación
    x = 10
    x <<= 2 // x = x << 2
    fmt.Printf("Desplazamiento a la izquierda: %d (binario: %b)\n", x, x)

    fmt.Println(3==3);
    fmt.Println(3!=3);
    fmt.Println(3<4);
    fmt.Println(3>4);
    fmt.Println(3<=4);
    fmt.Println(3>=4);
    fmt.Println("convined of logic arguments");
    fmt.Println(!true);
    fmt.Println(true||false);
    fmt.Println(true&&true);
    fmt.Println(true&&false);
    fmt.Println(false||true);
    fmt.Println(true||true);
    fmt.Println(false||false);
    fmt.Println(false&&true);
    //flow control statements: for, if, else, switch and defer
  fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
  
	fmt.Println("done")
  fmt.Println("EXERCICE");
  for i := 9; i< 56; i++ {
    if(i%2==0 && i!=16 && i%3!=0){
      fmt.Println(i);
    }
  }
}
