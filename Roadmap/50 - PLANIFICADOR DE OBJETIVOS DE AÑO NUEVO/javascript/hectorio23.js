// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const { v4: uuidv4 } = require('uuid');
const fs = require('fs').promises;


/**
 * Represents a goal with a specific amount, description, unit, and time limit.
 */
class Goal {
  static MAX_MONTHS_LIMIT = 12;

  constructor({ amount, description, monthsLimit, units }) {
    if (monthsLimit < 1 || monthsLimit > Goal.MAX_MONTHS_LIMIT) {
      throw new Error(`Months limit must be between 1 and ${Goal.MAX_MONTHS_LIMIT}.`);
    }

    this.id = uuidv4();
    this.amount = amount;
    this.description = description;
    this.monthsLimit = monthsLimit;
    this.units = units;
  }

  /**
   * Generates a year plan based on the goal's properties.
   * @returns {Object} The year plan for the goal.
   */
  toYearPlan() {
    const yearPlan = Goal.initializeYearPlan();
    let remainingAmount = this.amount;
    let monthsAvailable = this.monthsLimit;

    for (const month of Object.keys(yearPlan)) {
      if (remainingAmount === 0 || monthsAvailable === 0) break;

      const monthlyAmount = Math.min(remainingAmount, 1); // Distribute one unit per month
      yearPlan[month].push({ goal: this, amount: monthlyAmount });

      remainingAmount -= monthlyAmount;
      monthsAvailable--;
    }

    return yearPlan;
  }

  static initializeYearPlan() {
    return {
      january: [],
      february: [],
      march: [],
      april: [],
      may: [],
      june: [],
      july: [],
      august: [],
      september: [],
      october: [],
      november: [],
      december: []
    };
  }
}

/**
 * Manages a collection of goals and their yearly plans.
 */
class YearGoals {
  static MAX_GOALS = 10;

  constructor() {
    this.goals = [];
    this.plan = Goal.initializeYearPlan();
  }

  /**
   * Adds a new goal to the collection and updates the yearly plan.
   * @param {Goal} goal - The goal to be added.
   * @returns {boolean} True if the goal was added, false otherwise.
   */
  addGoal(goal) {
    if (this.goals.length >= YearGoals.MAX_GOALS) return false;

    if (this.goals.some(g => g.id === goal.id)) return false;

    this.goals.push(goal);
    this.updatePlan(goal.toYearPlan());
    return true;
  }

  /**
   * Removes a goal from the collection and updates the yearly plan.
   * @param {string} goalId - The ID of the goal to remove.
   * @returns {boolean} True if the goal was removed, false otherwise.
   */
  removeGoal(goalId) {
    const goalIndex = this.goals.findIndex(goal => goal.id === goalId);
    if (goalIndex === -1) return false;

    this.goals.splice(goalIndex, 1);
    this.rebuildPlan();
    return true;
  }

  /**
   * Saves the yearly plan to a file.
   * @param {string} filePath - The path to save the plan.
   * @returns {Promise<void>}
   */
  async savePlan(filePath) {
    const data = Object.entries(this.plan)
      .map(([month, goals]) => {
        const goalsText = goals
          .map(({ goal, amount }, index) => `${index + 1}. ${goal.description} (${amount} ${goal.units}/month)`)
          .join('\n');

        return `${month.toUpperCase()}\n${goalsText}\n`;
      })
      .join('\n');

    await fs.writeFile(filePath, data, 'utf-8');
  }

  /**
   * Updates the yearly plan with a new goal's plan.
   * @param {Object} goalPlan - The plan of the goal to add.
   */
  updatePlan(goalPlan) {
    for (const [month, goals] of Object.entries(goalPlan)) {
      this.plan[month].push(...goals);
    }
  }

  /**
   * Rebuilds the yearly plan based on current goals.
   */
  rebuildPlan() {
    this.plan = Goal.initializeYearPlan();
    this.goals.forEach(goal => this.updatePlan(goal.toYearPlan()));
  }
}


const yearGoals = new YearGoals();

const operations = `
Available Operations:
1 - Add a new goal
2 - Remove a goal
3 - Show all goals
4 - Show yearly plan
5 - Save plan to file
0 - Exit
`;

const promptUser = async () => {
  console.log(operations);

  const userInput = (await import('readline/promises')).createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const choice = await userInput.question('Select an operation: ');
  switch (choice) {
    case '1': {
      const amount = parseInt(await userInput.question('Enter goal amount: '), 10);
      const description = await userInput.question('Enter goal description: ');
      const monthsLimit = parseInt(await userInput.question('Enter months limit (1-12): '), 10);
      const units = await userInput.question('Enter goal units: ');

      const goal = new Goal({ amount, description, monthsLimit, units });
      if (yearGoals.addGoal(goal)) {
        console.log('Goal added successfully.');
      } else {
        console.log('Failed to add goal. Maximum limit reached or duplicate goal.');
      }
      break;
    }
    case '2': {
      const goalId = await userInput.question('Enter the goal ID to remove: ');
      if (yearGoals.removeGoal(goalId)) {
        console.log('Goal removed successfully.');
      } else {
        console.log('Goal not found.');
      }
      break;
    }
    case '3': {
      yearGoals.goals.forEach((goal, index) => {
        console.log(`${index + 1}. ${goal.description} - ${goal.amount} ${goal.units} (ID: ${goal.id})`);
      });
      break;
    }
    case '4': {
      Object.entries(yearGoals.plan).forEach(([month, goals]) => {
        console.log(`${month.toUpperCase()}:`);
        goals.forEach(({ goal, amount }, index) => {
          console.log(`${index + 1}. ${goal.description} (${amount} ${goal.units}/month)`);
        });
      });
      break;
    }
    case '5': {
      const filePath = await userInput.question('Enter file path to save the plan: ');
      await yearGoals.savePlan(filePath);
      console.log(`Plan saved to ${filePath}`);
      break;
    }
    case '0': {
      console.log('Exiting...');
      process.exit(0);
    }
    default:
      console.log('Invalid choice.');
  }

  userInput.close();
  promptUser();
};

// Start the CLI application
promptUser();
