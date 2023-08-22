import Foundation

func generateTable(_ width: Int) -> [Int]{
    var table: [Int] = Array(repeating: 0, count: width)
    if width == 1 || width == 2 { return [1, 3] }
    table[0] = 1
    table[1] = 3
    
    for i in 2..<width{
        table[i] = (table[i-1] + table[i-2] * 2) % 10007
    }
    return table
}

let tileWidth = Int(readLine()!)
let table = generateTable(tileWidth!)
print(table[tileWidth! - 1])
