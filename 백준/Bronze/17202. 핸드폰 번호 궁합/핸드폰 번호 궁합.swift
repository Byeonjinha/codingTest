import Foundation

func input() -> String? {
    guard let n1 = readLine(), let n2 = readLine() else { return nil }
    var num = ""
    for i in n1.indices {
        num += String(n1[i]) + String(n2[i])
    }
    return num
}

func generateNum(_ numStr: String) -> String {
    var newArray: [String] = []
    let numStr = Array(numStr)
    for i in 1..<numStr.count {
        newArray.append(String((Int(String(numStr[i]))! + Int(String(numStr[i - 1]))!)%10))
    }
    return newArray.joined()
}


if let input = input() {
    var dp: [String] = Array(repeating: "", count: input.count)
    for num in input.enumerated() {
        if num.offset == 0 { dp[num.offset] = input }
        else {
            let nextNum = generateNum(dp[num.offset - 1])
            dp[num.offset] = nextNum
        }
    }
    dp.removeLast()
    print(dp.last!)
}