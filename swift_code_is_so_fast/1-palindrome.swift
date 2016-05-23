/*
        project directory: https://github.com/WaBlueKey/holbertonschool-higher_level_programming
        task #: 1
        file name: 1-palindrome.swift

        summary: this script returns true if a string is a palindrome.

        by Zee Adams, May 2016

 */

func is_palindrome(s: String) -> Bool {

    func palindromeTest(charSet: String.CharacterView) -> Bool {
        var wordOrder = charSet
        if wordOrder.count < 2 {
            return true
        } else {
            if wordOrder.popFirst() != wordOrder.popLast() {
                return false
            } else {
                return palindromeTest(wordOrder)
            }
        }
    }
    return palindromeTest(s.characters)
}
