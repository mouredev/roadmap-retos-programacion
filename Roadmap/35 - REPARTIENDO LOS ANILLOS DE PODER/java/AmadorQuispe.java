package com.amsoft.roadmap.example35;

import java.util.Objects;
import java.util.Optional;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Example35 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the total number of rings: ");
        int totalRings = scanner.nextInt();

        if (totalRings <= 1) {
            System.out.println("Error: Not enough rings to distribute.");
            return;
        }

        int remainingRings = totalRings - 1;

        Optional<Distribution> result = findValidDistribution(remainingRings);

        result.ifPresentOrElse(
                Example35::printDistribution,
                () -> System.out.println("No valid distribution found for the given number of rings.")
        );

        scanner.close();
    }

    private static Optional<Distribution> findValidDistribution(int remainingRings) {
        return IntStream.iterate(1, i -> i + 2)
                .limit(remainingRings / 2)
                .boxed()
                .flatMap(elves -> IntStream.range(2, remainingRings)
                        .filter(Example35::isPrime)
                        .boxed()
                        .map(dwarves -> {
                            int men = remainingRings - elves - dwarves;
                            if (men > 0 && men % 2 == 0) {
                                return new Distribution(elves, dwarves, men);
                            }
                            return null;
                        })
                        .filter(Objects::nonNull))
                .findFirst();
    }

    private static boolean isPrime(int number) {
        return number > 1 && IntStream.rangeClosed(2, (int) Math.sqrt(number))
                .allMatch(i -> number % i != 0);
    }

    private static void printDistribution(Distribution distribution) {
        System.out.println("Valid distribution found:");
        System.out.println("Elves: " + distribution.elves());
        System.out.println("Dwarves: " + distribution.dwarves());
        System.out.println("Men: " + distribution.men());
        System.out.println("Sauron: 1");
    }

    record Distribution(int elves, int dwarves, int men) {
    }
}
