/*
    project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
    task #: 6
    file name: 6-reverse_array.swift

    summary: this script returns a reversed array.

    by Zee Adams, May 2016

 */

func reverse_array(a: [Int]) -> ([Int]) {
    var aReversed = a //local var introduced to complete reversing process.
    aReversed = a.reverse()
    return aReversed
}
