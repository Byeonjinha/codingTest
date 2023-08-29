import Foundation

func topologicalSort(graph: [Int: [Int]], indegree: inout [Int]) -> [Int] {
    var queue = [Int]()
    var result = [Int](repeating: 0, count: indegree.count)
    
    // 선행 과목이 없는 과목들을 큐에 추가
    for i in 1..<indegree.count {
        if indegree[i] == 0 {
            queue.append(i)
            result[i] = 1
        }
    }
    
    while !queue.isEmpty {
        let course = queue.removeFirst()
        for nextCourse in graph[course] ?? [] {
            indegree[nextCourse] -= 1
            result[nextCourse] = max(result[nextCourse], result[course] + 1)
            if indegree[nextCourse] == 0 {
                queue.append(nextCourse)
            }
        }
    }
    
    return result
}

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var graph = [Int: [Int]]()
var indegree = [Int](repeating: 0, count: N + 1)

for _ in 0..<M {
    let line = readLine()!.split(separator: " ").map { Int($0)! }
    let A = line[0]
    let B = line[1]
    
    graph[A, default: []].append(B)
    indegree[B] += 1
}

let result = topologicalSort(graph: graph, indegree: &indegree)
print(result.map{ String($0)}.dropFirst().joined(separator: " "))
