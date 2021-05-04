// Created by BinaryKim on 2021/05/04.
// 메모리 초과

import Foundation

let input = readLine()!.components(separatedBy: " ")

//let str = "5 3 1 4 11 5 10"
//let input = str.components(separatedBy: " ")

let s = Int(input[0])!
let N = Int(input[1])!
let K = Int(input[2])!
let R1 = Int(input[3])!
let R2 = Int(input[4])!
let C1 = Int(input[5])!
let C2 = Int(input[6])!

var dp: [[[Bool]]] = [[[false]]]
let resultRow: [Bool] = Array.init(repeating: false, count: C2-C1+1)
var result: [[Bool]] = Array.init(repeating: resultRow, count: R2-R1+1)

// black == true == 1

for i in 0..<result.count {
    for j in 0..<resultRow.count {
        result[i][j] = getColor(row: i + R1, col: j + C1, time: s, N: N, K: K)
    }
}

func getColor(row: Int, col: Int, time: Int, N: Int, K: Int) -> Bool {
    if time == 0 { return false }
    getMap(time)
    if dp.count > time { return dp[time][row][col] }
    else {
        return getColor(row: row/N, col: col/N, time: time-1, N: N, K: K) == true ? true: getColor(row: row/N/N, col: col/N/N, time: time - 2, N: N, K: K)
    }
}

//이것도 메모리초과
//func getColor(row: Int, col: Int, time: Int, N: Int, K: Int) -> Bool {
//    if time == 0 { return false }
//    if dp.count > time { return dp[time][row][col] }
//    else {
//        getMap(time)
//        return dp[time][row][col]
//    }
//}

func getMap(_ time: Int) {
    var size = dp[dp.count-1].count
    for t in dp.count-1..<time {
        let oldSize = size
        size *= N

        let map = dp[dp.count-1]
        let newRow = Array.init(repeating: true, count: size)
        var newMap = Array.init(repeating: newRow, count: size)
        
        let remainWhite = (N-K)/2 * oldSize

        for i in 0..<N {
            for j in 0..<N {
                for r in 0..<oldSize {
                    for c in 0..<oldSize {
                        if (map[i/N][j/N] == false && ((i * oldSize + r) < remainWhite || (j * oldSize + c) < remainWhite || (i * oldSize + r) >= size - remainWhite || (j * oldSize + c) >= size - remainWhite)) {
                            newMap[i * oldSize + r][j * oldSize + c] = oldSize == 1 ? false: map[r][c]
                        }
                    }
                }
            }
        }
        dp.append(newMap)
        
        if size > 500 { return } // map size가 아니라 재귀에서 메모리 초과가 나는 듯
    }
}

printMap(result)


func printMap(_ map: [[Bool]]) {
    for row in map {
        var line = ""
        for cell in row {
            
            line.append("\(cell == true ? 1 : 0)")
        }
        print(line)
    }
}
