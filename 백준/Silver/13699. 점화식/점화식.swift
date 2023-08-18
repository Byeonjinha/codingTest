import Foundation

func generateTable(_ num: Int) throws -> [Int]{
    
    var table: [Int] = Array(repeating: 1, count: num + 1)

    table[0] = 1
    for i in 0..<num {
        var tableValue: Int = 0
        for j in 0...i{
            tableValue += table[j] * table[i - j]
        }
        table[i + 1] = tableValue
    }
    return table
}

func main() throws {
    guard let num =  Int(readLine()!) else  { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
    let table = try generateTable(num)
    print(table[table.count - 1])
}
do {
    try main()
} catch {
    print(error)
}

enum ErrorCase: Error {
    case numError(text: String)
    case stringError(text: String)
}

