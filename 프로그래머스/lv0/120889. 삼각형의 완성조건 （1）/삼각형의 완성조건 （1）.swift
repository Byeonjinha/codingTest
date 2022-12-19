import Foundation

func solution(_ sides:[Int]) -> Int {
    var maxNum = 0 
    for i in sides {
        maxNum = max(maxNum, i)
    }
    if maxNum >= sum(sides) - maxNum {
        return 2
    }   
    return 1
}
func sum(_ numberArray:[Int]) -> Int {
    return numberArray.reduce(0,+)
}