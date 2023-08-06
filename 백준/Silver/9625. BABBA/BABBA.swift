func generateTable(_ num: Int) -> [[Int]]{
    var dp: [[Int]] = Array(repeating: [0, 0], count: num + 1)
    (dp[0], dp[1]) = ([1,0], [0,1])
    dp.enumerated().forEach {
        let idx = $0.offset
        if $0.offset != 0 && $0.offset != 1 {
            dp[idx] = [dp[idx - 1][0] + dp[idx - 2][0], dp[idx - 1][1] + dp[idx - 2][1]]
        }
    }
    return dp
}

func main(){
    guard let nStr = readLine(), let n = Int(nStr) else { return }
    let table = generateTable(n)
    print(table[n][0], table[n][1])
}
main()
