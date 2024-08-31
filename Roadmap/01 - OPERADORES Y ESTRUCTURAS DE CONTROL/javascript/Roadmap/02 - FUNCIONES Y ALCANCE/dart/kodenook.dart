
String global = 'global';

void main(){
    name();
    fullName(lname: 'kodenook');
    print(addition([5, -2.5, 1.3]));
    first();
    scope();
    print('number of times it was a number and not words: ${exercise('hello', 'dart')}');
}

/// The function "name" in Dart prints the string "kodenook".
void name() {
    print('kodenook');
}

/// The function fullName in Dart prints the full name by concatenating the provided first and last
/// names.
///
/// Args:
///   fname (String): The `fname` parameter in the `fullName` function is a String type parameter with a
/// default value of `'hello'`. Defaults to hello
///   lname (String): The `lname` parameter in the `fullName` function is a String parameter with a
/// default value of `'name'`. Defaults to name
void fullName({String fname = 'hello', String lname = 'name'}) { // with {} is optional
    print('$fname $lname');
}

/// The `addition` function takes a list of numbers as input and returns the sum of all the numbers in
/// the list.
///
/// Args:
///   numbers (List<num>): A list of numbers that you want to add together.
///
/// Returns:
///   the sum of all the numbers in the input list.
num addition(List<num> numbers) {
    num result = 0;

    for(var value in numbers) {
        result += value;
    }

    return result;
}

/// The function `first` prints 'First' and then calls the nested function `second` which prints
/// 'second'.
void first() {
    print('First');

    void second() {
        print('second');
    }

    second();
}

/// The function `scope` defines a local variable `local` and attempts to print both a global variable
/// `global` and the local variable `local`.
void scope() {
    String local = 'local';

    print(global);
    print(local);
}

/*
    Exercise
*/

/// This Dart function prints words based on divisibility rules and returns the count of numbers that do
/// not meet those rules.
///
/// Args:
///   word1 (String): Thank you for providing the code snippet. It looks like you are trying to
/// implement a function that prints different words based on certain conditions for numbers from 1 to
/// 100.
///   word2 (String): It looks like you are trying to create a function that prints different words
/// based on the divisibility of numbers from 1 to 100. However, there are a few issues in your code
/// snippet:
///
/// Returns:
///   The function `exercise` returns the count of numbers that are not divisible by 3 or 5 within the
/// range of 1 to 100.
int exercise(String word1, String word2) {
    int countNumbers = 0;

    for(int value = 1; value <= 100; value++) {
        if(value % 3 == 0 && value % 5 == 0) {
            print('$word1 $word2');
        } else if (value % 3 == 0) {
            print(word1);
        } else if (value % 5 == 0) {
            print(word2);
        } else {
            countNumbers++;
        }
    }

    return countNumbers;
}