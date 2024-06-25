<?php

    // Ejercicio básico

    class User {
        private $name;
        private $role;

        public function __construct($name, $role){
            $this->name = $name;
            $this->role = $role;
        }

        public function getName(){
            return $this->name;
        }

        public function getRole(){
            return $this->role;
        }

        public function saveUser(){
            $file = fopen('usersBD.txt', 'a');
            fwrite($file, $this->name . ' is a  ' . $this->role . PHP_EOL);
            fclose($file);
        }
    }

    echo "\n\nVamos a mostrar primero una clase que no cumple el SRP. Esto se debe a que la clase, ademas de gestionar el usuario, realizar la inserccion en BD (en este caso simualdo con un txt)\n\n";
    $user1 = new User('Miguel', 'Admin');
    $user1->saveUser();
    $user2 = new User('Maria', 'user');
    $user2->saveUser();
    echo "\nSe ha creado el archivo y podemos ver se ha ineertado correctamente. Vamos a refactorizar ahora para cumplir el SRP\n\n";


    class Users {
        private $name;
        private $role;

        public function __construct($name, $role){
            $this->name = $name;
            $this->role = $role;
        }

        public function getName(){
            return $this->name;
        }

        public function getRole(){
            return $this->role;
        }
    }

    class UsersBD {
        private $path;

        public function __construct($path){
            $this->path = $path;
        }

        public function saveUser(Users $users){
            $file = fopen($this->path, 'a');
            fwrite($file, $users->getName() . ' is a  ' . $users->getRole() . PHP_EOL);
            fclose($file);
        }
    }

    echo "\n\nHemos refactorizado el codigo anterior, separando la parte de usuarios de la parte de BD\n\n";
    $user1 = new Users('Miguel', 'Admin');
    $user2 = new Users('Maria', 'user');
    $userBD = new UsersBD('userBDSRP.txt');
    $userBD->saveUser($user1);
    $userBD->saveUser($user2);
    echo "\nSe ha creado el archivo y podemos ver se ha insertado correctamente. A efectos de funcionamiento ambas solucioens funcionan igual pero la segunda es mas legible y mantenible\n\n";

    echo "\n\nEjercicio Extra\n\n";

    // Extra

   