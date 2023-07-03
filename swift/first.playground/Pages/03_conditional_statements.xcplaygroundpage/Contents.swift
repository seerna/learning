import Foundation

// Logical Operators
// && == "and"
// || == "or"

let myNumber = 6

// if

if myNumber < 6 {
    print("less than six")
} else if myNumber > 6 {
    print("more than six")
} else if myNumber == 6 {
    print("equal six")
}

if myNumber <= 5 || myNumber  >= 7 {
    print("it's not six")
} else {
    print("it's six")
}

if myNumber < 6 && myNumber < 3 {
    print("less than 3 and 6")
} else if myNumber < 6 && myNumber >= 3 {
    print("less than 6")
} else if myNumber == 6 {
    print("six")
} else {
    print("more than six")
}

if myNumber != 6 {
    print("not six")
} else {
    print("six")
}

// This should work according to switch 5.9 docs

//let myReturn = if myNumber <= 6 {
//    "it's six!"
//} else {
//    "not six :("
//}
