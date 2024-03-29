public class Astra {

	/*
	 * Funcion que devuelve la suma de 2 numeros enteros*/
	public int sumar(int num1, int num2) {
		int sol = 0;
		
		sol = num1 + num2;
		System.out.println(sol);
		return sol;
	}
}



//Test

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class SumarTest {

	@Test
	void testSumar() {
		Astra llamar = new Astra();
		
		/*numero positivo en los 2 numeros*/
		assertEquals(20, llamar.sumar(10, 10));
		/*numero positivo y negativo en los 2 con resultado positivo*/
		assertEquals(2, llamar.sumar(5, -3));
		assertEquals(5, llamar.sumar(-5, 10));
		/*numero positivo y negativo en los 2 con resultado negativo*/
		assertEquals(-8, llamar.sumar(-10, 2));
		assertEquals(-8, llamar.sumar(2, -10));
	}

}
