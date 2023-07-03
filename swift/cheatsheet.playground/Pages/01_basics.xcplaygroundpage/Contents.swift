import Foundation

//: Constans and Variables

let maxNumberOfLoginAttempts = 10 // Unmutable
var currentLoginAttempt = 0 // Mutable

var x = 0, y = 1, z = 2

/* Remember to use variables only when values are going to change */

//: Type Annotations

var welcomeMessage: String // Will annotate that the value must be a string

welcomeMessage = "Hey" // Now it can be set, as it was declared before
//welcomeMessage = 9 // Will not work as the value is not a String

var red, green, blue: Double // You can annotate multiple variables at once

/* Swift usually infer the type to be used for a constant or variable */

print(maxNumberOfLoginAttempts, terminator: "") // Will print without the line break (\n)
print("\n")

print("You current loggin attempt is: \(currentLoginAttempt).")
print("The max number of attempts is: \(maxNumberOfLoginAttempts).")

//: Semicolons

let cat = "🐱"; print(cat) // Using ; lets you write multiple separate statements on a single line
