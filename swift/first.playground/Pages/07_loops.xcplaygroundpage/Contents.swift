import Foundation

// For, While, Repeat While

let myArray = ["Name", "Code"]
let myDict =  [
    "Santiago":13,
    "Ramirez":11,
    "Alpaca":10,
    "Celeste":12,
    "Alepa":14,
    "Vega":15]

// For

for strings in myArray {
    print(strings)
}

print("")
for element in myDict.values { // Iterating on values only
    print("Value: \(element)")
}

print("")
for index in 1...5 { // To iterate on a range, inclusive. use '1..<5' for exclusive
    print(index)
}

print("")
myDict.forEach { (key, value) in // Methods can also be used for iteration
    print("key \(key), value \(value)")
}

print("")
myDict.forEach { (key, value) in // Calling from an external array is possible
    print("\(myArray[0]): \(key). \(myArray[1]): \(value)")
}

// While

print("\nGoing for Whiles:\n")

var index = 0
while index < 10 {
    print("Current index: \(index)")
    index += 1
}

// Repeat While

print("\nRepeat from now on:\n")
repeat {
    print("Current index: \(index)")
    index += 1
} while index < 20
