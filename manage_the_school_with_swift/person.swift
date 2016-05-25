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

enum Subject {
    case Math
    case English
    case French
    case History
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

    func className() -> String {
        return "Person"
    }
}
class Mentor: Person, Classify {
    override func className () -> String {
        return "Mentor"
    }

    func isStudent() -> Bool {
        return false
    }
    let subject: Subject

    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }

    func stringSubject() -> String {
        if self.subject == Subject.Math {
            return "Math"
        }
        if self.subject == Subject.English {
            return "English"
        }
        if self.subject == Subject.French {
            return "French"
        }
        if self.subject == Subject.History {
            return "History"
        }
        return "String"
    }
}

class Student: Person, Classify {
    override func className () -> String {
        return "Student"
    }
    func isStudent() -> Bool {
        return true
    }
}

class School {
    var name: String
    var list_persons: [Person]


    init(name: String) {
        self.name = name
        self.list_persons = []
    }

    func addStudent(p: Person) -> Bool {
        if p.className() == "Student" {
            self.list_persons.append(p)
            return true
        }
        return false
    }

    func addMentor(p: Person) -> Bool {
        if p.className() == "Mentor" {
            self.list_persons.append(p)
            return true
        }
        return false
    }

    func listStudents() -> [Person] {
        var list_students = self.list_persons.filter {($0 is Student)}
        list_students.sortInPlace {($0.age > $1.age)}
        return list_students
    }

    func listMentors() -> [Person] {
        var list_mentors = self.list_persons.filter {($0 is Mentor)}
        list_mentors.sortInPlace {($0.age > $1.age)}
        return list_mentors
    }

    func listMentorsBySubject(subject: Subject) -> [Person] {
        let mentors = self.listMentors() as! [Mentor]
        let mentorsBySubject: [Mentor] = mentors.filter {(mentor: Mentor) -> Bool in
            mentor.subject == subject
        }
        return mentorsBySubject
    }
}
