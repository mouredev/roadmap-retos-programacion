<?php
/*
* EXERCISE:
* Explore the concept of a class and create an example that implements an initializer,
* attributes, and a function that prints them (taking into account the possibilities
* of your language).
* Once implemented, create it, set its parameters, modify them, and print them
* using its function.
*/
class My_Class
{
    // This would be the private properties:
    private $data;

    // Constructor
    public function __construct()
    {
        $this->data = [];
    }

    // Private functions are available only internally

    private function _count()
    {
        return count($this->data);
    }

    // Public Functions are available outside
    public function add(string $item): int
    {
        $this->data[] = $item;
        return  $this->_count();
    }

    public function delete($item): int
    {
        $pos = array_search($item, $this->data);
        unset($this->data[$pos]);
        return  $this->_count();
    }

    public function clear(): int
    {
        $this->data = [];
        return  $this->_count();
    }

    public function find($item)
    {
        $pos = array_search($item, $this->data);
        return $this->data[$pos];
    }

    public function is_empty()
    {
        return empty($this->data);
    }


    // Getters
    public function get_data(): array
    {
        return $this->data;
    }

    // Setters
    public function set_data(array $data): void
    {
        $this->data = $data;
    }
}

$my_class = new My_Class();
$my_class->add("item1");
$my_class->add("item2");
$my_class->add("item3");
$my_class->add("item4");
$my_class->add("item5");

foreach ($my_class->get_data() as $data) {
    echo "Data: " . $data . "\n";
}

$my_class->set_data([1, 2, 3, 4, 5]);
foreach ($my_class->get_data() as $data) {
    echo "Data: " . $data . "\n";
}
$is_empty = $my_class->is_empty() ? " YES\n" : " NO\n";
echo "Is Empty? : " .  $is_empty;
$my_class->clear();
$is_empty2 = $my_class->is_empty() ? " YES\n" : " NO\n";
echo "And Now? : " . $is_empty2;

/* EXTRA DIFFICULTY (optional):
* Implement two classes that represent the Stack and Queue structures (studied
* in exercise number 7 of the study path)
* - They must be able to initialize and have operations to add, remove,
*   return the number of elements, and print all their contents.
*/


class Stack
{
    private $pages;
    private $length;

    // Constructor
    public function __construct()
    {
        $this->items =  [];
        $this->length = 0;
    }

    public function push($item)
    {
        $this->length += 1;
        array_push($this->items, $item);
    }

    public function pop()
    {
        $this->length -= 1;
        return array_pop($this->items);
    }

    public function peek()
    {
        if (empty($this->items)) {
            return null;
        }

        return  $this->items[count($this->items) - 1];
    }

    public function size()
    {
        return  $this->length;
    }

    public function search($item)
    {
        $index = array_search($item, $this->items);

        if (!$index && $index !== 0) {
            return -1;
        }

        return $index;
    }

    public function clear()
    {
        $this->length = 0;
        $this->items = [];
    }
}

echo "====== STACK ======\n";
$st = new Stack();
$st->push(1);
echo $st->peek() . "\n"; // 1
$st->push(2);
echo $st->peek() . "\n"; // 2
echo $st->search(1) . "\n"; //0
echo $st->pop() . "\n"; // 2
echo $st->peek() . "\n"; // 1
echo $st->search(2) . "\n"; // -1


class Queue
{
    private $items;
    private $length;

    // Constructor
    public function __construct()
    {
        $this->items =  [];
        $this->length = 0;
    }

    public function enqueue($item)
    {
        $this->length += 1;
        array_push($this->items, $item);
    }

    public function dequeue()
    {
        $this->length -= 1;
        return array_shift($this->items);
    }

    public function peek()
    {
        if (empty($this->items)) {
            return null;
        }

        return  $this->items[0];
    }

    public function size()
    {
        return  $this->length;
    }

    public function search($item)
    {
        $index = array_search($item, $this->items);

        if (!$index && $index !== 0) {
            return -1;
        }

        return $index;
    }

    public function clear()
    {
        $this->length = 0;
        $this->items = [];
    }
}

echo "====== QUEUE ======\n";
$qu = new Queue();
$qu->enqueue(1);
echo $qu->peek() . "\n"; // 1
$qu->enqueue(2);
echo $qu->peek() . "\n"; // 1
echo $qu->search(1) . "\n"; // 0
echo $qu->dequeue() . "\n"; // 1
echo $qu->peek() . "\n"; // 2
echo $qu->search(2) . "\n"; // 0