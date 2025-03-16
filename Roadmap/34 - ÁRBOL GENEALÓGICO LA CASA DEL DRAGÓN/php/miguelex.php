<?php

class Person {
    private $id;
    private $name;
    private $partner;
    private $children = [];

    public function __construct($id, $name) {
        $this->id = $id;
        $this->name = $name;
    }

    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function setPartner($partner) {
        $this->partner = $partner;
    }

    public function getPartner() {
        return $this->partner;
    }

    public function addChild($child) {
        $this->children[] = $child;
    }

    public function getChildren() {
        return $this->children;
    }
}

class FamilyTree {
    private $people = [];

    public function addPerson($id, $name) {
        $this->people[$id] = new Person($id, $name);
    }

    public function removePerson($id) {
        unset($this->people[$id]);
    }

    public function setPartner($id1, $id2) {
        if (isset($this->people[$id1]) && isset($this->people[$id2])) {
            $this->people[$id1]->setPartner($this->people[$id2]);
            $this->people[$id2]->setPartner($this->people[$id1]);
        }
    }

    public function addChild($parentId, $childId) {
        if (isset($this->people[$parentId]) && isset($this->people[$childId])) {
            $this->people[$parentId]->addChild($this->people[$childId]);
        }
    }

    public function printTree() {
        foreach ($this->people as $person) {
            if (!$this->hasParents($person)) {
                $this->printSubTree($person);
                echo "\n";
            }
        }
    }

    private function printSubTree($person, $indent = 0) {
        echo str_repeat(" ", $indent) . $person->getName();
        if ($person->getPartner()) {
            echo " ⟷ " . $person->getPartner()->getName();
        }
        echo "\n";

        foreach ($person->getChildren() as $child) {
            $this->printSubTree($child, $indent + 4);
        }
    }

    private function hasParents($person) {
        foreach ($this->people as $other) {
            if (in_array($person, $other->getChildren())) {
                return true;
            }
        }
        return false;
    }
}

$tree = new FamilyTree();
$tree->addPerson(1, "Aegon I Targaryen");
$tree->addPerson(2, "Rhaenys Targaryen");
$tree->addPerson(3, "Visenya Targaryen");

$tree->addPerson(4, "Aenys I Targaryen");
$tree->addPerson(5, "Maegor I Targaryen");

$tree->addPerson(6, "Jaehaerys I Targaryen");
$tree->addPerson(7, "Alysanne Targaryen");

$tree->addPerson(8, "Aegon II Targaryen");
$tree->addPerson(9, "Helaena Targaryen");

$tree->addPerson(10, "Viserys II Targaryen");

$tree->addPerson(11, "Rhaenyra Targaryen");
$tree->addPerson(12, "Daemon Targaryen");

$tree->setPartner(1, 2); // Aegon I y Rhaenys
$tree->setPartner(1, 3); // Aegon I y Visenya
$tree->setPartner(4, 7); // Jaehaerys I y Alysanne
$tree->setPartner(8, 9); // Aegon II y Helaena
$tree->setPartner(11, 12); // Rhaenyra y Daemon

$tree->addChild(1, 4); // Aenys I hijo de Aegon I y Rhaenys
$tree->addChild(1, 5); // Maegor I hijo de Aegon I y Visenya

$tree->addChild(4, 6); // Jaehaerys I hijo de Aenys I
$tree->addChild(4, 11); // Rhaenyra hija de Aenys I

$tree->addChild(6, 8); // Aegon II hijo de Jaehaerys I
$tree->addChild(6, 10); // Viserys II hijo de Jaehaerys I

$tree->printTree();
