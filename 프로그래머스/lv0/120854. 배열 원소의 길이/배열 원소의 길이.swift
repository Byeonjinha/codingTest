import Foundation

func solution(_ strlist:[String]) -> [Int] {
    var answer = [Int]()
    for word in strlist {
        answer.append(word.count)
    }
    return answer
}