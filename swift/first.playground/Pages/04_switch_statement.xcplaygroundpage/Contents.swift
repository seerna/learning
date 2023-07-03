import Foundation

// Switch

let myCountry = "Colombia"

switch myCountry {
case "Colombia":
    print("Tierra bonita")
case "México":
    print("Orale cabrón")
default:
    print("None of these")
}

// One return for multiple options

switch myCountry {
case "Colombia", "Argentina", "Peru", "Chile":
    print("Se habla Español")
case "US", "Australia":
    print("Se habla Inglés")
default:
    print("idk")
}

// Checks in a range of ints

let myAge = 28

switch myAge {
case 1 ... 10: // ... is inclusive
    print("between 1 and 10")
case 11 ..< 20: // ..< is exclusive
    print("between 11 and 19")
case 20 ..< 29:
    print("between 20 and 28")
default:
    print("more")
}
