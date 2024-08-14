package es.armenta.roadmap;

public enum Hero {

    DEADPOOL("Deadpool", 10, 100, 25),
    WOLVERINE("Wolverine", 10, 120, 20);

    final String name;
    final int minDamage;
    final int maxDamage;
    final int defendAttackPercentage;

    private Hero(String name, int minDamage, int maxDamage, int defendAttackPercentage) {
        this.name = name;
        this.minDamage = minDamage;
        this.maxDamage = maxDamage;
        this.defendAttackPercentage = defendAttackPercentage;
    }
}
