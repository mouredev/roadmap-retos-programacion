<?php

    $stack = new SplStack();

    $stack->push(1);
    $stack->push(2);
    $stack->push(3);

    echo "Stack: ";

    $stack->rewind();
    while($stack->valid()) {
        echo $stack->current();
        $stack->next();
    }

    $queue= new SplQueue();

    $queue->enqueue(1);
    $queue->enqueue(2);
    $queue->enqueue(3);

    echo "\nQueue: ";

    $queue->rewind();
    while($queue->valid()) {
        echo $queue->current();
        $queue->next();
    }

?>
