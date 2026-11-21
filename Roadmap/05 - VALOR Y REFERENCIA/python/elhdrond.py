"""
 Value and Reference
"""

# --- By value (primitives: int, float, bool, str, tuple) ---

player_level = 10
enemy_level = player_level
enemy_level = 25
print(f"Player level: {player_level}")  # 10 - unchanged
print(f"Enemy level: {enemy_level}")    # 25 - independent copy

health = 100.0
backup_health = health
backup_health = 999.0
print(f"Current health: {health}")      # 100.0 - unchanged
print(f"Backup health: {backup_health}")  # 999.0

is_alive = True
is_clone_alive = is_alive
is_clone_alive = False
print(f"Player alive: {is_alive}")      # True - unchanged
print(f"Clone alive: {is_clone_alive}") # False

player_name = "Elhdrond"
alias = player_name
alias = "The Shadow"
print(f"Player name: {player_name}")    # Elhdrond - unchanged
print(f"Alias: {alias}")               # The Shadow

# Tuples are immutable, so they behave like by-value
coordinates = (10, 20)
backup_coordinates = coordinates
backup_coordinates = (30, 40)
print(f"Coordinates: {coordinates}")          # (10, 20) - unchanged
print(f"Backup coordinates: {backup_coordinates}")  # (30, 40)

# --- By reference (mutables: list, dict, set) ---

inventory = ["sword", "shield", "potion"]
backup_inventory = inventory
backup_inventory.append("dragon egg")
print(f"Inventory: {inventory}")         # includes dragon egg - same object
print(f"Backup inventory: {backup_inventory}")  # same

stats = {"strength": 80, "agility": 60}
cloned_stats = stats
cloned_stats["strength"] = 999
print(f"Stats: {stats}")                # strength is 999 - same object
print(f"Cloned stats: {cloned_stats}")  # same

active_buffs = {"rage", "haste"}
backup_buffs = active_buffs
backup_buffs.add("shield")
print(f"Active buffs: {active_buffs}")  # includes shield - same object
print(f"Backup buffs: {backup_buffs}")  # same

# --- Functions with by-value parameters ---


def level_up(level: int):
    level += 10
    print(f"Level inside function: {level}")


hero_level = 5
level_up(hero_level)
print(f"Hero level after call: {hero_level}")  # 5 - unchanged


def rename_player(name: str):
    name = "Anonymous"
    print(f"Name inside function: {name}")


hero_name = "Elhdrond"
rename_player(hero_name)
print(f"Hero name after call: {hero_name}")  # Elhdrond - unchanged

# --- Functions with by-reference parameters ---


def loot_item(inv: list, item: str):
    inv.append(item)
    print(f"Inventory inside function: {inv}")


hero_inventory = ["dagger", "rope"]
loot_item(hero_inventory, "golden key")
print(f"Hero inventory after call: {hero_inventory}")  # includes golden key


def boost_stat(s: dict, stat: str, amount: int):
    s[stat] += amount
    print(f"Stats inside function: {s}")


hero_stats = {"strength": 50, "agility": 40}
boost_stat(hero_stats, "strength", 20)
print(f"Hero stats after call: {hero_stats}")  # strength is 70


"""
 Extra
"""


# Swap by value
def swap_scores(score_a: int, score_b: int) -> tuple:
    score_a, score_b = score_b, score_a
    return score_a, score_b


original_score_a = 1500
original_score_b = 3200
new_score_a, new_score_b = swap_scores(original_score_a, original_score_b)

print(f"Original scores: {original_score_a}, {original_score_b}")  # unchanged
print(f"Swapped scores:  {new_score_a}, {new_score_b}")            # swapped


# Swap by reference - modifies originals directly
def swap_inventories(inv_a: list, inv_b: list):
    temp = inv_a.copy()
    inv_a.clear()
    inv_a.extend(inv_b)
    inv_b.clear()
    inv_b.extend(temp)


original_inv_a = ["bow", "arrows"]
original_inv_b = ["staff", "tome"]
print (f"Original inventories: {original_inv_a}, {original_inv_b}")  # before swap
swap_inventories(original_inv_a, original_inv_b)

print(f"Inventories after swap: {original_inv_a}, {original_inv_b}")  # both swapped in-place

# swap by reference - returns new references

def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")