/*
    project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
    task #: 8
    file name: 8-main.swift

    summary: this script joins a list of string with a space using a closure not a function.

    by Zee Adams, May 2016

 */



let strings = ["We", "Heart", "Swift"]

let string = strings.reduce("") {
    if $0 == "" {
        return $1
    } else {
        return $0 + " " + $1
    }
}

print(string)
