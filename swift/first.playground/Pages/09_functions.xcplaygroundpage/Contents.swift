import Foundation

// Declaring a function

func myFunction() {
    print("This is how you go\n")
}

//myFunction() // Commented as it was nested in main()

// Functions with argumentos

func sayAName(name: String, age: Int) {
    print("Oeee \(name), tenés \(age).\n")
}

//sayAName(name: "Santi", age: 29) // Commented as it was nested in main()

// Function with return

func sumOfNumbers(firstN: Int, secondN: Int) -> Int {
    let sum = firstN + secondN
    return sum
}

func main() {
    myFunction()
    sayAName(name: "Santi", age: 29)
    
    let sum = sumOfNumbers(firstN: 3, secondN: 3)
    print("Sum: \(sum), Return type: \(type(of: sum))\n")
}

main()

// Taken from swift docs, function with multiple returns

func minMax(array: [Int]) -> (min: Int, max: Int) { // The declaration defined the names of the values that will be returned: 'min' & 'max' in our case.
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax) // Returns the min and max values
}

let myArray = [1,2,3,4,5,6,7,8,9,10,23,34,235,1,213,2,223,23,324,-12,132]
let bounds = minMax(array: myArray) // Returns an object containing the two values

print("min is \(bounds.max) and max is \(bounds.max), bound type is \(type(of: bounds))\n\nAnd bounds looks like \(bounds)")


