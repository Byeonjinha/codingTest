import Foundation

let NK = readLine()!.split(separator: " ").map { Int($0)! }
let N = NK[0], K = NK[1]

var circle: [Int] = Array(1...N)
var answer: [String] = []

var currentIndex = 0

while !circle.isEmpty {
    currentIndex = (currentIndex + K - 1) % circle.count  // K만큼 뒤의 인덱스 계산
    answer.append(String(circle.remove(at: currentIndex)))
}

print("<\(answer.joined(separator: ", "))>")
