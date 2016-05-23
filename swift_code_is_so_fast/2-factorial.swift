/*
        project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
        task #: 2
        file name: 2-factorial.swift

        summary: this script computes the Factorial number.

        by Zee Adams, May 2016

 */

func factorial(N: Int) -> (Int) {
    if N == 0 || N == 1 {
        return 1
    } else {
    return N * factorial(N - 1)
    }
}
