import Foundation

var results: [Int] = []
var check: Int = 1000
var answer: Int = 9999999999

func calValue(pick: Picks, _ minerals: [String]) -> Int{
    var value = 0
    switch pick {
    case.diamond:
        return minerals.count
    case .iron:
        for mineral in minerals {
            if mineral == "diamond" {
                value += 5
            } else {
                value += 1
            }
        }
        return value
    case .stone:
        for mineral in minerals {
            if mineral == "diamond" {
                value += 25
            } else if mineral == "iron" {
                value += 5
            } else {
                value += 1
            }
        }
        return value
    }
}
func dfs(_ userPick: UserPicks, _ value: Int, _ minerals: [String]) {
    if userPick.diamond + userPick.iron + userPick.stone == 0 || minerals.count == 0 {
        answer = min(answer, value)
    }
    
    if userPick.diamond != 0 {
        let diaPicks = UserPicks(diamond: userPick.diamond - 1, iron: userPick.iron, stone: userPick.stone)
        let newValue = value + calValue(pick: .diamond, Array(minerals.prefix(5)))
        dfs(diaPicks, newValue, Array(minerals.dropFirst(5)))
    }
    if userPick.iron != 0 {
        let ironPicks = UserPicks(diamond: userPick.diamond, iron: userPick.iron - 1, stone: userPick.stone)
        let newValue = value + calValue(pick: .iron, Array(minerals.prefix(5)))
        dfs(ironPicks, newValue, Array(minerals.dropFirst(5)))
    }
    if userPick.stone != 0 {
        let stonePicks = UserPicks(diamond: userPick.diamond, iron: userPick.iron, stone: userPick.stone - 1)
        let newValue = value + calValue(pick: .stone, Array(minerals.prefix(5)))
        dfs(stonePicks, newValue, Array(minerals.dropFirst(5)))
    }
}

func solution(_ picks:[Int], _ minerals:[String]) -> Int {
    var userPick: UserPicks = UserPicks(diamond: picks[0], iron: picks[1], stone: picks[2])
    dfs(userPick, 0, minerals)
    print(answer)
    return answer
}

struct UserPicks {
    var diamond: Int
    var iron: Int
    var stone: Int
}

enum Picks: String {
    case diamond
    case iron
    case stone
}