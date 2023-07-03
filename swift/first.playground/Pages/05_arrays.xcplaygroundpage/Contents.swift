import Foundation

// Arrays

let myName = "Santiago"
let myLastName = "nonas"
let myCompany = "Jiff United LTDA"
let myAge = "35"

var shoppingList = ["Eggs", "Milk"]

// datatype must be specified in some cases, to indicate the program
// how to operate the data within the array

let myClassicArray: [String] = ["like this", "the classic way"]
let myModernArray: [String] = ["This is", "another way"]

let arrays = myClassicArray + myModernArray // Concatenating two arrays

// Inicializando arrays

var anArray = [Int]()
var myNewArray: [String] = []

anArray.append(contentsOf: [1,2,3,4,5,6,7,8,9,10])
print("there are \(anArray.count) items now")

myNewArray.append(myName)
myNewArray.append(myLastName)
myNewArray += [myCompany, myAge] // More ways to append items to a list
myNewArray.append(contentsOf: ["hey there, ", "this is santi again"]) // Append multiple items


// Creating arrays from values that repeat

var repeatingArray = Array(repeating: 6, count: 3)

// Modifying items in an array

repeatingArray[1] = 9 // Use indexing
print(repeatingArray)

// Removing items

repeatingArray.remove(at: 2)
print(repeatingArray)

// Appending single values

repeatingArray.append(6)

// looping through items

for value in anArray {
    print("loop: \(value)")
}

// Creating an array with repeated values

var otherRepeatingArray = Array(repeating: "~", count:6)

// Modifying multiple values within one statement (2 and 3 in this case)

otherRepeatingArray[1 ... 4] = ["two", "three"]

for value in otherRepeatingArray {
    print("Current value: \(value)")
}

// Counting items in an array

print("\nNumber of items in 'other repeating array': \(otherRepeatingArray.count)")
// otherRepeatingArray.removeAll()
print(otherRepeatingArray)

// Accesing data in an array

anArray[2] // Use indexing

// Clean an array

anArray.removeAll()
