
func generateTable(_ year: Int, _ money: Double) throws -> [Int]{
    var table: [Int] = Array(repeating: Int(money), count: year + 1)
    for i in 1...year {
        if i < 3 {
            table[i] = Int(Double(table[i - 1]) * 1.05)
        } else if i >= 5 {
            table[i] = max(Int(Double(table[i - 5]) * 1.35), Int(Double(table[i - 3]) * 1.2), Int(Double(table[i - 1]) * 1.05))
        } else if i >= 3{
            table[i] = max(Int(Double(table[i - 3]) * 1.2), Int(Double(table[i - 1]) * 1.05))
        }
    }
 
    
    return table
}

func main() throws {
    guard let input = readLine()?.split(separator: " ") else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    guard input.count > 1 else { throw ErrorCase.stringError(text: "입력 개수 부족")}
    
    guard let money = Double(input[0]), let year = Int(input[1]) else { throw ErrorCase.numError(text: "year 입력 오류")}
    let table = try generateTable(year, money)
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


extension String {
    subscript(i: Int) -> String {
        get {
            return String(self[index(startIndex, offsetBy: i)])
        }
    }
}
