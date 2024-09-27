def main():
    test_list = [1, 2, 3, 4]

    test_list.insert(0, 0)
    test_list.append(5)
    test_list += [6, 7, 8]
    test_list[3:3] = [9, 10]
    test_list.pop(3)
    test_list[3] = 3
    is_in_list = True if 10 in test_list else False
    test_list.clear()

    union_list = list(set([0, 1, 3, 2]) | set([4, 1, 2]))
    intersection_list = list(set([0, 1, 3, 2]) & set([4, 1, 2]))
    difference_list = list(set([0, 1, 3, 2]) - set([4, 1, 2]))
    simetric_difference_list = list(set([0, 1, 3, 2]) ^ set([4, 1, 2]))


if __name__ == '__main__':
    main()
