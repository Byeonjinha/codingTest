
func generateTable() throws -> [Int]{
    
    var table: [Int] = Array(repeating: -1, count: 5001)
    (table[0], table[1],table[2], table[3],table[4], table[5],table[6], table[7],table[8], table[9],table[10], table[11], table[12]) = (-1, -1 , -1, 1, -1, 1, 2, -1, 2, 3, 2, 3, 4)
    for i in 13..<5001 {
        table[i] = table[i - 5] + 1
    }
    return table
}

func main() throws {
    guard let weightStr = readLine() else  { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
    guard let weight = Int(weightStr) else { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
    let table = try generateTable()
    print(table[weight])
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

