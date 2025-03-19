// Types of data structure

// Array: Stores an ordered collection of elements of the same data type.
var daysOfTheWeek = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
daysOfTheWeek.append("Saturday")
var firstDay = daysOfTheWeek[0]
daysOfTheWeek.sort()
daysOfTheWeek.removeAll()

// Set: Stores an unordered collection of elements of the same data type.
var favoriteMusic: Set = ["Pop","Rock","Electronic","Jazz"]
favoriteMusic.insert("Country")
favoriteMusic.remove("Pop")
//favoriteMusic.sorted(by:>)

// Dictionary: Stores associations between keys of the same type and values of the same type in a collection with no defined ordering.
var seasons = ["Winter": "Cold", "Summer": "Hot", "Autumn": "Windy", "Fall": "Colorful"]
seasons["Other"] = "Random weather"
seasons["Fall"] = nil
//seasons.sorted(by: <)



