class Deque<T: Equatable> {
    var enqueue: [T]
    var dequeue: [T] = []
    var count: Int {
        return enqueue.count + dequeue.count
    }
    var isEmpty: Bool {
        return enqueue.isEmpty && dequeue.isEmpty
    }
    var first: T? {
        if dequeue.isEmpty {
            return enqueue.first
        }
        return dequeue.last
    }
    init(_ queue: [T]) {
        enqueue = queue
    }
    func appendleft(_ n: T) {
        dequeue.append(n)
    }
    func append(_ n: T) {
        enqueue.append(n)
    }
    func popleft() -> T? {
        if dequeue.isEmpty {
            dequeue = enqueue.reversed()
            enqueue.removeAll()
        }
        return dequeue.popLast()
    }
    func pop() -> T? {
        var returnValue: T?
        if enqueue.isEmpty {
            dequeue.reverse()
            returnValue = dequeue.popLast()
            dequeue.reverse()
        } else {
            returnValue = enqueue.popLast()
        }
        return returnValue
    }
    func contains(_ n: T) -> Bool {
        return enqueue.contains(n) || dequeue.contains(n)
    }
    func removeAll() {
        enqueue.removeAll()
        dequeue.removeAll()
    }
}

var dx = [-1, 1, 0, 0]
var dy = [0, 0, -1, 1]
func bfs(_ x: Int, _ y: Int, _ n: Int, _ m: Int, _ maps: [[Int]], _ water: Int) -> [[Int]] {
    var maps = maps
    let dequeue = Deque([([x,y])])
    while !dequeue.isEmpty {
        let cxcy = dequeue.pop()!
        let x = cxcy[0]
        let y = cxcy[ 1]
        for i in 0..<4{
            let nx = x+dx[i]
            let ny = y+dy[i]
            if nx < 0 || ny < 0 || nx >= n || ny >= m {
                continue
            }
            if maps[nx][ny] > water {
                continue
            } else {
                maps[nx][ny] = 101
                dequeue.append([nx,ny])
            }
        }
    }
    return maps
}

func bfs2(_ x: Int, _ y: Int, _ n: Int, _ m: Int, _ maps: [[Int]], _ water: Int) -> [[Int]] {
    var maps = maps
   
    if maps[x][y] < 101 {
        maps[x][y] = islandCount
        islandCount += 1
        let dequeue = Deque([([x,y])])
     
        while !dequeue.isEmpty {
            let cxcy = dequeue.pop()!
            let x = cxcy[0]
            let y = cxcy[ 1]
            for i in 0..<4{
                let nx = x+dx[i]
                let ny = y+dy[i]
                if nx < 0 || ny < 0 || nx >= n || ny >= m {
                    continue
                }
                if maps[nx][ny] > 100 {
                    continue
                } else {
                    maps[nx][ny] = islandCount
                    dequeue.append([nx,ny])
                }
            }
        }
    }
  
    
    return maps
}
var islandCount = 1001
var answerArray: [Int] = [1]
var a = Int(readLine()!)
var graph = [[Int]]()
for _ in 0..<a!{
    let arrayInt = readLine()!.split(separator: " ").map { Int(String($0))! }
    graph.append(arrayInt)
}
var graph3 = graph
var maxHeight = 0
for j in 0..<graph.count{
    maxHeight = graph[j].max()!
}
    
for p in 0...maxHeight{
    for j in 0..<graph.count{
        for k in 0..<graph[0].count{
            graph = bfs(j, k, graph.count, graph[0].count, graph, p)
        }
    }
    for j2 in 0..<graph.count{
        for k2 in 0..<graph[0].count{
            let graph2 = graph
            graph = bfs2(j2, k2, graph.count, graph[0].count, graph, p)
        }
    }
    answerArray.append(islandCount - 1001)
  
    graph = graph3
    islandCount = 1001
}
print(answerArray.max()!)
