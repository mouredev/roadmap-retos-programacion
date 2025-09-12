// Array
let fruits = ["Apple", "Banana"]
console.log(fruits)
fruits.push("Orange") // Insert
console.log(fruits)
fruits.pop() // Remove
console.log(fruits)
console.log(fruits[0]) // Get
fruits[0] = "Blueberry" // Update
console.log(fruits)
fruits.sort() // Sort
console.log(fruits)
console.log(typeof fruits)

// Tuple
let my_Tuple = [5, false, 'Coding God was here']
console.log(my_Tuple)
my_Tuple.push("39") // Insert
console.log(my_Tuple)
my_Tuple.pop() // Remove
console.log(my_Tuple)
console.log(my_Tuple[1]) // Get
console.log(my_Tuple)
my_Tuple[1] = true // Update
console.log(my_Tuple)
my_Tuple.sort() // Sort
console.log(my_Tuple)
console.log(typeof my_Tuple)

// Sets
const my_Set = new Set(["orange", "apple", "banana"])
console.log(my_Set)
my_Set.add("3") // Insert
console.log(my_Set)
my_Set.delete("3") // Remove
console.log(my_Set)
console.log(my_Set.has("orange")) // Get
console.log(typeof my_Set)

// Dictionary
let my_dict = {
  "name": "Sniker",
  "surname": "Dev",
  "age": "20"
}
console.log(my_dict)
my_dict["email"] = "sniker@gmail.com"  // Insert
console.log(my_dict)
delete my_dict["surname"] // Remove
console.log(my_dict)
console.log(my_dict["name"]) // Get
my_dict["name"] = "Stick";
console.log(my_dict) // Update
console.log(typeof my_dict)

// Map
const my_Map = new Map();
my_Map.set('Apples', 500) // Insert
my_Map.set('Orange', 100)
console.log(my_Map)
console.log(my_Map.get("Apples")) // Get
my_Map.set('Apples', 200) // Update
console.log(my_Map)
my_Map.delete("Apples") // Remove
console.log(my_Map)