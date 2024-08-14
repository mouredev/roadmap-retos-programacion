package es.armenta.roadmap;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // Create a Scanner object

        System.out.println("Enter Deadpool's life points:");
        Fighter deadpool = new Fighter(Hero.DEADPOOL, scanner.nextInt()) ;

        System.out.println("Enter Wolverine's life points:");
        Fighter wolverine = new Fighter(Hero.WOLVERINE, scanner.nextInt()) ;

        Game game = new Game(deadpool, wolverine);
        game.start();
    }
}
