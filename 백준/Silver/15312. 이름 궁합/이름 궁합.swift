let alphabetArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
let valueArray =  [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 ]

func searchNum(_ eachName: String) throws -> Int{
    guard let ecahNameIdx = alphabetArray.firstIndex(of: eachName) else { throw ErrorCase.stringError(text: "올바르지 않는 문자열 입니다.") }
    return valueArray[ecahNameIdx]
}

func generateTable(_ numArray: [Int]) -> [[Int]]{
    var table: [[Int]] = []
    
    var numArray = numArray
    while true {
        if numArray.count == 2 { break }
        var tmpArray: [Int] = []
        for num in 1..<numArray.count {
            tmpArray.append((numArray[num - 1] + numArray[num]) % 10)
        }
        numArray = tmpArray
        table.append(numArray)
    }
    return table
}

func main() throws {
    guard let jongmin = readLine() else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    guard let her = readLine() else { throw ErrorCase.numError(text: "입력값이 올바르지 않습니다.") }
    var nameValue: [Int] = []
    for i in 0..<jongmin.count {
        nameValue.append(try searchNum(String(jongmin[i])))
        nameValue.append(try searchNum(String(her[i])))
    }
    let table = generateTable(nameValue)
    print("\(table[table.count - 1][0])\(table[table.count - 1][1])")
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
        set {
            var StringArray: [Character]
            StringArray = Array(self)
            StringArray[i] = Character(newValue)
            self = String(StringArray)
        }
    }
}
