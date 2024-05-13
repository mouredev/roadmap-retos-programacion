<?php
/*
 * EXERCISE:
 * Implement the mechanisms of introduction and retrieval of elements typical of
 * stacks (stacks - LIFO) and queues (queue - FIFO) using an array
 * or list (depending on the possibilities of your language).
 */

class Stack
{
    private $items;
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

/*
 * EXTRA DIFFICULTY (optional):
 * - Using the stack implementation and text strings, simulate the forward/back
 *   mechanism of a web browser. Create a program in which you can navigate to a page or tell it
 *   that you want to move forward or backward, showing in each case the name of the web.
 *   The words "forward", "backward" trigger this action, the rest is interpreted as
 *   the name of a new web.
 * - Using the queue implementation and text strings, simulate the mechanism of a
 *   shared printer that receives documents and prints them when indicated.
 *   The word "print" prints an element from the queue, the rest of the words are
 *   interpreted as document names.
 */