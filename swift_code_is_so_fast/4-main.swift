/*
        project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
        task #: 4
        file name: 0-main.swift

        summary: this script prints the string Hello Holberton school! in reverse.

        by Zee Adams, May 2016

 */

var numbers = [4, 7, 1, 9, 6, 5, 6, 9]

let max = numbers.reduce(numbers[0]) {
    if $0 > $1 {
        return $0
    } else {
        return $1
    }
}
print(max)
