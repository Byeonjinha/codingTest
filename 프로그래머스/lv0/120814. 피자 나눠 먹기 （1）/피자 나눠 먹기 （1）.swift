import Foundation

func solution(_ n:Int) -> Int {
    if Double(n / 7) == Double(n)/7 {
        return Int (n / 7)
    }
    return Int (n / 7) + 1
}