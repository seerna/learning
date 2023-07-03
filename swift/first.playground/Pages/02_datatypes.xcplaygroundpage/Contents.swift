import UIKit

// Strings

let myString0 = "Text to plant ideas"
let myString1 = "that can change"
let myString2 = myString0 + " " + myString1

// Int

let myInt0 = 30
let myInt1 = 3
let myInt2 = myInt0 + myInt1

print(myInt0 + myInt1 * 2) // Can concatenate & operate in print arguments

// Double (for short decimals)

let myDouble0 = 1.5
let myDouble1 = 1.8

print(myDouble0 + myDouble1)

// Float (for long decimals, very tiny numbers)

let myFloat0: Float = 1.6 // these must be declared as floats
let myFloat1: Float = 1.8

print(myFloat0 + myFloat1) // Can only operate Float vs Float

// Bool

var myBool0 = false
let myBool1 = true

//myBool0 = myBool1 // if var, then it can be changed

print(myBool0)

print(myBool0 && myBool1)
print(myBool0 == myBool1)
