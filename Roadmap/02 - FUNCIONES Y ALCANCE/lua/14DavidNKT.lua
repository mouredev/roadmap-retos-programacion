-- FUNCIONES SIMPLES

function Hola()
    print("Hola, Lua!")
end

Hola()

-- FUNCIONES CON RETORNO

function return_Hola()
    return "Hola, Lua!"
end

Hola = return_Hola()
print(Hola)
print(return_Hola()) -- otra forma de llamar a la funcion sin almacenarla en una variable

-- FUNCION CON UN ARGUMENTO

function arg_Hola(name)
    print("Hola " .. name)
end

arg_Hola("David")

-- FUNCION CON ARGUMENTOS

function args_Hola(hola, name)
    print(hola, name)
end

args_Hola("Hi", "David")

-- FUNCION CON ARGUMENTOS CON VALOR PREDETERMINADO

function default_args_Hola(hola, name)
    local name = name or "Desconocido"
    print(hola, name)
end

default_args_Hola("Hi")

-- FUNCION CON ARGUMENTOS Y RETORNO

function return_args_Hola(hola, name)
    return hola, name
end

print(return_args_Hola("Hi", "David"))

-- FUNCION CON RETORNO DE VARIOS VALORES

function multiple_return_Hola()
    return "Hi", "David"
end

hola, name = multiple_return_Hola()
print(hola)
print(name)

-- FUNCION CON UN NUMERO VARIABLE DE ARGUMENTOS (VARARG)

function variable_args_Hola(name, ...)
    local names = {...}
    print("Hola " .. name .. "!")
    for _, name in ipairs(names) do
        print("Hola " .. name .. "!")
    end
end

variable_args_Hola("David", "Lua", "Todos")

-- FUNCION CON TABLA DE ARGUMENTOS

function table_args_Hola(args)
    local hola = args.hola
    local name = args.name
    local lastname = args.lastname
    print(hola, name, lastname)
end

table_args_Hola({hola = "Hola", name = "David", lastname = "Marques"})

-- FUNCIONES DEL LENGUAJE (BUILT-IN)

print("Hola")
print(type(8))
print(tostring(123))
print(tonumber("A", 16))
print(string.len("Hola"))
print(string.sub("Hola", 2, 3))
print(string.upper("Hola"))
print(string.lower("HOLA"))
print(math.abs(-10))
print(math.ceil(2.3))
print(math.floor(2.7))
print(math.random(1, 100))
print(os.time())
print(os.date("%Y-%m-%d %H:%M:%S"))

-- VARIABLES LOCALES Y GLOBALES
global_var = "Lua"

function hello_lua()
    local_var = "Hola"
    print(local_var, global_var)
end

print(global_var)
-- print(local_var) No se puede usar desde fuera de la funcion, en este caso arroja valor "nulo" (nil)

hello_lua()

-- Extra

function range(start, stop, step)
    local step = step or 1
    local t = {}
    for i = start, stop, step do
        table.insert(t, i)
    end
    return t
end

function print_number(text1, text2)
    local r = range(1, 100)
    local count = 0
    for _, v in ipairs(r) do
        if v % 3 == 0 and v % 5 == 0 then
            print(text1 .. text2)
        elseif v % 3 == 0 then
            print(text1)
        elseif v % 5 == 0 then
            print(text2)
        else
            print(v)
            count = count + 1
        end
    end
    print(count)
end

print_number("Fizz", "Buzz")