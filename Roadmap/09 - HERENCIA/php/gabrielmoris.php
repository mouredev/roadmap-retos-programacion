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
class Employee
{
    protected $name;
    protected $identifier;
    protected $activity;

    public function __construct($name, $identifier, $activity)
    {
        $this->name = $name;
        $this->identifier = $identifier;
        $this->activity = $activity;
    }

    public function what_are_you_doing()
    {
        echo $this->name . " is " . $this->activity . "\n";
    }

    public function get_name()
    {
        return $this->name;
    }
};


class Manager extends Employee
{
    private $managed_pm;

    public function __construct($name, $identifier, $activity)
    {
        parent::__construct($name, $identifier, $activity);
        $this->managed_pm = [];
    }

    // OverWrite Parent Method
    public function what_are_you_doing()
    {
        if (!empty($this->managed_pm)) {

            foreach ($this->managed_pm as $project_manager) {
                echo $this->name . " asks " . $project_manager->get_name() . " what is he doing.\n";
                $project_manager->what_are_you_doing();
            }
        } else {
            echo $this->name . " " . $this->activity . "\n";
        }
    }

    public function add_pm($new_pm)
    {
        $this->managed_pm[] = $new_pm;
    }

    public function fire_everyone()
    {
        $output = "";
        foreach ($this->managed_pm as $project_manager) {
            if ($project_manager instanceof Project_manager) {
                $output .=  $project_manager->fire_devs();
            }
        }
        $this->managed_pm = [];
        $output .= $this->name . " is now alone and sad.\n";
        echo $output;
    }
}

class Project_manager extends Employee
{
    private $managed_devs;

    public function __construct($name, $identifier, $activity)
    {
        parent::__construct($name, $identifier, $activity);
        $this->managed_devs = [];
    }

    // OverWrite Parent Method
    public function what_are_you_doing()
    {
        if (!empty($this->managed_devs)) {

            foreach ($this->managed_devs as $dev) {
                echo $this->name . " asks " . $dev->get_name() . " what is he doing. " . $dev->what_are_you_doing();
            }
        } else {
            echo $this->name . " " . $this->activity . "\n";
        }
    }

    public function add_dev($new_dev)
    {
        $this->managed_devs[] = $new_dev;
    }


    public function fire_devs()
    {
        $output = "";
        foreach ($this->managed_devs as $dev) {
            $output .= $this->name . " fired " . $dev->get_name() . ". He " . $dev->complain() . ".\n";
        }
        $this->managed_devs = [];
        return $output;
    }
}

class Developer extends Employee
{
    public function __construct($name, $identifier, $activity)
    {
        parent::__construct($name, $identifier, $activity);
    }

    // OverWrite Parent Method
    public function what_are_you_doing()
    {
        return $this->name . " " . $this->activity  . ".\n";
    }

    public function complain()
    {
        $arr_of_complains = ["says - NOOOoooo", "cries silently..", "enters in a state of rage and burns the complete building", "runs in circles", "now has more time for his other side jobs", "doesn't accept it"];

        $complain = $arr_of_complains[array_rand($arr_of_complains)];

        return $complain;
    }
}

echo "================== THE OFFICE ==================\n";
$manager = new Manager("Juan", "Manager", "is making a coffe");
$pm1 = new Project_manager("Jean", "P_M", "hepls devs to make a cofffe");
$pm2 = new Project_manager("Julian", "P_M", "drinks his coffe");
$dev1 = new Developer("John", "Dev", "looks the manager how he makes a coffe");
$dev2 = new Developer("Jim", "Dev", "grinds coffe");
$dev3 = new Developer("Jan", "Dev", "coding");
$future_dev4 = new Developer("Jonny", "Dev", "something");
$pm1->add_dev($dev1);
$pm1->add_dev($dev2);
$pm2->add_dev($dev3);

$manager->what_are_you_doing(); // Juan is making a coffee.
$manager->add_pm($pm1);
$manager->add_pm($pm2);
$pm1->what_are_you_doing();
// Jean asks John what is he doing. John looks the manager how he makes a coffe. 
// Jean asks Jim what is he doing. Jim grinds coffe.
echo $pm2->fire_devs(); // Julian fired Jan. He runs in circles.
$pm2->add_dev($future_dev4);
$manager->fire_everyone();
// Jean fired John. He cries silently...
// Jean fired Jim. He runs in circles.
// Julian fired Jonny. He enters in a state of rage and burns the complete building.
// Juan is now alone and sad.