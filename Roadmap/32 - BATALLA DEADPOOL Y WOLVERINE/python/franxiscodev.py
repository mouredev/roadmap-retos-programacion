'''
Batalla deadpool vs wolverine
'''
import random
import time

# DEADPOOL_HEALTH = 1000
# WOLVERINE_HEALTH = 1200

deadpool_health = 1000
wolverine_health = 1200

turn = 0
regenerate = False

while deadpool_health > 0 and wolverine_health > 0:

    turn += 1
    print(f"\n⌛ Turno {turn}")

    # Deadpooll ataca
    if regenerate:
        print("❌ Deadpool se está regenerando y no ataca")
        regenerate = False
    elif random.random() > 0.2:
        deadpool_damage = random.randint(10, 100)
        print(f"Deadpool ataca con daño {deadpool_damage}")
        if deadpool_damage > 80:
            regenerate = True
            print(
                f"🤜🤜🤜 Deadpool crítico! {deadpool_damage}: Wolverine no atacará en el siguiente turno")
        wolverine_health -= deadpool_damage

        if wolverine_health <= 0:
            print(f"Vida de Wolverine a CERO fin: {wolverine_health}")
            break
        else:
            print(f"Vida restante de Wolverine {wolverine_health}")
    else:
        print("🛡️  Wolverine esquiva el ataque de Deadpool")

    # Wolverine ataca
    if regenerate:
        print("❌ Wolverine se está regenerando y no ataca")
        regenerate = False
    elif random.random() > 0.25:
        wolverine_damage = random.randint(10, 120)
        print(f"Wolverine ataca con daño {wolverine_damage}")
        if wolverine_damage > 100:
            regenerate = True
            print(
                f"🤜🤜🤜 Wolverine crítico! {wolverine_damage}: Deadpool no atacará en el siguiente turno")
        deadpool_health -= wolverine_damage

        if deadpool_health <= 0:
            print(f"Vida de Deadpool a CERO fin: {deadpool_health}")
            break
        else:
            print(f"Vida restante de Deadpool {deadpool_health}")
    else:
        print("🛡️  Deadpool esquiva el ataque de Wolverine")
    time.sleep(1)

if deadpool_health > 0:
    print(f"💯 Deadpool gana la batalla {deadpool_health}")
else:
    print(f"💪 Wolverine gana la batalla {wolverine_health}")
