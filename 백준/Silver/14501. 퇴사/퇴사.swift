import Foundation

func generateTable(_ schedule: [Schedule]) -> [Int]{
    var table: [Int] = Array(repeating: 0, count: schedule.count + 1)
    for (idx, element) in schedule.enumerated() {
        if idx != 0 {
            table[idx] = max(table[idx], table[idx - 1])
        }
        let deadLine = idx + element.day
        if deadLine <= schedule.count {
            table[deadLine] = max(table[idx] + element.money, table[deadLine])
        }
        
    }
    return table
}

let n = Int(readLine()!)
var schedule: [Schedule] = []
for _ in 0..<n! {
    let input = readLine()!.split(separator: " ").map { Int($0) }
    let (day, money) = (input[0], input[1])
    schedule.append(Schedule(day: day!, money: money!))
}
let table = generateTable(schedule)
print(table.max()!)

struct Schedule {
    let day: Int
    let money: Int
}
