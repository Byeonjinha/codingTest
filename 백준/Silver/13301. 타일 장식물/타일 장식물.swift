
let table = generateTable(80)

func generateTable(_ num: Int) -> [Int]{
    if num == 0 { return [4] }
    
    var dp: [Int] = Array(repeating:0, count: num + 1)
    (dp[0], dp[1]) = (4, 6)
    for i in 2..<dp.count {
        dp[i] = dp[i - 1] + dp[i - 2]
    }
    
    return dp
}


func main() throws {
    guard let nStr = readLine(),
          let n = Int(nStr)
    else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    
    print(table[n - 1])
}
do {
    try main()
} catch {
    print(error)
}

enum ErrorCase: Error {
    case numError(text: String)
}
