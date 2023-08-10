
func generateTable(_ num: Int) throws -> [Int]{
    let tmpTable = [0, 0, 1, 3]
    guard num > 3 else { return tmpTable }
    var table: [Int] = Array(repeating: 0, count: num + 1)
    (table[0], table[1], table[2], table[3]) = (0, 0, 1, 3)
    for i in 4...num {
        if i % 2 == 0 { //짝수이면
            table[i] = table[Int(i / 2)] * 2 + Int(i / 2) * Int(i / 2)
        } else { //홀수이면
            table[i] = table[Int(i / 2)] + table[Int(i / 2) + 1] + Int(i / 2) * (Int(i / 2) + 1)
        }
    }
    
    return table
}

func main() throws {
    guard let pizzaStr = readLine() else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    guard let pizzaCount = Int(pizzaStr) else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    let table = try generateTable(pizzaCount)
    print(table[pizzaCount])
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


extension String {
    subscript(i: Int) -> String {
        get {
            return String(self[index(startIndex, offsetBy: i)])
        }
    }
}
