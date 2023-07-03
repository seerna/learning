import Foundation

var myString = "666"
//myString = "Santi" // Uncomment to get a 'nil' output
let myInt = Int(myString) // Value is optional as the argument can be empty or non-compatible

// To operate over an optional, we must unpack it first
// Do it with an !

if myInt != nil {
    print("It's an unpacked int! <\(myInt!)>")
} else {
    print ("it's nil lol")
}

// Defining optionals

var myNewString: String? // This way, the variable can have a string or be nil
myNewString = "Hey" // Comment to get a 'nil' return
print(myNewString)

// Optional link

if let myNoNilString = myNewString {
    print(myNoNilString)
}
