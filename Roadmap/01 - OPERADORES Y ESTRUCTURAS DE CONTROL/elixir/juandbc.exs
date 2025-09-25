# Operadores aritméticos
IO.puts("# Operadores aritméticos")
IO.puts("Suma 5 + 5 = #{5 + 5}")
IO.puts("Resta 5 - 5 = #{5 - 5}")
IO.puts("Multiplicación 5 * 5 = #{5 * 5}")
IO.puts("División 5 / 5 = #{5 / 5}")
# No hay operador % para el modulo cómo en otros lenguajes, pero si una función llamada rem(n,m)
IO.puts("Módulo 31 % 3 = #{rem(31, 3)}")
# Operadores de asignación
IO.puts("# Operadores de asignación")
x = "asignación"
IO.puts("x = #{x}")
[head, middle | tail] = ["cabeza", :middle, "cola"]
Enum.join([head, middle, tail], ",") |> IO.puts()

# Operadores lógicos
IO.puts("# Operadores lógicos")
# and, or y not son operadores de corto circuito y deben usarse con Booleans
op_or_corto_circuito = true or false
op_and_corto_circuito = true and nil
IO.puts("Operador or (true or false) -> #{op_or_corto_circuito}")
IO.puts("Operador and (true and nil) -> #{op_and_corto_circuito}")
IO.puts("Operador not (not true) -> #{not true}")
# Para valores no booleanos
op_or = true || false
op_and = true && false
IO.puts("Operador || (true || false) -> #{op_or}")
IO.puts("Operador && (true && false) -> #{op_and}")
IO.puts("Operador ! (!true) -> #{!true}")

# Operadores de comparación
IO.puts("# Operadores de comparación")
IO.puts("1 < 1.0 -> #{1 < 1.0}")
IO.puts("1 > 2.0 -> #{1 > 2.0}")
IO.puts("1 <= 1.0 -> #{1 <= 1.0}")
IO.puts("1 >= 2.0 -> #{1 >= 2.0}")
IO.puts("1 == 1.0 -> #{1 == 1.0}")
IO.puts("1 != 1.0 -> #{1 != 1.0}")
IO.puts("1 === 1.0 -> #{1 === 1.0}")
IO.puts("1 !== 1.0 -> #{1 !== 1.0}")

# Operador de pertenencia
IO.puts("# Operadores de comparación")
list_has_fives = 5 in [1, 2, 3, 4, 5]
list_hasnt_fives = 5 in [1, 2, 3, 4]
IO.puts("5 in [1, 2, 3, 4, 5] -> #{list_has_fives}")
IO.puts("5 not in [1, 2, 3, 4] -> #{list_hasnt_fives}")

# Estructuras de control
# A difererencia de otros lenguajes, no son estructuras de control nativas sino macros (if/2, case/2, cond/1)
IO.puts("# Estructuras de control (aunque no son nativas, sino macros)")
# if
IO.puts("- if else")
if String.valid?("H") do
  IO.puts("Válido!")
else
  IO.puts("No válido")
end
# unless (deprecada)
IO.puts("- unless")
unless is_atom("test"), do: IO.puts("No es átomo")
# case/switch
IO.puts("- case/switch")
case {:ok, "Hola mundo"} do
  {:ok, result} -> result
  {:error} -> "Error!"
  _ -> "Este es el default"
end
# cond
IO.puts("- Cond como: elsif/elseif")
cond do
  2 + 2 == 5 -> IO.puts("Este no se imprimirá porque 2 + 2 no es igual 5")
  2 + 2 == 4 -> IO.puts("Este también siempre se imprimirá porque 2 + 2 = 4")
  true -> IO.puts("Este no se imprimirá porque se cumplió el anterior")
end

# Excepciones
IO.puts("- Try/Rescue/After")
try do
  1 = x
rescue
  e in MatchError -> IO.puts("Excepción capturada [#{Exception.message(e)}]")
after
  IO.puts("Este es como el finally en Java o ensure en Ruby")
end
IO.puts("- Try/Catch")
try do
  e = "Throws error"
  throw(e)
catch
  e -> IO.puts("Excepción capturada [#{e}]")
end
# Ejercicio extra:  números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
lista = 10..55

Enum.filter(lista, fn i -> i !== 16 and rem(i, 3) != 0 end)
|> Enum.join(",")
|> IO.puts()
