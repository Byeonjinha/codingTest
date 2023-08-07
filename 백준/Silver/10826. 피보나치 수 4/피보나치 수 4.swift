
let table = generateTable(10001)

func sumElement(_ prevArray: [Int], _ pprevArray: [Int], num: Int) -> [Int]{
    var newArray = Array(repeating: 0, count: 2100)
    for i in prevArray.indices.reversed() {
        var idx = i
        var sum: Int = prevArray[idx] + pprevArray[idx]
        while sum > 0 {
            newArray[idx] += sum % 10
            if newArray[idx] > 9 {
                newArray[idx - 1] += newArray[idx] / 10
                newArray[idx] -= 10
            }
            idx -= 1
            sum /= 10
        }
    }
    
    return newArray
}

func generateTable(_ num: Int) -> [[Int]]{
    if num == 0 { return [[0]] }
    var dp: [[Int]] = Array(repeating: Array(repeating: 0, count: 2100), count: num + 1)
    dp[1][dp[1].count - 1] = 1

    for i in dp.indices {
        let idx = i
        if i != 0 && i != 1 {
            dp[idx] = sumElement(dp[idx - 1], dp[idx - 2], num: num)
        }
    }
    
    return dp
}

func printAnswer(_ num: [Int]) -> String{
    var isFind = false
    var answer = ""
    for i in num {
        if i != 0 {
            isFind = true
        }
        if isFind {
            answer += "\(i)"
        }
    }
    return answer
}


func main() throws {
    guard let nStr = readLine(),
          let n = Int(nStr)
    else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    
    let answer = printAnswer(table[n])
    if answer == "" {
        print("0")
    } else {
        print("\(answer)")
    }
}
do {
    try main()
} catch {
    print(error)
}

enum ErrorCase: Error {
    case numError(text: String)
}
