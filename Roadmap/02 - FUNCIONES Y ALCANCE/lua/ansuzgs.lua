-- Funcion sin parametros ni retorno
function test1()
  print("test1")
end

-- Funcion con parametros, pero sin retorno
function test2(a, b)
  print("test2", a, b)
end

-- Funcion con parametros y retorno
function test3(a, b)
  print("test3", a, b)
  return a + b
end

print("test3(1, 2) = ", test3(1, 2))

-- Funciones anidadas
function test4(a, b)
  function test5(c, d)
    print("test5", c, d)
    return c + d
  end
  print("test4", a, b)
  return test5(a, b)
end

print("test4(1, 2) = ", test4(1, 2))

-- Funciones anonimas
test6 = function(a, b)
  print("test6", a, b)
  return a + b
end

print("test6(1, 2) = ", test6(1, 2))

-- Funciones con retorno multiple
function test7(a, b)
  print("test7", a, b)
  return a, b
end

x, y = test7(1, 2)
print("test7(1, 2) = ", x, y)

-- Variables locales
function test8(a, b)
  local c = a + b
  print("test8", a, b, c)
  return c
end

print("test8(1, 2) = ", test8(1, 2))

-- Variables globales
c = 0
print("c = ", c)
function test9(a, b)
  c = a + b
  print("test9", a, b, c)
  return c
end
print("test9(1, 2) = ", test9(1, 2))

--[[
  EXTRA
]]

function extra(text_1, text_2)
  local count = 0
  for i = 1, 100, 1 do
    if i % 3 == 0 and i % 5 == 0 then
      print(text_1 .. text_2)
    elseif i % 3 == 0 then
      print(text_1)
    elseif i % 5 == 0 then
      print(text_2)
    else
      print(i)
      count = count + 1
    end
  end
  return count
end

print("extra('Fizz', 'Buzz') = ", extra('Fizz', 'Buzz'))
