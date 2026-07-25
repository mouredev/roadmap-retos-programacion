/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.christmastree;

import java.util.Scanner;

/**
 *
 * @author JOHN
 */
public class ChristmasTree {
    static class Tree{
        private String treeDraw;
        private int column;
        private int row;
        private boolean star;
        private boolean onLight;
        private int balls;
        private int lights;

        public Tree(int heigth, boolean star) {
            this.setColumn(heigth);
            this.setRow(heigth);
            this.star = star;
            this.balls = 0;
            this.lights = 0;
            this.treeDraw = "";
        }
        
        public void setRow(int h){
            this.row = h;
        }
        
        public void setColumn(int h){
            for(int i=0; i<h; i++){
                this.column = (2*i)+1;
            }
        }

        public int getBalls() {
            return balls;
        }

        public void setBalls(int balls) {
            this.balls = balls;
        }

        public String getTreeDraw() {
            return treeDraw;
        }

        public int getLights() {
            return lights;
        }

        public void setLights(int lights) {
            this.lights = lights;
        }

        public boolean isOnLight() {
            return onLight;
        }

        public void setOnLight(boolean onLight) {
            this.onLight = onLight;
        }
        
        public String draw(){
            String tree = "";
            int amountBall = this.getBalls();
            int amountLight = this.getLights();
            
            for(int x=0; x<this.row; x++){
                tree += "\n";
                int asterisksNumber = (2*x)+1;
                int spacesNumber = this.column - asterisksNumber;
                
                for(int j=0; j<spacesNumber; j++){
                    tree += " ";
                    if(j == ((spacesNumber/2)-1)){
                        for(int i=0; i<asterisksNumber; i++){
                            if(this.star && x < 1){
                                tree += "@";
                                continue;
                            }else if(amountBall > 0 && (i+1)%2 == 0 ){
                                tree += "o";
                                amountBall -= 1;
                            }else if(amountLight > 0 && (i+1)%3 == 0 && this.isOnLight()){
                                tree += "+";
                                amountLight -= 1;
                            }else{
                                tree += "*";
                            }
                        }
                    }
                }
            }
            
            //base
            for(int k=0; k<this.column; k++){
                tree += "*";
            }
            
            //tronco
            tree += "\n";
            int base2 = 0;
            int base = this.column - 3;
            
            while(base2 < 2){
                base2 += 1;
                for(int p=0; p<base; p++){
                    tree += " ";
                    if(p == ((base/2)-1)){
                        tree += "|||";
                    }
                }
                tree += "\n";
            }
            
            return tree;
        }
    }

    public static void main(String[] args) {
        System.out.println("Christmas Tree!");
        Scanner scanner = new Scanner(System.in);
        /*El usuario podrá seleccionar las siguientes acciones:
            * - Una luz y una bola no pueden estar en el mismo sitio
        */
        //  * - Altura del arbol
        System.out.println("Ingresa la altura del arbol: ");
        String heigth = scanner.nextLine();
        boolean star = false;
        
        //  * - Añadir o eliminar la estrella en la copa del árbol (@)
        System.out.println("Colocar estrella en la copa del arbol (@) (si/no):");
        String q = scanner.nextLine();
        switch(q.toLowerCase()){
            case "si":
                star = true;
                break;
            case "no":
                star = false;
                break;
            default:
                System.out.println("Respuesta no permirida");
        }
        
        Tree t = new Tree(Integer.parseInt(heigth), star);
        
        //  * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
        int countBall = 0;
        boolean flap = true;
        
        do{
            System.out.println("Añadir (+2/-2) bolas (0) o exit para AÑADIR: ");
            String addOrDelete = scanner.nextLine();
            
            switch(addOrDelete){
                case "+2":
                    countBall += 2;
                    System.out.println("añadir: "+ countBall+"bolas");
                    break;
                case "-2":
                    if(countBall == 0) break;
                    countBall -= 2;
                    System.out.println("Eliminar: "+ countBall+"bolas");
                    break;
                case "exit":
                    flap = false;
                    break;
                default:
                    System.out.println("operacion no permitida.");
            }
            
        }while(flap);
        
        t.setBalls(countBall);
        
        // * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
        int countLight = 0;
        flap = true;
        
        do{
            System.out.println("Añadir (+3/-3) luces (+) o exit para AÑADIR: ");
            String addOrDeleteLight = scanner.nextLine();
            
            switch(addOrDeleteLight){
                case "+3":
                    countLight += 3;
                    System.out.println("añadir: "+ countLight+ " luces");
                    break;
                case "-3":
                    if(countLight == 0) break;
                    countLight -= 3;
                    System.out.println("Eliminar: "+ countLight+" luces");
                    break;
                case "exit":
                    flap = false;
                    break;
                default:
                    System.out.println("operacion no permitida.");
            }
            
        }while(flap);
        
        t.setLights(countLight);
        
        //  * - Apagar (*) o encender (+) las luces (conservando su posición)
        flap = true;
        
        do{
            System.out.println("Encender o Apagar luces (on/off): ");
            String onOff = scanner.nextLine();
            switch(onOff){
                case "on":
                    t.setOnLight(true);
                    break;
                case "off":
                    t.setOnLight(false);
                    break;
                default:
                    System.out.println("operacion no permitida.");
            }

            System.out.println("=======================================");
            String status = (t.isOnLight())?"Encendidas":"Apagadas";
            System.out.println(countBall+ " bolas, "+countLight+" luces, luces: "+status);
            System.out.println(t.draw());
            System.out.println("=======================================");
            
        }while(flap);
        
    }
}
