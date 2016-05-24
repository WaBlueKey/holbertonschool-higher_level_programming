/*
        project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
        task #: 5
        file name: 5-fibonnacci.swift

        summary: this script computes the Fibonnacci number.

        by Zee Adams, May 2016

 */

func fibonacci(number: Int) -> (Int) {
    if number == 0 || number == 1{
        return number
    } else if number == 2 {
        return 1
    } else if number < 0 {
        if number == -1 {
            return 1
        } else if number == (-2) {
            return -1
        } else if number < -2 {
            return (fibonacci(number + 2) - fibonacci(number + 1))
        }
    }
    return (fibonacci(number - 1) + fibonacci(number - 2))
}
