
func generateTable(intArray: [Int?]) throws -> ([Int], [Int]){
    
    var maxTable: [Int] = Array(repeating: 1, count: intArray.count)
    var minTable:  [Int] = Array(repeating: 1, count: intArray.count)
    for i in 1..<intArray.count {
        if intArray[i]! >= intArray[i - 1]! {
            maxTable[i] = maxTable[i - 1] + 1
        }
        if intArray[i]! <= intArray[i - 1]! {
            minTable[i] = minTable[i - 1] + 1
        }
    }
    return (maxTable, minTable)
}

func main() throws {
    guard let numCount =  readLine() else  { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
    guard let intStr = readLine() else  { throw ErrorCase.numError(text: "입력 값이 올바르지 않습니다.") }
    let intArray = Array(intStr.split(separator: " ")).map{ Int($0)}
    let (maxTable, minTable) = try generateTable(intArray: intArray)
    print(max(maxTable.max()!, minTable.max()!))
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

