# -- exercise
for i in range(1, 11):
    print(i)

i: int = 1
while i <= 10:
    print(i)
    i += 1

[print(i) for i in range(1, 11)]


# -- extra challenge
data_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in data_list:
    print(i)
    i += 1

i: int = 0
while i < len(data_list):
    print(data_list[i])
    i += 1

for i in range(len(data_list)):
    print(data_list[i])
    i += 1

for i in range(0, len(data_list)):
    print(data_list[i])
    i += 1


def recursive_print(data_list: list, i: int) -> None:
    if i < len(data_list):
        print(data_list[i])
        recursive_print(data_list, i + 1)
    else:
        return


recursive_print(data_list, 0)


def anonymous_print(data_list: list) -> None:
    [print(i) for i in data_list]


anonymous_print(data_list)
