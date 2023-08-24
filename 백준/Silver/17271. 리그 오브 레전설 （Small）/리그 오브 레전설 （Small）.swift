import Foundation

func generateTable(_ n: Int, _ m: Int) -> [Int] {
    var table: [Int] = Array(repeating: 0, count: n + 1)
    table[0] = 1
    if n < 1 {
        return table
    }
    for i in 1...n {
        table[i] = table[i - 1] % 1000000007
        if i >= m {
            table[i] =  (table[i] + table[i - m]) % 1000000007
        }
    }
    return table
}

let input = readLine()!.split(separator: " ").map{ Int($0) }
let (n, m) = (input[0], input[1])
let table = generateTable(n!, m!)
//print(table)
print(table[n!])

