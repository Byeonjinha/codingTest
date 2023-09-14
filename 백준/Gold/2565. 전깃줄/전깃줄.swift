func findMinRemovalCount(n: Int, wires: [(Int, Int)]) -> Int {
    // 전깃줄을 B 위치를 기준으로 오름차순 정렬
    let sortedWires = wires.sorted { $0.1 < $1.1 }

    // LIS (가장 긴 증가하는 부분 수열)을 찾는 함수
    func findLIS(arr: [(Int, Int)]) -> Int {
        var lis = [Int](repeating: 1, count: arr.count)
        for i in 1..<arr.count {
            for j in 0..<i {
                if arr[i].0 > arr[j].0 {
                    lis[i] = max(lis[i], lis[j] + 1)
                }
            }
        }
        return lis.max() ?? 0
    }

    // 가장 긴 증가하는 부분 수열의 길이를 전체 전깃줄 개수에서 빼면 최소 제거해야 하는 개수를 얻을 수 있음
    let lisLength = findLIS(arr: sortedWires)
    let minRemovalCount = n - lisLength

    return minRemovalCount
}

// 입력 처리
let n = Int(readLine()!)!  // 전깃줄의 개수
var wires = [(Int, Int)]()  // 전깃줄의 위치 정보를 저장할 배열

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    wires.append((input[0], input[1]))
}

// 최소 제거해야 하는 전깃줄 개수 구하기
let result = findMinRemovalCount(n: n, wires: wires)
print(result) 