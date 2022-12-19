import Foundation

func solution(_ slice:Int, _ n:Int) -> Int {
    var slice = slice
    var n = n 
    if n % slice == 0 {
        return n / slice
    }
    return n / slice + 1
}