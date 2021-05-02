// 런타임 에러 해결하려다 반례를 찾았지만 일단 틀렸어도 숙제는 제출을 해야겠고
// 알고보니 남들 다 제출 안해서 B+ 맞은 과목 같은 느낌적인 느낌으루다가

import Foundation

let firstLine = readLine()!.components(separatedBy: " ")
let n = Int(firstLine[0])!
let m = Int(firstLine[1])!

let boys = readLine()!.components(separatedBy: " ").map { Int($0)! }
let girls = readLine()!.components(separatedBy: " ").map { Int($0)! }

struct Jack: Comparable {
    static func < (lhs: Jack, rhs: Jack) -> Bool {
        return lhs.distance < rhs.distance
    }
    
    let score: Int
    let distance: Int
}

let _minorGender: [Int] = girls.count < boys.count ? girls : boys
var majorGender: [Int] = girls.count < boys.count ? boys : girls
var minorGender = _minorGender

for person in _minorGender {
    if let match = majorGender.firstIndex(of: person) {
        if let soulmate = minorGender.firstIndex(of: person) {
            minorGender.remove(at: soulmate)
            majorGender.remove(at: match)
        }
    }
}

minorGender.sort()
majorGender.sort()

var jacks: [Jack] = []

for jack in majorGender {
    var minSub = Int.max
    for queen in minorGender { // 여기도 이분탐색으로 하고
        let sub = abs(jack - queen)
        if sub >= minSub && minSub != Int.max { break }
        else { minSub = sub }
    }
    jacks.append(Jack(score: jack, distance: minSub))
}

jacks.sort()

var answer = 0
if minorGender.count == 0 || !jacks.indices.contains(minorGender.count) { print(0) }
else {
    for i in 0..<minorGender.count {
        answer += abs(minorGender[i] - jacks[i].score)
    }
    print(answer)
}
