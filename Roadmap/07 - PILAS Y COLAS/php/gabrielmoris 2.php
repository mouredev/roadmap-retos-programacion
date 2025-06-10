<?php
/*
 * EXERCISE:
 * Implement the mechanisms of introduction and retrieval of elements typical of
 * stacks (stacks - LIFO) and queues (queue - FIFO) using an array
 * or list (depending on the possibilities of your language).
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

class Printer
{
    private $documents;
    private $position;
    // Constructor
    public function __construct()
    {
        $this->documents =  [];
        $this->position = 0;
    }

    public function add_document($document)
    {
        $this->documents[] = $document;
        $this->position = count($this->documents) - 1;
    }

    public function print_all()
    {
        if (empty($this->documents)) {
            echo "Nothing to print. \n";
            return;
        }

        $print_positioned_docs = array_reverse($this->documents);

        foreach ($print_positioned_docs as $document) {
            echo "Printing " . $document . ".pdf\n";
        }
        $this->position = 0;
        $this->documents = [];
    }

    public function print_current()
    {
        if (empty($this->documents)) {
            echo "Nothing to print. \n";
            return;
        }

        $document = $this->documents[$this->position];

        echo "Printing " . $document . ".pdf\n";
        unset($this->documents[$this->position]);
        $this->position = ($this->position > 0) ? $this->position - 1 : 0;
    }

    public function search_doc($doc_name)
    {
        $position =  array_search($doc_name, $this->documents);

        if ($position !== false) {
            
            echo "The document is in position " . $position + 1 . ".\n";
            return;
        } else {
            echo "No document named: " . $doc_name . ".pdf \n";
            return;
        }
    }

    public function next_document()
    {
        if (empty($this->documents)) {
            echo "Printer is empty. \n";
            return;
        }

        if ($this->position < count($this->documents) - 1) {
            $this->position += 1;
            echo "You are in position " . ($this->position + 1) . ": " . $this->documents[$this->position] . ".pdf \n";
        } else {
            echo " You are already in LAST possition with document " . $this->documents[$this->position] . ".pdf \n";
            return;
        }
    }

    public function back_document()
    {
        if (empty($this->documents)) {
            echo "Printer is empty. \n";
            return;
        }

        if ($this->position > 0) {
            $this->position -= 1;
            echo "You are in postition " . ($this->position + 1) . ": " .  $this->documents[$this->position] . ".pdf \n";
        } else {
            echo " You are already in the FIRST position with document " . $this->documents[$this->position] . ".pdf \n";
            return;
        }
    }

    public function clear_printer()
    {
        $this->position = 0;
        $this->documents = [];

        echo "Printer queue has been cleared.";
    }
};

function printer()
{

    $printer = new Printer();

    echo "\033c";
    echo "
    ===== PRINTER =====
     1.- New Document 
     2.- Print All
     3.- Print Current
     4.- Search Document
     5.- Go Forward
     6.- Go Back
     7.- Clear Printer
     8.- Exit
    ==================
     \n";

    do {
        $selection = readline("Select an option\n");
        switch ($selection) {
            case 1:
                add_document($printer);
                break;
            case 2:
                print_documents($printer);
                break;
            case 3:
                print_document($printer);
                break;
            case 4:
                search_document($printer);
                break;
            case 5:
                forward($printer);
                break;
            case 6:
                back($printer);
                break;
            case 7:
                clear_printer($printer);
                break;
            case 8:
                echo "\033c";
                echo "Good bye 👋 🌐\n";
                exit;
            default:
                echo "This option doesn't exist.\n";
        }
    } while (true);
};

function add_document($printer)
{
    $name = readline("Write the name of the document without extenstion (.pdf only):\n");
    $printer->add_document($name);
};

function print_documents($printer)
{
    $printer->print_all();
};

function print_document($printer)
{
    $printer->print_current();
};

function search_document($printer)
{
    $document_name = readline("Write the name of the document without extenstion (.pdf only):\n");
    $printer->search_doc($document_name);
};

function forward($printer)
{
    $printer->next_document();
};

function back($printer)
{
    $printer->back_document();
};

function clear_printer($printer)
{
    $printer->clear_printer();
};


printer();
