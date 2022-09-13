let inp = readLine()!.split(separator: " " ).map{Int(String($0))!}
var N = inp[0], M = inp[1], oils = inp[2]
var arr = [[Int]]()
for _ in 0..<N {
    arr.append(readLine()!.split(separator: " " ).map{Int(String($0))!})
}
let inp2 = readLine()!.split(separator: " " ).map{Int(String($0))!}
var taxi = (inp2[0]-1, inp2[1]-1)
var passengers = [((Int,Int),(Int,Int))]()
for _ in 0..<M {
    let q = readLine()!.split(separator: " " ).map{Int(String($0))!}
    passengers.append(((q[0]-1,q[1]-1),(q[2]-1,q[3]-1)))
}
let dir = [(0,1),(0,-1),(1,0),(-1,0)]

func search(start:(Int,Int), end: (Int,Int), _ oil: Int, _ visit: inout [[Int]]) {
    var queue = [(start,0,oil)], q = 0
    visit[start.0][start.1] = 0
    while queue.count>q {
        let f = queue[q]
        if f.0 == end { break }
        q += 1
        if f.2 == 0 { continue }
        for i in 0..<4 {
            let n = (f.0.0+dir[i].0, f.0.1+dir[i].1)
            if n.0>=N||n.1>=N||n.0<0||n.1<0{ continue }
            if arr[n.0][n.1] == 1 || visit[n.0][n.1] != Int.max { continue }
            visit[n.0][n.1] = f.1+1
            queue.append((n,f.1+1,f.2-1))
        }
    }
}

func getNextPassenger(_ visit: inout [[Int]] ) -> ((Int,Int),(Int,Int)) {
    passengers.sort(by: {visit[$0.0.0][$0.0.1] == visit[$1.0.0][$1.0.1] ? $0.0.0 == $1.0.0 ? $0.0.1 < $1.0.1 : $0.0.0 < $1.0.0 : visit[$0.0.0][$0.0.1] < visit[$1.0.0][$1.0.1] })
    return  passengers.first!
}

func removePassenger(_ visit: inout [[Int]], _ passenger: ((Int,Int),(Int,Int))) {
    passengers.remove(at: passengers.firstIndex(where: {$0.0 == passenger.0})!)
    let consum = visit[passenger.1.0][passenger.1.1]
    oils -= consum
    oils += consum*2
    taxi = passenger.1
}

var answer = true
while !passengers.isEmpty {
    var visit = Array(repeating: Array(repeating: Int.max, count: N), count: N)
    // 승객을 찾는다.
    search(start: taxi, end: (-1,-1), oils, &visit)
    let next = getNextPassenger(&visit)
    // 갈수있는 승객인지 확인한다.
    if visit[next.0.0][next.0.1] == Int.max { answer = false; break }
    oils -= visit[next.0.0][next.0.1]
    visit = Array(repeating: Array(repeating: Int.max, count: N), count: N)
    // 찾은승객을 데려다준다.
    search(start: next.0, end: next.1, oils, &visit)
    // 데려다줄수있는지 확인한다.
    if visit[next.1.0][next.1.1] == Int.max { answer = false; break }
    removePassenger(&visit, next)
}
print(answer ? oils : -1 )

