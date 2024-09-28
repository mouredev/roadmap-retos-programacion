<?php
/*
 * EXERCISE:
 * Using your language, create a program capable of asynchronously executing
 * a function that will take a specific number of seconds to complete, which
 * can be parameterized. You should also be able to assign it a name.
 * The function prints its name, when it starts, the duration of its execution,
 * and when it finishes.
 */


function async($name, $sleep)
{
    $pid = pcntl_fork(); // creates a new child process.

    if ($pid == -1) {
        die('Failed to fork process');
    } elseif ($pid) {
        return $pid; // Parent process
        // pcntl_wait($status); // Parent process
    } else {
        // Child process
        echo "Starting : $name\n";
        $startTime = time();
        sleep($sleep);
        $endTime = time();
        $executionTime = $endTime - $startTime;
        echo "Function: $name completed in $executionTime seconds\n";
        exit(0);
    }
}
// echo async('Function first', 1);
// echo async('Function second', 2);
// echo async('Function third', 3);
echo "======================\n";
echo "Main process continues\n";

/*
 * EXTRA DIFFICULTY (optional):
 * Using the concept of asynchrony and the previous function, create
 * the following program that executes in this order:
 * - A function C that lasts 3 seconds.
 * - A function B that lasts 2 seconds.
 * - A function A that lasts 1 second.
 * - A function D that lasts 1 second.
 * - Functions C, B, and A are executed in parallel.
 * - Function D starts its execution when the previous 3 have finished.
 */

function executeAsyncFunctions()
{
    $childPids = [];

    // Execute async functions and store child process IDs
    $childPids[] = async('C', 3);
    $childPids[] = async('B', 2);
    $childPids[] = async('A', 1);

    // Wait for all child processes to complete
    foreach ($childPids as $childPid) {
        pcntl_waitpid($childPid, $status);
    }

    // Execute the final async function
    $childPids[] = async('D', 1);
    foreach ($childPids as $childPid) {
        pcntl_waitpid($childPid, $status);
    }
    echo "Main process Finished\n";
    exit(0);
}

executeAsyncFunctions();
