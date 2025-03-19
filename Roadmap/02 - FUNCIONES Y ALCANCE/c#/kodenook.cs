
void name() {
    Console.WriteLine("kodenook");
}

name();

void fullName(string fname = "my", string lname = "surname") {
    Console.WriteLine($"{fname} {lname}");
}

fullName();

void ageAddition(ref int age) {
    age += 5;
}

int age = 20;
ageAddition(ref age);
Console.WriteLine(age);

void first() {
    Console.WriteLine("First");

    void second() {
        Console.WriteLine("Second");
    }

    second();
}

first();

/*
    Exercise
*/

int exercise(string word1, string word2) {
    int countNumbers = 0;

    foreach (var i in Enumerable.Range(1, 100))
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            Console.WriteLine($"{word1} {word2}");
        } else if (i % 3 == 0) {
            Console.WriteLine(word1);
        } else if (i % 5 == 0) {
            Console.WriteLine(word2);
        } else {
            countNumbers++;
        }
    }

    return countNumbers;
}

Console.WriteLine($"number of times it was a number and not words: {exercise("hello", "c#")}");