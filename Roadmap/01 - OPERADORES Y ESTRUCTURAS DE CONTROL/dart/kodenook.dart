void main() {
    /*
        Arithmetic Operators
    */

    print('Arithmetic Operators\n');
    print('2 + 2 = ${2 + 2}');
    print('2 - 2 = ${2 - 2}');
    print('2 * 2 = ${2 * 2}');
    print('2 / 2 = ${2 / 2}');
    print('2 ~/ 2 = ${2 ~/ 2}'); // return an integer
    print('2 % 2 = ${2 % 2}');

    /*
        Bitwise Operators
    */

    print('\nBitwise Operators\n');
    print('&: 5 & 2 = ${5 & 2}');
	print('|: 5 | 2 = ${5 | 2}');
	print('^: 5 ^ 2 = ${5 ^ 2}');
	print('>>: 5 >> 2 = ${5 >> 2}');
	print('<<: 5 << 2 = ${5 << 2}');

    /*
        Assignment Operators
    */

    print('\nAssignment Operators\n');
    print('x = 5');
    print('x += 5, x = x + 5');
    print('x -= 5, x = x - 5');
    print('x *= 5, x = x * 5');
    print('x /= 5, x = x / 5');
    print('x ~/= 5, x = x ~/ 5');
    print('x %= 5, x = x % 5');
    print('x &= 5, x = x & 5');
    print('x |= 5, x = x | 5');
    print('x ^= 5, x = x ^ 5');
    print('x >>= 5, x = x >> 5');
    print('x <<= 5, x = x << 5');
    print('x >>>= 5, x = x >>> 5');

    /*
        Comparison Operators
    */

    print('\nComparison Operators\n');
    print('Equal to 4 == 5, ${4 == 5}');
    print('Not Equal to 4 != 5, ${4 != 5}');
    print('Grater Than 4 > 5, ${4 > 5}');
    print('Less Than 4 < 5, ${4<= 5}');
    print('Grater Than Or Equal to 4 >= 5, ${4 >= 5}');
    print('Less Than Or Equal to 4 <= 5, ${4 <= 5}');

    /*
        Logical Operators
    */

    print('\nLogical Operators\n');
    print('&&, 3 < 5 && 3 < 10, ${3 < 5 && 3 < 10}');
    print('||, 3 < 5 || 3 < 10, ${3 < 5 || 3 < 10}');
    print('!, !(4 < 5), ${!(4 < 5)}');

    /*
        If
    */

    if (6 > 5) {
        print('6 is grater than 5');
    } else if (5 < 6) {
        print('5 is less than 6');
    } else {
        print('Good Bye');
    }

    /*
        Switch
    */

    switch (10) {
        case 2:
            print('The case is 2');
        case 5 when (5 < 10):
            print('The case is 5');
        case 8:
            print('The case is 8');
        default:
            print('The case is not here');
    }

    /*
        For loop
    */

    for (var i = 0; i < 5; i++) {
        print(i);
    }

    var collection = [1, 2, 3];

    for(final c in collection) {
        print(c);
    }

    collection.forEach(print);

    /*
        While Loop
    */

    int i = 5;
    while (i > 0) {
        print(i);
        i--;
    }

    do {
        print(i);
        i++;
    } while (i < 5);

    /*
        Exercise
    */

    for(var i = 10; i < 56; i += 2) {
        if(i == 16 || i % 3 != 0) {
            continue;
        }
        print(i);
    }
}