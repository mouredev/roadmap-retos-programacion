package dev.asjordi.five.r50;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main plan = new Main();
        Scanner sc = new Scanner(System.in);

        System.out.println("Plan de objetivos 2025\nAgrega tus objetivos para el 2025\n");

        while (plan.getTotalObjetivos() < 10) {
            System.out.println("Objetivo " + (plan.getTotalObjetivos() + 1) + ":");
            System.out.print("Meta: ");
            String meta = sc.nextLine();
            System.out.print("Cantidad: ");
            int cantidad = sc.nextInt();
            sc.nextLine();
            System.out.print("Unidad: ");
            String unidad = sc.nextLine();
            System.out.print("Plazo (meses): ");
            int plazo = sc.nextInt();
            sc.nextLine();

            plan.addObjetivo(new Objetivo(meta, cantidad, unidad, plazo));

            System.out.println("¿Quieres añadir otro objetivo? (s/n)");
            if (sc.nextLine().equalsIgnoreCase("n")) break;
        }

        plan.calcularObjetivos();

    }

    private final List<Objetivo> objetivos;
    private final String[] months = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    private final StringBuilder plan;

    public Main() {
        this.objetivos = new ArrayList<>();
        this.plan = new StringBuilder();
    }

    public void addObjetivo(Objetivo objetivo) {
        if (this.objetivos.size() < 10) this.objetivos.add(objetivo);
        else System.out.println("No se pueden añadir más de 10 objetivos");
    }

    public void calcularObjetivos() {
        int maxMonth = objetivos.stream()
                .map(o -> o.getPlazo())
                .max(Integer::compareTo).orElseGet(() -> 12);

        System.out.println("Plan de objetivos 2025\n");
        this.plan.append("Plan de objetivos 2025\n\n");

        for (int i = 0; i < maxMonth; i++) {
            System.out.println(months[i] + ":");
            this.plan.append(months[i]).append(":\n");
            int c = 1;
            for (var objetivo : objetivos) {
                if (objetivo.getPlazo() > i) {
                    System.out.print("[ ] " + c + ". " + objetivo + "\n");
                    this.plan.append("[ ] ").append(c).append(". ").append(objetivo).append("\n");
                    c++;
                }
            }
            System.out.println();
            this.plan.append("\n");
        }

        guardarPlan();
    }

    public void guardarPlan() {
        Path path = Paths.get("plan.txt");

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path.toFile()))) {

            if (this.plan.isEmpty()) {
                System.out.println("No hay ningún plan que guardar");
                return;
            }

            bw.write(this.plan.toString());
            bw.flush();
            System.out.println("Plan guardado correctamente");
        } catch (IOException e) {
            System.out.println("Error al guardar el plan");
            e.printStackTrace();
        }
    }

    public int getTotalObjetivos() {
        return this.objetivos.size();
    }

    static class Objetivo {
        private final String meta;
        private final int cantidad;
        private final String unidad;
        private final int plazo;
        private final double porMes;

        public Objetivo(String meta, int cantidad, String unidad, int plazo) {
            this.meta = meta;
            this.cantidad = cantidad;
            this.unidad = unidad;
            this.plazo = Math.min(plazo, 12);
            this.porMes = (double) this.cantidad / this.plazo;
        }

        public int getPlazo() {
            return plazo;
        }

        @Override
        public String toString() {
            return this.meta + " (" + this.porMes + " " + this.unidad + "/mes). Total: " + this.cantidad;
        }
    }

}
