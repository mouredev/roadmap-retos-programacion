# pylint: disable=missing-function-docstring,pointless-string-statement,expression-not-assigned

"""
    Sets...
"""

print("Sets...")

states: list[str] = ["Buenos Aires", "Texas", "Madrid", "Houston", "California"]


print('\nstates: list[str] = ["Texas", "Madrid", "Houston", "California"]')

print(f"{states=}")

print("\nAppend new state at the end...")
print('\nstates.append("Berlin")')

states.append("Berlin")
print(f"{states=}")

print("\nAppend new state at the start...")
print('\nstates.insert(0, "Chaco")')

states.insert(0, "Chaco")
print(f"{states=}")

print("\nAppend several states at the end...")
print('\nstates.extend(["Paris", "Montana"])')

states.extend(["Paris", "Montana"])
print(f"{states=}")

print("\nAppend several states at index 4...")
print('\nstates = [*states[0:4], *["Jujuy", "Formosa"], *states[4:]]')

states = [*states[0:4], *["Jujuy", "Formosa"], *states[4:]]
print(f"{states=}")

print("\nDelete state at index 3...")
print("\nstates = [*states[0:3], *states[3 + 1:]]")

states = [*states[0:3], *states[3 + 1 :]]
print(f"{states=}")

print("\nUpdate state at index 6...")
print('\nstates[6] = "Miami"')

states[6] = "Miami"
print(f"{states=}")

print("\nCheck if a state is present...")
print(f'\nstates.count("Buenos Aires") > 0 => {states.count("Buenos Aires") > 0}')

print(f"{states=}")

print("\nClear saved data...")
print("\ndata.clear()")

states.clear()
print(f"{states=}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")

first_set: set[str] = {"Hello", "TypeScript", "World!"}
second_set: set[str] = {"By", "TypeScript"}

print(f"\n{first_set=}")
print(f"{second_set=}")

intersected: set[str] = first_set.intersection(second_set)

print("\nintersected: set[str] = first_set.intersection(second_set)")
print(f"{intersected=}")

joined: set[str] = first_set.union(second_set)

print("\njoined: set[str] = first_set.union(second_set)")
print(f"{joined=}")

difference: set[str] = first_set.difference(second_set)

print("\ndifference: set[str] = first_set.difference(second_set)")
print(f"{difference=}")

symmetric_difference: set[str] = first_set.symmetric_difference(second_set)

print("\nsymmetric_difference: set[str] = first_set.symmetric_difference(second_set)")
print(f"{symmetric_difference=}")
