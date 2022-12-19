import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var odd = 0
    var even = 0
    for i in num_list.indices {
        if num_list[i] % 2 == 0 {
            odd += 1
        }
        else {
            even += 1
        }
    }
    return [odd, even]
}