def fn_no_params_no_return() -> None:
    print("fn_no_params_no_return")


print(f"example1: {fn_no_params_no_return()}")


def fn_one_param_no_return(param1) -> None:
    print("fn_one_param_no_return: " + param1)


print(f"example2: {fn_one_param_no_return('param1')}")


def fn_params_return(param1: int, param2: int) -> int:
    return param1 + param2


print(f"example3: {fn_params_return(1, 2)}")


def fn_params_return(*params: int) -> int:
    return sum(params)


print(f"example4: {fn_params_return(1, 2, 3, 4, 5)}")


def fn_outside():
    def fn_inside():
        print("fn_inside")

    fn_inside()


print(f"example5: {fn_outside()}")


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print(f"example6: {all([True, True, True])}")


def fn_local_global():
    global global_var
    global_var = 1
    local_var = 2
    print(f"global_var: {global_var}")
    print(f"local_var: {local_var}")


print(f"example7: {fn_local_global()}")
print(f"global_var: {global_var}")


# -- extra challenge
def fn_challenge(param1: str, param2: str) -> int:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1 + param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
    return 100


print(f"extra chanllenge: {fn_challenge('param1', 'param2')}")
