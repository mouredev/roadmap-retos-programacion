<?php
/*
 * EXERCISE:
 * Explore the concept of inheritance in your language. Create an example that
 * implements a superclass Animal and a pair of subclasses Dog and Cat,
 * along with a function that prints the sound each Animal makes.
 */


class Animal
{
    protected $name;
    protected $activity;

    public function __construct($name, $activity)
    {
        $this->name = $name;
        $this->activity = $activity;
    }

    public function what_is_doing()
    {
        echo $this->name . " " . $this->activity . "\n";
    }
}

class Dog extends Animal
{
    private $sound;

    public function __construct($name, $activity, $sound)
    {
        parent::__construct($name, $activity); // Call the parent constructor
        $this->sound = $sound;
    }

    public function make_sound()
    {
        echo $this->name . " makes " . $this->sound . "\n";
    }
}

class Cat extends Animal
{
    private $sound;

    public function __construct($name, $activity, $sound)
    {
        parent::__construct($name, $activity);
        $this->sound = $sound;
    }

    public function make_sound()
    {
        echo $this->name . " makes " . $this->sound . "\n";
    }
}

$cat = new Cat("Felix", "asks for food", "Miauuuu");
$cat->what_is_doing();
$cat->make_sound();

$dog = new Dog("Pipo", "runs after a cat", "Woof Wof");
$dog->what_is_doing();
$dog->make_sound();

 /* EXTRA CHALLENGE (optional):
 * Implement the hierarchy of a development company consisting of Employees who
 * can be Managers, Project Managers, or Programmers.
 * Each employee has an identifier and a name.
 * Depending on their role, they have properties and functions exclusive to their
 * activity, and they store the employees under their supervision.
 */

 