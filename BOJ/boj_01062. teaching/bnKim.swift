//
//  main.swift
//  ProblemSolving
//
//  Created by BinaryKim on 2021/06/09.
//

//백준 1062. 가르침

import Foundation
import Foundation

let firstLine = readLine()!.components(separatedBy: " ")

let N = Int(firstLine[0])!
let K = Int(firstLine[1])!

if K < 5 {
    print(0)
    exit(0)
} else if K == 26 {
    print(N)
    exit(0)
}

let learnable = K - 5

let base: [Bool] = Array.init(repeating: false, count: 26)
var list: [AntarticWord] = []
let removeList: [Character] = ["a", "c", "i", "n", "t"].reversed()
for _ in 0..<N {
    let str = readLine()!
    let startIndex = str.index(str.startIndex, offsetBy: 4)
    let endIndex = str.index(str.endIndex, offsetBy: -4)
    let range = startIndex..<endIndex
    let subStr = str[range]
    let charToIndex = subStr.map { Int($0.asciiValue! - Character("a").asciiValue!) }
    var array = base
    charToIndex.forEach {
        array[$0] = true
    }
    removeList.forEach {
        array.remove(at: Int($0.asciiValue! - Character("a").asciiValue!))
    }
    if let idx = list.firstIndex(where: { $0.alphabet == array }) {
        list[idx].duplicateCount += 1
    } else {
        list.append(AntarticWord(duplicateCount: 1, alphabet: array))
    }
}

var wordList: [AntarticWord] = []
list.forEach { word in
    if word.learnCount <= learnable { wordList.append(word) }
}

let alphabet = Array.init(repeating: false, count: 21)
var maxScore = 0

dfs(learnable, alphabet, 0)

print(maxScore)


func dfs(_ learnableCount: Int, _ learnedAlphabet: [Bool], _ idx: Int) {
    if learnableCount == 0 {
        var readCount = 0
        for word in wordList {
            var readable = true
            for (i, learned) in learnedAlphabet.enumerated() {
                if word.alphabet[i] && !learned {
                    readable = false
                    break
                }
            }
            if readable {
                readCount += word.duplicateCount
            }
        }
        if maxScore < readCount { maxScore = readCount }
        return
    }

    if learnedAlphabet.count <= idx { return }
    
    dfs(learnableCount, learnedAlphabet, idx+1)

    var newLearnedAlphabet = learnedAlphabet
    newLearnedAlphabet[idx] = true
    dfs(learnableCount - 1, newLearnedAlphabet, idx+1)
}

struct AntarticWord: Equatable {
    
    init(duplicateCount: Int, alphabet: [Bool]) {
        self.duplicateCount = duplicateCount
        self.alphabet = alphabet
        var count = 0
        alphabet.forEach {
            if $0 { count += 1 }
        }
        self.learnCount = count
    }
    
    let learnCount: Int
    var duplicateCount: Int
    let alphabet: [Bool]
    
    public static func == (lhs: AntarticWord, rhs: AntarticWord) -> Bool {
        return lhs.alphabet == rhs.alphabet
    }
}
