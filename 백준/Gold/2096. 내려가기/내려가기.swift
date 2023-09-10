import Foundation

func generateTable(graph: [[Int]]) {
    var maxTable = graph
    var minTable = graph
    for i in 1..<graph.count {
        for j in 0..<graph[i].count {
            var maxCompareArray:[Int] = []
            var minCompareArray:[Int] = []
            for number in [-1, 0, 1] {
                if j + number < 0 || j + number >= graph[i - 1].count { continue }
                else {
                    maxCompareArray.append(maxTable[i - 1][j + number])
                    minCompareArray.append(minTable[i - 1][j + number])
                }
            }
            maxTable[i][j] += maxCompareArray.max()!
            minTable[i][j] += minCompareArray.min()!
        }
    }
    print(maxTable[graph.count - 1].max()!, minTable[graph.count - 1].min()!)
}

let n = Int(readLine()!)!
var graph: [[Int]] = []
for _ in 0..<n {
    let component = readLine()?.split(separator: " ").compactMap{ Int($0) }
    graph.append(component!)
}
generateTable(graph: graph)

