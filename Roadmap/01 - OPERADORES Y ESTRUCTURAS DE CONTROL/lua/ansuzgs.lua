--[[
    OPERATORS
]]

-- Arithmetic operators

print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 * 2 = ", 5 * 2)
print("5 / 2 = ", 5 / 2)
print("5 % 2 = ", 5 % 2)
print("5 ^ 2 = ", 5 ^ 2)
print("-5 = ", -5)

-- Relational operators

print("5 == 2 is ", 5 == 2)
print("5 ~= 2 is ", 5 ~= 2)
print("5 > 2 is ", 5 > 2)
print("5 < 2 is ", 5 < 2)
print("5 >= 2 is ", 5 >= 2)
print("5 <= 2 is ", 5 <= 2)

-- Logical operators

print("true and false is ", true and false)
print("true or false is ", true or false)
print("not true is ", not true)

-- Other operators

print("Hello" .. "World")
print("#'Hello' is ", #'Hello')

-- EXTRA

for i = 10, 55, 2 do
  if i ~= 16 and i % 3 ~= 0 then
    print(i)
  end
end
