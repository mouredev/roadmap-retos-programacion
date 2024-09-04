import random, time

deadpool_health = int(input("Introduce la vida de Deadpool: "))
wolverine_health = int(input("Introduce la vida de Wolverine: "))

turn = 0
regenerate = False

while deadpool_health > 0 and wolverine_health > 0:

  turn += 1
  print(f"\nTurno {turn}")

  if regenerate:
    print("Deadpool se está regenerando y no ataca.")
    regenerate = False

  elif random.random() > 0.2:
    deadpool_damage = random.randint(10, 100)
    print(f"Deadpool ataca a Wolverine con {deadpool_damage} de daño.")
    if deadpool_damage == 100:
      regenerate = True
      print(
        "¡Golpe crítico de Deadpool! Wolverine no atacará en el siguiente turno ya que tiene que regenerarse."
      )

    wolverine_health  -= deadpool_damage

    if wolverine_health <= 0:
      print(f"La vida de Wolverine ha llegado a cero.")
      break
    else:
      print(f"Vida restante de Wolverine: {wolverine_health}")
  else:
    print("¡Wolverine esquiva el ataque de Deadpool!")

  if regenerate:
    print("Wolverine se está regenerando y no ataca.")
    regenerate = False

  elif random.random() > 0.25:
    wolverine_damage = random.randint(10, 120)
    print(f"Wolverine ataca a Deadpool con {wolverine_damage} de daño.")
    if wolverine_damage == 120:
      regenerate = True
      print(
        "¡Golpe crítico de Wolverine! Deadpool no atacará en el siguiente turno ya que tiene que regenerarse."
      )

    deadpool_health -= wolverine_damage
    if deadpool_health <= 0:
      print(f"La vida de Deadpool ha llegado a cero.")
      break
    else:
      print(f"Vida restante de Deadpool: {deadpool_health}")
  else:
    print("¡Deadpool esquiva el ataque de Wolverine!")

  time.sleep(1)

if deadpool_health > 0:
  print(f"Deadpool gana la batalla con {deadpool_health} de vida restante.")
else:
  print(f"Wolverine gana la batalla con {wolverine_health} de vida restante.")