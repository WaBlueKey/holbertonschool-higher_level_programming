/*
    project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
    task #: 0, 1, 2, 3, 4
    file name: person.swift

    summary: this project is to manipulate Object, Class, Enum and Protocol in Swift.

    by Zee Adams, May 2016

 */

 protocol Classify {

     func isStudent() -> Bool
 }

 class Person {

     var first_name: String
     var last_name: String
     var age: Int

     init(first_name: String, last_name: String, age: Int) {

         self.first_name = first_name
         self.last_name = last_name
         self.age = age
     }

     func fullName() -> String {
         return first_name + " " + last_name
     }
 }
 class Mentor: Person, Classify {
     func isStudent() -> Bool {
         return false
     }

    }

 class Student: Person, Classify {
     func isStudent() -> Bool {
         return true
     }

 }
