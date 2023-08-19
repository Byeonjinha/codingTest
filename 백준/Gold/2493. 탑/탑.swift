import Foundation

let n = Int(readLine()!)!
let top = readLine()!.split(separator: " ").map { Int($0)! }
var stack: [(Int, Int)] = []
var answer = Array(repeating: 0, count: n)

for i in 0..<n {
    while !stack.isEmpty {
        if stack.last!.1 > top[i] {
            answer[i] = stack.last!.0 + 1
            break
        } else {
            stack.popLast()
        }
    }
    stack.append((i, top[i]))
}

print(answer.map { String($0) }.joined(separator: " "))
