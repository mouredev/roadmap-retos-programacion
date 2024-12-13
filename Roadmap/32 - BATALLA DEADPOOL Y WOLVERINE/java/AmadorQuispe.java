package com.amsoft.roadmap.example32;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class Example32 {
    public static void main(String[] args) {
        Character deadpool = new Character.Builder()
                .name("Deadpool")
                .health(1000)
                .minDamage(10)
                .maxDamage(100)
                .probabilityDefend(25)
                .build();
        Character wolverine = new Character.Builder()
                .name("Wolverine")
                .health(1000)
                .minDamage(10)
                .maxDamage(120)
                .probabilityDefend(20)
                .build();
        simulateBattle simulateBattle = new simulateBattle();
        simulateBattle.battle(deadpool, wolverine);
    }
}

class simulateBattle {
    public void battle(Character hero1, Character hero2) {
        int turn = 0; //Turnos pares ataca el hero1, turnos impares ataca el hero2
        boolean loseTurn;
        while (hero1.getHealth() > 0 && hero2.getHealth() > 0) {
            System.out.println("-----------------" + "Turno " + turn + "-----------------");
            if (turn % 2 == 0) {
                loseTurn = turnAttack(hero1, hero2);
            } else {
                loseTurn = turnAttack(hero2, hero1);
            }
            if (!loseTurn){
                turn++;
            }
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
        System.out.println("Batalla finalizada");
        System.out.println("-----------------");
        if (hero1.getHealth() <= 0) {
            System.out.println(hero2.getName() + " gana la batalla");
        } else {
            System.out.println(hero1.getName() + " gana la batalla");
        }
    }

    public boolean turnAttack(Character attacker, Character defender){
        int damage = attacker.attack();
        int defend = defender.defend();
        if(damage == attacker.getMaxDamage()){
            String message = String.format(
                    "%s ataca con %d de daño crítico, %s pierde el turno",
                    attacker.getName(), damage, defender.getName()
            );
            System.out.println(message);
            return true;
        }
        if (defend == 0) {
            String message = String.format(
                    "%s ataca con %d de daño, y %s evade el ataque, queda con %d de vida",
                    attacker.getName(), damage, defender.getName(), defender.getHealth()
            );
            System.out.println(message);
        } else {
            defender.decreaseHealth(damage);
            String message = String.format(
                    "%s ataca con %d de daño, deja a %s con %d de vida",
                    attacker.getName(), damage,
                    defender.getName(), defender.getHealth()
            );
            System.out.println(message);
        }
        return false;
    }
}





class Character {
    private final String name;
    private Integer health;
    private final Integer minDamage;
    private final Integer maxDamage;
    private final Integer probabilityDefend;

    private Character(Builder builder) {
        this.name = builder.name;
        this.health = builder.health;
        this.minDamage = builder.minDamage;
        this.maxDamage = builder.maxDamage;
        this.probabilityDefend = builder.probabilityDefend;
    }


    public Integer attack() {
        return new Random().nextInt(maxDamage - minDamage + 1) + minDamage;
    }

    public Integer defend() {
        int defend = new Random().nextInt(100);
        return defend <= probabilityDefend ? 0 : 1;
    }

    public void decreaseHealth(Integer damage) {
        health -= damage;
    }

    static class Builder {
        private String name;
        private Integer health;
        private Integer minDamage;
        private Integer maxDamage;
        private Integer probabilityDefend;

        public Builder name(String name) {
            this.name = name;
            return this;
        }

        public Builder health(Integer health) {
            this.health = health;
            return this;
        }

        public Builder minDamage(Integer minDamage) {
            this.minDamage = minDamage;
            return this;
        }

        public Builder maxDamage(Integer maxDamage) {
            this.maxDamage = maxDamage;
            return this;
        }

        public Builder probabilityDefend(Integer probabilityDefend) {
            this.probabilityDefend = probabilityDefend;
            return this;
        }

        public Character build() {
            return new Character(this);
        }
    }

    public String getName() {
        return name;
    }

    public Integer getHealth() {
        return health;
    }

    public Integer getMinDamage() {
        return minDamage;
    }

    public Integer getMaxDamage() {
        return maxDamage;
    }

    public Integer getProbabilityDefend() {
        return probabilityDefend;
    }
}
