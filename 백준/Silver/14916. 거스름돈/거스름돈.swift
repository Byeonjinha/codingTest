func generateTable() -> [Int]{
    var table: [Int] = Array(repeating: -1, count: 100001)
    let initArray: [Int] = [-1, 1, -1, 2, 1, 3, 2, 4, 3, 2]
    table.enumerated().forEach {
        if $0.offset <= 9 {
            table[$0.offset] = initArray[$0.offset]
        } else {
            table[$0.offset] = table[$0.offset - 5] + 1
        }
    }
    return table
}

func main(){
    let dp = generateTable()
    guard let nStr = readLine(), let n = Int(nStr) else { return }
    print(dp[n - 1])
}
main()


