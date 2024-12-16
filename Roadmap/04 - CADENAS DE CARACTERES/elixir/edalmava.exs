# Concatenación de cadenas
cadena1 = "Programando con"
cadena2 = "Elixir"
IO.puts cadena1 <> " " <> cadena2

# Interpolación de cadenas
IO.puts "#{cadena1} #{cadena2}"

IO.puts "Cadena: " <> cadena1
IO.puts "Longitud de la cadena: #{String.length(cadena1)}"

# Acceso a un caracter específico
IO.puts "Primer caracter de la cadena: #{String.at(cadena1, 0)}"

# Subcadenas
IO.puts "Primeros cinco caracteres: #{String.slice(cadena1, 0..4)}" # slice(string, range)
IO.puts "Primeros cinco caracteres: #{String.slice(cadena1, 0, 5)}" # slice(string, start, length)

# Invertir una cadena
cadena = "anitalavalatina"
IO.puts String.reverse(cadena)

# Repetir o duplicar una cadena
cadena3 = "*****"
IO.puts String.duplicate(cadena3, 5)

# Buscar si la cadena tiene un contenido dado
IO.puts "La cadena contiene 'lava': #{String.contains?(cadena, "lava")}"

# División de una cadena en palabras
cadena = "Anita lava la tina"
[nombre | _resto] = String.split cadena
IO.puts nombre

# Dividir una cadena basada en un patrón
[primero | _resto] = String.split("1,2,3,4,5", ",")
IO.puts "Primer Número: #{primero}"

# Reemplazar partes de una cadena
cadena = "Loro"
IO.puts String.replace(cadena, "r", "c")

# cambiar a mayúscula
IO.puts String.upcase cadena

# Cambiar a minúscula
IO.puts String.downcase cadena

# RETO EXTRA

defmodule Grapheme do
  def anagrams?(a, b) when is_binary(a) and is_binary(b) do
    sort_string(a) == sort_string(b)
  end

  def sort_string(string) do
    string
    |> String.downcase()
    |> String.graphemes()
    |> Enum.sort()
  end

  def isograms?(string) do
    string
    |> String.downcase()
    |> String.graphemes()
    |> Enum.frequencies()
    |> Enum.all?(fn {_k, v} -> v == 1 end)
  end
end

check = fn (word1, word2) ->
  word1 = word1 |> String.trim() |> String.downcase()
  word2 = word2 |> String.trim() |> String.downcase()
  IO.puts "Palabra 1: #{word1} y Palabra 2: #{word2}"
  IO.puts "Primera palabra es palindromo: #{String.reverse(word1) === word1}"
  IO.puts "Segunda palabra es palindromo: #{String.reverse(word2) === word2}"
  IO.puts "Las dos palabras son anagramas (solución 1): #{String.bag_distance(word1, word2) === 1.0}"
  IO.puts "Las dos palabras son anagramas (solución 2): #{Grapheme.anagrams?(word1, word2)}"
  IO.puts "La primera palabra es isograma: #{Grapheme.isograms?(word1)}"
  IO.puts "La segunda palabra es isograma: #{Grapheme.isograms?(word2)}"
  IO.puts ""
end

check.("amor", "roma")
check.("radar", "anitalavalatina")
check.("python", "murciélago")
