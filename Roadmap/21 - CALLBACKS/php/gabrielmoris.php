<?php
/*
 * EXERCISE:
 * Explore the concept of callbacks in your language by creating a
 * simple example (of your choice) that demonstrates its functionality.
 */

function return_callback($callback)
{
    return $callback();
}

function echo_sth()
{
    echo "I am in a calback";
}

return_callback("echo_sth");

 /*
 * EXTRA DIFFICULTY (optional):
 * Create a restaurant order simulator using callbacks.
 * It will consist of a function that processes orders.
 * It should accept the dish name, a confirmation callback, a
 * ready callback, and a delivery callback.
 * - It should print a confirmation when processing starts.
 * - It should simulate a random time between 1 to 10 seconds between
 *   processes.
 * - It should invoke each callback following a processing order.
 * - It should notify when the dish is ready or has been delivered.
 */
