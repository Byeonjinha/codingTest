import Foundation

func solution(_ numbers:[Int]) -> Int {
    var numbers = numbers
    numbers.sort(by: >)
    return numbers[0] * numbers[1]
}