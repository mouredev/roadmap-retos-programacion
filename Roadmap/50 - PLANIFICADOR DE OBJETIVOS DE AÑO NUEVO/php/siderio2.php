<?php

/**
 * @author Desiderio Martínez Silva aka siderio2
 * @version 1.0
 * @link https://github.com/siderio2
 * @see https://retosdeprogramacion.com/roadmap/
 *
 * PHP implementation of the New Year Goals Planner 50 exercise from Mouredev Roadmap
 * Program a goal manager with the following features:
 *  - Allows you to add goals (maximum 10)
 *  - Calculate the detailed plan
 *  - Save the planning
 *
 * Each goal entry is made up of (with an example):
 *  - Goal: Read books
 *  - Quantity: 12
 *  - Units: books
 *  - Deadline (in months): 12 (maximum 12)
 *
 * The detailed plan calculation will generate the following output:
 * - A section for each month
 * - A list of calculated goals to be met in each month
 * (example: if I want to read 12 books, it will result in
 * one per month)
 * - Each goal must have its name, the number of
 * units to be completed in each month and its total. For example:
 *
 * January:
 * [ ] 1. Read books (1 book/month). Total: 12.
 * [ ] 2. Study Git (1 course/month). Total: 1.
 * February:
 * [ ] 1. Read books (1 book/month). Total: 12.
 * ...
 * December:
 * [ ] 1. Read books (1 book/month). Total: 12.
 *
 * - If the duration is less than a year, it will end in the corresponding
 * month.
 *
 * Finally, the detailed calculation must be exportable to .txt
 */

// Defining constants
const YEAR = ['January:', 'February:', 'March:', 'April:', 'May:', 'June:', 'July:', 'August:', 'September:', 'October:', 'November:', 'December:'];
const MAX_GOALS = 10;

// Defining the varible to store the goals
$goals = [];

/*
 * Main loop
 * Allows user to add goals (maximum determined by MAX_GOALS constant)
 * Each iteration of the loop allows the user to add a goal
 * If the user does not want to add a goal, the loop will end
 * If the user wants to add a goal, the loop will ask for the goal details,
 * checking that they are valid and adding them to the goal array
 */
do {
  do {
    $opt = readline("Do you want to add a goal to your 2025 calendar? (y)es / (n)o:");
    $opt = strtolower($opt);
  } while ($opt != 'y' && $opt != 'n');

  if ($opt === 'n') {
    break;
  }

  $goal = [];
  do {
    $goal['name'] = readline("Goal name (min 3 / máx. 30 chars): ");
  } while (strlen($goal['name']) < 2 || strlen($goal['name']) > 30);

  do {
    $goal['unity'] = readline("Unities (min 3 / máx. 30 chars): ");
  } while (strlen($goal['unity']) < 2 || strlen($goal['unity']) > 30);

  do {
    $quantity = readline("How many " . $goal['unity'] . " (1 at least)? ");
  } while (!is_numeric($quantity) || (int)$quantity <= 0);
  $goal['quantity'] = (int)$quantity;

  do {
    $deadline = readline("How many months to reach the goal (1 - 12)? ");
  } while (!is_numeric($deadline) || (int)$deadline < 1 || (int)$deadline > 12);
  $goal['deadline'] = (int)$deadline;

  $goals[] = $goal;
} while (count($goals) < MAX_GOALS);

/**
 * Generates a yearly plan based on the given goals.
 *
 * The plan is broken down per month and will show the goal name, the number of
 * units to be completed in each month and its total.
 *
 * @param array $goals The goals to generate the plan for.
 * @return array The yearly plan, one item per month.
 */
function calculatePlan(array $goals): array
{
  $yearlyPlan = [];
  foreach (YEAR as $month) {
    $monthlyPlan = $month . "\n";
    $goalOrder = 1;

    foreach ($goals as $goal) {
      if (array_search($month, YEAR) >= $goal['deadline']) {
        continue;
      }
      $monthlyGoal = $goal['quantity'] / $goal['deadline'];
      if (is_float($monthlyGoal)) {
        $monthlyGoal = number_format($monthlyGoal, 2);
      }
      $monthlyPlan .= "[ ] " . $goalOrder . ". " . $goal['name'] . " (" . $monthlyGoal . " " . $goal['unity'] . "/month). Total: " . $goal['quantity'] . ".\n";
      $goalOrder++;
    }

    $yearlyPlan[] = $monthlyPlan;
  }
  return $yearlyPlan;
}

/**
 * Prints the given yearly plan to the console.
 *
 * @param array $yearlyPlan The yearly plan to print, one item per month.
 */
function printPlan(array $yearlyPlan): void
{
  foreach ($yearlyPlan as $monthlyPlan) {
    echo $monthlyPlan;
  }
}

/**
 * Saves the given yearly plan to a file named "plan_2025.txt"
 *
 * @param array $yearlyPlan The yearly plan to save, one item per month.
 */
function planToFile(array $yearlyPlan): void
{
  $fileName = "plan_2025.txt";
  $content = "\n2025 Goals:\n";
  foreach ($yearlyPlan as $monthlyPlan) {
    $content .= $monthlyPlan;
  }

  $file = fopen($fileName, 'w');

  if ($file === FALSE) {
    echo "\nOOOPS! There's been a problem opening the " . $fileName . " file: " . error_get_last()['message'];
  } else {
    if (fwrite($file, $content) === FALSE) {
      echo "\nOOOPS! There's been a problem writing the content to " . $fileName . " file: " . error_get_last()['message'];
    } else {
      echo "\nThe " . $fileName . " with your 2025 goals is ready!";
    }
  }
}

$yearlyPlan = calculatePlan($goals);
printPlan($yearlyPlan);
planToFile($yearlyPlan);
