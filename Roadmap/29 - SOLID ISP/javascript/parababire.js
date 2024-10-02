// Incorrecto

/* class Entity {
  constructor(name, attackDamage, health) {
    this.name = name
    this.attackDamage = attackDamage
    this.health = health
  }
  move() {
    console.log(`${this.name} moved`)
  }
  attack(targetEntity) {
    console.log(`${this.name} attacked ${targetEntity.name} for ${this.attackDamage} damage`)
    targetEntity.takeDamage(this.attackDamage)
  }
  takeDamage(amount) {
    this.health -= amount
    console.log(`${this.name} has ${this.health} remaining`)
  }
}

class Character extends Entity {
  
}

class Wall extends Entity {
  constructor(name, health) {
    super(name, 0, health)
  }
  move() {
    return null
  }
  attack() {
    return null
  }
}

class Turret extends Entity {
  constructor(name, attackDamage) {
    super(name, attackDamage, -1)
  }
  move() {
    return null
  }
  takeDamage() {
    return null
  }
}

const turret = new Turret('Turret', 5)
const character = new Character('Character', 3, 100)
const wall = new Wall('Wall', 100)

turret.attack(character)
character.move()
character.attack(wall) */

//Correcto

class Entity {
  constructor(name) {
    this.name = name
  }
}

const mover = {
  move() {
    console.log(`${this.name} moved`)
  }
}

const attacker = {
  attack(targetEntity) {
    console.log(`${this.name} attacked ${targetEntity.name} for ${this.attackDamage} damage`)
    targetEntity.takeDamage(this.attackDamage)
  }
}

const hasHealth = {
  takeDamage(amount) {
    this.health -= amount
    console.log(`${this.name} has ${this.health} remaining`)
  }
}

class Character extends Entity {
  constructor(name, attackDamage, health) {
    super(name)
    this.attackDamage = attackDamage
    this.health = health
  }
}

Object.assign(Character.prototype, mover)
Object.assign(Character.prototype, attacker)
Object.assign(Character.prototype, hasHealth)

class Wall extends Entity {
  constructor(name, health) {
    super(name)
    this.health = health
  }
}

Object.assign(Wall.prototype, hasHealth)

class Turret extends Entity {
  constructor(name, attackDamage) {
    super(name)
    this.attackDamage = attackDamage
  }
}

Object.assign(Turret.prototype, attacker)

const turret = new Turret('Turret', 5)
const character = new Character('Character', 3, 100)
const wall = new Wall('Wall', 100)

turret.attack(character)
character.move()
character.attack(wall)