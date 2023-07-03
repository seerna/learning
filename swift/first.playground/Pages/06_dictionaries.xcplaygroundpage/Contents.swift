import Foundation

// In swift, dictionary data types must be consistent
// Keys and values can have different types

// Declaring a dict

var myOldDict = Dictionary<String, Int>() // Clasic way
var myDict = [String:Int]() // Modern way

// Adding values

myDict = ["Santiago":13, "Ramirez":11, "Alpaca":10, "Celeste":12]
myDict["Alepa"] = 14
myDict.updateValue(15, forKey: "Vega")

// Accessing data

print("Vega: \(myDict["Vega"])")
print("Juaneste: \(myDict["Juaneste"])") // 'nil' if the key doesn't exist

// Updating a value
myDict["Alepa"] = 09 // By direct assignation
myDict.updateValue(14, forKey: "Alepa") // By using a method

// Delete a value

myDict["Alepa"] = nil
myDict.removeValue(forKey: "Vega")
print("Vega: \(myDict["Vega"])")

// Looping through a dict

print("\n- Looping though keys and values:")
for (key, value) in myDict {
    print("Key: \(key). Value: \(value).")
}

print("\n- Looping though keys:")
for key in myDict.keys {
    print("Key: \(key).")
}

print("\n- Looping though values:")
for value in myDict.values {
    print("Value: \(value).")
}
