/*
    project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
    task #: 3
    file name: 3-longest_word.swift

    summary: this script find the first longest word in a text.

    by Zee Adams, May 2016

 */
import Foundation

func longest_word(text: String) -> (String) {
    let stringSplit = text.componentsSeparatedByString(" ")
    let longest = stringSplit.maxElement({$1.characters.count > $0.characters.count})
    return longest!
}
