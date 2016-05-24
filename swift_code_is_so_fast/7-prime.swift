/*
    project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
    task #: 7
    file name: 7-prime.swift

    summary: this script searches if the number is prime or not.

    by Zee Adams, May 2016

*/

func is_prime(number: Int) -> (Bool) {
    if number <= 1 {
        return false
    }
    if number <= 3 {
        return true
    }
    var i = 2
    while i * i <= number { //loop to find if number is divisible by any other number.
        if number % i == 0 {
            return false
        }
        i = i + 1
    }
    return true
}
