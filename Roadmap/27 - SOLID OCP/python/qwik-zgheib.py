# -- exercise 
# incorrect
class LegionCommander:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def add_skill(self, skill_name, damage):
        skill = {"skill_name": skill_name, "damage": damage}
        self.skills.append(skill)

    def use_skill(self, skill_name):
        for skill in self.skills:
            if skill["skill_name"] == skill_name:
                print(f"{self.name} uses {skill_name} dealing {skill['damage']} damage")
                return
        print(f"{self.name} does not have the skill {skill_name}")

legion = LegionCommander("Legion Commander")
legion.add_skill("Overwhelming Odds", 100)
legion.add_skill("Press the Attack", 50)
legion.use_skill("Overwhelming Odds")
legion.use_skill("Duel")

# If we want to add a new skill, we have to modify the class.
legion.add_skill("Duel", 150)
legion.use_skill("Duel")


# correct
class Skill:
    def use(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class OverwhelmingOdds(Skill):
    def use(self, hero_name):
        print(f"{hero_name} uses Overwhelming Odds dealing 100 damage")

class PressTheAttack(Skill):
    def use(self, hero_name):
        print(f"{hero_name} uses Press the Attack healing 50 health")

class Duel(Skill):
    def use(self, hero_name):
        print(f"{hero_name} uses Duel dealing 150 damage")

class LegionCommander:
    def __init__(self, name):
        self.name = name
        self.skills = {}

    def add_skill(self, skill_name, skill):
        self.skills[skill_name] = skill

    def use_skill(self, skill_name):
        skill = self.skills.get(skill_name)
        if skill:
            skill.use(self.name)
        else:
            print(f"{self.name} does not have the skill {skill_name}")

print("----------------------------------------------------------------")
legion = LegionCommander("Legion Commander")
legion.add_skill("Overwhelming Odds", OverwhelmingOdds())
legion.add_skill("Press the Attack", PressTheAttack())
legion.use_skill("Overwhelming Odds")
legion.use_skill("Duel")

# We can add new skills without modifying the LegionCommander class
legion.add_skill("Duel", Duel())
legion.use_skill("Duel")


# -- extra challenge
import math

class Operation:
    def calculate(self, a, b):
        raise NotImplementedError("Subclasses should implement this method")

class Addition(Operation):
    def calculate(self, a, b):
        return a + b

class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b

class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b

class Division(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

class Power(Operation):
    def calculate(self, a, b):
        return math.pow(a, b)

class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, operator, operation):
        self.operations[operator] = operation

    def calculate(self, operator, a, b):
        if operator in self.operations:
            return self.operations[operator].calculate(a, b)
        else:
            raise ValueError(f"Operation '{operator}' not supported")

print("----------------------------------------------------------------")
calculator = Calculator()

# add basic operations
calculator.add_operation('+', Addition())
calculator.add_operation('-', Subtraction())
calculator.add_operation('*', Multiplication())
calculator.add_operation('/', Division())

a, b = 10, 5
print(f"Addition: {a} + {b} = {calculator.calculate('+', a, b)}")
print(f"Subtraction: {a} - {b} = {calculator.calculate('-', a, b)}")
print(f"Multiplication: {a} * {b} = {calculator.calculate('*', a, b)}")
print(f"Division: {a} / {b} = {calculator.calculate('/', a, b)}")

# add new operation - power
calculator.add_operation('^', Power())
print(f"Power: {a} ^ {b} = {calculator.calculate('^', a, b)}")
