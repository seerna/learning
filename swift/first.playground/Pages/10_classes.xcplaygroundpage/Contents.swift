import Foundation

class Programmer {
    
    let name: String
    let age: Int
    var languages: [Language]
    var friends: [Programmer]?
    
    enum Language { // This is a list of possible items the object can have
        case swift
        case python
        case html
        case css
    }
    
    init(name:String, age: Int, languages: [Language]) {
        self.name = name
        self.age = age
        self.languages = languages
    }
    
    func code() {
        for language in languages {
            print(language)
        }
        print("Coding lol...")
    }
    
}


// Creating an instance

let santi = Programmer(name: "Santiago", age: 29, languages: [.python, .swift])

santi.code()

let sara = Programmer(name: "Sara", age: 25, languages: [.python, .swift, .html])

// Adding a value to the optional attribute, another class, in this case

santi.friends = [sara]

print(santi.friends?.first?.name) // we need to look inside the class to print what we need
