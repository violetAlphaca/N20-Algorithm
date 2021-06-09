//
//  main.swift
//  ProblemSolving
//
//  Created by BinaryKim on 2021/06/09.
//

import Foundation

//var input =
//"""
//2 4
//CAAB
//ADCB
//"""

//let lines = input.split(separator: "\n")
//let firstLine = lines[0].components(separatedBy: " ")

let firstLine = readLine()!.components(separatedBy: " ")

let R = Int(firstLine[0])!
let C = Int(firstLine[1])!

let base: [Character] = Array.init(repeating: "A", count: C)
var board: [[Character]] = Array.init(repeating: base, count: R)

//for i in 0..<R {
//    board[i] = lines[i+1].map { $0 }
//}

// 콘솔 입력
for i in 0..<R {
    board[i] = Array(readLine()!)//.components(separatedBy: " ").map { Int($0)! }
}

var visited: [Bool] = Array.init(repeating: false, count: 26)
var maxDepth: Int = 1

visited[Int(board[0][0].asciiValue!) - 65] = true
dfs(pos: Position(x: 0, y: 0), depth: 1)

func dfs(pos: Position, depth: Int) {
    if depth > maxDepth {
        maxDepth = depth
    }
    if maxDepth == 26 { return }
    
    let dx = [0, 1, 0, -1]
    let dy = [1, 0, -1, 0]
    
    for i in 0..<4 {
        let nx = pos.x + dx[i]
        let ny = pos.y + dy[i]
        
        if (nx < 0 || ny < 0 || nx >= C || ny >= R) { continue }
        if visited[Int(board[ny][nx].asciiValue!) - 65] == true {
            continue
        } else {
            visited[Int(board[ny][nx].asciiValue!) - 65] = true
            dfs(pos: Position(x: nx, y: ny), depth: depth + 1)
            visited[Int(board[ny][nx].asciiValue!) - 65] = false
        }
    }
}

print(maxDepth)

struct Position: Equatable {
    let x: Int
    let y: Int
}
