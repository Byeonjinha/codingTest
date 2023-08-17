import Foundation

func generateTable(doubleArray: [Double?]) throws -> [Double]{
    
    var table: [Double] = Array(repeating: 1, count: doubleArray.count)
    table[0] = doubleArray[0]!
    for i in 1..<doubleArray.count {
        if doubleArray[i]! <= doubleArray[i]! * table[i - 1] {
            table[i] = doubleArray[i]! * table[i - 1]
        } else {
            table[i] = doubleArray[i]!
        }
    }
    return table
}

func main() throws {
    guard let numCount =  Int(readLine()!) else  { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
    var numArray = [Double]()
    for _ in 0..<numCount {
        guard let num =  Double(readLine()!) else  { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
        numArray.append(num)
    }
    let table = try generateTable(doubleArray: numArray)
    print(String(format: "%.3f", table.max()!))
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

