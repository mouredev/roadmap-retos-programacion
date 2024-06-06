-- asignacion de variables por valor

local a = 1
local b = 2

print("a: ", a)
print("b: ", b)

-- asignacion por referencia
-- No es posible hacer asignacion por referencia en lua ya que las variables
-- son por valor y no por referencia

-- funciones con datos por valor
function sumar(a, b)
  return a + b
end

print("sumar(1, 2): ", sumar(1, 2))

-- funciones con datos por referencia
function sumar2(a, b)
  local tabla = {}
  for i = 1, #a do
    tabla[i] = a[i] + b[i]
  end
  return tabla
end

local a = {1, 2, 3}
local b = {4, 5, 6}
local c = sumar2(a, b)
for i = 1, #c do
  print("a["..i.."] + b["..i.."] = " .. a[i] .. " + " .. b[i] .. " = " .. c[i])
end 


--[[
-- EXTRA
--]]

-- funcion que intercambia dos variables por valor
function swap(a, b)
  local c, d = b, a
  return c, d
end

local a = 1
local b = 2
print("a: ", a)
print("b: ", b)
a, b = swap(a, b)
print("a: ", a)
print("b: ", b)

-- funcion que intercambia dos variables por referencia
-- no es posible hacerlo en lua, ya que las variables son por valor
-- y no por referencia

