package org.example;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        // agregar una lista de 10 objetivos para alcanzar en el nuevo año
        List<Goal> goals = Arrays.asList(
                new Goal("Leer Libros",24, "Libro", 12),
                new Goal("Estudiar Git", 1, "curso", 1),
                new Goal("Hablar Ingles", 1, "Curso", 6),
                new Goal("Aprender a Tocar Guitarra", 8, "Curso", 8),
                new Goal("Aprender a Nadar", 2, "Curso", 2),
                new Goal("ldkfldkf", 45, "Curso", 6)
        );

        // permitir añadir solo 10 objetivos como maximo
        if(goals.size() > 10){
            System.out.println("Solo es permitido maximo 10 Objetivos");
            System.out.println("Debes eliminar " + (goals.size() - 10));
            System.exit(1);
        }
        System.out.println("Total Objetivos: " + goals.size());

        // Cada objetivo tiene un plazo maximo de 12 meses
        boolean anyHaveTimeMaxTwelveMonths = goals.stream()
                .anyMatch(e -> e.getNumberMonths() > 12);

        if(anyHaveTimeMaxTwelveMonths){
            System.out.println("existe un objetivo con plazo mayor a 12 meses.");
            System.out.println("revisa el plazo de tus objetivos.");
            System.exit(1);
        }

        // Calcular el plan detallado
        // arreglo type String con los meses del año
        String [] months = {"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
        // map type key-value donde la key es el plazo en meses para alcanzar el objetivo
        // el value es una lista de objetivos que tienen la misma duración en meses
        Map<Integer, List<Goal>> goalsByAmount = goals.stream()
                .collect(Collectors.groupingBy(Goal::getNumberMonths));
        // HashMap <String, List<Goal>> para
        HashMap <String, List<Goal>> plan = new HashMap<>();

        for(String m : months){
            List <Goal> goalList = new ArrayList<>();
            for (Integer i: goalsByAmount.keySet()){
                if(plan.size() >= i){
                    continue;
                }else{
                    for(Goal g : goalsByAmount.get(i)){
                        goalList.add(g);
                    }

                }
            }
            plan.put(m, goalList);
        }

        //Mostrar la planificación de objetivos por mes
        for (String m: months) {
            System.out.println(m + ":");
            for(Goal g: plan.get(m)){
                System.out.println(g);

            }
        }

        // Guardar la planificación en archivo txt
        try {
            File fileData = new File("planificacion.txt");
            if(fileData.createNewFile()){
                FileWriter fileWriter = new FileWriter(fileData.getPath());
                for (String m: months) {
                    fileWriter.write(m + "\n");
                    for(Goal g: plan.get(m)){
                        fileWriter.write(g.toString() + "\n");
                    }
                }
                fileWriter.close();
                System.out.println("fichero: " + fileData.getName() + " creado");
                System.out.println(fileData.getPath());
            }else{
                System.out.println("No se ha podido crear el fichero.");
                System.out.println(fileData.getPath());
            }
        }catch (IOException error){
            System.out.println("Error de creacion de fichero.");
            error.printStackTrace();
        }
    }


    static class Goal{
        private String title;
        private int amount;
        private String units;
        private int numberMonths;

        public Goal(String title, int amount, String units, int numberMonths) {
            this.title = title;
            this.amount = amount;
            this.units = units;
            this.numberMonths = numberMonths;

        }

        public String getTitle() {
            return title;
        }

        public int getAmount() {
            return amount;
        }

        public String getUnits() {
            return units;
        }

        public int getNumberMonths() {
            return numberMonths;
        }

        // calcular el numero de unidades aplicadas en cada mes
        public int getUnitByMonth(){
            if(this.amount == this.numberMonths) return (this.amount / this.numberMonths);
            if(this.amount < this.numberMonths) return 1;
            if(this.amount > this.numberMonths) {
                var resM = Math.round((float) this.amount / this.numberMonths);
                var resU = this.amount % this.numberMonths;
                //System.out.println("r:"+resU);
                if(resU == 0) return resM;
                return resM;
            }

            return 3;
        }

        // cada objetivo debe poseer un nombre, la cantidad de unidades a completar y su total
        @Override
        public String toString() {
            return "[] 1. " + this.getTitle() + " ("+ this.getUnitByMonth() + " " + this.getUnits() + "/mes). Total: " + this.getAmount() + ".";
        }
    }

}