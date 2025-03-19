-- Strings

--[[
-- OPERACIONES
-- ]]

-- To byte
print("string.byte('abc', 1, 3): " .. string.byte("abc", 1, 3)) -- 97 98 99

-- From byte
print("string.char(97, 98, 99): " .. string.char(97, 98, 99)) -- abc

-- Concatenar
print("'abc' .. 'def': " .. "abc" .. "def") -- abcdef

-- Formatear
print("string.format('%.2f', 3.1416): " .. string.format("%.2f", 3.1416)) -- 3.14

-- Buscar
print("string.find('abc', 'b'): " .. string.find("abc", "b")) -- 2

-- Reemplazar
print("string.gsub('abc', 'b', 'B'): " .. string.gsub("abc", "b", "B")) -- aBc

-- dump
print("string.dump(function() print('hola') end): " .. string.dump(function()
  print("hola")
end)) -- function() print("hola") end

-- gmacth
for word in string.gmatch("hola mundo", "%a+") do
  print(word)
end

-- match
print("string.match('hola mundo', '%a+'): " .. string.match("hola mundo", "%a+")) -- hola

-- gsub
print("string.gsub('hola mundo', '%a+', 'X'): " .. string.gsub("hola mundo", "%a+", "X")) -- X X

-- len
print("string.len('hola mundo'): " .. string.len("hola mundo")) -- 10

-- lowercase
print("string.lower('HOLA MUNDO'): " .. string.lower("HOLA MUNDO")) -- hola mundo

-- pack
-- print("string.pack('i4i4', 3, 4): " .. string.pack("i4i4", 3, 4)) -- 3 0 0 0 4 0 0 0

-- packsize
-- print("string.packsize('i4i4'): " .. string.packsize("i4i4")) -- 8

-- rep
print("string.rep('hola', 3): " .. string.rep("hola", 3)) -- holaholahola

-- reverse
print("string.reverse('hola mundo'): " .. string.reverse("hola mundo")) -- odnum aloh

-- sub
print("string.sub('hola mundo', 1, 4): " .. string.sub("hola mundo", 1, 4)) -- hola

-- unpack
-- print("string.unpack('i4i4', '3 0 0 0 4 0 0 0'): " .. string.unpack("i4i4", "3 0 0 0 4 0 0 0")) -- 3 4

-- uppercase
print("string.upper('hola mundo'): " .. string.upper("hola mundo")) -- HOLA MUNDO

--[[
-- EXTRA
-- ]]

local function palindrome(word)
  -- Check si es palindromo
  if word == string.reverse(word) then
    return true
  else
    return false
  end
end

local function sort_word(word)
  -- Ordenar las palabras
  word = string.gsub(word, "%s+", "")
  word = string.lower(word)
  local tabla = {}
  for c in string.gmatch(word, "%a") do
    table.insert(tabla, c)
  end
  table.sort(tabla)
  return tabla
end

local function isogramas(word)
  word = string.gsub(word, "%s+", "")
  word = string.lower(word)
  local tabla = {}
  for c in string.gmatch(word, "%a") do
    if tabla[c] == nil then
      tabla[c] = 0
    end
    tabla[c] = tabla[c] + 1
  end
  -- comprobar que todas las letras aparezcan el mismo numero de veces
  -- si es asi, es un isograma
  local initial_char = string.sub(word, 1, 1)
  local isogram_length = tabla[initial_char]
  for c in string.gmatch(word, "%a", 2) do
    if isogram_length ~= tabla[c] then
      return false
    end
  end
  return true
end

local function check(word1, word2)
  -- Check si son palindromos
  if palindrome(word1) then
    print(word1 .. " es palindromo")
  else
    print(word1 .. " no es palindromo")
  end

  if palindrome(word2) then
    print(word2 .. " es palindromo")
  else
    print(word2 .. " no es palindromo")
  end

  -- Check si son anagramas
  local word1_table = sort_word(word1)
  local word2_table = sort_word(word2)
  local anagrama = true
  for i = 1, #word1_table do
    if word1_table[i] ~= word2_table[i] then
      print(word1 .. " y " .. word2 .. " no son anagramas")
      anagrama = false
      break
    end
  end
  if anagrama then
    print(word1 .. " y " .. word2 .. " son anagramas")
  end

  -- Check si son isogramas
  if isogramas(word1) then
    print(word1 .. " es isograma")
  else
    print(word1 .. " no es isograma")
  end

  if isogramas(word2) then
    print(word2 .. " es isograma")
  else
    print(word2 .. " no es isograma")
  end
end

check("oso", "oso")
check("radar", "lualualua")
